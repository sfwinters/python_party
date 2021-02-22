# PEP8 - Python documentation, best practices, etc

python_list = ['string', 5, 2.5] # Use 'snake_case' (underscores between words, all lower case) instead of 'camelCase' (pythonList)
python_list = ['string', 5, 2.5] # Use 'snake_case' (underscores between words, all lower case) instead of 'camelCase' (pythonList)
python_list = ['string', 5, 2.5] # Use 'snake_case' (underscores between words, all lower case) instead of 'camelCase' (pythonList)
# shift + alt + down will copy/paste your current line

# shift + arrow key to highlight multiple lines or characters in that direction

python_list.append('new thing')
python_list.insert(2, 'cutting in line') # Inserts new string at python_list[2]

python_tuple = ('other string', 6, 3.5)
python_tuple = python_tuple + tuple('another new thing') # This will split the new string into individual characters and add all of them

print(python_list, python_tuple)

# class PythonParty:  For class names, no underscore and all words capitalized

# Use descriptive variable names, not things like 'x'
# To change all instances of a word: double-click word to highlight and ctrl-D will highlight each next instance

python_dictionary = {
    'key' : "value",
    "number" : 5,
    "list" : [
        1, 
        "string", 
        8.8
        ],
} 
# Same as an object in javascript EXCEPT the order of the key/value pairs will not necessarily remain consistent; reference by key instead of numerical index

print(python_dictionary['key']) # prints 'value' (without quotes) to console
python_dictionary["address"] = "1234 Party Lane" # adds "address" : "1234 Party Lane" as a key/value pair to the dictionary

print(python_dictionary)

# ctrl + / will comment/uncomment the current line

python_boolean = False

if python_boolean: # Defaults to True if not specified
    print("True dat")
else:
    print("Naw")

# Insert a blank line above and below classes and functions for readability
# Vertical white space will not interfere with code as long as things are indented appropriately

family = {
    "members" : {
        "Roy" : {
            "age" : 45,
            "height" : "6'2"
        },
        "Francis" : {
            "age" : 41,
            "height" : "5'5"
        },
        "Draylen" : {
            "age" : 15,
            "height" : "5'7"
        },
        "Henry" : {
            "age" : 17,
            "height" : "cat-sized"
        },
        "Goblin Face" : {
            "age" : 14,
            "height" : "fat"
        },
        "Scrambles the Death Dealer" : {
            "age" : 6,
            "height" : "very tiny"
        }
    }
}

print(family)

for key, value in family['members'].items(): # This prints family member name and family member stats collection each on their own line
    print(f'{key}\n{value}')

name_ = "Billy"
string_1 = "Hi, my name is " + name_ + ". Nice to meet you!"
string_2 = "Hi, my name is {}. Nice to meet you!".format(name_)
string_3 = f"Hi, my name is {name_}. Nice to meet you!"
# All three of the above strings will return the same thing

print(f'{string_1}\n{string_2}\n{string_3}') # "Hi, my name is Billy. Nice to meet you!" will print three times in a row, each on its own line

def multiply_this(first_num, second_num):
    return first_num * second_num # This temporarily stores the result but will not print it anywhere

print(multiply_this(2, 3)) # This will run the function and print the result to the console


first_number = 3  #global scope
second_number = 4

def multiply_weird():
    # global first_number
    # global second_number
    # print(f'{first_number}, {second_number}') # This prints 3, 4
    # not recommended to use 'global' keyword - gets too confusing. Use unique variable names instead
    first_number = 2  # local scope
    second_number = 5
    print(f'{first_number}, {second_number}') # Identical to line 93, but this prints 2, 5 because values are re-declared before this line runs
    return first_number * second_number

print(f'{first_number}, {second_number}') # Prints 3, 4
print(multiply_weird()) # Prints 10 even though alternate values are declared globally. If new values are not assigned locally, it will return 12 (3 * 4)

def modify_num():
    first_number = 10
    second_number = 6
    return first_number, second_number

print(multiply_this(*modify_num()))  # Prints 60 to the console