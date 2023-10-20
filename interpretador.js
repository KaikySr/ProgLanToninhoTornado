const printNaTela = 333
const sumValores = 444
const subValores= 555
const divValores = 666
const multValores = 777
const ifValores = 888
const endComando = 999 

const CodigoInteiro = process.argv.slice(2).map(Number); // Recebendo a lista do Python

let i = 0;
while (i < CodigoInteiro.length) {
    const command = CodigoInteiro[i];
    let content = "";
    i++;

    while (CodigoInteiro[i] !== endComando) {
        content += String.fromCharCode(CodigoInteiro[i]);
        i++;
    }

    switch (command) {
        case printNaTela:
            console.log(content);
            break;
        case sumValores:
            const sum = content.split('+').reduce((acc, val) => acc + parseFloat(val), 0);
            console.log(sum);
            break;
        // case subValores:
        //     const sub = content.split('-').reduce((acc, val) => acc - parseFloat(val), 0);
        //     console.log(sub);
        //     break;
        // case divValores:
        //     const div = content.split('/').reduce((acc, val) => acc / parseFloat(val), 0);
        //     console.log(div);
        //     break;
        // case multValores:
        //     const mult = content.split('*').reduce((acc, val) => acc * parseFloat(val), 0);
        //     console.log(mult);
        //     break;
        case ifValores:
            const [condition, action] = content.split(')');
            if (eval(condition.split('vouTerQueRepetirIvetoSangalo(')[1])) {
                // Aqui, estamos assumindo que a ação é um comando de impressão. 
                // Você pode expandir isso para lidar com outras ações.
                console.log(action.split('vejasocagatronco("')[1]);
            }
            break;
        default:
            console.log("default");
        // Adicione mais cases para outros comandos aqui
    }
    i++; // Avançar após o endComando
}
