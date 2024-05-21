var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split(' ');

const N = Number.parseInt(lines[0]);
const L = Number.parseInt(lines[1]);

console.log(N*L);