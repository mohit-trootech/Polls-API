import numpy as np
import matplotlib.pyplot as plt

# Create a random image
width, height = 800, 600
random_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Display the image
plt.imshow(random_image)
plt.axis("off")
plt.show()

# Save the image
plt.imsave("test_img_numpy.png", random_image)
