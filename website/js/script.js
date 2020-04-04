'use strict';

const tab = document.querySelectorAll("button");
const panel = document.querySelectorAll(".inside-container");

function tabClick(event) {
    for (let i = 0; i < tab.length; i++) {
        tab[i].classList.remove("active");
        console.log(tab[i]);
    }
    for (let i = 0; i < panel.length; i++) {
        panel[i].classList.remove("active");
        console.log(panel[i]);
    }
    event.target.classList.add('active');
    let classString = event.target.getAttribute('data-target');
    document.getElementById('tabs-content').getElementsByClassName(classString)[0].classList.add("active");
}
for (let i = 0; i < tab.length; i++) {
    tab[i].addEventListener('click', tabClick, false);
}
