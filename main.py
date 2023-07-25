from hello import hello_world, say_hello

if __name__ == '__main__':
    hello_world()
    name = input('What\'s your name?: ')
    say_hello(name)