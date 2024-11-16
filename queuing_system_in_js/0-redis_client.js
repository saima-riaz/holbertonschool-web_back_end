import { createClient } from 'redis';

const client = createClient(); // Use the new `createClient` method.

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Connect the client
(async () => {
  try {
    await client.connect();
    console.log('Connection to Redis established');
  } catch (error) {
    console.error('Error connecting to Redis:', error);
  }
})();
