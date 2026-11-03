def count_occurrences(sub: str, text: str) -> int:
    return text.count(sub) if sub else 0

def main():
    print(count_occurrences("ab", "ababab"))  # 3
    print(count_occurrences("aa", "aaaa"))    # 2
    print(count_occurrences("aa", "aaa"))     # 1
    print(count_occurrences("Ab", "abAb"))    # 1
    print(count_occurrences("x", "abc"))      # 0
    print(count_occurrences("abc", "ab"))     # 0
    print(count_occurrences("", "abc"))       # 0

main()
