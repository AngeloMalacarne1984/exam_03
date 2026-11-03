def first_unique_char(s: str) -> int:
    return next((i for i, c in enumerate(s) if s.count(c) == 1), -1)

def main():
    print(first_unique_char("leetcode"))      # 0
    print(first_unique_char("aabbc"))         # 4
    print(first_unique_char("loveleetcode"))  # 2
    print(first_unique_char("aabb"))          # -1
    print(first_unique_char("aA"))            # 0
    print(first_unique_char("z"))             # 0
    print(first_unique_char(""))              # -1

main()
