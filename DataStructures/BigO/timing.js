// Function that adds up to n
// 5+4+3+2+1+0

// Solved up to n
// This is the most optimum solution.

function uptoN(n) {
  let total = 0; //1 Assignment Operation a
  // i=0 b operation; ccomparision ; daddition
  for (let i = 0; i <= n; i++) {
    //e and f
    console.log(`total=${total} And i${i}`);
    total = total + i; // adding 1, assignmentr
  }
  console.log(`for n=${n}, total=${total}`); // operation
  return total; //opration
}

// 4o+n(20)
// a+b+c+d+n(e+f)=> 4O+n(2O)
// BIG FOCUS NIJA
// 40=> section a
// N(20) -> section B

// if n =10
// 1000

// n(20)

// n
//n =0, t=0
// n=10, t=10
// BIG 0 function o(n)

// Linear Time

// n=50, t=4
// n=10000, t=35

// let start_time = Date.now();
// console.log("Start time: " + start_time);
// uptoN(100000000);
// let end_time = Date.now();
// console.log("End time: " + end_time);
// let diff = end_time - start_time;
// console.log("Diff: " + diff);

// spouces

const users = [
  {
    user: "Sam",
    spouces: ["a", "b", "c", "d", "e"],
  },
  {
    user: "Joan",
    spouces: ["ja", "jb", "jc", "jd", "je"],
  },
  {
    user: "Samson",
    spouces: ["delilah", "philistines", "jc", "jd", "je"],
  },
];

function sendEmails() {
  const allEmails = []; // a=assignment to all emails
  // b,c,d
  for (let i = 0; i < users.length; i++) {
    const user = users[i]; // e
    const spouces = user.spouces; //f

    // g,h,i
    for (let j = 0; j < spouces.length; j++) {
      const spouce = spouces[j]; // j
      //   console.log(`user ${user.user} ${spouce}`);
      email = `From ${user.user}
       Sorry for heart break ${spouce} `; // k
      allEmails.push(email); // l
    }
  }
  console.log(allEmails); //m
}

function sayHello() {
  console.log("Hello World"); //O(1)
}

// a+b+c+d+users(e+f+g+h+i+spouces(j+k+l))+m
// 5op+users(50p+spouces(3ops))
//users(spouces)
// 5n+users(50n+spouces(3n))
// users(spouces)
// n*n => n^2

sendEmails();
