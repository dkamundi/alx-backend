// Import necessary modules using ES6 import syntax
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

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
const displaySchoolValue = async (schoolName) => {
	try{
		const value = await getAsync(schoolName);
		console.log(`The value for ${schoolName} is: ${value}`);
	} catch (error) {
		console.error(`Error retrieving value for ${schoolName}: ${error.message}`);
	}
};

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
