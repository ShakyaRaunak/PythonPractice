# https://www.learnpython.org/en/List_Comprehensions
# Example to create a list of integers which specify the length of each word in a certain sentence,
# but only if the word is not "the".
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(word_lengths)

# Using a list comprehension, we could simplify this process to this notation:
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)

# Create a new list out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)


# Loop through a list of lists using list comprehension
def printElement(element):
    print(element)


list_of_lists = [[1, 2], [2, 3], [4, 5], [3, 4], [6, 7], [6, 7], [3, 8]]
[printElement(x[1]) for x in list_of_lists]
