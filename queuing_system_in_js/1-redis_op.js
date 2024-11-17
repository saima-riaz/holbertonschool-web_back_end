import { createClient } from 'redis';

const client = createClient();

client.connect()
  .then(() => {
    console.log("Redis client connected");

    // Test the functions
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100').then(() => {
      displaySchoolValue('HolbertonSanFrancisco');
    });
  })
  .catch((err) => {
    console.error("Error connecting to Redis", err);
  });

async function setNewSchool(schoolName, value) {
  try {
    await client.set(schoolName, value); // Set the value for the school
    console.log('Reply:', 'OK'); // Confirmation message after setting the value
  } catch (err) {
    console.error("Error setting school value:", err);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName); // Retrieve the value of the school
    console.log(value); // Display the value in the console
  } catch (err) {
    console.error("Error retrieving school value:", err);
  }
}
