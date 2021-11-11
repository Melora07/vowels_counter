
def get_vowels_numbers(word):
    # creates a vowels counter
    count_vowels = 0

    # verifies the vowels letter in the choose word
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # adds to the counter
            count_vowels += 1
    # a the end sends to the counter
    return count_vowels

# enter a word
word = input("Entrez un mot:")
# associates the function with result
result = get_vowels_numbers(word)
# displays the vowels counter
print("Il y a ", result, "voyelles dans ", word)
