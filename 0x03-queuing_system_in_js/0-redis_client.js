import { createClient } from 'redis';

async function connectToRedis() {
  const client = createClient();
  
  await new Promise((resolve, reject) => {
    client.on('connect', () => {
      resolve()
    });

    client.on('error', (err) => {
      reject(err)
    });
  });

  return client; // to use later
}

connectToRedis().then(() => {
  console.log('Redis client connected to the server')
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})
