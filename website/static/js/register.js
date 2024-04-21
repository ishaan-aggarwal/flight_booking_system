const signupLink = document.getElementById("signup-link");
const loginContainer = document.querySelector(".login-container");
const signupContainer = document.querySelector(".signup-container");

signupLink.addEventListener("click", () => {
  loginContainer.style.display = "none";
  signupContainer.style.display = "block";
});

document.getElementById("signupForm").addEventListener("submit", (e) => {
  e.preventDefault();
  loginContainer.style.display = "block";
  signupContainer.style.display = "none";
});
