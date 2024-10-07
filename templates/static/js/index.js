/*Toast Messages Autohide */
$(document).ready(() => {
  const toastElem = document.getElementById("toast-messages");
  if (toastElem) {
    /**Automatically Hide Toast */
    setTimeout(() => {
      $("#toast-messages").fadeOut();
    }, 5000);
  }
});
