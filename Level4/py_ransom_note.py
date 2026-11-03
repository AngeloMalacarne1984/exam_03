def ransom_note(note: str, letters: str) -> bool:
    return all(note.count(char) <= letters.count(char) for char in set(note) if not char.isspace())

def main():
    print(ransom_note("aa", "ab"))                   # False
    print(ransom_note("aa", "ab"))                   # False
    print(ransom_note("hello world", "dlrowolleh"))  # True
    print(ransom_note("Hi", "hi"))                   # False
    print(ransom_note("", "abc"))                    # True
    print(ransom_note("abc", ""))                    # False

main()
