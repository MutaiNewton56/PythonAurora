console.log(document);
function sum(obj) {
  let keys = Object.keys(obj);
  console.log(obj);
  console.log(keys);

  let total = 0;
  for (let i = 0; i < keys.length; i++) {
    total = total + obj[keys[i]];
  }
  console.log(total);
  return total;
}

sum({ a: 0, b: 2, c: 34, d: 34, e: -70 });
