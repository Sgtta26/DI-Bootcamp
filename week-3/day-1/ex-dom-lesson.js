// //lesson DOM :

// // i want to retrieve the h1
// const title =  document.body.firstElementChild;
// console.log(title); //h1


// //Document.body.children --> dans chrome affiche une LISTE de tout les enfants du document

// // exemple i want to retrieve the div = premier enfant
// const div = document.body.children[1];
// console.log(div); //div

// //document.body.children[1].firstElementChild --> <p></p>

// //retrieve depending on the sibling relationship
// const div = title.nextElementSibling // --> <div></div>
// console.log(div);


// //document.body.children[1].textContent = "hello" --> juste le texte

// //document.body.children[1].textContent += "how are you" --> dans chrome rajoute du texte / modifie le contenu



// ex1-lesson

const div = document.body.children[0]; //--> one way find div
console.log(div);

const divTwo = document.body.firstElementChild; //-->2nd way find div
console.log(divTwo);


const ul = document.body.children[1]; //--> one way find ul
console.log(ul);

const ulTwo = document.body.firstElementChild.nextElementSibling; //-->2nd way find ul
console.log(ulTwo);

const li = document.body.children[1].children[2]; //--> one way find ul
console.log(li);

const liTwo = ul.children[1]; //-->2nd way find li - 2nd one de la liste : peter
console.log(liTwo);

const liThree = ul.lastElementChild;
console.log(liThree); //-->3th way find li - 2nd one de la liste : peter



//retrieve element by id :

//html : <h1 id="title"> Hello </h1>
//js : const lastH1 = document.getElementById("title");


//retrieve tout les elements d'un meme groupe :

// const allH1 = document.getElementByTagName("h1");

function changeH1 (){
    const allH1 = document.getElementByTagName("h1");
    for (let i = 0; i < allH1.length; i++){
        const plus = i++;
        allH1[i].textContent += " students";
    }
}



//retrieve all the paragraphe inside the div
const allPara = document.querySelectorAll("div p");
const allP = document.querySelector("#block");

