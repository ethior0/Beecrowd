var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

while (lines.length > 1) {
  let nums = lines.shift().split(' '),
      num1 = Number(nums[0]), num2 = Number(nums[1]);

  console.log(num1 * 2 * num2 + 0);
}