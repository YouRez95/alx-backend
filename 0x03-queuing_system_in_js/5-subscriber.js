import { promisify } from 'util';
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

connectToRedis().then((client) => {
  console.log('Redis client connected to the server')
  client.subscribe('holberton school channel')
  client.on('message', (channel, message) => {
    if (channel === 'holberton school channel') {
      console.log(message)
    }

    if (message === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel')
      client.quit()
    }
  })
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})
