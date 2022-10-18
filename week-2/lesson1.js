//ex lesson
const adressNumber = 10;
const adressStreet = "geva";
const country = "france";


//let globalAdress = "I live in " + adressNumber + " " + adressStreet + " in " + country
const globalAdress = `I live in ${adressNumber} ${adressStreet}, in ${country}`
//console.log(globalAdress);
console.log(globalAdress);



//ex lesson

const birthYear = 2001;
const futureYear = 2055;
let age = futureYear - birthYear;
console.log(`I will be ${age} in ${futureYear}`)


//ex1

const favoriteFood = "pasta";
const favoriteMeal = "lunch";
let eat = `I eat ${favoriteFood} at every ${favoriteMeal}`
console.log(eat)


//ex2


const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length
const myWatchedSeriesSentence = myWatchedSeries[0] + ", " + myWatchedSeries[1] + ", and " + myWatchedSeries[2];
console.log(myWatchedSeriesSentence) 
const newSentence = "I watched "+myWatchedSeriesLength+" series :" + myWatchedSeriesSentence
console.log(newSentence)

myWatchedSeries[2] = "friends"
console.log(myWatchedSeries)

myWatchedSeries.push("you")
console.log(myWatchedSeries)

//myWatchedSeries.unshift();
delete myWatchedSeries [0]
console.log(myWatchedSeries)

console.log(myWatchedSeries[1][3]);
console.log(myWatchedSeries)

//ex3

const temperature = 36;
console.log(temperature + "°C is " + temperature + "°F ");
console.log(`${temperature}°C is ${(temperature / 5) * 9 + 32 }°F`)


//ex4

let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: it will output 55, because 34 and 21 are numbers
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: it will output 23, because 2 and 21 are numbers
    // Actual: 23
    // value of c is undefined

    console.log(3 + 4 + ' 5');
    // Prediction: 75 because 3 and 4 are number and '5' is sentence
    // Actual: 75


//ex5


typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: decimal number
// Actual: decimal number

typeof(NaN)
// Prediction: not a number 
// Actual: not a number 

typeof("hello")
// Prediction: sentence
// Actual: text

typeof(true)
// Prediction: boolean
// Actual:1

typeof(1 != 2)
// Prediction: true
// Actual: true

"hamburger" + "s"
// Prediction: sentence
// Actual: sentence

"hamburgers" - "s"
// Prediction: NaN
// Actual: not a number 

"1" + "3"
// Prediction: 4
// Actual: sentence

"1" - "3"
// Prediction: -2
// Actual: sentence

"johnny" + 5
// Prediction: NaN
// Actual: not a number

"johnny" - 5
// Prediction:NaN
// Actual: not a number

99 * "hello"
// Prediction: NaN
// Actual:not a number

1 != 1
// Prediction: false because 1=1
// Actual:false

1 == "1"
// Prediction: true
// Actual: true

1 === "1"
// Prediction: false
// Actual: false



//ex6 


5 + "34"
// Prediction:534
// Actual: because 5 is a number and 34 sentence

5 - "4"
// Prediction: 54
// Actual: 1 

10 % 5
// Prediction:2
// Actual:0

5 % 10
// Prediction:0,5
// Actual:5

"Java" + "Script"
// Prediction: JavaScript
// Actual: because it is two texts

" " + " "
// Prediction: nothing
// Actual: nothing is rigth inside

" " + 0
// Prediction: 0
// Actual: nothing + 0 = 0

true + true
// Prediction: 2 
// Actual: 2 because true=1 so 1+1=2

true + false
// Prediction:1
// Actual:2 because true=1 and false=0 so 1+0=1

false + true
// Prediction:1
// Actual: 1 because true=1 and false=0 so 0+1=1

false - true
// Prediction:-1
// Actual:-1 because true=1 and false=0 so 0-1=-1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction:-1
// Actual: -1 because calculation

"Bob" - "bill"
// Prediction:NaN
// Actual: NaN because they are not number