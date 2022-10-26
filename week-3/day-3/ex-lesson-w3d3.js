// // mettre un timer (temps chrono):

// //syntaxe
// setTimeout(function to call, time cb de temps elle part en seconde)

// setTimeout(sayHi, 1000) //the function sayHi is going to run after 1sec 1000=1sec
// function sayHi (){
//     console.log("Hello");  //Hello apparait 1 sec apres l'ouverture de l'ecran
// }

// //retrieve the button
// const bouton = document.getElementById("btn");
// bouton.addEventListener("click", start)

// function start (){
//     console.log("starting");
//     setTimeout(sayHi,2000); // call the function after 2 sec
// }

//function sayHi (){
//   console.log("hello");
//}

//ex : faire apparaitre un message apres 5 sec sur le site - (display:none = invisible / display="block" = apparait) 

// setTimeout(sale, 5000)

// function sale (){
//     console.log("Last sales end in 10min !"); 
//     let div = document.getElementById("div"); //le div existe deja dans html sinon doit creer un div avec:
//     // const div = document.createElement("div");
//     // div.textContent = "exemple";
//     // document.body.appendChild(div);
//     div.style.display = "block"
// }


// //syntaxe
// setInterval(function to call,delay) //i want to call the sayHi functon(hello) EVERY second
// clearInterval (index of the interval) // stoper la repetition de hello

// setInterval(sayHi, 1000); 

// function sayHi(){
//     console.log("hello");
// }


// //ex:


setTimeout(sale, 1000)

let timer;
function sale (){
    let div = document.getElementById("div"); 
    div.style.display = "block"
    
    timer = setInterval(decreaseCounter, 1000);
}

const span = document.getElementById("num");
let counter1 = 10;

function decreaseCounter(){
    counter1 --;
    if( counter1 >= 0){
        span.textContent = counter1;
    } else {
        clearInterval(timer);
    }
}
