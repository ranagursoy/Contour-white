# Image and Video Processing Tools
This repository contains Python scripts for processing images and videos. The main functionalities include extracting frames from videos, segmenting images based on connected components and density, and compiling results into a CSV file with additional data from text files. The project was developed to collect and analyze real data from a newly produced machine, where image processing methods are used to determine key machine parameters. By experimenting with different parameter combinations, a large amount of data is gathered, which is then evaluated and made meaningful through these scripts.

## Overview

The repository includes the following scripts:

1. **video_to_frames.py**: Extracts frames from video files at specified intervals and saves them as images.
2. **image_segmentation_analysis.py**: Analyzes images by segmenting them based on connected components and density, and calculates gap and overlap ratios.
3. **csv_edited.py**: Reads additional data from text files and updates a CSV file with image segmentation results.

**segmented-yonga.py**: Provides visualization for segmented images and density-based segmentation.

1. Extract Frames from Videos: Use video_to_frames.py to extract frames from all .avi videos in a specified folder.
2. Image Segmentation and Analysis: Run image_segmentation_analysis.py to segment images, calculate ratios, and save results to a CSV file.
3.  Update CSV with Additional Information: Use csv_edited.py to add additional data from .txt files to the existing CSV file.

### Example Images
#### Original Image
<img src="https://github.com/user-attachments/assets/17495eb7-54b8-4bef-beb8-f516b582a02d" alt="Original Image" width="400"/>

#### Segmented Image
<img src="https://github.com/user-attachments/assets/34d2c135-e453-4833-aa70-73e9e6063da5" alt="Segmented Image" width="400"/>

#### Density-Based Segmentation
<img src="https://github.com/user-attachments/assets/e0ee375b-4f14-469c-b27b-327b2a15a76f" alt="Density-Based Segmentation" width="400"/>




