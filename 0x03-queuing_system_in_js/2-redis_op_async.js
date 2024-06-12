import { promisify } from 'util';
import { createClient, print } from 'redis';

const client = createClient();
client.get = promisify(client.get);


async function connectToRedis() {
  await new Promise((resolve, reject) => {
    client.on('connect', () => {
      resolve()
    });

    client.on('error', (err) => {
      reject(err)
    });
  });
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    throw err;    
  }
}

connectToRedis().then(() => {
  console.log('Redis client connected to the server')
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})


displaySchoolValue('Holberton').then(() => {
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});
