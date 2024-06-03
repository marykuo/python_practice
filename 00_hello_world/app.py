def hello():
    print("Hello, world!")
    return {"message": "Hello, world!"}


def demo_print():
    print("I say 'Hello'")
    print('I say "Hello"')
    print('I say \n\'Hello\'')


def demo_input():
    answer = input("say something: ")
    print(answer)


if __name__ == "__main__":
    result = hello()
    print(result)

    demo_print()

    demo_input()
