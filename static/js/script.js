document.querySelector("#create-user").addEventListener("click", function(){
    document.querySelector(".createUser-popup").classList.add("active");
});

document.querySelector(".createUser-popup .close-btn").addEventListener("click", function(){
    document.querySelector(".createUser-popup").classList.remove("active");
});