const { createQueue } = require('kue');
const redis = require('redis');
const express = require('express');
const { promisify } = require('util');

const client = redis.createClient();
let reservationEnabled = true;

function reserveSeat(number) {
  client.set('available_seats', number)
}

async function getCurrentAvailableSeats() {
  const getSeat = promisify(client.get).bind(client);

  return getSeat('available_seats');
};

const queue = createQueue();
const app = express();

app.get('/available_seats', (req, res) => {
  getCurrentAvailableSeats()
    .then((reply) => {
      if (reply) {
        res.send({"numberOfAvailableSeats":reply});
      } else {
        res.status(404).send("No available seats information found");
      }
    });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.send({ "status": "Reservation are blocked" });
  }

  const reserveSeatJob = queue.create('reserve_seat')
    .on('complete', () => {
      console.log(`Seat reservation job ${reserveSeatJob.id} completed`);
    }).on('failed', (error) => {
      console.log(`Seat reservation job ${reserveSeatJob.id} failed: ${error}`);
    });

  reserveSeatJob.save((error) => {
   if (error) {
     res.send({ "status": "Reservation failed" });
   }

   res.send({ "status": "Reservation in process" });
  });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const reply = await getCurrentAvailableSeats();

    let availableSeat = reply - 1;

    reserveSeat(availableSeat);

    if (availableSeat === 0) {
      reservationEnabled = false;
      done();
    }

    if (availableSeat > 0) {
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
  res.send({ "status": "Queue processing" });
});

app.listen(1245, () => {
  reserveSeat(0);
  console.log('Server listening on port 1245');
});
