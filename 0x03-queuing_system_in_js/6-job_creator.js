import { createClient } from 'redis';
import { createQueue } from 'kue';

const client = createClient();
const queue = createQueue();


const job = queue.create('push_notification_code', {
  phoneNumber: '4153518781',
  message: 'This is the code to verify your account',
}).save((err) => {
  if (!err) console.log('Notification job created: ', job.id)
})

job.on('complete', function(result){
  console.log('Notification job completed');

}).on('failed', function(errorMessage){
  console.log('Notification job failed');
})

