def display(str):
    print(str)


def displaydecorator(fn):
    def display_wrapper(str):
        print('Output:', end=" ")
        fn(str)

    return display_wrapper


out = displaydecorator(display)
out('Hello World')  # Output: Hello World
