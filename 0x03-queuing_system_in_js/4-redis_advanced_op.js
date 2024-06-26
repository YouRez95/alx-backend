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
  client.hset('HolbertonSchools', 'Portland', 50, print)
  client.hset('HolbertonSchools', 'Seattle', 80, print)
  client.hset('HolbertonSchools', 'New York', 20, print)
  client.hset('HolbertonSchools', 'Bogota', 20, print)
  client.hset('HolbertonSchools', 'Cali', 40, print)
  client.hset('HolbertonSchools', 'Paris', 2, print)
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) throw err;
    console.log(reply)
  })
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})
