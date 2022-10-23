// function playTheGame() {
//     confirm("Would you like to play a game ?");
// }

function playTheGame() {
    let text = "Would you like to play a game ?\n YES or NO";
    if (confirm(text) == true) {

      number = prompt("Enter a number between 0 and 10")
        if ( isNaN(number)){
        alert("Sorry Not a number, Goodbye")

        } else if (number >10 ){
        alert("Sorry it’s not a good number, Goodbye")

        } else if  (number <= 10 && number > 0) {
            const computerNumber = Math.random(5) 
            // if(computerNumber > number ){
            //     console.log("Your number is small");
            // }
            compareNumbers(number, computerNumber)
        }
        

    } else {
        alert("No problem, Goodbye")
    }
  }

  function compareNumbers(userNumber,computerNumber) {

    if (userNumber === computerNumber){
    alert("WINNER")

    } else if(userNumber < computerNumber){ 
    alert("Your number is smaller then the computer’s, guess again")
    prompt("Try a new number")

    } else if (userNumber > computerNumber) {
    alert("Your number is bigger then the computer’s, guess again")
    prompt("Try a new number")
    }
   
  }