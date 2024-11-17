import { createClient } from 'redis';

const client = createClient();
client.connect().then(() => {
  console.log("Redis client connected");
}).catch((err) => {
  console.error("Error connecting to Redis", err);
});
