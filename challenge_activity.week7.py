text = input ("Enter a text: ")
print(text.lower())


# Asks what the three letters are
letter1 = input("Enter the first letter: ").lower()

letter2 = input("Enter the second letter: ").lower()

letter3 = input("Enter the third letter: ").lower()


# converts the three letters into a list
letters_list = [letter1, letter2, letter3]
print(letters_list)

# how many times those letters appear, then print
text_tuple = tuple(text) # puts text into a tuple
print(tuple(letters_list)) # converts list to tuple

small_letter1 = text_tuple.count(letter1) # coutnts how many of letter 1, after it has been lowered ^
small_letter2 = text_tuple.count(letter2) # counts how many of letter 2, after it has been lowered ^
small_letter3 = text_tuple.count(letter3) # counts how many of letter 3, after it has been lowered ^

total_letters = small_letter1 + small_letter2 + small_letter3
print(f"The three letters appear {total_letters} times")


# how many words are in the entire text (tranform into list)
print(len(text)) #Prints the number of characters in the list is

# find first and last letter of the text (index)
first_char = text[0]
print(f"The first letter of the text is: {first_char}")
last_char = text[-1]
print(f"The last letter of the text is: {last_char}")

# invert order of list, join elemnets with spaces inbetween 
joined_list = " ".join(letters_list)
print(joined_list)
inverted_text = (joined_list)

# see if "Python" is inside text using a boolean

if "Python" in text: # Checks if the word "Python" is found in the text 
   print('true') #Prints true if the word "Python" is in the text
else:
    print('false') #Prints false if the word "Python" is not in text









