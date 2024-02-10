def count_words(text):
    """

    Function to Counts the number of words in a given text
    string.
    
    """
    # if the string is empty then return the words_count as 0
    if not text:
        return 0

    # Split the text into words, removing leading/trailing whitespace and empty strings
    words = [word.strip() for word in text.split() if word.strip()]
    return len(words)
# Main function
text = input("Enter some text:\n")
word_count = count_words(text)
print(f"The text contains {word_count} words.")