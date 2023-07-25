from hello import hello_world, say_hello
import numerical_functions as nf

if __name__ == '__main__':
    hello_world()
    name = input('What\'s your name?: ')
    say_hello(name)
    print(nf.add(1, 1), nf.subtract(5, 4), nf.multiply(5, 5), nf.divide(20, 4))