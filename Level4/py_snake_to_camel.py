def snake_to_camel(text: str) -> str:
    words = [w for w in text.split("_") if w]
    return words[0].lower() + "".join(w.capitalize() for w in words[1:]) if words else ""
