def atbash_cipher(text: str) -> str:
    return "".join(
        chr(219 - ord(c)) if "a" <= c <= "z" else
        chr(155 - ord(c)) if "A" <= c <= "Z" else c
        for c in text
    )

def main():
    print(atbash_cipher("abc"))           # zyx
    print(atbash_cipher("Hello World!"))  # Svool Dliow!
    print(atbash_cipher("xyz123"))        # cba123
    print(atbash_cipher("Zz"))            # Aa
    print(atbash_cipher(""))              # (linha vazia)

main()
