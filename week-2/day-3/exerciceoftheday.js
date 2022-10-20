//ex1-part1

const people = ["Greg", "Mary", "Devon", "James"];
    //console.log(people);
people.shift()
    //console.log(people);
people.splice(2,1,"Jason");
    //console.log(people);
people.push("Sarah");
    //console.log(people);
    console.log(people.indexOf("Mary"));

console.log(people.slice(1,3));
console.log(people.indexOf("Foo")); //-1 because is doesnt exist

const last = people.length
    console.log(last);

//-part2

for( let name in people){
    console.log(name)
}

for( let name in people){
    console.log(name)
    if (name === "Jason"){
        break;
    }
}


//ex2

const colors = ["blue", "black", "red", "green","purple"];

for (let pink in colors){
    console.log(colors[pink]);
}


//ex3 peut pas finir on a pas fait loop while

// let userWant = prompt("Choose a number ?")
//     console.log(typeof userWant);

//     for (let counter = 1; counter <10; counter++) {
//         if(counter <10 )
//             console.log(`${counter} is choose number bigger thant 10`);
//         // else  {
//         //     console.log(`${counter} `);
//         // }
//     }


//ex4

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor,building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants [1]+ building.numberOfRoomsAndRent['dan']);

if (building.numberOfRoomsAndRent.sarah [1] +building.numberOfRoomsAndRent.david [1] > building.numberOfRoomsAndRent.dan [1]){
    building.numberOfRoomsAndRent.dan [1] = 1200
}
    console.log(building)



//ex5

const family = {
    father: "titi",
    mother: "jojo",
    sister: "elsa",
    me: "sarah",
};

for (const key in family) {
  console.log(`${key} ${family[key]}`);
}


//ex6

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  for (const key in details) {
    console.log(`${key} ${details[key]}`);
  }


//ex7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
console.log(names);

let group = ""
for (const letter in names){
    group +=  names[letter][0]
}
console.log(group);