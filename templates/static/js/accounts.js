document.addEventListener("submit", (event) => {
  const formId = event.target.id;
  if (formId == "login-form") {
    event.preventDefault();
    handleLoginForm();
  } else if (formId == "register-form") {
    event.preventDefault();
    handleRegisterForm();
  }
});

function handleLoginForm() {
  /*Handling Login Form */
  const username = document.querySelector("input[name=username]").value;
  const password = document.querySelector("input[name=password]").value;
  postRequest(
    "/accounts/login/",
    { username: username, password: password },
    accountSuccess
  );
}

function handleRegisterForm() {
  /*Handling Register Form */
  const username = document.querySelector("input[name=username]").value;
  const password = document.querySelector("input[name=password]").value;
  postRequest(
    "/accounts/register/",
    { username: username, password: password },
    accountSuccess
  );
}
function accountSuccess(content) {
  triggerToast(content.message);
  setTimeout(() => {
    if (window.location.pathname.includes("/register/")) {
      window.location.pathname = "/accounts/login";
    }
  }, 5000);
}
function triggerToast(content) {
  const toast = `<div class="absolute top-0 end-0 m-5" id="toast-messages">
    <div role="alert" class="alert alert-info">
        <i class="fa fa-info-circle"></i>
        <span>
            <strong>${content}</strong>
        </span>
        <i class="fa fa-xmark scale-95 hover:scale-100 hover:rotate-90 delay-50 duration-300 transition" id="alert-close"></i>        
    </div>
</div>`;
  const triggerMessage = document.getElementById("triggerMessage");
  triggerMessage.innerHTML = toast;
  setTimeout(() => {
    $("#toast-messages").fadeOut();
  }, 5000);
}

document.addEventListener("click", (event) => {
  if (event.target.id == "alert-close") {
    $("#toast-messages").fadeOut();
  }
});
