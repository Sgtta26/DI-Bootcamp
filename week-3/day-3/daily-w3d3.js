document.getElementById("daily").addEventListener("keydown", function(){


console.log(event.key);
   if(event.key.match(/[0-9]/)) return event.preventDefault()
})




