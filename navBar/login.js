const goBackLink = document.querySelector(".goBack");

goBackLink.addEventListener("click", handleGoBack);

function handleGoBack() {
  const back = confirm("Are you sure you want to go back to the main page ?");
  if (back) {
    // window.location.href = "index.html";
    window.history.back();
  }
}
