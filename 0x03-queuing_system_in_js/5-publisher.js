// Import necessary modules using ES6 import syntax
import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Event listener for successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message to the holberton school channel after a specified time
const publishMessage = (message, time) => {
  console.log(`About to send ${message}`);
  setTimeout(() => {
    publisher.publish('holberton school channel', message);
  }, time);
};

// Call the publishMessage function
publishMessage('Hello Holberton', 1000);
publishMessage('KILL_SERVER', 2000);

