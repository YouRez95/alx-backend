import { createQueue } from 'kue';

const queue = createQueue();
const blackListNumbers = ['4153518780', '4153518781'];
function sendNotification(phoneNumber, message, job, done) {
  // track the progress of the job of 0 out of 100
  let progress = 0;
  job.progress(progress, 100)
  if (blackListNumbers.includes(phoneNumber)) {
    throw new Error(`Phone number ${phoneNumber} is blacklisted`);
  }
  progress = 50
  job.progress(progress, 100)
  if (progress >= 50) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

queue.process('push_notification_code_2', function(job, done) {
  try {
    sendNotification(job.data.phoneNumber, job.data.message, job, done)
  } catch (err) {
    done(err.message)
  }
})