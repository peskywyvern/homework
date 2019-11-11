# Write a function copy_string which takes a string and recursively, character
# by character creates a copy of it.


def copy_string(string: str, copy='') -> str:
    if len(string) != len(copy):
        copy += string[len(copy)]
        return copy_string(string, copy)
    return copy


# Write a function first_letter which takes a string and returns first
# uppercase letter in it


def first_letter(string: str, index=0) -> str:
    if string[index].isupper():
        return string[index]
    return first_letter(string, index + 1)


# Write a function is_palindrome which takes a string and returns boolean
# whether the string is a palindrome or not


def is_palindrome(word: str, index=0) -> bool:
    if index == len(word) // 2:
        return True
    if word[index] == word[len(word) - 1 - index]:
        return is_palindrome(word, index+1)
    return False


