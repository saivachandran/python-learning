# 🤖 NumPy for MLOps — Top 20 Most Important Topics

When preparing for **MLOps**, NumPy plays a critical role in data preprocessing, numerical computation, and model deployment pipelines. Below are the **20 key concepts** you should master with short explanations and examples.

---

## 🧠 1. NumPy Arrays (`ndarray`)
**Why it matters:** Core data structure for ML data operations.  
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

---

## ⚙️ 2. Array Shape and Reshaping
**Used for:** Preparing tensors before training or model input.
```python
arr.shape     # (2, 3)
arr.reshape(3, 2)
```

---

## 🧩 3. Broadcasting
**Used for:** Efficient arithmetic between arrays of different shapes.
```python
a = np.array([1, 2, 3])
b = 2
a + b   # [3 4 5]
```

---

## ⚡ 4. Vectorization
**Why:** Avoids Python loops for faster computations — critical in MLOps pipelines.
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a * b   # [4 10 18]
```

---

## 📊 5. Statistical Functions
**Used for:** Analyzing datasets, model predictions.
```python
np.mean(a)
np.std(a)
np.median(a)
```

---

## 🧮 6. Matrix Operations
**Used in:** Neural networks, transformations, covariance matrices.
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.dot(A, B)
```

---

## 🧰 7. Random Number Generation
**Used for:** Weight initialization, data sampling, augmentation.
```python
np.random.rand(3, 2)
np.random.randint(0, 10, 5)
```

---

## 🧱 8. Data Type Management (`dtype`)
**Why:** Ensures numerical precision during model training (float32 vs float64).
```python
arr = np.array([1, 2, 3], dtype=np.float32)
```

---

## 🧼 9. Handling Missing Data (NaN)
**Used in:** Cleaning datasets before ML model input.
```python
arr = np.array([1, np.nan, 3])
np.nanmean(arr)   # Ignores NaN
```

---

## 🔄 10. Stacking and Concatenation
**Used for:** Combining datasets or feature arrays.
```python
a = np.array([[1, 2]])
b = np.array([[3, 4]])
np.vstack((a, b))
```

---

## 🧾 11. Boolean Indexing and Masking
**Used for:** Filtering data efficiently.
```python
arr = np.array([10, 20, 30, 40])
arr[arr > 20]   # [30, 40]
```

---

## ⚖️ 12. Normalization and Scaling
**Used in:** Preprocessing for training models.
```python
arr = np.array([10, 20, 30])
(arr - np.min(arr)) / (np.max(arr) - np.min(arr))
```

---

## 🧠 13. Axis Operations
**Used for:** Performing row/column-wise computations.
```python
arr = np.array([[1,2,3],[4,5,6]])
arr.sum(axis=0)  # Column sum
```

---

## 📦 14. Saving and Loading Arrays
**Used for:** Caching preprocessed data in MLOps workflows.
```python
np.save('data.npy', arr)
arr = np.load('data.npy')
```

---

## 🧬 15. Flattening and Ravel
**Used for:** Converting multidimensional arrays into 1D.
```python
arr.flatten()
```

---

## 🔁 16. Unique and Counting
**Used for:** Label analysis and categorical data preprocessing.
```python
arr = np.array([1,2,2,3,3,3])
np.unique(arr, return_counts=True)
```

---

## 📈 17. Mathematical Operations
**Used in:** Feature transformations, loss functions, gradient calculations.
```python
np.exp(arr)
np.log(arr)
np.sqrt(arr)
```

---

## ⚙️ 18. Performance Optimization
**Tip:** Use NumPy vectorization and avoid loops for speed.
```python
# Instead of:
sum([i*i for i in range(10000)])

# Use:
np.sum(np.arange(10000)**2)
```

---

## 🧠 19. Integration with Pandas and Scikit-learn
**Why:** NumPy arrays are the backbone of ML frameworks.
```python
import pandas as pd
import sklearn
df = pd.DataFrame(np.random.rand(5,3))
```

---

## 🧩 20. Linear Algebra Module (`np.linalg`)
**Used in:** Model optimization, PCA, regression, and transformations.
```python
A = np.array([[1,2],[3,4]])
np.linalg.inv(A)
np.linalg.det(A)
```

---

✅ **MLOps Tip:**  
Focus on how NumPy integrates with **data pipelines**, **feature engineering**, and **ML frameworks (TensorFlow, PyTorch, Scikit-learn)** — not just syntax.

---
