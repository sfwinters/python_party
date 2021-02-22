# for loops - use when you know how many iterations you need
example_list = [
    "one",
    "two",
    "red",
    "blue"
    ]

for word in example_list:
    print(word)

for word in example_list:
    if "o" in word:
        print(word)

# i = 0
# for i in range(10): # prints up to one less than the value passed into the range: 0 1 2 3 4 5 6 7 8 9
    # for i in range(1, 11) will print: 1 2 3 4 5 6 7 8 9 10
    #for i in range(1, 11, 2): # starts at 1 and prints every other number: 1 3 5 7 9
    # print(i)

for i in range(1, 101):
    if i == 10: # arrange if statements from most to least specific
        break # this stops the looping
    if i % 2 == 0:
        continue # skips over items that fit this condition
    print(i) # prints 1 3 5 7 9