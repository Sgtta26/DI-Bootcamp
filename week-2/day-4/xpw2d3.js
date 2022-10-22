//ex1 - part1

function infoAboutMe(){
    let name = "sarah";
    let age = 21;
    let hobbies = "code";
    console.log(`${name} ${age} ${hobbies}`);
}

infoAboutMe();

//-part2

function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")


//ex2

function calculateTip(){
    let bill = prompt('What the amount of the bill ?');
    if(bill < 50){
        console.log(`tip 20%`);
    } else if(bill > 50 && bill < 200){
        console.log(`tip 15%`);
    } else if(bill < 200){
        console.log(`tip 10%`);
    }
}
//calculateTip()


//ex3

function isDivisible(){
    for(i =0; i<500; i++){
        if(i % 23 === 0){
            console.log(i);
        }
    }
}

isDivisible()


//ex4

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

const shoppingList =["banana", "orange", "apple"];

function myBill(){
    let totalbill = 0
    for (let fruit in stock){
        console.log(stock[fruit]);
        if(stock[fruit] > 0){
            console.log(prices[fruit]);
            totalbill += prices[fruit];
        }
    }
    return totalbill;
}
console.log(myBill());
let result = myBill()
console.log(result,'here');


//ex5

function changeEnough(itemPrice, amountOfChange){
    console.log(`The item price is ${itemPrice}`);

    const sum = calulateSum(amountOfChange)
    if(sum > itemPrice){
        console.log(`You can afford it`);
        return true
    } else {
        console.log(`You can't afford it`);
        return false
    }
    
}

function calulateSum(array){
    let sum = 0 
    for (let i=0; i < array.length; i++);{
        let coinValue
        const numberOfCoins = array[i]
        if (i === 0) {coinValue = 0.25}
        if (i === 1) {coinValue = 0.10}
        if (i === 2) {coinValue = 0.05}
        if (i === 3) {coinValue = 0.01}

        sum= sum + numberOfCoins * coinValue
    }

    return sum
}
changeEnough(4.25, [25, 20, 5, 0])


//ex6

function hotelCost(){

    // let answer = null 
    // while (typeof answer != "number"){

    // }
    const numberNight = prompt ("How many night you want to stay ?")
    console.log("numberNight")
}
hotelCost()