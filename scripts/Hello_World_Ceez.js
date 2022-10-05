// LANGUAGE: Javascript
// ENV: Node.js
// AUTHOR: Cesar Infante
// GITHUB: https://github.com/Cesar-Infante

console.log('Hello, World!');

// quick tutorial to get a nice scroll effect on your pages

/*
* If the element is within 150px of the bottom of the viewport, add the class 'active' to it,
* otherwise remove the class 'active' from it.
*/
function reveal() {
    let revealCards = document.querySelectorAll(".reveal");

    for (let i = 0; i < revealCards.length; i++) {
        let windowHeight = window.innerHeight;
        let elementTop = revealCards[i].getBoundingClientRect().top;
        let elementVisible = 150;

        if (elementTop < windowHeight - elementVisible) {
            revealCards[i].classList.add("active");
        } else {
            revealCards[i].classList.remove("active");
        }
    }
}

// what is need in the index.html is a class of reveal
/* Ex. class="reveal" */

//this is what is needed in the css file
 /* Making the elements appear on the page. */
// .reveal {
//     position: relative;
//     transform: translateY(150px);
//     opacity: 0;
//     transition: 1s all ease;
// }

/* Making the elements appear on the page. */
// .reveal.active {
//     transform: translateY(0);
//     opacity: 1;
// }