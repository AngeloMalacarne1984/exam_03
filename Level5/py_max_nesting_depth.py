def max_nesting_depth(s: str) -> int:
    depth: int = 0
    max_depth: int = 0

    for c in s:
        if c == "(":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif c == ")":
            depth -= 1
            if depth < 0:
                return -1

    if depth == 0:
        return max_depth
    else:
        return -1
