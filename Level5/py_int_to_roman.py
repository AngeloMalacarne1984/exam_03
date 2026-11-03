ROMAN_MAP = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10: "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
)

def int_to_roman(number: int) -> str:
    if not 1 <= number <= 3999:
        return "ERROR"
    res = []
    for val, symbol in ROMAN_MAP:
        count, number = divmod(number, val)
        res.append(symbol * count)
    return "".join(res)
