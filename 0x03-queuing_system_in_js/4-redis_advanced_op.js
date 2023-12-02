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

// Function to create a hash in Redis using hset
const createHash = () => {
	// key of the hash
	const key = 'HolbertonSchools';


	// Values for the hash
	const values = {
		Portland: 50,
		Seattle: 80,
		'New York': 20,
		Bogota: 20,
		Cali: 40,
		Paris: 2,
	};

	// Loop through values and set them using hset
	for (const [field, value] of Object.entries(values)) {
		client.hset(key, field, value, redis.print);
	}
};

// Function to display the hash using hgetall
const displayHash = () => {
	// Key of the hash
	const key = 'HolbertonSchools';

	// Use hgetall to get all fields and values of the hash
	client.hgetall(key, (err, hash) => {
		if (err) {
			console.error(`Error retrieving hash ${key}: ${err.message}`);
		} else {
			console.log(`Hash ${key}:`, hash);
		}
	});
};

// Call functions
createHash();
displayHash();
