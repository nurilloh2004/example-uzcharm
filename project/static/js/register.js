const username = document.querySelector('#username');
const feedBackArea = document.querySelector(".invalid_feedback");
const email = document.querySelector('#email');
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const submitBtn = document.querySelector(".submit-btn");

email.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    email.classList.remove("is-invalid");
    EmailFeedBackArea.style.display = "None";


    if (email.length > 0)
    {
        fetch("/authentication/validate-email", {
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                if (data.email_error) {
                    submitBtn.disabled = true;
                    email.classList.add("is-invalid");
                    EmailFeedBackArea.style.display = "block";
                    EmailFeedBackArea.innerHTML = '<p>${data.email_error}</p>';
                }
                else {
                    submitBtn.removeAttribute("disabled");
                }
            });
    }
});

username.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameSuccessOutput.textContent = `Checking  ${usernameVal}`;

    username.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res => res.json())
            .then(data => {
                console.log('data', data);
                if (data.username_error) {
                    username.classList.add("is-invalid");
                    feedBackArea.style.display = "block";
                    feedBackArea.innerHTML = '<p>${data.username_error}</p>';
                    submitBtn.disabled = true;
                }
            });
    }
});
