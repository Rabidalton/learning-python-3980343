# Python code​​​​​​‌‌​‌‌​‌‌‌​‌‌‌​‌‌​‌​​​​‌‌​ below
# Use print("messages...") to debug your solution.

# import string

# text = "Hello, World! Let's remove spaces and punctuation."
# cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
# print(cleaned_text)  
# Output: HelloWorldLetsremovespacesandpunctuation

import string

def is_palindrome(teststr):
    if(teststr.isalpha() == False):
        cleanteststr = teststr.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
        cleanteststrlower = cleanteststr.lower()
        backwardstr = cleanteststrlower[::-1]
        if(backwardstr == cleanteststrlower):
            return True
        else:
            return False
    else:
        print("Invalid strings!")

test_word1 = "Madam, I'm Adam."
# try using some of these other words:
test_word2 = "RACE CAR!"
test_word3 = "Hello, world"
test_word4 = "Radar?"
test_word5 = "A man, a plan, a canal Panama!"

result1 = is_palindrome(test_word1)
result2 = is_palindrome(test_word2)
result3 = is_palindrome(test_word3)
result4 = is_palindrome(test_word4)
result5 = is_palindrome(test_word5)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


# text = "Hello, World!"
# no_whitespace = text.replace(" ", "")
# no_punctuation = text.replace(",", "").replace("!", "")
# print(no_whitespace)   # Output: Hello,World!
# print(no_punctuation)  # Output: Hello World

# text = "Hello, world! How's it going?"
# punctuation = ".,!?;:'\""
# for char in punctuation:
#     text = text.replace(char, "")
# print(text)  # Output: Hello world Hows it going
