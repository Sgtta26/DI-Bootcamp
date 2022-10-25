// // //1st retrieve the button

// // const firstBtn = document.getElementById("btn");


// // //syntaxe
// // // Element.addEventListener(event,function);

// // firstBtn.addEventListener("click",alertUser);


// // //callback function -> because called only after the event is fired
// // function alertUser(){
// //     console.log('you clicked the button');
// //     document.body.style.backgroundColor = "lightblue";
// // }


// // const para = document.querySelector("p");
// // para.addEventListener("click",welcomeUser);
// // function welcome(){
// //     alert ("Heyyyy");
// // }



// //1st retrieve the button

// const firstBtn = document.getElementById("btn");
// // const firstBtn = document.querySelector("#btn");

// //syntax
// // element.addEventListener(event, function);
// // call the function as soon as the event fired
// // the function is called a callback function - called only after the event is fired

// firstBtn.addEventListener("click", alertUser);
// firstBtn.addEventListener("mouseover", alertUser);
// firstBtn.addEventListener("mouseout", alertUserTwo);

// function alertUser(){
//     console.log("You clicked the button");
//     document.body.style.backgroundColor = "lightblue";
// }

// function alertUserTwo(){
//     document.body.style.backgroundColor = "pink";
// }

// // -------------------------------
// // with a paragraph

// const para = document.querySelector("p");

// para.addEventListener("click", welcomeUser);

// function welcomeUser() {
//     alert("Heyyyy")
// }

// //Use Toggle
// firstBtn.addEventListener("mouseover", alertUser);
// firstBtn.addEventListener("mouseout", alertUser);

// //callback function - called only after the event is fired
// function alertUser(){
//     firstBtn.classList.toggle("ocean");
// }


// //1 retrieve the two buttons

// const firstBtn1 = document.getElementById("btnOne");
// const secondBtn2 = document.getElementById("btnTwo");

// firstBtn.addEventListener("click", changeToBlue);
// secondBtn.addEventListener("click", changeToRed);

// function changeToBlue(){
//     document.body.style.backgroundColor="blue"
// }

// function changeToRed(){
//     document.body.style.backgroundColor="red";
// }

// // ----------------------------
// // change the color of the body depending on the textContent of the button
// // with the event object

// const firstBtn3 = document.getElementById("btnOne");
// const secondBtn = document.getElementById("btnTwo");
// firstBtn.addEventListener("click", changeColor);
// secondBtn.addEventListener("click", changeColor);

// function changeColor(event){
//     console.log(event.target); //
//     console.log(event.target.textContent);

//     const color = event.target.textContent.toLowerCase();
//     document.body.style.backgroundColor=color;
// }




// //ex1

// const bouton = document.getElementById("btn1");
// const bouton2 = document.getElementById("btn2");

// bouton.addEventListener("click", changeToBlue);
// bouton2.addEventListener("click", changeToRed);

// function changeToBlue(){
//     document.body.style.backgroundColor="red"
// }

// function changeToRed(){
//     document.body.style.backgroundColor="blue";
// }


//ex2

const colors = ["blue", "yellow", "green", "pink"];

function addButtons(){
    const divContainer = document.querySelector("container")
    for (let i = 0; i < colors.length; i++) {
        const newBtn = document.createElement("button");
        newBtn.textContent = colors [i];
        console.log(newBtn);
        newBtn.setAttribute("id",colors [i])
        newBtn.addEventListener("click",changebg)
        document.getElementById("container").append(newBtn);
}
}
addButtons()

function changebg(event){
    console.log(event);
    console.log(event.target.id);
    document.body.style.backgroundColor = event.target.id;
}



