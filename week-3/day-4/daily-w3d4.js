const form = document.getElementById("form")
form.addEventListener("submit", handleSubmit)

const tasks = [];

function handleSubmit(e){
    e.preventDefault();
    const formData = new FormData(form);
    //const task = document.querySelector("input").value;
    const task = formData.get("task");
    if (task ==="") return;
    tasks.push(task);
    renderTasks(tasks)
    form.reset();
}

function renderTasks (tasks){

    ul.innerHTML = "";

    for (let i = 0; i < tasks.length; i++) {
        
    }
    function logTask(task){

    }
    tasks.forEach(logTask);

    for (const task of tasks){

    }

    const task = tasks [0];
    const li = document.createElement("li")
    const xMark = '<i class="fa-solid fa-xmark"></i>';
    li.innerText = task + xMark;
    const ul = document.getElementById("list-tasks");
    ul.appendChild(li);
}