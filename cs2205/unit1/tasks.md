Discussion Forum:
Question:
1. As the person in charge of this project,
    a. Describe the fundamental web development concepts involved in this process.
    b. Explain the role of the client and the server in the application, detailing how the client-server architecture facilitates the interaction between the user’s browser and the bookstore's database.
2. Identify issues in an existing website you know or frequently visit by running an HTML validator tool.
    a. Examine and document findings from the HTML validator tool regarding three identified issues on visited website.
    b. What works well on this website and what could be improved to be implemented in your project?


Answer:
1. 
   a. The fundamental web development concepts involved in this process include HTML (Hypertext Markup Language) for structuring the content of the web pages, CSS (Cascading Style Sheets) for styling and layout, and JavaScript for adding interactivity and dynamic features to the website. Additionally, understanding responsive design principles is crucial to ensure that the website is accessible and visually appealing across various devices and screen sizes. Other important concepts include web hosting, domain management, and the use of frameworks or libraries (such as Bootstrap or React) to streamline development and enhance functionality.

   b. In a client-server architecture, the client refers to the user's web browser that requests resources from the server, which hosts the bookstore's database and web application. When a user interacts with the website (e.g., searching for books or adding items to their cart), the client sends HTTP requests to the server. The server processes these requests, retrieves data from the database as needed, and sends back HTTP responses containing the requested information or confirmation of actions taken. This interaction allows users to seamlessly browse, search, and purchase books while ensuring that data is securely managed on the server side.

2. I checked the UoPeople site(https://my.uopeople.edu/my/courses.php)
   a. After running an HTML validator tool on a frequently visited website, three identified issues include:
      1. Uncaught ReferenceError: $ is not defined
      This error indicates that the jQuery library, which defines the $ symbol, is not properly loaded or referenced in the HTML file. This can lead to JavaScript functions that rely on jQuery failing to execute.
      2. Uncaught TypeError: Cannot read properties of undefined (reading 'style')
      This error suggests that a JavaScript function is attempting to access the 'style' property of an undefined object, which may occur if the DOM element being targeted does not exist or has not been properly initialized.
      3. Uncaught TypeError: Failed to execute 'insertAdjacentElement' on 'Element': parameter 2 is not of type 'Element'.
      This error indicates that the second parameter passed to the 'insertAdjacentElement' method is not a valid DOM element, which can happen if the variable being used is null or of an incorrect type.

    b. For improvements of above errors, the website could ensure that all necessary libraries (like jQuery) are correctly loaded before any scripts that depend on them are executed. Additionally, implementing proper error handling and validation checks in JavaScript can prevent attempts to access properties of undefined objects. Lastly, ensuring that all DOM elements being manipulated exist and are of the correct type before performing operations like 'insertAdjacentElement' can help avoid runtime errors. Overall, improving code quality and robustness will enhance the user experience and reliability of the website. It is also important to accurately understand how these errors actually affect users, or how they may affect them. If these errors do not affect users, it may be better to prioritize other improvements that have a more direct impact on user experience.

Last question:
When was the first time you used a browser's developer tools and what did you use them for?
