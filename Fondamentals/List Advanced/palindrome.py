# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".
def palindrome_func(word):
    if word == word[::-1]:
        return word


sequence=input().split()
palindrome=input()

palindrome_list=[pal for pal in sequence if palindrome_func(pal)]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")