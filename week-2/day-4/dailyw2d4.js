// const answer = prompt("few words separated by commas:");

// const words = answer.split(",");

// let lengthLongestWord =0
// for (const mot of words){
//     console.log(mot);
//     const wordLength = mot.length;
// }


// let promtString = prompt ("Put Words separeted by commas");

// let words = promtString.split(",");
// let maxLength = 0;
// for (let i = 0; i < words.length; i++) {
//     if (words[i].length > maxLength) {
//     maxLength = words[i].length;
//     }
// }

// for (let i = 0; i < words.length; i++) {
//     if (i === 0) {
//         console. log("*".repeat (maxLength + 2));
//     }
//     console. log("*"+ words [i]+ "".repeat(maxLength - words[i].length) + "*");

//     if (i === words-length - 1) {
//         console. log("*".repeat(maxLength + 2));
//     }
//  if (i === 0) {
//      console. log("*".repeat (maxLength + 2));
//  }
// }


//  function printWords(words){
//      firstAndLast();
//      for (let word of words){
//          console.log(`*` ${word + ' '.repeat(max - word.length)} *`);
//      }
//       fistAndLast();
//  }

//  function firstAndLast() {
//     console.log("*".repeat(max +4));
//  }


const promptInput = prompt("Enter comma separated words");
const words = promptInput.split(",");
function findLongestWord() {
    //find the longest word
    let max = 0;
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > max) {
            max = words[i].length;
        }
    }
    return max;
}
function printWords(words,max) {
    firstAndLast(max);
    for (let word of words) {
        console.log(`* ${word + ' '.repeat(max - word.length)} *`);
    }
    firstAndLast(max);

}
function firstAndLast(max) {
    console.log('*'.repeat(max + 4));
}
printWords(words,findLongestWord());