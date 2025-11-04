function validateLogin() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  if (email === "" || password === "") {
    alert("Please enter all fields.");
    return false;
  }
  alert("Login Successful!");
  window.location.href = "live_map.html";
  return false;
}

function validateSignup() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  if (name === "" || email === "" || password === "") {
    alert("All fields required!");
    return false;
  }
  alert("Signup Successful!");
  window.location.href = "user_login.html";
  return false;
}

function validateAdmin() {
  const email = document.getElementById("adminEmail").value;
  const pass = document.getElementById("adminPass").value;
  if (email === "admin@smarttrack.ai" && pass === "admin123") {
    alert("Welcome Admin!");
    window.location.href = "admin_dashboard.html";
  } else {
    alert("Invalid Admin Credentials!");
  }
  return false;
}
