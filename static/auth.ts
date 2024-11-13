function authenticateUser(username, password) {
    if (username === 'your_username' && password === 'your_password') {
      return true;
    } else {
      return false;
    }
  }
  
  let username = prompt("Enter your username:");
  let password = prompt("Enter your password:");
  
  if (authenticateUser(username, password)) {
    console.log("Authentication successful!");
    window.location.href = "https://www.youtube.com";
  } else {
    console.log("Authentication failed. Please try again.");
  }