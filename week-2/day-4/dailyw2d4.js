// const answer = prompt("few words separated by commas:");

// const words = answer.split(",");

// let lengthLongestWord =0
// for (const mot of words){
//     console.log(mot);
//     const wordLength = mot.length;
// }


let promtString = prompt ("Put Words separeted by commas");

let words = promtString.split(",");
let maxLength = 0;
for (let i = 0; i < words.length; i++) {
    if (words[i].length > maxLength) {
    maxLength = words[i].length;
    }
}

for (let i = 0; i < words.length; i++) {
    if (i === 0) {
        console. log("*".repeat (maxLength + 2));
    }
    console. log("*"+ words [i]+ "".repeat(maxLength - words[i].length) + "*");

    if (i === words-length - 1) {
        console. log("*".repeat(maxLength + 2));
    }
    if (i === 0) {
        console. log("*".repeat (maxLength + 2));
    }
}

