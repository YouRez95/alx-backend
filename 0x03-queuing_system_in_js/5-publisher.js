import { createClient, print } from 'redis';

const client = createClient();


async function connectToRedis() {
  await new Promise((resolve, reject) => {
    client.on('connect', () => {
      resolve()
    });

    client.on('error', (err) => {
      reject(err)
    });
  });
  return client;
}

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`)
    client.publish('holberton school channel', message)
  }, time)
}


connectToRedis().then((client) => {
  console.log('Redis client connected to the server')
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
