const sentence =  "The movie is not that bad, I like it";

const wordNot = sentence.indexOf("not");

const wordBad = sentence.indexOf("bad");

console.log(wordNot);
console.log(wordBad);

if (wordBad > wordNot) {
    console.log(sentence.substring(0, wordNot) +" good "+ sentence.substring(wordBad +3, sentence.length));
}

