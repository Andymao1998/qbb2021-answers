Overall it looks like you're well on your way towards understanding how to put together the different data types, for loops, and if statements to solve the problem. It would be really handy for both you and anyone else reading your code to put in comments to tell the reader what each chunk of code is intended to do. Also, if you use more specific descriptive variable names, it helps in figuring out what is needed where and what you're trying to accomplish.

The logic of the code is sound and after a few bug fixes, it should solve the assignment correctly. Just a couple of things to note.

You aren't currently using the variables you create in lines 3 and 4. Try not to create extra code as it can be confusing.

In line 10, you're value being added to the dictionary is `line_d[1]`. If you look at the line before, you split the line into two fields. However, whenever you read in a line from a file, it still has the newline character on the end. So, you'll want to strip that off.

In line 14, you put `list()` around the file stream. This is going to only return the first line. It's a strange quirk about converting a filestream to a list (It really shouldn't work at all). The syntax you used in line 8 was correct and you should repeat that approach on line 10.

Remember that if there isn't a third argument passed to your program, that you shouldn't keep the line. Also, you could replace the nested if statement with `elif len(sys.argv) == 4:` and then the same else statement.

% completion: 90%

keep up the good work