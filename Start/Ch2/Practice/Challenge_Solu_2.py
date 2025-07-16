# Python code​​​​​​‌‌​‌‌​‌‌​‌​​‌‌​‌​​‌‌‌‌‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    # Your code goes here
    if(which != "even" and which != "odd"):
        return -1

    result = 0
    for n in numbers:
        if(n%2 == 0 and which == "even"):
            result += 1
        if(n%2 == 1 and which == "odd"):
            result += 1
    return result

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

result1 = count_numbers("even", numbers)
result2 = count_numbers("odd", numbers)
result3 = count_numbers("Blarg", numbers)

print(result1)
print(result2)
print(result3)