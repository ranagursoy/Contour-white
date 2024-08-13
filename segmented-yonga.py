from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, label

def segment_image(image_path):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    image_array = np.array(gray_image)
    
    plt.imshow(image_array, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.show()

    binary_image = image_array > 200
    labeled_array, num_features = label(binary_image)
    
    plt.imshow(labeled_array, cmap='nipy_spectral')
    plt.title('Segmented Image')
    plt.axis('off')
    plt.show()
    
    print(f"Number of segments: {num_features}")

def segment_image_based_on_density(image_path, threshold=0.5, sigma=5):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    image_array = np.array(gray_image)

    binary_image = image_array > 200
    density_map = gaussian_filter(binary_image.astype(float), sigma=sigma)
    density_map_normalized = (density_map - np.min(density_map)) / (np.max(density_map) - np.min(density_map))
    high_density_regions = density_map_normalized > threshold

    segmented_colormap = np.zeros((image_array.shape[0], image_array.shape[1], 3))
    segmented_colormap[..., 0] = high_density_regions
    segmented_colormap[..., 2] = ~high_density_regions

    plt.imshow(segmented_colormap)
    plt.title('Density-based Segmentation')
    plt.axis('off')
    plt.show()

image_path = '.bmp'
segment_image(image_path)
segment_image_based_on_density(image_path)
