// //ex1

// const div = document.body.children[0]; 
// console.log(div);

// function changeName (){
//     const div1 = div.children[1];
//     div1.children[1].textContent="Richard";
// }
// changeName ()

// function changeMyName (){
//     const div1 = div.children[0];
//     div1.children[0].textContent="Sarah";
//     const div2 = div.children[1];
//     div2.children[0].textContent="Sarah";
// }
// changeMyName ()

// function removeMyName (){
//     const div1 = div.children[0];
//     div1.children[0].remove();
//     const div2 = div.children[1];
//     div2.children[0].remove();
// }

// removeMyName ()




// //ex2

// document.querySelector('div').style.backgroundColor = "blue"


// const div = document.body.children[0]; 

// function displayJohn (){
//         const div1 = div.children[0];
//         div1.children[0].style.display= "none";
//      }
// displayJohn()


// function addBorder (){
//     const div2 = div.children[0];
//     div2.children[1].style.border = "2px solid black"
//  }
// addBorder()

// function fontSize (){
//     const div2 = div.children[0];
//     div2.style.fontSize = "22px"
//  }
// fontSize()





// //ex3

// const div = document.body.children[0]; 
// console.log(div);
// navBar.setAttribute("id","socialNetworkNavigation")

// const newLi = document.createElement("li");
// const text = document.createTextNode("Logout");
// newLi.appendChild(text);
// const section = document.getElementsByTagName('ul');
// section[0].appendChild(newLi);





//ex4


const allBooks =[
    {
        title: "Harry Potter",
        author: "Jk",
        image: "https://m.media-amazon.com/images/I/81oND6XuHsL._AC_SY445_.jpg",
        alreadyRead: true
    },
    {
        title: "Raiponse",
        author: "Jojo",
        image: "https://fr.web.img6.acsta.net/medias/nmedia/18/78/47/32/19539636.jpg",
        alreadyRead: false
    }

];

function nameBook (){
    const div = document.getElementsByClassName("list-books")[0]; 
    console.log(div);

    const table = document.createElement("table");
    table.style.border= "1px solid black";
    div.appendChild(table);

    for (let i = 0; i< allBooks.length; i++) {
        const tr = document.createElement("tr");
        table.appendChild(tr);

        const title = document.createElement("td");
        title.textContent = allBooks[i].title;
        title.style.border= "1px solid black";
        tr.appendChild(title);
       
        const author = document.createElement("td");
        author.textContent = allBooks[i].author;
        author.style.border= "1px solid black";
        tr.appendChild(author);

        const image = document.createElement("td");
        image.style.border= "1px solid black";
        const img = document.createElement("img");
        img.src= allBooks[i].image;
        img.style.width= "100px";
        image.appendChild(img);
        tr.appendChild(image);

        const alreadyRead = document.createElement("td");
        alreadyRead.style.border= "1px solid black";
        if(allBooks[i].alreadyRead){
            alreadyRead.style.backgroundColor= "red";
        }
        alreadyRead.textContent = allBooks[i].alreadyRead;
        tr.appendChild(alreadyRead);
    }
}

nameBook ();

