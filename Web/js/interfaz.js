var datosproyecto = [];

function agregardatosproyecto(proyectotitulo, puntajeproyecto,) {
    
    var nuevoproyecto = {
        title: proyectotitulo,
        puntaje: puntajeproyecto,
    };

    console.log(nuevoproyecto); 
    datosproyecto.push(nuevoproyecto);
}

function obtenerlistapuntajes() {
    return datosproyecto;
}