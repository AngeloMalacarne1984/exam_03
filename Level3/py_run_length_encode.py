def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    res, count = "", 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            res += f"{text[i - 1]}{count}"
            count = 1

    return res + f"{text[-1]}{count}"

def main():
    print(run_length_encode("aaabcc"))        # a3b1c2
    print(run_length_encode("a"))             # a1
    print(run_length_encode("aAa"))           # a1A1a1
    print(run_length_encode("zzzzzzzzzzzz"))  # z12
    print(run_length_encode("aa  b"))         # a2 2b1
    print(run_length_encode(""))              # (empty line)

main()
