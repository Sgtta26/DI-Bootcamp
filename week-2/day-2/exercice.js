//ex1

let x = 5;
let y = 2;

if(x > y) {
    console.log("x is the biggest number");
}

if(y > x) {
    console.log("y is the biggest number");
}

//ex2

const newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog) {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}


//ex3

const number = prompt("Choose a number")

 console.log(number);
 if (number % 2 == 0) {
    console.log(`${number} is an even number`);
 } else {
    console.log(`${number} is an odd number`);
 }


//ex4

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
    console.log(users.length);

if(users.length == 0) {
    console.log("No one is online");
}
else if(users.length == 1) {
    console.log(`${users[0]} is on line`);
}
else if(users.length == 2) {
    console.log(`${users[0]} and ${users[1]} are on line`);
}
else {
    console.log(`${users[0]} and ${users[1]} and${users.length - 2} more are on line`);
}