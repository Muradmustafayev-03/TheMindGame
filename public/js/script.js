let signInBtn = document.getElementsByClassName("sign-in")
let signUpBtn = document.getElementsByClassName("sign-up")
let nickName = document.getElementsByClassName("nickname")
console.log({ signInBtn }, { signUpBtn }, { nickName })

signInBtn.addEventListener("click", function (e) {
  e.preventDefault()
  signUpBtn.classList.remove("active_btn")
  signInBtn.classList.add("active_btn")
  nickName.classList.add("none")
})
signUpBtn.addEventListener("click", function (e) {
  e.preventDefault()
  signInBtn.classList.remove("active_btn")
  signUpBtn.classList.add("active_btn")
  nickName.classList.remove("none")
})

let filter = document.querySelector(".check")
let pass = document.querySelector(".pass_input")

filter.addEventListener("click", function () {
  console.log(this.checked);
  if (this.checked === true) {
    pass.type = "text"
  } else {
    pass.type = "password"

  }
})