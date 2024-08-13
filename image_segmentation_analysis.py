import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, label
import csv

def segment_image(image_path, binary_threshold=200):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    image_array = np.array(gray_image)
    
    binary_image = image_array > binary_threshold
    labeled_array, num_features = label(binary_image)
    
    return labeled_array, num_features

def calculate_gap_and_overlap_ratios(labeled_array, density_map, threshold):
    total_area = labeled_array.size
    
    gap_area = np.sum(labeled_array == 0)
    gap_ratio = gap_area / total_area
    
    high_density_regions = density_map > threshold
    overlap_area = np.sum(high_density_regions)
    overlap_ratio = overlap_area / total_area
    
    return gap_ratio, overlap_ratio

def segment_image_based_on_density(image_path, threshold=0.5, sigma=5, binary_threshold=200):
    image = Image.open(image_path)
    gray_image = image.convert('L')
    image_array = np.array(gray_image)

    binary_image = image_array > binary_threshold
    density_map = gaussian_filter(binary_image.astype(float), sigma=sigma)
    
    return density_map

def process_and_save_images_in_folder(parent_folder, csv_filename='segmentation_results.csv'):
    # CSV dosyası oluştur ve başlıkları yaz
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['name', 'number of segmentation', 'gap ratio', 'overlap ratio'])
        
        for folder_name in os.listdir(parent_folder):
            folder_path = os.path.join(parent_folder, folder_name)
            if os.path.isdir(folder_path):
                for image_name in os.listdir(folder_path):
                    image_path = os.path.join(folder_path, image_name)
                    if image_path.endswith('.png'):  # İşlenecek dosya türünü belirt
                        labeled_array, num_segments = segment_image(image_path, binary_threshold=200)
                        density_map = segment_image_based_on_density(image_path, threshold=0.5, sigma=5, binary_threshold=200)

                        gap_ratio, overlap_ratio = calculate_gap_and_overlap_ratios(labeled_array, density_map, threshold=0.5)

                        # Verileri CSV'ye yaz
                        csv_writer.writerow([folder_name, num_segments, f"{gap_ratio:.2f}", f"{overlap_ratio:.2f}"])

                        # Görselleştirme ve kaydetme
                        plt.figure()
                        plt.imshow(labeled_array, cmap='nipy_spectral')
                        plt.title(f'Segmented Image: {image_name}')
                        plt.axis('off')
                        segment_filename = os.path.join(folder_path, f"segmented_{image_name}")
                        plt.savefig(segment_filename)
                        plt.close()

                        plt.figure()
                        plt.imshow(density_map, cmap='hot')
                        plt.title(f'Density Map: {image_name}')
                        plt.axis('off')
                        density_filename = os.path.join(folder_path, f"density_{image_name}")
                        plt.savefig(density_filename)
                        plt.close()

output_folder = r'C:\Users\ranag\Downloads\Görüntüler-20240813T122831Z-001\Görüntüler'  # Çıktıların bulunduğu ana dizin
process_and_save_images_in_folder(output_folder, csv_filename='segmentation_results.csv')
