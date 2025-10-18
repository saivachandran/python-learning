# 🧮 NumPy Python — Top 20 Interview Questions and Answers

---

## 🧠 Basic Level

### 1. What is NumPy and why is it used?
**Answer:**  
NumPy (Numerical Python) is a Python library for numerical computing. It provides:
- Powerful **N-dimensional arrays (ndarray)**
- Fast mathematical operations
- Tools for linear algebra, Fourier transform, and random number generation

---

### 2. What is the difference between Python lists and NumPy arrays?
| Feature | Python List | NumPy Array |
|----------|--------------|-------------|
| Data Type | Can store mixed data types | Stores only one data type |
| Speed | Slower | Faster (implemented in C) |
| Memory | More memory | Less memory |
| Vectorization | Not supported | Supported |

---

### 3. How do you create a NumPy array?
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
