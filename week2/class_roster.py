import random

with open('homework.txt', 'w') as open_file:
    class_members = [
        'Jasmine',
        'Kimmy',
        'De\'Amber',
        'Trane',
        'Sarah',
        'Sam',
        'Ty',
        'Roy'
    ]
    # total = 0
    for i in range(5000):
        name = random.choice(class_members)
        number = random.randrange(50, 450)
        open_file.write(f'{name}, {number}\n')
    #     if name == "Sarah":
    #         # print(number)
    #         total += number
    #     else:
    #         continue

