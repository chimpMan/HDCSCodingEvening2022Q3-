# getting the user input

my_input = input("Enter a string thats at least 3 characters long ")

if(len(my_input) < 3):
    print("your string is less than 3 char long")

middle_char = ""


def main():

    # creating the array to store my output
    my_output = [string_length(), first_character(), last_character(),
                 middle_characters(), my_index()]

    # printing the output
    print(my_output)
    return my_output

# function to get the length of a string


def string_length():

    lengths = len(my_input)
    # print(length_of_String)
    return lengths

# function to get the first character of a string


def first_character():
    first_char = my_input[0]
    # print (first_char)
    return first_char

# function to get the last character of a string


def last_character():

    last_char = my_input[string_length()-1]
    # print (last_char)
    return last_char


# fucntion to get the middle characters


def middle_characters():
    mid = int((string_length()/2))
    if (string_length() % 2) == 0:
        middle_char = my_input[mid-1:mid+1]
    else:
        middle_char = my_input[int(mid)]
    return middle_char

# function to get the index of  repeating second char in a string


def my_index():
    i = 1
    ind_positon = ''
    if (i != string_length()-1):
        i = i+1
        print(i)
        if (my_input[i] == my_input[1]):
            ind_positon = f'@ index {i}'
        else:
            ind_positon = 'not found'

    return ind_positon


main()
