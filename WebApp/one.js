const fs = require("fs");

// Define the options object
const options = {
  1: "Go home",
  2: "Go To World",
  3: "Go to School",
};

// Function to get user input from the console
function getInput(prompt) {
  const readlineSync = require("readline-sync");
  return readlineSync.question(prompt);
}

// Main loop to repeatedly get user input
while (true) {
  const username = getInput("Enter username: ");
  console.log("Username is: " + username);

  const option = getInput("Enter Options \n 1 to 3 \n");
  console.log(option);
  console.log(options[option]);

  // Write to file "one.txt"
  fs.writeFileSync("one.txt", `username: ${username} \noption: ${option} \n`);
}
