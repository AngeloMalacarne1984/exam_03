def run_length_encode(text: str) -> str:
    res = []
    curr, count = "", 0
    for c in text:
        if c == curr:
            count += 1
        else:
            if curr:
                res.append(f"{curr}{count}")
            curr, count = c, 1
    if curr:
        res.append(f"{curr}{count}")
    return "".join(res)

def main():
    print(run_length_encode("aaabcc"))        # a3b1c2
    print(run_length_encode("a"))             # a1
    print(run_length_encode("aAa"))           # a1A1a1
    print(run_length_encode("zzzzzzzzzzzz"))  # z12
    print(run_length_encode("aa  b"))         # a2 2b1
    print(run_length_encode(""))              # (empty line)

main()
