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

  // return client; // to use later
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) throw err;
    print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) throw err;
    console.log(value);
  });
}

connectToRedis().then(() => {
  console.log('Redis client connected to the server')
}).catch((err) => {
  console.log('Redis client not connected to the server: ' + err.message)
})


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
