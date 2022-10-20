//dailychallenge !!!


// const loops = A
// for (let counter = 1; counter <=6 ; counter++) {  
//     if(counter <=6 )
//         console.log(`${counter}`);
//     else  {
//         console.log(`${counter}`);
//     }
// }


const maxNumber = 6

for (let i = 0;i < maxNumber; i++){
    const numberOfStars =i + 1
    let lineOfStars =""
for(let counter =0;counter <numberOfStars; counter++){
      lineOfStars +="*"
    }
    console.log(lineOfStars)
}