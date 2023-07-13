function addTask() {
  var taskInput = document.getElementById("taskInput");
  var taskList = document.getElementById("taskList");
  const taskText = taskInput.value.trim();

  if (taskInput.value == "") {
    alert("Please enter a task.");
    return;
  }

  var task = document.createElement("li");
  task.innerText = taskText;
  taskList.appendChild(task);
  taskInput.value = "";

  task.addEventListener("click", function () {
    toggleStrike(task);
  });

  var removeButton = document.createElement("button");
  removeButton.innerHTML = "Remove";
  task.appendChild(removeButton);

  removeButton.addEventListener("click", function () {
    removeTask(task);
  });
}

function toggleStrike(task) {
  task.classList.toggle("strike");
}

function removeTask(task) {
  task.parentNode.removeChild(task);
}
