Data Science Fellowship Group (2)
Month 01 (Data Analysis)
Week 01
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
Week 02
Deadline: 21/6/2024
🔴 Task 6: File Handling, Exception Handling
Look at this topic and try to create a small practical application. For example, you could create an application that records and retrieves data from a file. One such example is storing student data in a file. When the application starts, it should load the recorded data and provide options for searching and deleting records. You can use multiple attributes such as student_id, student_name, student_age, and student_grade.
The student_id should be unique, and searching/deleting will be done using this. When adding a new record, no duplicate IDs should be allowed. Also, display the list of available students.
This is the last task for basic programming. After this, we will move towards OOP and some common data structures in Python (dictionary, list, set, tuple).
Resource: https://www.w3schools.com/python/python_file_handling.asp
Deadline: 22/6/2024
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
Deadline: 23/6/2024
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
Week 03
Deadline: 24/6/2024
🔴 Task 9: Introduction to Statistics
Statistics and probability are very important when we talk about data analysis. You should at least know mean, median, mode, some common distributions (for example: normal distribution, binomial distribution, Poisson distribution, and uniform distribution) and some concepts of probability. You will learn and try to solve some related problems by hand, take screenshots, and submit a PDF.
Resource: https://www.geeksforgeeks.org/introduction-of-statistics-and-its-types/
Deadline: 25/6/2024
🔴 Task 10: Introduction to NumPy (arrays, basic operations)
Now that you have a basic knowledge of statistics and probability, it is time to code it. Try to learn the basics of NumPy (arrays, etc.), perform some array operations in multiple dimensions, and try to solve the problems you solved in Task 9 using NumPy.
Everyone must do:
Create a 1D NumPy array containing the integers from 0 to 9.
Create a 2D NumPy array (3x3) containing random integers between 1 and 20.
Create a 3D NumPy array with dimensions (2, 3, 4) filled with ones.
Add two 1D arrays element-wise.
Multiply two 2D arrays element-wise.
Calculate the dot product of two matrices.
Calculate the mean, median, and standard deviation of a 1D array.
Find the maximum and minimum values in a 2D array.
Generate an array of 1000 random numbers from a normal distribution with a mean of 0 and a standard deviation of 1.
Create a 2D array of shapes (5, 5) with random integers from a uniform distribution between 10 and 50.
Calculate the cumulative sum of a 1D array.
Compute the correlation coefficient matrix of a 2D array.
Simulate rolling a six-sided die 1000 times and count the frequency of each outcome.
Resource: https://drive.google.com/file/d/1j9BePhvRWPMnBPnxHFP6vlRnWQAr-yZy/view?usp=sharing
Deadline: 26/6/2024
🔴 Task 11: NumPy advanced operations (indexing, slicing, broadcasting)
Now that you have learned the basic concepts of NumPy and know how to create arrays, it's time to explore it further.
Everyone must do:
For serials 1 to 15:
Indexing and Slicing
Given a 2D array of shape (5, 5), extract a 3x3 sub-array starting from the element at position (1, 1).
From a 3D array of shape (4, 3, 2), extract all elements in the first two rows and all columns of the second slice along the third axis.
Given an array of integers, use fancy indexing to extract elements at positions [1, 3, 4, 7].
Given a 2D array, use fancy indexing to select rows [0, 2, 3] and columns [1, 3].
From a 1D array of random integers, extract all elements that are greater than 10.
Given a 2D array of shape (5, 5), replace all elements greater than 15 with the value 0.
Broadcasting
Add a 1D array of shape (3,) to each row of a 2D array of shape (4, 3).
Multiply a 2D array of shape (3, 3) by a 1D array of shape (3,).
Create two 2D arrays of shapes (3, 1) and (1, 4) respectively, and perform element-wise addition.
Given a 3D array of shape (2, 3, 4), add a 2D array of shape (3, 4) to each 2D slice along the first axis.
Some more
Given a 2D array, use slicing to extract every second row and every second column, then add a 1D array to each row of the sliced array.
From a 3D array of shape (4, 3, 2), extract a sub-array using slicing and then use broadcasting to subtract a 2D array from each slice along the third axis.
Given a 2D array, extract the diagonal elements and create a 1D array.
Use slicing to reverse the order of elements in each row of a 2D array.
Given a 3D array of shape (4, 5, 6), use slicing to extract a sub-array of shape (2, 3, 4) and then use broadcasting to add a 1D array of shape (4,) to each row along the third axis.
Create a 2D array and use both slicing and broadcasting to set the last column to the sum of the first two columns for each row.
For serial 16 to last:
Indexing and Slicing
Given a 2D array of shape (6, 6), extract a 2x2 sub-array starting from the element at position (1, 1).
From a 3D array of shape (3, 2, 1), extract all elements in the first two rows and all columns of the second slice along the third axis.
Given an array of integers, use fancy indexing to extract elements at positions [1, 3, 4, 6].
Given a 2D array, use fancy indexing to select rows [0, 2, 2] and columns [1, 3].
From a 1D array of random integers, extract all elements that are greater than 8.
Given a 2D array of shape (6, 6), replace all elements greater than 13 with the value 0.
Broadcasting
Add a 1D array of shape (3,) to each row of a 2D array of shape (4, 3).
Multiply a 2D array of shape (3, 3) by a 1D array of shape (3,).
Create two 2D arrays of shapes (3, 1) and (1, 4) respectively, and perform element-wise addition.
Given a 3D array of shape (2, 3, 4), add a 2D array of shape (3, 4) to each 2D slice along the first axis.
Some more
Given a 2D array, use slicing to extract every second row and every second column, then add a 1D array to each row of the sliced array.
From a 3D array of shape (3, 2, 1), extract a sub-array using slicing and then use broadcasting to subtract a 2D array from each slice along the third axis.
Given a 2D array, extract the diagonal elements and create a 1D array.
Use slicing to reverse the order of elements in each row of a 2D array.
Given a 3D array of shape (7, 6, 5), use slicing to extract a sub-array of shape (2, 3, 4) and then use broadcasting to add a 1D array of shape (4,) to each row along the third axis.
Create a 2D array and use both slicing and broadcasting to set the last column to the sum of the first two columns for each row.
Resource: https://drive.google.com/file/d/1j9BePhvRWPMnBPnxHFP6vlRnWQAr-yZy/view?usp=sharing
Deadline: 27/6/2024
🔴 Task 12: Introduction to Pandas (Series, DataFrame basics)
Now that you have a basic understanding of Python, NumPy, and statistics, it's time to explore the powerful tools for data manipulation offered by the Pandas library. Start by learning about Series and DataFrames and their operations.
Create a Pandas Series from a Python list, numpy array, and a dictionary.
Assign a custom index to the Series.
Perform basic arithmetic operations on Series.
Access elements using index labels and positions.
Filter the Series to include only values greater than a specific threshold.
Create a DataFrame from a dictionary of lists.
Create a DataFrame from a numpy array, specifying column and index names.
Load a DataFrame from a CSV file.
Display the first and last five rows of the DataFrame.
Get a summary of the DataFrame including the mean, median, and standard deviation of numeric columns.
Extract a specific column as a Series.
Filter rows based on column values.
Select rows based on multiple conditions.
Add a new column to the DataFrame.
Delete a column from the DataFrame.
Rename columns in the DataFrame.
Resource: https://drive.google.com/file/d/1j9BePhvRWPMnBPnxHFP6vlRnWQAr-yZy/view?usp=sharing
Deadline: 28/6/2024
🔴 Task 13: Data manipulation with Pandas (indexing, selection, grouping)
Load a DataFrame from a CSV file. Display the first and last five rows of the DataFrame.
Set a specific column as the index of the DataFrame.
Select a specific column and display its values.
Select multiple columns and display the resulting DataFrame.
Select a subset of rows using the .loc method.
Select a subset of rows and columns using the .iloc method.
Filter rows based on a condition.
Group the DataFrame by a specific column and calculate the mean of each group.
Group the DataFrame by multiple columns and calculate the sum of each group.
Use the agg method to apply multiple aggregation functions to grouped data.
Calculate the size of each group.
Select rows based on multiple conditions.
Use the query method to filter rows.
Use isin to filter rows based on a list of values.
Select specific columns and rename them.
Resource: https://drive.google.com/file/d/1j9BePhvRWPMnBPnxHFP6vlRnWQAr-yZy/view?usp=sharing
Deadline: 30/6/2024
🔴 Task 14: Data cleaning and preprocessing with Pandas
Develop a comprehensive understanding of data cleaning and preprocessing techniques using Pandas, which are crucial for preparing data for analysis and machine learning.
Identify missing values in the DataFrame.
Drop rows with any missing values.
Drop columns with any missing values.
Fill missing values with a specific value.
Fill missing values using forward fill and backward fill methods.
Interpolate missing values.
Convert a column to a different data type.
Apply a function to transform the values of a column.
Normalize a column using Min-Max scaling.
Standardize a column (z-score normalization).
Identify duplicate rows in the DataFrame.
Drop duplicate rows.
Drop duplicate rows based on specific columns.
Convert all string values in a column to lowercase.
Remove leading and trailing spaces from string values in a column.
Replace a specific substring in a column with another substring.
Extract a substring from each value in a column.
Convert a column to datetime format.
Extract year, month, and day from a datetime column.
Filter rows based on a date range.
Convert a categorical column to numerical using one-hot encoding.
Convert a categorical column to numerical using label encoding.
Group values in a categorical column and create a new column with grouped categories.
Merge two DataFrames based on a common column.
Concatenate two DataFrames vertically.
Concatenate two DataFrames horizontally.
Create a new column based on existing columns.
Discretize a continuous column into bins.
Create polynomial features from existing numerical columns.
Resource: https://drive.google.com/file/d/1j9BePhvRWPMnBPnxHFP6vlRnWQAr-yZy/view?usp=sharing
