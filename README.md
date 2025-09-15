# 🔐 Criptografía y Computación Cuántica: Algoritmo de Shor con Qiskit

---

## 📌 Description / Descripción

**EN**  
This project explores the relationship between **classical cryptography (RSA)** and **quantum computing**, highlighting the threat posed by **Shor’s algorithm** to cryptographic systems based on integer factorization.

Using [Qiskit](https://qiskit.org/), we implement a **simulation of Shor’s algorithm** to factorize small numbers (e.g., 15 or 21), allowing us to understand how quantum computing can endanger current digital security.

**ES**  
Este proyecto explora la relación entre la **criptografía clásica (RSA)** y la **computación cuántica**, destacando la amenaza que supone el **algoritmo de Shor** para los sistemas criptográficos basados en la factorización de enteros.

Con [Qiskit](https://qiskit.org/), se implementa una **simulación del algoritmo de Shor** para factorizar números pequeños (como 15 o 21), con el objetivo de comprender cómo la computación cuántica puede poner en riesgo la seguridad digital actual.

---

## 📖 Contents / Contenido

- 🔑 RSA Algorithm / El algoritmo RSA
- 📉 Shor’s algorithm / El algoritmo de Shor
- 📊 Results of the algorithm with 15/ Resultados del algoritmo con 15

---

## ⚡ Requirements / Requisitos

**Conda environment** is recommended / **Se recomienda** utilizar la herramienta de Conda
A IBM cloud account is also needed if you want to run in the QPU / Se necesitará una cuenta de IBM cloud si se quiere correr en los QPU

```bash
python 3.9+
pip install qiskit
pip install qiskit_aer
pip install qiskit_ibm_runtime
pip install matplotlib
pip install pandas
```

---

## 🧩 Example Usage / Ejemplo de uso

**Python code (classic Shor's algorithm):**

```python
import random
from math import gcd

def find_period(a, N):
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None

def shor_simulation(N):
    a = random.randint(2, N - 1)
    print(f"Using a = {a}")

    if gcd(a, N) != 1:
        return [gcd(a, N), N // gcd(a, N)]

    r = find_period(a, N)
    if r is None or r % 2 != 0:
        return None

    x = pow(a, r // 2, N)
    if x == 1 or x == N - 1:
        return None

    factor1 = gcd(x - 1, N)
    factor2 = gcd(x + 1, N)
    return factor1, factor2

N = 15
result = shor_simulation(N)
if result:
    print(f"Factors of {N}: {result[0]} and {result[1]}")
else:
    print("No valid factors found in this run.")
```

**Expected output:**

```
Using a = 2
Factors of 15: 3 and 5
```

---

## Results / Resultados
In the experiment, the simulator gets 5 and 3, while the QPU has some errors.
---

## ✨ Acknowledgment / Agradecimientos

- **Qiskit**: that helped me to understand the basics of quantum programming / **Qiskit**: que me ha ayudado mucho a entender la programación cuántica.
- Also to [Diego Emilio Serrano](https://youtube.com/@diemilio?si=9FtAxE6Qgd3o8u_s) that helped me with his video in this amazing world of quantum computing / También a [Diego Emilio Serrano](https://youtube.com/@diemilio?si=9FtAxE6Qgd3o8u_s) que me ha ayudado en este maravilloso mundo de la computación cuántica.
- The book of **National Geographic** of cryptography / El libro de **National Geograpchic** de criptografía.
