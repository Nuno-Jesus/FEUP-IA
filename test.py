import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

string = "Nuno Miguel Carvalho de Jesus"
print(string.replace("z", "a"))

# ----------------------------------------------------- #

num = 3 / 5
print(num)

# ----------------------------------------------------- #

is_male = True
print(is_male)

# ----------------------------------------------------- #

list = [1, 2, 'o teu cu']
print(list)

# ----------------------------------------------------- #

tuple = (1, 4)
print(tuple)

# ----------------------------------------------------- #

tuplesList = [(1, 5), (2, 9), (6, 2)]
tuplesList[0] = (2, 4)
print(tuplesList)

# ----------------------------------------------------- #

def doSomething():
  print("Do something")

doSomething()

# ----------------------------------------------------- #

is_tall = False
if is_male and is_tall:
  print("You are a tall male")
elif is_male and not(is_tall):
  print("You are not a tall male")
elif not(is_male) and is_tall:
  print("You are a tall female")
else:
  print("You are not a tall female")

# ----------------------------------------------------- #

def max_string(string1, string2):
  if string1 > string2:
    return string1
  else:
    return string2

print(max_string("Dog", "Cat"))

# ----------------------------------------------------- #

dictionary = {
  "Jan" : "January",
  "Feb" : "February"
}

print(dictionary)
print(dictionary["Jan"])
print(dictionary.get("Feb"))
print(dictionary.get("Mar", "Not a valid key"))

# ----------------------------------------------------- #

for letter in "Girrafe Academy":
  print(letter)

for tuple in tuplesList:
  print(tuple)

for number in range(len("Girrafe Academy")):
  print(number)