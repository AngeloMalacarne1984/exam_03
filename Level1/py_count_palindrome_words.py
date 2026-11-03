def count_palindrome_words(text: str) -> int:
    return sum(1 for w in text.lower().split() if w == w[::-1])

if __name__ == "__main__":
    print(count_palindrome_words("Anna saw a racecar"))  # 3
    print(count_palindrome_words("Level   noon"))        # 2
    print(count_palindrome_words("Bob"))                 # 1
    print(count_palindrome_words("hello world"))         # 0
    print(count_palindrome_words("abc cba"))             # 0
    print(count_palindrome_words(""))                    # 0
