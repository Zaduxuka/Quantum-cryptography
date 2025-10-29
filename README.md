
# Quantum-cryptography

**Repositorio para el proyecto / informe:** "Criptografía cuántica: El algoritmo de Shor y su impacto en la actualidad".  
Autor: **Zihao Xu** .  
URL: https://github.com/Zaduxuka/Quantum-cryptography

---

## Resumen
Implementación y experimentos con el **algoritmo de Shor** usando Qiskit. Incluye notebooks reproducibles, scripts y el informe asociado en `docs/`.

---

## Estructura del repositorio
- `README.md` — este fichero.
- `LICENSE` — licencia MIT.
- `CITATION.cff` — metadatos para citación.
- `requirements.txt` — dependencias.
- `src/` — módulos Python.
- `data/` — resultados.
- `docs/` — informe en PDF y documentación adicional.

---

## Dependencias e instalación
1. Crear entorno (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   pip install --upgrade pip
   pip install -r requirements.txt

## 📌 Description / Descripción

**EN**  
This project explores the relationship between **classical cryptography (RSA)** and **quantum computing**, highlighting the threat posed by **Shor’s algorithm** to cryptographic systems based on integer factorization.

Using [Qiskit](https://qiskit.org/), we implement a **simulation of Shor’s algorithm** to factorize small numbers (e.g., 15 or 21), allowing us to understand how quantum computing can endanger current digital security.

**ES**  
Este proyecto explora la relación entre la **criptografía clásica (RSA)** y la **computación cuántica**, destacando la amenaza que supone el **algoritmo de Shor** para los sistemas criptográficos basados en la factorización de enteros.

Con [Qiskit](https://qiskit.org/), se implementa una **simulación del algoritmo de Shor** para factorizar números pequeños (como 15 o 21), con el objetivo de comprender cómo la computación cuántica puede poner en riesgo la seguridad digital actual.


## ✨ Acknowledgment / Agradecimientos

- **Qiskit**: that helped me to understand the basics of quantum programming / **Qiskit**: que me ha ayudado mucho a entender la programación cuántica.
- Also to [Diego Emilio Serrano](https://youtube.com/@diemilio?si=9FtAxE6Qgd3o8u_s) that helped me with his video in this amazing world of quantum computing / También a [Diego Emilio Serrano](https://youtube.com/@diemilio?si=9FtAxE6Qgd3o8u_s) que me ha ayudado en este maravilloso mundo de la computación cuántica.
- The book of **National Geographic** of cryptography / El libro de **National Geograpchic** de criptografía.
