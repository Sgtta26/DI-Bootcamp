// //ex1 - part1

// setTimeout(hello, 2000)

// function hello (){
//     alert("Hello World");
// }

// // -part2

// setTimeout(addPara, 2000)

// function addPara (){
//     const p = document.createElement("p");
//     p.textContent = "Hello World"
//     document.getElementById('container').appendChild(p);
// }

// // -part3

// setInterval(para, 2000)

// function para (){
//     const p = document.createElement("p");
//     p.textContent = "Hello World"
//     document.getElementById('container').appendChild(p);
// }

// let id = setInterval(para, 2000)

// let counter = 3
// function para(){   
//     if (counter > 0){
//         console.log(counter);
//         counter--
//     } else { 
//         clearInterval(id)
//     }
   
// }




//ex2:


function myMove (){
    setInterval(game, 5)
}

const span = document.getElementById("animate");
let counter1 =0;

function game(){
    counter1++ ;
    if( counter1 <= 350){
        span.style.left = counter1+'px';
    } else {
        clearInterval(animate);
    }
}