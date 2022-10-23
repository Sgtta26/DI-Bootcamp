let numberOfBeers = Number(prompt("How many beers you want ?"))

let numberOfBeersToTakeAway = 1;

while(numberOfBeers >0 ){
    const stanza = makeStanza(numberOfBeers, numberOfBeersToTakeAway);
    console.log(stanza);
    numberOfBeers = numberOfBeers - numberOfBeersToTakeAway
    numberOfBeersToTakeAway = numberOfBeersToTakeAway +1;
}

function makeStanza(numberOfBeers, counter){
//console.log('this is number more than 1 ?', inPlural(numberOfBeers));


const bottleOrBottles = getBottleOrBottles(numberOfBeers)

if(numberOfBeers-counter <=0){
    counter = numberOfBeers;
}
const stanza = `${numberOfBeers} ${bottleOrBottles} of beer on the wall
${numberOfBeers} ${bottleOrBottles} of beer
Take ${counter} down, pass it around
${numberOfBeers - counter } ${getBottleOrBottles(numberOfBeers - counter )} of beer on the wall`


return stanza;
}

function inPlural(numberOfBeers){
    if (numberOfBeers > 1){
        return true;
    } else {
        return false;
    }

}

function getBottleOrBottles(numberOfBeers){
    if (inPlural(numberOfBeers)) {
        return "bottles";
    } else {
        return "bottle";
    }
}

//console.log("stanza",stanza);