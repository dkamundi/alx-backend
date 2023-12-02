// Import necessary modules using ES6 import syntax
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
};

// Function to display a new school value in Redis
const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (error, value) => {
		if (error) {

			console.error(`Error retreiving value for ${schoolName}: ${err.message}`);
		} else {
			console.log(`The value for ${schoolName} is: ${value}`);
		}
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
