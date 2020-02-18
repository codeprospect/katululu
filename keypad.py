# put the letters in the respective keys
list2 = ["A", "B", "C"]
list3 = ["D", "E", "F"]
list4 = ["G", "H", "I"]
list5 = ["J", "K", "L"]
list6 = ["M", "N", "O"]
list7 = ["P", "Q", "R", "S"]
list8 = ["T", "U", "V"]
list9 = ["W", "X", "Y", "Z"]

# created an array made of the above arrays
list_big = [list2, list3, list4, list5, list6, list7, list8, list9]

numbers = list(range(0,8))

print("Input the word you want to type: ")
name = input()
name = name.upper() #converting inputted string into uppercase
name_list = list(name) #converting inputted string into a list

clicks = 0 #counter

for number in name_list:
    letter = number
    for number in numbers:
        insta = list_big[number]
        for number in insta:
            if number == letter:
                index = insta.index(number) + 1
                clicks = clicks + index

print(clicks)
