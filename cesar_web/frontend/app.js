function cifradoCesar(texto, llave) {
    const alfabeto = 'abcdefghijklmnopqrstuvwxyz';
    let resultado = '';
    for (let char of texto) {
        if (alfabeto.includes(char)) {
            const pos = alfabeto.indexOf(char);
            const nuevaPos = (pos + llave) % 26;
            resultado += alfabeto[nuevaPos];
        } else {
            resultado += char;
        }
    }
    return resultado;
}

function animarTexto(texto, elemento) {
    elemento.textContent = '';
    let i = 0;
    function animar() {
        if (i < texto.length) {
            elemento.textContent += texto[i];
            i++;
            setTimeout(animar, 100);
        }
    }
    animar();
}

function cifrar() {
    const input = document.getElementById('entrada').value.toLowerCase();
    const llave = parseInt(document.getElementById('llave').value) || 3;
    const cifrado = cifradoCesar(input, llave);
    const resultado = document.getElementById('resultado');
    animarTexto(cifrado, resultado);

    fetch('/guardar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ original: input, cifrado })
    });
}
