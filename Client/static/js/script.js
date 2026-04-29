//Hero Section
var heroSwiper = new Swiper(".heroSwiper", {
    effect: "fade",
    fadeEffect: {
        crossFade: true 
    },
    speed: 1500,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },

    loop: true,
});

function animateText(row) {
    const elementi = document.querySelectorAll(row);
    
    elementi.forEach(elemento => {
        const testo = elemento.innerText;
        elemento.innerHTML = ''; 

        testo.split('').forEach((lettera, indice) => {
            const span = document.createElement('span');
            span.innerHTML = lettera === ' ' ? '&nbsp;' : lettera; 
            span.style.animationDelay = `${indice * 0.04}s`; 
            elemento.appendChild(span);
        });
    });
}


animateText('.up-row');
animateText('.down-row');

window.addEventListener('load', function() {
    const sipario = document.getElementById('preloader'); 
    sipario.style.opacity = '0';
    
    setTimeout(() => { sipario.style.display = 'none'; }, 500); 
});

   const toggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.navbar-menu');

    toggle.addEventListener('click', () => {
        menu.classList.toggle('active');
        toggle.classList.toggle('active'); // <--- AGGIUNGI SOLO QUESTA RIGA!
    });
    // Apre e chiude il sottomenu (Azienda) su mobile
    document.querySelectorAll('.dropdown > .navbar-link').forEach(item => {
        item.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                this.parentElement.classList.toggle('active');
            }
        });
    });