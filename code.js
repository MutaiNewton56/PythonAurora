function mergeArrays(arr1, arr2) {
  let newArr = [...arr1, ...arr2];

  let ans = newArr.sort((a, b) => {
    return a - b;
  });

  let set = new Set(ans);

  return Array.from(set);
}

let a1 = [1, 3, 5, 7, 9, 11, 12];
let a2 = [1, 2, 3, 4, 5, 10, 12];
let ans = [1, 2, 3, 4, 5, 7, 9, 10, 11, 12];

let ans2 = mergeArrays(a1, a2);

console.log(ans);
console.log(ans2);
