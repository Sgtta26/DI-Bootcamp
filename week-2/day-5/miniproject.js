// function playTheGame() {
//     confirm("Would you like to play a game ?");
// }

function playTheGame() {
    let text = "Would you like to play a game ?\n YES or NO";
    if (confirm(text) == true) {

      let number = prompt("Enter a number between 0 and 10")
        if ( isNaN(number)){
        alert("Sorry Not a number, Goodbye")

        } else if (number >10 || number < 0 ){
        alert("Sorry it’s not a good number, Goodbye")

        } else if  (number <= 10 && number > 0) {
            let computerNumber = Math.floor(Math.random() * 11) 
            console.log(computerNumber);
            compareNumbers(number, computerNumber)
        }
        

    } else {
        alert("No problem, Goodbye")
    }
  }

  function compareNumbers(userNumber,computerNumber) {

    let counter= 0
    while(userNumber  != computerNumber && counter<3){
        counter=counter+1

     if(userNumber < computerNumber){ 
    
        userNumber = prompt("Your number is smaller then the computer’s, guess again")

    } else if (userNumber > computerNumber) {
    
        userNumber= prompt("Your number is bigger then the computer’s, guess again")
    } 
    if (userNumber == computerNumber){
        alert("WINNER")
        console.log("winner");
        break
    }
    }
    if (counter === 3 ){
        alert("out of chances...")
    }

    // 0 == 'yes' true
    // 0 ==='yes' false
  
  }
