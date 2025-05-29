# notebook created Jan 2025
# by Philipp Seiler, University of Toronto Institute for Aerospace Studies
# 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Number of singular values to use when creating compressed image (try modifying it)
k = 3000

filenames = ['image1.png', 'image2.png', 'image3.png']
i = 0 # index for filenames
# Load and preprocess the image
A1 = Image.open(filenames[i]).convert('L')
A1_array=np.array(A1)
A1_double = A1_array.astype(np.float64)

# Perform Singular Value Decomposition
U1, S1, Vt1 = np.linalg.svd(A1_double, full_matrices=False)
print(S1)

# Reconstruct the image using the top k singular values
A1_compressed = np.dot(U1[:, :k], np.dot(np.diag(S1[:k]), Vt1[:k, :]))
print(A1_compressed)

# # you can use this code for plotting:
plt.plot(S1, label = filenames[i])
plt.ylim(1E0)
plt.legend()
plt.yscale('log')
plt.show()

# Display the original and compressed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(A1, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(A1_compressed, cmap='gray')
plt.title(f'Compressed image with {k} singular values')

plt.show()