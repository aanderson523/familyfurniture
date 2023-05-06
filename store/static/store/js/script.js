

const menu = document.querySelector('.menu');
const closeMenu = document.querySelector('.closeMenu');
const openMenu = document.querySelector('.openMenu');
const subMenuOpen = document.querySelector('.subMenuOpen')
const subMenu = document.querySelector('.subMenu')

openMenu.addEventListener('click',show)
closeMenu.addEventListener('click',close)
subMenuOpen.addEventListener('click', show)

function show(){
    menu.style.display = 'flex';
    menu.style.top = '0';
}

function close(){
    menu.style.top = '-100%';
}

