show_expected_result = False
show_hints = False

def count_numbers(which, *numbers):
    # Your code goes here
    even_num = []
    odd_num = []
    count_num = 0
    for n in numbers[0]: # Access the list of numbers passed as the first argument
        if n > 0:
            count_num += 1
            remainder = n % 2
            if remainder == 0 and which == "even":
                even_num.append(n)
            elif remainder == 1 and which == "odd":
                odd_num.append(n)
        else:
            print("Invalid number in the list")

    if which == "even":
        return len(even_num) if count_num > 0 else -1
    elif which == "odd":
        return len(odd_num) if count_num > 0 else -1
    else:
        return -1

numType = input("What do type of numbers are you counting? ").lower()
mylist_str = input("Enter list of numbers: ")
mylist = [int(x.strip()) for x in mylist_str.split(',')] # Split the input string by comma and convert each number to int

count_result = count_numbers(numType, mylist)
print(count_result)