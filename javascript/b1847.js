var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split(' ');

const A = Number.parseInt(lines[0]);
const B = Number.parseInt(lines[1]);
const C = Number.parseInt(lines[2]);

if (A > B && C >= B) console.log(":)");
else if (A < B && B >= C) console.log(":(");
else if (A < B && (C - B) < (B - A)) console.log(":(");
else if (A < B && (C - B) >= (B - A)) console.log(":)");
else if (A > B && (B - C) < (A - B)) console.log(":)");
else if (A > B && (B - C) >= (A - B)) console.log(":(");
else if (A === B) {
  if (C > B) console.log(":)");
  else console.log(":(");
} 