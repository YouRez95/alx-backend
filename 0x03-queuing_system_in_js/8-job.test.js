import { createQueue } from 'kue';
import  createPushNotificationsJobs from './8-job';
import { expect } from 'chai';


const queue = createQueue();

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('display a error message if jobs is not an array', function() {
  expect(() => createPushNotificationsJobs('', queue)).to.throw(Error).with.property('message', 'Jobs is not an array');
});



