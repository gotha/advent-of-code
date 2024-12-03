const fs = require("fs");

if (process.argv.lenght < 3) {
  console.log("please specify input file")
  process.exit(1);
}

const colours_max = {"red": 12, "green": 13, "blue": 14};
const data = fs.readFileSync(process.argv[2]).toString().split("\n").filter(i => i != "")
let total = 0;
outer:
for (let line of data) {
  [p1, p2] = line.split(":");
  [_, gameNumber] = p1.split(" ");
  for (const [_, num, colour] of line.split(":").pop().matchAll(/([0-9]+)\s(blue|green|red)(,|;|$)/g)) {
    if (num > colours_max[colour]) {
      continue outer;
    }
  }
  total += parseInt(gameNumber);
}
console.log(total);
