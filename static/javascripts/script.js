const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");
const conversationThread = document.querySelector(".room__box");

if (dropdownMenu)
  dropdownButton.addEventListener("click", () => { dropdownMenu.classList.toggle("show"); });

if (conversationThread)
  conversationThread.scrollTop = conversationThread.scrollHeight;
