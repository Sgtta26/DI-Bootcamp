// const planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

// for (const planet of planets){
//     const div = document.createElement("div")
//     div.classList.add("planet")
//     div.classList.add(planet)

//     const section = document.querySelector(".listPlanets")
//     section.appendChild(div)
// }
// console.log(div);


let solarSystem = [
    {name : 'Mercury', moons : 0, color: "orange",radius:2439},
    {name : 'Venus' ,  moons: 0, color: "grey",radius:6051},
    {name : 'Earth' ,  moons: 1, color: "blue",radius:6378},
    {name : 'Mars' ,   moons : 2, color: "red",radius:3396},
    {name : 'Jupiter', moons : 79, color: "brown",radius:71492},
    {name : 'Saturn' , moons: 82, color: "yellow",radius:60268},
    {name : 'Uranus' , moons : 27, color: "lightblue",radius:25559},
    {name : 'Neptune',moons : 14, color: "darkblue",radius:24764}
]
​
for(planet of solarSystem) {
    let planetDiv = document.createElement('div');
    planetDiv.style.width = planet.radius*2/1000*2 + 'px';
    planetDiv.style.height = planet.radius*2/1000*2 + 'px';
    planetDiv.innerHTML = `<p>${planet.name}</p>`
    planetDiv.classList.add('planet', planet.name.toLowerCase());
    let i = 1
    let moonDiv;
    while(i <= planet.moons){
        moonDiv = document.createElement('div');
        moonDiv.classList.add('moon', planet.name.toLowerCase());
        let moveMoon = (90 + (i * 30)) + 'px';
        moonDiv.style.top = moveMoon;
        planetDiv.appendChild(moonDiv);
        i++
    }
    planetDiv.style.backgroundColor = planet.color;
    document.body.appendChild(planetDiv);