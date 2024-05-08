const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '080 293 932 41',
  message: 'Welcome',
}

const job = queue.create('push_notification_code', jobData)
  .save();

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.error('Notification job failed');
});
