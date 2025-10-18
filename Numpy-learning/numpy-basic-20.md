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
```

---

### 4. How do you create arrays of zeros, ones, and a range?
```python
np.zeros((3,3))      # 3x3 matrix of zeros
np.ones((2,2))       # 2x2 matrix of ones
np.arange(0,10,2)    # [0 2 4 6 8]
```

---

### 5. How do you get the shape, size, and data type of a NumPy array?
```python
arr.shape    # Dimensions
arr.size     # Total elements
arr.dtype    # Data type
```

---

## ⚙️ Intermediate Level

### 6. What is broadcasting in NumPy?
**Answer:**  
Broadcasting allows operations between arrays of different shapes by automatically expanding smaller arrays.  
Example:
```python
a = np.array([1,2,3])
b = 2
print(a + b)   # [3 4 5]
```

---

### 7. What is vectorization?
**Answer:**  
Vectorization means performing operations on entire arrays without explicit loops.  
Example:
```python
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)   # [5 7 9]
```

---

### 8. How do you perform slicing on NumPy arrays?
```python
arr = np.array([10,20,30,40,50])
print(arr[1:4])  # [20 30 40]
```

---

### 9. How to reshape a NumPy array?
```python
arr = np.arange(6)
arr2 = arr.reshape((2,3))
```

---

### 10. What are some commonly used NumPy functions?
| Function | Purpose |
|-----------|----------|
| `np.mean()` | Average |
| `np.median()` | Median |
| `np.std()` | Standard deviation |
| `np.sum()` | Sum of elements |
| `np.dot()` | Matrix multiplication |

---

## 📊 Advanced Level

### 11. What is the difference between `np.copy()` and simple assignment (`=`)?
**Answer:**
- `=` creates a **view/reference** (changes affect both arrays)
- `np.copy()` creates a **deep copy** (independent data)

```python
a = np.array([1,2,3])
b = a
c = np.copy(a)
b[0] = 99
print(a)  # [99  2  3]
print(c)  # [1 2 3]
```

---

### 12. How do you stack arrays vertically and horizontally?
```python
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
print(np.vstack((a,b)))  # Vertical
print(np.hstack((a,b.T)))  # Horizontal
```

---

### 13. What are NumPy axes?
**Answer:**  
Axes represent dimensions.  
- Axis 0 → rows  
- Axis 1 → columns  

Example:
```python
arr = np.array([[1,2,3],[4,5,6]])
arr.sum(axis=0)  # [5 7 9]
```

---

### 14. How to generate random numbers using NumPy?
```python
np.random.rand(3)        # Random floats between 0–1
np.random.randint(0,10,5) # 5 random integers [0–9]
```

---

### 15. What is the difference between `np.ndarray` and `np.matrix`?
**Answer:**
- `ndarray` is a general-purpose array.
- `matrix` is strictly 2D and supports only matrix operations.  
NumPy recommends **using ndarray** instead of matrix.

---

### 16. How do you find unique elements in an array?
```python
arr = np.array([1,2,2,3,3,3])
np.unique(arr)   # [1 2 3]
```

---

### 17. How can you save and load NumPy arrays?
```python
np.save('myarr.npy', arr)
loaded = np.load('myarr.npy')
```

---

### 18. How to handle missing values (`NaN`) in NumPy?
```python
arr = np.array([1, 2, np.nan, 4])
np.nanmean(arr)   # Ignores NaN while computing mean
```

---

### 19. How to flatten a multi-dimensional array?
```python
arr = np.array([[1,2],[3,4]])
arr.flatten()   # [1 2 3 4]
```

---

### 20. How to perform element-wise comparison in NumPy?
```python
a = np.array([1,2,3])
b = np.array([2,2,3])
a == b    # [False  True  True]
np.all(a == b)  # False
```

---

✅ **Tip:** Master these topics along with hands-on practice in slicing, reshaping, and broadcasting — these are among the most asked NumPy concepts in interviews!
