# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
print("hello world!")
name = input("What is your name? ")
print("Nice to meet you,", name)

# function that takes parameters
def conversation():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

conversation()

def dialog():
  print("Hello. Nice to meet you")
  name = input("What's your name? ")
  state = input("How are you?")
  if(state == "I am fine"):
    print("Good to know, ", name)
  elif state == "I am not well":
    print("I am so sorry, ", name,".")
  else: 
    print("Ok. Thanks for letting me know.")

dialog()

# function that returns a value
def multiplier(n):
    return n*n
val = multiplier(8)
print(val)

# function with default value for an parameter
def currency_converter(user_input):
    rate = int(input("What is conversion rate? "))
    if (user_input > 0 or rate !=0):
        return user_input/rate
    else:
        print("Undefined")

FromCurrency = input("What currency are you converting from? ")
ToCurrency = input("What currency are you converting to? ")
amount_to_convert = int(input("Enter your amount: "))
ans = currency_converter(amount_to_convert)
print(f"{amount_to_convert} in {FromCurrency} is {ans} in {ToCurrency}.")

# function with variable number of parameters
def age_adder(*ages):
    result = 0
    for n in ages:
        result = result + n
    return result
print(age_adder(30, 40, 25, 18, 19))