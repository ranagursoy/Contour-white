import cv2
import os
from PIL import Image

def extract_frames_from_video(video_path, output_folder, frame_interval=30):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = frame_interval  
    success, image = cap.read()
    
    while success:
        if frame_count % frame_interval == 0:

            pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            frame_filename = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_path))[0]}_frame_{frame_count}.png")
            
            try:
                pil_image.save(frame_filename)
                print(f"Saved {frame_filename}")
            except Exception as e:
                print(f"Failed to save {frame_filename}. Error: {e}")
        
        success, image = cap.read()
        frame_count += 1
    
    cap.release()

def process_all_videos_in_folder(parent_folder, frame_interval=60):
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            for video_name in os.listdir(folder_path):
                video_path = os.path.join(folder_path, video_name)
                if video_path.endswith('.avi'): 
                    extract_frames_from_video(video_path, folder_path, frame_interval)

if __name__ == "__main__":

    parent_folder = r'C:\Users\ranag\Downloads\Görüntüler-20240813T122831Z-001\Görüntüler'  
    process_all_videos_in_folder(parent_folder, frame_interval=60)
