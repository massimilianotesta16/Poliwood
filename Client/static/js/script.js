//Hero Section
var heroSwiper = new Swiper(".heroSwiper", {
    effect: "fade",       // Dissolvenza invece di scorrimento (MOLTO più elegante)
    fadeEffect: {
        crossFade: true   // Evita che si veda lo sfondo bianco durante il cambio
    },
    speed: 1500,          // La dissolvenza dura 1.5 secondi (morbida)
    autoplay: {
        delay: 5000,      // Cambia immagine ogni 5 secondi
        disableOnInteraction: false,
    },

    loop: true,
});