def fibonacci(n):
    a, b = 0, 1
    if n == a or n == b:
        return f'O número{n} pertence à sequência Fibonacci.'
    
    while b < n:
        a, b = b, a + b

    if b == n:
        return f'O número {n} pertence à sequência Fibonacci.'
    else:
        return f'O número {n} não pertence à sequência Fibonacci.'
    
numero = int(input('Informe um número: '))
resultado = fibonacci(numero)
print(resultado)