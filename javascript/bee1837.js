var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split(' ');

let a = Number.parseInt(lines[0]);
let b = Number.parseInt(lines[1]);
let q = Number.parseInt(Math.trunc(a / b));
let r = Number.parseInt(a % b);

if (a < 0 && b < 0 && a % b !== 0) {
  console.log(q + 1, Number.parseInt(Math.abs(b) + r));
} else if (a < 0 && b > 0) {
  if (a % b === 0) {
    console.log(q, r);
  } else {
    console.log(q - 1, b + r);
  }
} else {
  console.log(q, r);
}

// -988 19 -> -52 0 (sol)