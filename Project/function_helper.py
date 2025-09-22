from qiskit import QuantumCircuit
import numpy as np
import random
import math
from typing import Any, Callable
import time

def timer(func) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start: float = time.time()
        result: Any = func(*args, **kwargs)
        end: float = time.time()
        print(f"Ran '{func.__name__!r} in {(end - start)*1000:.2f} miliseconds'")

        return result
    
    return wrapper



def QFT(n):
    # Número de qubits
    qft_circ = QuantumCircuit(n)
    for i in range(n//2):
        qft_circ.swap(i, n - i - 1)
    for j in range(n):
        for m in range(j):
            qft_circ.cp(-np.pi/float(2**(j-m)), m, j)
        qft_circ.h(j)

    puerta = qft_circ.to_gate()
    puerta.name = "QFT" + str(n)
    return puerta


# Puerta para módulo quince
def c_amod15(a, power):
    u = QuantumCircuit(4)
    for i in range(power):
        u.swap(2, 3)
        u.swap(1, 2)
        u.swap(0, 1)
        for q in range(4):
            u.x(q)
    u = u.to_gate()
    u.name = "%i ^ %i mod 15" % (a, power)
    c_u = u.control()
    return c_u

# Encuentra n valores máximos

@timer
def find_n_max_value(list: list, n: int) -> list:
    temp_list = list.copy()
    output_list = []
    for i in range(0, n):
        output_list.append(max(temp_list))
        temp_list.remove(output_list[i])
    return output_list

# Encuentra los valores mínimos

@timer
def find_n_min_value(list: list, n: int) -> list:
    temp_list = list.copy()
    output_list = []
    for i in range(0, n):
        output_list.append(min(temp_list))
        temp_list.remove(output_list[i])
    return output_list

# Verifica si es un número primo

@timer
def ver_prime(n: int) -> bool:
    is_prime = True
    if n >= 2:
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n == 2:
                continue
            elif n % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime == True:
        return True
    else:
        return False


# Genera un número primo random
@timer
def generate_prime(min, max) -> int:
    prime = random.randint(min, max)
    while not ver_prime(prime):
        prime = random.randint(min, max)
    return prime


if __name__ == '__main__':
    prime = generate_prime(1, 10000)
    print(f'This is your prime number: {prime}')
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_n_max_value(list, 4))
    print(find_n_min_value(list, 4))
