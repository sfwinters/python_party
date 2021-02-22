open_file = open('test_input.txt') # If file is not in same folder, need to specify path
for line in open_file:
    # print(line) # prints each line of the text file double-spaced; a return is implicitly added
    print(line, end="") # this removes the extra return at the end of each line

print(open_file.readlines()) # prints ['green\n', 'eggs\n', 'and\n', 'ham']

open_file.close() # this closes the file when done

with open('test_input.txt') as other_way: # This tells Python to auto close the file when finished - file is only open during use
    for line in other_way:
        print(line, end="")

print('\ndone') # \n tells Python to print the word "done" on a new line
# print(other_way.readlines()) # This throws an error, because Python closed the file at the end of the above function
