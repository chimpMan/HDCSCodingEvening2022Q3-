# getting the user input
my_Input = input("Enter a string thats at least 3 characters long ")
if(len(my_Input) < 3):
    print("your string is less than 3 char long")

middle_char = ""

# function to get the length of a string


def string_length():

    lengths = len(my_Input)
    # print(length_of_String)
    return lengths

# function to get the first character of a string


def first_character():
    first_char = my_Input[0]
    # print (first_char)
    return first_char

# function to get the last character of a string


def last_character():

    last_char = my_Input[string_length()-1]
    # print (last_char)
    return last_char


# fucntion to get the middle characters


def middle_characters():
    mid = int((string_length()/2))
    if (string_length() % 2) == 0:
        middle_char = my_Input[int(mid)-1, int(mid)]
    else:
        middle_char = my_Input[int(mid)]
    return middle_char

# function to get the index of  repeating second char in a string


def my_index():
    i = 2
    ind_positon = ''
    if (my_Input[i] == my_Input[1]):
        ind_positon = f'@ index {i}'
        i = i+1
    else:
        ind_positon = 'not found'

    print(ind_positon)
    return ind_positon


# creating the array to store my output
myOutput = [string_length(), first_character(), last_character(),
            middle_characters(), my_index()]

# printing the output
print(myOutput)
