## Discussion Forum:
Question:
Based on the scenario, answer the following questions:

1. Discuss how you will use JavaScript to manipulate the DOM to update the chat window dynamically. You are expected to use three of the following features:
<div>, or <p> 
appendChild or insertAdjacentHTML
scrollIntoView

2. Consider how you would handle user interactions, such as sending a message or receiving notifications for new messages. You are expected to use three of the following features:
addEventListener method
click events
keydown events
3. End your discussion post with one question related to the concepts learned in this unit from which your colleagues can formulate a response or generate further discussion.


Answer:
1. To dynamically update the chat window using JavaScript, I would utilize the following features:
- **<div> or <p>**: I would create new `<div>` or `<p>` elements to represent each message in the chat. Each time a user sends or receives a message, a new element would be created to display the message content.
```javascript
const messageElement = document.createElement('div');
messageElement.textContent = messageText; // messageText is the content of the message
chatWindow.appendChild(messageElement); // chatWindow is the container for chat messages
```
- **appendChild or insertAdjacentHTML**: I would use `appendChild` to add the newly created message elements to the chat window. This method allows me to append the new message at the end of the chat history, ensuring that messages are displayed in the order they are sent or received.
```javascript
chatWindow.appendChild(messageElement);
```
- **scrollIntoView**: After appending a new message, I would use the `scrollIntoView` method to ensure that the latest message is visible to the user. This is particularly useful in a chat application where new messages may push older messages out of view.
```javascript
messageElement.scrollIntoView({ behavior: 'smooth' });
```
2. To handle user interactions such as sending a message or receiving notifications for new messages, I would implement the following features:
- **addEventListener method**: I would use the `addEventListener` method to listen for user actions, such as clicking the send button or pressing the Enter key to send a message.
```javascript

sendButton.addEventListener('click', sendMessage); // sendButton is the button to send messages
messageInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
```
- **click events**: I would handle click events on the send button to trigger the message sending function. This function would retrieve the message from the input field, create a new message element, and append it to the chat window.
```javascript
sendButton.addEventListener('click', sendMessage);
function sendMessage() {
    const messageText = messageInput.value; // messageInput is the input field for messages
    if (messageText.trim() !== '') {
        // Create and append message element as shown above
        messageInput.value = ''; // Clear the input field after sending
    }
}
```
- **keydown events**: I would also listen for keydown events on the message input field to allow users to send messages by pressing the Enter key. This enhances the user experience by providing a quick way to send messages without needing to click the send button.
```javascript
messageInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
```


## Assignment Activity
Senario:
You are developing a to-do list application that allows users to add, edit, and remove tasks. You are required to implement event handling and event delegation to ensure that user interactions update the DOM dynamically to reflect changes in the application state. Your task is to:

1. Add New Tasks: Create an input field and an "Add Task" button. When the user enters a task and clicks the button, the task should be added to the to-do list.
2. Edit Existing Tasks: Each task should have an "Edit" button. When the user clicks this button, the task should become editable. The user should be able to modify the task and save the changes.
3. Remove Tasks: Each task should have a "Remove" button. When the user clicks this button, the task should be removed from the to-do list.
4. Mark Tasks as Complete/Incomplete: Each task should have a checkbox. When the user clicks this checkbox, the task should be marked as complete or incomplete, and the visual representation of the task should be updated accordingly (e.g., strike-through for completed tasks).


Answer:
1. To add new tasks to the to-do list, I would create an input field and an "Add Task" button in the HTML. When the user enters a task and clicks the button, I would use JavaScript to capture the input value, create a new task element, and append it to the to-do list. Here’s how I would implement this:
```html
<input type="text" id="taskInput" placeholder="Enter a new task">
<button id="addTaskButton">Add Task</button>
<ul id="taskList"></ul>
```
```javascript
const addTaskButton = document.getElementById('addTaskButton');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');
addTaskButton.addEventListener('click', function() {
    const taskText = taskInput.value.trim();
    if (taskText !== '') {
        const taskItem = document.createElement('li');
        taskItem.textContent = taskText;
        taskList.appendChild(taskItem);
        taskInput.value = ''; // Clear the input field after adding
    }
});
```
2. To edit existing tasks, I would add an "Edit" button next to each task
   and implement an event listener that allows the user to modify the task text. When the "Edit" button is clicked, the task text would become editable, and a "Save" button would appear to save the changes. Here’s how I would implement this:
```javascript
taskList.addEventListener('click', function(event) {
    if (event.target.tagName === 'BUTTON' && event.target.classList.contains('edit-button')) {
        const taskItem = event.target.parentElement;
        const taskText = taskItem.firstChild.textContent;
        const inputField = document.createElement('input');
        inputField.type = 'text';
        inputField.value = taskText;
        taskItem.replaceChild(inputField, taskItem.firstChild);
        event.target.textContent = 'Save';
        event.target.classList.remove('edit-button');
        event.target.classList.add('save-button');
    } else if (event.target.tagName === 'BUTTON' && event.target.classList.contains('save-button')) {
        const taskItem = event.target.parentElement;
        const inputField = taskItem.firstChild;
        const updatedText = inputField.value.trim();
        if (updatedText !== '') {
            const taskTextNode = document.createTextNode(updatedText);
            taskItem.replaceChild(taskTextNode, inputField);
            event.target.textContent = 'Edit';
            event.target.classList.remove('save-button');
            event.target.classList.add('edit-button');
        }
    }
});
```
3. To remove tasks, I would add a "Remove" button next to each task and implement an event listener that removes the task from the to-do list when clicked. Here’s how I would implement this:
```javascript
taskList.addEventListener('click', function(event) {
    if (event.target.tagName === 'BUTTON' && event.target.classList.contains('remove-button')) {
        const taskItem = event.target.parentElement;
        taskList.removeChild(taskItem);
    }
});
```

4. To mark tasks as complete or incomplete, I would add a checkbox next to each task. When the user clicks the checkbox, I would update the visual representation of the task (e.g., strike-through for completed tasks) and toggle the task's completion status. Here’s how I would implement this:
```javascript
taskList.addEventListener('click', function(event) {
    if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {
        const taskItem = event.target.parentElement;
        if (event.target.checked) {
            taskItem.style.textDecoration = 'line-through'; // Mark as complete
        } else {
            taskItem.style.textDecoration = 'none'; // Mark as incomplete
        }
    }
});
```


# Description of content of index.html and style.css and script.js:

- **index.html**: This file contains the structure of the To-Do List application. It includes an input field for adding new tasks, a button to add tasks, and a list to display the tasks. Each task has associated buttons for editing, saving, and removing the task.

- **css**: This file contains the styles for the To-Do List application. It defines the layout, colors, and spacing for the various elements in the application, including the input field, buttons, and task list items.

- **script**: This file contains the JavaScript code that adds interactivity to the To-Do List application. It includes functions for adding new tasks, editing existing tasks, removing tasks, and marking tasks as complete or incomplete.