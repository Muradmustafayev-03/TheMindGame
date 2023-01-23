let barBtn = document.getElementsByClassName("user_img")
let closeMenu = document.getElementsByClassName("close_menu")
let menu = document.getElementsByClassName("user_profile")
barBtn.addEventListener("click", function (e) {
  e.preventDefault()
  menu.classList.add("active")
})
closeMenu.addEventListener("click", function (e) {
  e.preventDefault()
  menu.classList.remove("active")
})