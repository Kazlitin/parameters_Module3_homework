def test(a, b=None, c=''):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

test(1, 2, 'Привет')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  