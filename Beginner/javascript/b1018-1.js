var input = require("fs").readFileSync("stdin", "utf8");

let value = parseInt(input);

let valueI = value;
console.log(valueI);
let notes = parseInt(valueI / 100);
console.log(`${notes} nota(s) de R$ ${100},00`);
valueI = valueI % 100;
notes = parseInt(valueI / 50);
console.log(`${notes} nota(s) de R$ ${50},00`);
valueI = valueI % 50;
notes = parseInt(valueI / 20);
console.log(`${notes} nota(s) de R$ ${20},00`);
valueI = valueI % 20;
notes = parseInt(valueI / 10);
console.log(`${notes} nota(s) de R$ ${10},00`);
valueI = valueI % 10;
notes = parseInt(valueI / 5);
console.log(`${notes} nota(s) de R$ ${5},00`);
valueI = valueI % 5;
notes = parseInt(valueI / 2);
console.log(`${notes} nota(s) de R$ ${2},00`);
valueI = valueI % 2;
notes = parseInt(valueI);
console.log(`${notes} nota(s) de R$ ${1},00`);