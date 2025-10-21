Real-World MLOps Examples Using ndarray
The ndarray is utilized at various stages of an MLOps pipeline, from data preparation to model monitoring:

1. Feature Normalization Before Model Training
Python

import numpy as np

features = np.array([[50, 80, 100],
                     [20, 60, 90],
                     [30, 40, 70]])

# Normalize between 0 and 1 using vectorized operations
normalized = (features - np.min(features)) / (np.max(features) - np.min(features))

print(normalized)
✅ Purpose: Used before training ML models to ensure all features are on a similar scale, improving model convergence and performance. The operation is fast because it's vectorized.

2. Batch Processing in Model Pipelines
Python

# Simulating batches of input data
data = np.random.rand(100, 10)  # 100 samples, 10 features each

# Split into mini-batches for efficient model input
batches = np.array_split(data, 10)

for batch in batches:
    # Each batch (10x10) can be sent to model for inference or training
    print(batch.shape)
✅ Purpose: Essential in model serving or training jobs to process data in fixed-size mini-batches, which is necessary for efficient utilization of GPUs and common deep learning frameworks.

3. Model Predictions and Post-processing
Python

predictions = np.array([0.2, 0.9, 0.8, 0.4])
threshold = 0.5

# Vectorized post-processing to convert probabilities to binary labels
labels = (predictions > threshold).astype(int)

print(labels)  # [0 1 1 0]
✅ Purpose: Used for rapid post-processing of model outputs (e.g., applying a threshold for binary classification) before presenting final results to the user or downstream systems.

4. Data Drift Detection
Python

old_data = np.random.normal(50, 10, 1000)
new_data = np.random.normal(60, 10, 1000)

# Compare means to detect drift using NumPy's efficient statistical functions
drift = abs(np.mean(old_data) - np.mean(new_data))

print("Drift detected:", drift > 5)
✅ Purpose: Used in MLOps monitoring pipelines to quickly calculate statistics and detect significant shifts or data drift between production data and historical training data.

5. Saving Processed Arrays in MLOps Pipelines
Python

# Assuming 'normalized' from Example 1 is available
# np.save is used to store data in a compact, efficient binary format
np.save('/tmp/cleaned_data.npy', normalized)
loaded_data = np.load('/tmp/cleaned_data.npy')

print(loaded_data.shape)
✅ Purpose: Used in pipelines for storing intermediate processed data (e.g., after feature engineering) efficiently and compactly, facilitating quick loading for subsequent steps or model training.

🔑 Summary
Feature	Why it Matters in MLOps
Speed	Handles large data sets faster than standard Python lists for time-sensitive pipeline steps.
Vectorization	Enables efficient and concise code for data transformation and model preprocessing.
Integration	Works seamlessly with major Machine Learning and deep learning frameworks (TensorFlow, PyTorch).
Ease of Use	Provides a simple syntax for complex matrix and tensor operations fundamental to ML.
Storage	Efficiently saves and loads model-ready data and intermediate pipeline results.
