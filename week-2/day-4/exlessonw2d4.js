//  // enclose in a block an action
// // reuse this block without repeting yourself with many loops

//  //declare a fuction
//  function creaeChocolate(){
//     //statememt
//     console.log("I am creating a chocolate");
// }

// //invoke the function - call the function
// creaeChocolate()
// creaeChocolate()
// creaeChocolate()
// creaeChocolate()


// //function creaeChocolate(//parameter){}


// function creaeChocolate(typeChocolate){
//     //statememt
//     console.log(`I am creating ${typeChocolate} chocolate`);
// }

// creaeChocolate("dark");
// creaeChocolate("white");

// //calculate


// function calculator (first, second,operator){
//     let calculus;
//     if(operator === "add"){
//         calculus = first + second;
//     } else if (operator === "substract"){
//         calculus = first - second;
//     } else {
//         calculus = 0
//     } 
//     console.log("calculus is :, calculus");
// }

// calculator(34,65, "add");
// calculator(34,65, "substract");



// //ex slack


function quantity(number, name= "Client"){
    if (number>5 && number< 10 ){
        console.log(`Dear client, you won a bouquet of flowers`);
    } else if (number<10 && number< 20){
        console.log(`Dear ${name}, you won a bottle of wine`);
    } else if (number<20){
        console.log(`Dear ${name}, you won a trip to Paris`);
    }
}
quantity(5,"Sarah");
quantity(45,"Bob");
quantity(10,"Jojo");
quantity(7);




function quantity(number){
    if (number>5 && number< 10 ){
        return "Bouquet of flower";
    } else if (number>10 && number< 20){
        return "Bottle of wine";
    } else if (number>20){
       return "trip to Paris";
    }
}

function sendGift(){
    let gift = quantity(26) //ecrire  une quantite pour savoir quel gift envoyer
    console.log(`Dear client you will receive a ${gift}`);
}
sendGift();