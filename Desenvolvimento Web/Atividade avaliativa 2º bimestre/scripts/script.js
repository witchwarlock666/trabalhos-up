const atv1 = () => {
    let n1 = parseInt(window.prompt("Digite o primeiro número"));
    let n2 = parseInt(window.prompt("Digite o segundo número"));

    if (n1 < n2) {
        alert(n1 + ", " + n2);
    }
    else {
        alert(n2 + ", " + n1);
    }
}

const atv2 = () => {
    let genero = window.prompt("Digite o seu gênero (M/F)");
    let altura = parseFloat(window.prompt("Digite a sua altura"));
    let peso = 0;

    genero.replace("m", "M");
    genero.replace("f", "F");

    if (genero = "M") {
        peso = (72.7 * altura - 58).toFixed(2);
        alert("Peso ideal: " + peso + "kg")
    }
    else if (genero = "F") {
        peso = (62.1 * altura - 44.7).toFixed(2);
        alert("Peso ideal: " + peso + "kg")
    }
    else {
        alert("Erro!");
    }
}

const atv3 = () => {
    let n = [];
    n[0] = parseInt(window.prompt("Digite o primeiro número"));
    n[1] = parseInt(window.prompt("Digite o segundo número"));
    n[2] = parseInt(window.prompt("Digite o terceiro número"));

    n = bubble(n);

    alert("Menor numero: " + n[0]);
}

const atv4 = () => {
    let n = parseInt(window.prompt("Digite o número"));

    if (n < 0) {
        n = Math.abs(n);
    }
    else {
        if (n % 2 == 0) {
            n = "Par"
        }
        else {
            n = "Impar"
        }
    }
    alert("Resultado: " + n)
}

const atv5 = () => {
    let str = "";

    let n = parseInt(window.prompt("Digite o número"));

    if (n % 2 == 0) {
        str += "O número é divisivel por 2. "
    }
    else {
        str += "O número não é divisivel por 2. "
    }
    if (n % 3 == 0) {
        str += "O número é divisivel por 3."
    }
    else {
        str += "O número não é divisivel por 3. "
    }

    alert(str);
}

const atv6 = () => {
    let str = "";

    let n = parseInt(window.prompt("Digite o número"));

    if (n % 2 == 0) {
        str += "O número é divisivel por 2. "
    }
    else {
        str += "O número não é divisivel por 2. "
    }
    if (n % 7 == 0) {
        str += "O número é divisivel por 7."
    }
    else {
        str += "O número não é divisivel por 7. "
    }

    alert(str);
}

const atv7 = () => {
    let dia = parseInt(window.prompt("Digite o dia"));
    dia = getDia(dia);
    alert(dia);
}

const atv8 = () => {
    soma = 0;
    for (i = 0; i <= 20; i++) {
        soma += i;
    }
    alert(soma);
}

const atv9 = () => {
    let n = parseInt(window.prompt("Digite o número"));
    let str = "";

    for (i = 1; i <= 10; i++) {
        if (i < 10) {
            str += n + " x " + i + " = " + n * i + ", ";
        }
        else {
            str += n + " x " + i + " = " + n * i;
        }
    }
    alert(str);
}

const atv10 = () => {
    let n = parseInt(window.prompt("Digite o número"));
    let ini = n

    if (n > 0) {
        for (i = n - 1; i > 0; i--) {
            n = n * i;
        }
    }
    else if (n == 0) {
        n = 1;
    }
    else {
        n = "Não existe";
    }

    alert(ini + "! = " + n);
}

const getDia = (dia) => {
    let dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
        'default': 'Erro!'
    };

    return dias[dia] || dias['default'];
}

const swap = (n, i, j) => {
    let temp = n[i];
    n[i] = n[j];
    n[j] = temp;
    return n;
}

const bubble = (n) => {
    for (i = 0; i < n.length - 1; i++) {
        for (j = 0; j < n.length - i - 1; j++) {
            if (n[j] > n[j + 1]) {
                n = swap(n, j, j + 1);
            }
        }
    }
    return n;
}

function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}
