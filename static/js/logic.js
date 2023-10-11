function ejecutarEvento() {
    var textabout = document.getElementById('text-about');

    if (window.innerWidth <= 768) {
        textabout.classList.remove('col-6');
        textabout.classList.add('col-12');
    } else {
        textabout.classList.remove('col-12');
        textabout.classList.add('col-6');
    }
}

function verificarTamañoPantalla() {
    if (window.innerWidth <= 768) {
        ejecutarEvento();
    }
}

// Llama a verificarTamañoPantalla cuando se carga la página
verificarTamañoPantalla();

// Llama a verificarTamañoPantalla cuando se redimensiona la ventana
window.addEventListener("resize", verificarTamañoPantalla);