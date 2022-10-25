// //ex1

// const title =  document.body.firstElementChild;

// let article = document.querySelector('article');
// console.log(article);
// article.lastElementChild.remove()


// const h2 = document.getElementById("h2");
// h2.addEventListener("click", changeToRed);
// function changeToRed(e){
//     e.target.style.backgroundColor="red"
// }

// const h3 = document.getElementById("h3");
// h3.addEventListener("click", hide);

// function hide(){
//     h3.style.display = "none";
// }


// const forP = document.querySelector("button");
// const bp = document.querySelectorAll("p");

// forP.addEventListener("click", boldP);

// function boldP(){
//     for(let i=0; i< bp.length; i++){
//         bp[i].style.fontWeight = "bold";
//     }
// }




// //ex2

//  const form = document.querySelector("form");
//  console.log(form);
//  console.log(form.fname);
//  console.log(form.lname);

//  form.addEventListener("submit",form1);
//  function form1(event){
//     event.preventDefault();
//     let name = form.fname.value;
//     console.log(name);
//     let name2 = form.lname.value;
//     console.log(name2);

//     if(name.trim().length > 0 && name2.trim().length > 0){
//         const ul = document.querySelector("ul");
//         let li =document.createElement('li');
//         li.textContent= name;
//         ul.appendChild(li);

//         let li2 =document.createElement('li');
//         li2.textContent= name2;
//         ul.appendChild(li2);
//     }

//  }




// //ex3

// let allBoldItems;

// function getBoldItems() {
//     allBoldItems = document.getElementsByTagName("strong");
// }

// function highlight(){
//     getBoldItems();
//     for(const boldItem of allBoldItems){
//         boldItem.style.color = "blue";
//     }
// }

// function returnNormal(){
//     getBoldItems();
//     for(const item of allBoldItems){
//         item.style.color = "black";
//     }
// }

// const paragraph = document.querySelector("p");
// paragraph.addEventListener("mouseover", highlight);



// //ex4


const form = document.getElementById("myForm");
const raduis = document.getElementById("raduis");
const volume = document.getElementById("volume");
form.addEventListener("submit",handleSubmit);

const numberOfDecimals = 2;

function handleSubmit(e) {
    e.preventDefault();
    const r = Number(raduis.value);
    if (Number.isNaN(r)) return;
    const v = ( 4 / 3 ) * Math.PI * r ** 3;
    volume.value = v.toFixed(numberOfDecimals);
}



//ex5

document.addEventListener("DOMContentLoaded", sayContentLoaded);

function sayContentLoaded (){
    console.log("the HTML page was parsed and loaded");
}
