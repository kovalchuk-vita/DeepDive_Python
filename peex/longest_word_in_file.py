"""
Write a Python program to find the longest word in a text file.
"""
# file = 'file_with_longest_word.txt'
# with open(file) as f:  # open(file, 'r')
#     f = f.read().split()
#     length = 0
#     longest_word = ""
#     for word in f:
#         if len(word) > length:
#             length = len(word)
#             longest_word = word
#     print(longest_word, length)


# ______________
# How to find more then 1 word with same lengths
def find_longest_words(file_path):
    longest_words = []
    max_length = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_length = len(word)
                if word_length > max_length:
                    longest_words = [word]  # Start a new list for the longest word
                    max_length = word_length
                elif word_length == max_length:
                    longest_words.append(word)  # Add to the list of longest words

    return longest_words

# Example usage
file_path = 'file_with_longest_word.txt'
longest_words = find_longest_words(file_path)
print("Longest word(s):", longest_words)
