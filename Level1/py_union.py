def union(s1: str, s2: str) -> str:
    return "".join(dict.fromkeys(s1 + s2))

def main():
    print(union("abc", "bcd"))      # abcd
    print(union("hello", "world"))  # helowrd
    print(union("aaa", ""))         # a
    print(union("", "abc"))         # abc
    print(union("abc", "ABC"))      # abcABC
    print(union("", ""))            # (linha vazia)

main()
