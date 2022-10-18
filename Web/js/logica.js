document.querySelector('#btnSubmit').addEventListener('click', guardardatosproyecto);
imprimirTabla();


function guardardatosproyecto() {
    var guardarproyectotitulo = document.querySelector('#title').value,
        guardarpuntajeproyecto = document.querySelector('#puntaje').value;

    
    agregardatosproyecto(guardarproyectotitulo, guardarpuntajeproyecto);
    imprimirTabla();
}

function imprimirTabla() {
    var lista = obtenerlistapuntajes(),
    tbody = document.querySelector('#tablaproyecto tbody');

    tbody.innerHTML = '';

    for (var i = 0; i < lista.length; i++) {
        var row = tbody.insertRow(i),
            tituloCelda = row.insertCell(0),
            directorCelda = row.insertCell(1);
        
        tituloCelda.innerHTML = lista[i].title;
        directorCelda.innerHTML = lista[i].puntaje;


        tbody.appendChild(row);
    }
}