import createPushNotificationsJobs from './8-job.js';
const queue = require('kue').createQueue();
const { expect } = require('chai');

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('jobs', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    }];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

    it('should have the correct job type', () => {
    const jobs = [
    {
      phoneNumber: '415298083780',
      message: 'This is the code 833 to verify your account'
    },
    {
      phoneNumber: '0208735187',
      message: 'This is the code 99 to verify your account'
    }];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });
});

