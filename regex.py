import re

# 4. Write a Python program that matches a string that has an a followed by
# zero or one 'b'


def match_ab(string: str):
    pattern = re.compile(r'ab?')
    if pattern.match(string):
        return f'Matched: {pattern.match(string).group()}'
    return 'Match not found'


# print(match_ab("abbc"))
# print(match_ab("d"))


# 10. Write a Python program that matches a word at the beginning of a string.


def match_start(string: str):
    pattern = re.compile(r"^\w+")
    if pattern.match(string):
        return f'Matched: {pattern.match(string).group()}'
    return 'Match not found'


# print(match_start("hey there"))


# 11. Write a Python program that matches a word at end of string,
# with optional punctuation.


def match_end(string: str):
    pattern = re.compile(r'\w+\W?$')
    if pattern.search(string):
        return f'Matched: {pattern.search(string).group()}'
    return 'Match not found'


# print(match_end("hey there!"))


# 16. Write a Python program to remove leading zeros from an IP address.


def remove_zeros(string: str):
    return re.sub(r"\.[0]+", ".", string)


# print(remove_zeros("432.010.001.021"))


# 42. Write a Python program to find urls in a string.


def find_urls(string: str):
    pattern = r"(http(s?)://(www.)?\w+\.\w+(/\w+)?)+"
    urls = re.findall(pattern, string)
    for url in urls:
        print(url[0])


# find_urls('websites:"http://www.google.com/cats", '
#           '"https://youtube.com/feed"')


# 50. Write a Python program to remove the parenthesis area in a string.
# Sample data : ["example (.com)", "w3resource", "github (.com)",
# "stackoverflow (.com)"]

def remove_parenthesis(strings: list):
    return [re.sub(r"\([^\s]+\)", "", string).strip() for string in strings]


print(remove_parenthesis(["example (.com)", "w3resource", "github (.com)",
                          "stackoverflow (.com)"]))


