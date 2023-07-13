function clickHome() {
  document.getElementById("home").scrollIntoView();
}

function clickAbout() {
  document.getElementById("aboutus").scrollIntoView();
}

function clickService() {
  document.getElementById("services").scrollIntoView();
}

function clickContact() {
  document.getElementById("contact").scrollIntoView();
}

function clickLogin() {
  const leave = confirm(
    "Are you sure you want to leave this page and get redirected to login page ?"
  );
  if (leave) {
    window.location.href = "login.html";
  }
}
