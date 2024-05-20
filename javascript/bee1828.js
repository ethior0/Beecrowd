var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.trim().split('\n');
lines.shift();
let cc = 1;

const quemGanhou = (jog1, jog2) => {
  if (jog1 === "pedra" && jog2 === "tesoura") return 1;
  if (jog1 === "tesoura" && jog2 === "pedra") return 2;
  if (jog1 === "tesoura" && jog2 === "papel") return 1;
  if (jog1 === "papel" && jog2 === "tesoura") return 2;
  if (jog1 === "papel" && jog2 === "pedra") return 1;
  if (jog1 === "pedra" && jog2 === "papel") return 2;
  if (jog1 === "pedra" && jog2 === "lagarto") return 1;
  if (jog1 === "lagarto" && jog2 === "pedra") return 2;
  if (jog1 === "lagarto" && jog2 === "Spock") return 1;
  if (jog1 === "Spock" && jog2 === "lagarto") return 2;
  if (jog1 === "Spock" && jog2 === "tesoura") return 1;
  if (jog1 === "tesoura" && jog2 === "Spock") return 2;
  if (jog1 === "tesoura" && jog2 === "lagarto") return 1;
  if (jog1 === "lagarto" && jog2 === "tesoura") return 2;
  if (jog1 === "lagarto" && jog2 === "papel") return 1;
  if (jog1 === "papel" && jog2 === "lagarto") return 2;
  if (jog1 === "papel" && jog2 === "Spock") return 1;
  if (jog1 === "Spock" && jog2 === "papel") return 2;
  if (jog1 === "Spock" && jog2 === "pedra") return 1;
  if (jog1 === "pedra" && jog2 === "Spock") return 2;
}

while (lines.length) {
  const partida = lines.shift().split(" ");
  const jog1 = partida[0].trim();
  const jog2 = partida[1].trim();

  if (jog1 === jog2) {
    console.log(`Caso #${cc}: De novo!`);
  } else if (quemGanhou(jog1, jog2) === 1) {
    console.log(`Caso #${cc}: Bazinga!`);
  } else if (quemGanhou(jog1, jog2) === 2) {
    console.log(`Caso #${cc}: Raj trapaceou!`);
  }
  cc++;
}