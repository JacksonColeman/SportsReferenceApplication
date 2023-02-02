Sports Reference - Engineering Internship Question — Jackson Coleman

I decided to use Python for this task because of its simplicity of syntax and its powerful libraries for formatting tables.

My course of action to create a H2H record table was to first manipulate the raw JSON data into a dictionary that would essentially serve as the rows for the table and then use the pandas library to convert that dictionary into a dataframe (table). This is all done within the create_h2h_table() function.

The function begins by loading in the json data with the help of the JSON library for Python.

I then got the list of teams by simply taking the keys of that JSON data. Next, I built a dictionary for the teams and records using Python's nested dictionary comprehension. Looping through each team twice (once as the team itself and then all opponents), this checks if the team and opponent are the same, in which case "--" is assigned, and if they are different, then it retrieves the amount of wins that the one team had against its opponent from the json data loaded in. This essentially creates the rows of the table with all correct data and a null value when the team aligns with itself in the matrix.

Then, I utilized the pandas library, specifically the DataFrame.from_dict() function, to create a table from the values of the dictionary. I had to use the orient="index" parameter in that function in order for the data to show up as rows instead of columns. The last thing my function does is return that table.

The two lines after the end of the function call the function on the sample data provided (which I stored in a separate JSON file) and then print the table.
