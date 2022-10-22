//dailychallenge !!!


// const loops = A
// for (let counter = 1; counter <=6 ; counter++) {  
//     if(counter <=6 )
//         console.log(`${counter}`);
//     else  {
//         console.log(`${counter}`);
//     }
// }

//SOLUTION video:
// const maxNumber = 6

// for (let i = 0;i < maxNumber; i++){
//     const numberOfStars =i + 1
//     let lineOfStars =""
// for(let counter =0;counter <numberOfStars; counter++){
//       lineOfStars +="*"
//     }
//     console.log(lineOfStars)
// }



//SOLUTON LISE !:
    // before the loop

// let pattern = "";
// const stars = "*"

// for (let counter = 1; counter <= 6; counter++){
//     //let pattern = ""; c'est faut de l'ecrire a l'interieur car sinon la boucle recommence de zero(="") a chaque fois et pas de +1*
//     pattern += stars;
//     console.log(pattern)
// }




//SOLUTION + FACILE:
for (let counter = 1; counter<= 6; counter ++){
    patternThree= "*".repeat(counter);
    console.log(patternThree)
}