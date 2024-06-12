export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(job => {
    const jobToProcess = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) console.log('Notification job created: ', jobToProcess.id)
    })
    
    jobToProcess.on('complete', function(result){
      console.log(`Notification job #${jobToProcess.id} completed`);
    
    }).on('failed', function(errorMessage){
      console.log(`Notification job #${jobToProcess.id} failed: ${errorMessage}`);
    }).on('progress', function(progress, data){
      console.log(`Notification job #${jobToProcess.id} ${progress}% complete`);
    });
  })
}