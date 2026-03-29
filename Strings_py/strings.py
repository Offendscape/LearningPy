# Strings are a sequence of characters. 
# They are used to store and manipulate text. 
# In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").
# Example of a string
my_string = "Hello, World!"
print(my_string)

# You can also use triple quotes (''' ''' or """ """) for multi-line strings.
my_multiline_string = """This is a multi-line string.
It can span multiple lines."""
print(my_multiline_string)


# Strings are immutable, which means you cannot change them after they are created.
# You can concatenate strings using the + operator.
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)
# You can also repeat strings using the * operator.
laugh = "Ha"
print(laugh * 3)  # Output: HaHaHa

# Strings have many built-in methods for manipulation.
# For example, you can convert a string to uppercase using the upper() method.
lowercase_string = "hello"
uppercase_string = lowercase_string.upper()
print(uppercase_string)  # Output: HELLO

# You can also find the length of a string using the len() function.
string_length = len(my_string)
print(string_length)  # Output: 13

# You can access individual characters in a string using indexing.
first_character = my_string[0]
print(first_character)  # Output: H

# You can also slice strings to get a substring.
substring = my_string[0:5]
print(substring)  # Output: Hello

# Strings can also be formatted using f-strings (formatted string literals).
name = "Bob"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Bob and I am 30 years

# old.
# You can also use the format() method for string formatting.
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Bob and I am 30 years old.

# Strings can also be split into a list of substrings using the split() method.
sentence = "This is a sentence."
words = sentence.split()
print(words)  # Output: ['This', 'is', 'a', 'sentence.']

# You can join a list of strings into a single string using the join() method.
word_list = ['This', 'is', 'a', 'sentence.']
joined_string = ' '.join(word_list)
print(joined_string)  # Output: This is a sentence.

# Strings can also be stripped of whitespace using the strip() method.
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: Hello, World!

# You can also replace parts of a string using the replace() method.
original_string = "Hello, World!"
replaced_string = original_string.replace("World", "Python")
print(replaced_string)  # Output: Hello, Python!

# Strings can also be checked for certain properties using methods like isalpha(), isdigit(), etc.
alpha_string = "Hello"
digit_string = "12345"
print(alpha_string.isalpha())  # Output: True
print(digit_string.isdigit())  # Output: True

# You can also check if a string starts or ends with a certain substring using the startswith() and endswith() methods.
filename = "document.txt"
print(filename.endswith(".txt"))  # Output: True
print(filename.startswith("doc"))  # Output: True

# Strings can also be reversed using slicing.
reversed_string = my_string[::-1]
print(reversed_string)  # Output: !dlroW ,olleH

# You can also find the index of a substring using the find() method.
index = my_string.find("World")
print(index)  # Output: 7

# If the substring is not found, find() returns -1.
index_not_found = my_string.find("Python")
print(index_not_found)  # Output: -1

# You can also count the occurrences of a substring using the count() method.
count = my_string.count("o")
print(count)  # Output: 2

# Strings can also be formatted using the % operator (old-style string formatting).
name = "Charlie"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Charlie and I am 25 years old.

# You can also use the ord() function to get the ASCII value of a character.
ascii_value = ord('A')
print(ascii_value)  # Output: 65

# And the chr() function to get the character from an ASCII value.
character = chr(65)
print(character)  # Output: A

# Strings can also be compared using comparison operators.
string1 = "apple"
string2 = "banana"
print(string1 < string2)  # Output: True
print(string1 == string2)  # Output: False

# You can also use the in operator to check if a substring is in a string.
substring = "World"
print(substring in my_string)  # Output: True

# Finally, you can use the len() function to get the length of a string.
string_length = len(my_string)
print(string_length)  # Output: 13