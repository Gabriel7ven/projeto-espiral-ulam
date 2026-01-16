from turtle import *
import math

def isPrime(n):
    """Funcão para testar se um dado número inteiro é primo."""
    
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    
    # Testando para valors ímpares
    limit = math.floor(n/2)
    for i in range(3, limit):
        if n % i == 0:
            return False
    return True


def loopStep(count,i):
    """Função que permite a turtle avançar um dado número de passos na mesma direção e no final rotacionar
        90 graus para a esquerda."""
        
    contador = count
    for j in range(i):
        if isPrime(contador):
            dot(3,"black")
            
        fd(1*2)
        contador += 1
        
    left(90)
    return contador



def main():
    speed(0)
    count = 1
    limit = 200
    contador = 1
    penup()
    for i in range(1,limit):
        contador = loopStep(contador,i)
        contador = loopStep(contador,i)



main()
mainloop()



