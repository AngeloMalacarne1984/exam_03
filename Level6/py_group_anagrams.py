def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_dict: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        anagram_dict.setdefault(key, []).append(word)
    return list(anagram_dict.values())
