var input = require("fs").readFileSync("stdin", "utf8");

var valor = parseFloat(input);

const notes = [100, 50, 20, 10, 5, 2];
const coins = [100, 50, 25, 10, 5, 1];

console.log("NOTAS:")

for (let n of notes) {
  let qNotes = parseInt(valor / n);
  console.log(`${qNotes} nota(s) de R$ ${n}.00`);
  valor = valor % n;
}

console.log("MOEDAS:")
valor = Math.round(valor * 100);

for (let m of coins) {
  let qCoins = parseInt (valor / m)
  if (m <= 5) {
    console.log(`${qCoins} moeda(s) de R$ 0.0${m}`);
  } else if (m == 100) {
    console.log(`${qCoins} moeda(s) de R$ 1.00`);
  } else {
    console.log(`${qCoins} moeda(s) de R$ 0.${m}`);
  }
  valor = valor % m;
}