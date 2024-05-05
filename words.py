# Read a sentence from thhe user
sentence = input("Enter a sentence with at least two words: ")

# Split the sentence into words
words = sentence.split()

# Checl that the sentence contains at least two words
if len(words) < 2:
    print("You need to enter at least two words.")
else:
    # print the number of words
    print("There are", len(words), "words in the sentence.")
    # print the first word
    print("The first word is:", words[0])
    # print the last word
    print("The last word is:", words[-1])

