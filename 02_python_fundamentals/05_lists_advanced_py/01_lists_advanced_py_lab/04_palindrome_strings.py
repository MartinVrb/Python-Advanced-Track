def palindrome(words_list: list, searched_palindrome: str):
    palindrome_list = [word for word in words_list if word == "".join(reversed(word))]
    searched_palindrome_counts = palindrome_list.count(searched_palindrome)
    print(palindrome_list)
    print(f"Found palindrome {searched_palindrome_counts} times")

palindrome(input().split(), input())
