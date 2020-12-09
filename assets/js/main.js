// main js

const selection_menu = document.querySelector('li.selection');
const general_menu = document.querySelector('li.general');
const specialization_menu = document.querySelector('li.specialization');

const selection = document.querySelector('#selection');
const general = document.querySelector('#general');
const specialization = document.querySelector('#specialization');

const scrollElement = window.document.scrollingElement || window.document.body || window.document.documentElement;

selection_menu.addEventListener('click', () => {
    // use anime.js
    anime({
        targets: scrollElement,
        scrollTop: 0,
        duration: 500,
        easing: 'easeInOutQuad'
    });
});

general_menu.addEventListener('click', () => {
    // use anime.js
    anime({
        targets: scrollElement,
        scrollTop:general.offsetTop - 60,
        duration: 500,
        easing: 'easeInOutQuad'
    });
});

specialization_menu.addEventListener('click', () => {
    // use anime.js
    anime({
        targets: scrollElement,
        scrollTop:specialization.offsetTop - 60,
        duration: 500,
        easing: 'easeInOutQuad'
    });
});