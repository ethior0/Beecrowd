var input = require("fs").readFileSync("stdin", "utf8");

let value = parseInt(input);

const notes = [100, 50, 20, 10, 5, 2, 1];

console.log(value);

for (let n of notes) {
  let qNotes = parseInt(value / n);
  console.log(`${qNotes} nota(s) de R$ ${n},00`);
  value = value % n;
}