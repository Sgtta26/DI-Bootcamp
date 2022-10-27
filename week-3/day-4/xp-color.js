let color_col = 3;
let color_row = 8;
let color_count = color_col * color_row;

let main_col = 60;
let main_row = 50;
let main_count = main_col * main_row;

let color = null;
let mousedown = false;
let main_divs = [];


let sidebar = document.querySelector("#sidebar");
let main = document.querySelector("#main");
let body = document.getElementsByTagName("body")[0];
let button = document.querySelector("#clear");

for (let i=0; i < color_count; i++ ){
    let div = document.createElement("div");
    div.style.backgroundColor = randomColor();
    div.addEventListener("click", function(event){
        color = event.target.style.backgroundColor;
    })
    sidebar.appendChild(div)
}

for (let i = 0; i < main_count; i++) {
    let div = document.createElement("div");
    div.addEventListener("mousedown", function(event){
        event.target.style.backgroundColor = color;
    })
    div.addEventListener("mouseover", function(event){
        if (color != null && mousedown){
            event.target.style.backgroundColor = color;
        }
    })
    main_divs.push(div)
    main.appendChild(div)
}


body.addEventListener("mousedown", function(event){
    mousedown = true;
})
body.addEventListener("mouseup", function(event){
    mousedown = false;
})

button.addEventListener("click", function(event){
    for(x of main_divs){
        x.style.backgroundColor = "white";
    }
})

function randomColor (){
    let letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random()*16)]
    }
    return color
}
