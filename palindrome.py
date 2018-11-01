def clean_words(words):
    new_text = ""
    words = words.lower()   
    for char in words:
        if char.isalpha():
            new_text = new_text + char
    return new_text


def is_palindrome(words):
    if len(words) == 0 or len(words) == 1:
        print("is a palindrome")
        return True
    elif words[0] == words[-1]:
        return is_palindrome(words[1:-1])
    else:
        print("is not a palindrome")
        return False
words = input("What word would you like to use? ")
a = clean_words(words)
is_palindrome (a)


# def convert_grade(grade):
#     if grade >= 90:
#         print("A")
#     elif grade >= 80:
#         print("B")
#     elif grade >= 70:
#         print("C")
#     elif grade >= 60:
#         print("D")
#     else:
#         print("F")
# convert_grade(99)


# convert_grade(89)

# convert_grade(50)

# def addify(num, num2):
#     if num < num2:
#         num += 1
#         addify(num, num2)
#     else:

