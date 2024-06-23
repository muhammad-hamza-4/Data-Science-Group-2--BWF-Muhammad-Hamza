# Data-Science-Group-2--BWF-Muhammad-Hamza
# Week 01
🔴 Task 1 ->An introduction to Git. This will include installing Git and learning some basic commands: init, add, commit, etc.

Here’s what you need to do:

Install Git: Make sure Git is installed on your machine. You can find the installation instructions here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
Basic Commands (for example):
git init: Initialize a new Git repository.
git add: Add files to the staging area.
git commit: Commit your changes to the repository.
Documentation:

1. Run the above commands on your machine.
2. Take screenshots of each step (installation, initializing a repository, adding files, and committing changes).
3. Compile these screenshots into a Word document.

Resource: https://www.w3schools.com/git/git_staging_environment.asp?remote=github


🔴 Task 2 -> Git and GitHub
Now that you have a bit of information regarding Git, it's time to learn about GitHub and how to use both Git and GitHub collectively. For now, I don't expect any extraordinary command on both of these, but you must complete the following steps:

Create a GitHub Account: If you don't already have one, sign up for a GitHub account.

Create a Public Repository:

Title it as follows: Data Science (Group 2) - BWF - YOUR NAME
Ensure the repository is public so we can all view it.
Organize Your Repository:

After creating the repository, create a folder within it named Task 1.
I suggest making a separate folder for each task on your local system. When you complete a task, simply drag and drop that folder into this repository.
Submit Your Repository Link:

I've attached a form link where you can enter your name and the link to your GitHub repository.
Form link: https://forms.gle/wu1ZpctHfnNo4dMR8
Deadline: 12th June 2024




🔴Task 3: Introduction to Jupyter Notebook and Installation

This will be our last task related to setting up everything. After this task, we will start with Python.

In this task, you need to set up Jupyter Notebook on your systems. Explore it and see how you can add fancy headings to it.

For this task, you will submit a Jupyter Notebook. Like the previous tasks, create a folder named Task 3, place the notebook in it, and drag and drop it into the same repository (I will check it there).

Resources:
1. https://www.geeksforgeeks.org/install-jupyter-notebook-in-windows/  
2. https://www.geeksforgeeks.org/how-to-use-jupyter-notebook-an-ultimate-guide/


🔴 Task 4: Python Basics (Variable, Datatypes, Operators)

As I mentioned earlier, by Task 3, we have completed setting up the environment for future tasks. From Task 4, we will start with Python. I mentioned in the meeting that for every task I provide, try to think of a practical application you can create using the tools you have learned so far.

You can choose any project of your choice. Here is an example:

Simple DMAS Calculator:
Create a program that prompts the user to input two numbers. The program will then calculate and display the sum, difference, product, and quotient of the two numbers.

Submission: Jupyter Notebook on GitHub (Folder -> Task 4)
Resource: https://www.w3schools.com/python/default.asp


🔴 Task 5: If conditions, for loops, while loops, and functions using Python. 

This will be our last task until Eid. I recommend you all to practice these concepts. Try to create as many mini-projects as possible.

For example, you can use one Jupyter notebook with multiple cells representing a mini-project.

The best way to master loops is by printing patterns. I will share some examples soon. You can consider those or try some yourself as well.

The deadline for all tasks (previous and this one) is Sunday, June 16, 2024. I will close the form on Sunday, and after that, no one will be allowed to submit their repository link. I have seen some repositories and have given personal suggestions to some fellows. I will share the collective results soon for the tasks we have completed so far.

 Resources:  
1. https://www.w3schools.com/python/gloss_python_else.asp
2. https://www.w3schools.com/python/python_while_loops.asp
3. https://www.w3schools.com/python/python_for_loops.asp
4. https://www.w3schools.com/python/python_functions.asp
# Week 02

🔴 Task 6: File Handling, Exception Handling
Look at this topic and try to create a small practical application. For example, you could create an application that records and retrieves data from a file. One such example is storing student data in a file. When the application starts, it should load the recorded data and provide options for searching and deleting records. You can use multiple attributes such as student_id, student_name, student_age, and student_grade.
The student_id should be unique, and searching/deleting will be done using this. When adding a new record, no duplicate IDs should be allowed. Also, display the list of available students.
This is the last task for basic programming. After this, we will move towards OOP and some common data structures in Python (dictionary, list, set, tuple).
Resource: https://www.w3schools.com/python/python_file_handling.asp

🔴 Task 7: Object-Oriented Programming (OOP) basics. 
This will include classes, objects, and methods.
A Practical Example: 
Create a simple Library Management System using OOP concepts to manage books, members, and borrowing activities.
Key Features:
Book Class:
Attributes: title, author, ISBN, status (available/borrowed)
Methods: display info, mark as borrowed, mark as returned
Member Class:
Attributes: name, member ID, borrowed books (list)
Methods: borrow book, return book, display info
Library Class:
Attributes: list of books, list of members
Methods: add book, register member, issue book, return book, display all books, display all members
Steps:
Define Book class with necessary attributes and methods.
Define Member class with necessary attributes and methods.
Define Library class to manage books and members.
Test by creating instances, adding books, registering members, and simulating borrowing/returning books.
Resource: https://www.w3schools.com/python/python_classes.asp

🔴 Task 8: Simple Data Structures in Python (Dictionary, Set, List, Tuple)
Description: This task will cover the basics of Python's built-in data structures: Dictionary, Set, List, and Tuple. You will learn how to create, manipulate, and use these data structures effectively in Python programming.
Key Topics:
List:
Creation: my_list = [1, 2, 3, 4]
Accessing elements: my_list[0]
Modifying elements: my_list[1] = 5
Adding elements: my_list.append(6)
Removing elements: my_list.remove(3)
Tuple:
Creation: my_tuple = (1, 2, 3, 4)
Accessing elements: my_tuple[0]
Immutable nature: Elements cannot be modified after creation.
Set:
Creation: my_set = {1, 2, 3, 4}
Adding elements: my_set.add(5)
Removing elements: my_set.remove(2)
Unique elements: No duplicates allowed.
Dictionary:
Creation: my_dict = {'a': 1, 'b': 2, 'c': 3}
Accessing elements: my_dict['a']
Modifying elements: my_dict['b'] = 4
Adding elements: my_dict['d'] = 5
Removing elements: del my_dict['c']
Practical Mini Project: Inventory Management System
Description: Develop a simple Inventory Management System using Python's data structures to manage products, categories, and stock levels.
Steps:
Define Data Structures:
Use a dictionary to store product details (e.g., products = {'ID001': {'name': 'Product1', 'category': 'Category1', 'stock': 50}}).
Use a list to maintain the order of product additions.
Use a set to track unique categories.
Use a tuple to store immutable product information (e.g., product name and category).
Implement Functions:
Add a product: add_product(product_id, name, category, stock)
Update stock: update_stock(product_id, quantity)
Display all products: display_products()
Display products by category: display_by_category(category)
Testing:
Add multiple products.
Update stock levels.
Display all products and filter by category.

