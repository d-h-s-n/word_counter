import re
# Supports regular expressions 
# Uses ASCII values.
def count_words(input_given):
    
    # Count the number of words in the input given and ignore adjacent duplicates (case-sensitive).
    # Ignore numbers and non-alphabetic characters.
    # input_given (string): The paragraph to count words in.  
     
    # Use regular expression to split the input text into words and filter out non-alphabetic characters
    words = re.findall(r'\b[a-zA-Z]+\b', input_given)
    if not words:
        return 0

    # Initialize count and previous_word
    count = 1  # Start count with the first word
    previous_word = words[0]

    # Iterate through the list of words starting from the second word
    for word in words[1:]:
        if word != previous_word:
            count += 1
            previous_word = word

    return count

def main():
   
    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Please enter a sentence or paragraph: ")

        # Check if the input is empty
        if user_input.strip():
            break
        else:
            print("ERROR : The input cannot be empty. Please enter some sentence or paragraph.")

    # Count the words in the input, ignoring adjacent duplicates and non-alphabetic characters
    word_count = count_words(user_input)

    # Display the word count to the console
    # excluding adjacent duplicates, case-sensitive, ignoring numbers and special characters.
    print(f"The number of words in the entered \" text \" is: {word_count}")      

if __name__ == "__main__":
    main()
def count_words(input_given):
    
   # Count the number of words in the input given and ignore adjacent duplicates (case-sensitive).
   # input given : The paragraph to count words in.
  
   
    # Split the input text by whitespace to get a list of words
    words = input_given.split()

    if not words:
        return 0

    # Initialize count and previous_word
    count = 1  # Start count with the first word
    previous_word = words[0]

    # Iterate through the list of words starting from the second word
    for word in words[1:]:
        if word != previous_word:
            count += 1
            previous_word = word

    return count

def main():

   # Main function to prompt the user for input and display the word count.
   
    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Please enter a sentence or paragraph: ")

        # Check if the input is empty
        if user_input.strip():
            break
        else:
            print("Error: The input cannot be empty. Please enter some text.")

    # Count the words in the input, ignoring adjacent duplicates (case-sensitive)
    word_count = count_words(user_input)

    # Display the word count to the console
    print(f"The number of words in the entered text (excluding adjacent duplicates, case-sensitive) is: {word_count}")

if __name__ == "__main__":
    main()
