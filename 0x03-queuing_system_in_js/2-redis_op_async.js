import { createClient } from 'redis';
import redis from 'redis';
const { promisify } = require('util');

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, function(err, reply) {
    if (err) {
      callback(err);
    }
    else {
      callback(null, reply);
    }
  });
}

const displaySchoolValueAsync = promisify(displaySchoolValue);

displaySchoolValueAsync('Holberton', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});

setNewSchool('HolbertonSanFrancisco', '100');

displaySchoolValueAsync('HolbertonSanFrancisco', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});
