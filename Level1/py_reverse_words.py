def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])

if __name__ == "__main__":
    print(reverse_words("hello world"))           # world hello
    print(reverse_words("  the sky   is blue "))  # blue is sky the
    print(reverse_words("a b c"))                 # c b a
    print(reverse_words("one"))                   # one
    print(reverse_words("   "))                   # (linha vazia)
    print(reverse_words(""))                      # (linha vazia)
