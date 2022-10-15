// It's a Scroll Top Button for websites
// You can use this button for going to the top of a website on one click
// my name is aasish and my git-hub user name is aasish47



// here u are accessing the button which u will use as the scroll top button, and it should have its id as id = "top-btn"
let myBtn = document.getElementById("top-btn");

// here i m defining a topFunction
function topFunction(){
    // use it for safari
    document.body.scrollTop = 0;
    // use it for windows
    document.documentElement.scrollTop = 0;
}

// then u have to add some html and css to make it look better and also to fix it some where in the webpage.