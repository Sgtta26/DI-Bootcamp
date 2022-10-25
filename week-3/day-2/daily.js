let forms = document.getElementById("libform");
let allInputs = document.querySelectorAll("input");

forms.addEventListener("submit", function() {
    event.preventDefault();
    console.log("submit event !");
    let isEmpty =false;
    for (let i=0; i < allInputs.length; i++) {
        if (allInputs[i].value == ""){
            isEmpty = true;
        }
    }

    if (!isEmpty){
        let noun = document.getElementById("noun");
        let adjective = document.getElementById("adjective");
        let person = document.getElementById("person");
        let verb = document.getElementById("verb");
        let place = document.getElementById("place");
        let span = document.getElementById("story");
        span.innerHTML =
            noun.value + " is really " +
            adjective.value + " and " + 
            person.value + " adore " +
            verb.value + " dans " +
            place.value;
    }else{
    console.log("Empty Fields");
    }
 });