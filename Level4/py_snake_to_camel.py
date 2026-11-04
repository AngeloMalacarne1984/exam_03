def snake_to_camel(text: str) -> str:
    words = [w for w in text.split("_") if w]
    return words[0].lower() + "".join(w.capitalize() for w in words[1:]) if words else ""

def main():
    print(snake_to_camel("hello_world"))   # helloWorld
    print(snake_to_camel("make_it_work"))  # makeItWork
    print(snake_to_camel("HELLO_WORLD"))   # helloWorld
    print(snake_to_camel("user__id_2"))    # userId2
    print(snake_to_camel("__init__"))      # init
    print(snake_to_camel("already"))       # already
    print(snake_to_camel(""))              # (linha vazia)

main()
