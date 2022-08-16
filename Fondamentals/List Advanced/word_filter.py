# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even.
# Print each word on a new line.

words=input().split()
even_len_words=[word for word in words if len(word)%2==0]
for word in even_len_words:
    print(word)