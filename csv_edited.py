import os
import pandas as pd

def read_txt_file(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)  
                data[key.strip()] = value.strip()
            else:
                print(f"Warning: Skipping line in {file_path} - '{line.strip()}'")
    return data

def update_csv_with_txt_info(csv_path, parent_folder):
    df = pd.read_csv(csv_path, encoding='latin1')

    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            for txt_file_name in os.listdir(folder_path):
                if txt_file_name.endswith('.txt'):
                    txt_file_path = os.path.join(folder_path, txt_file_name)
                    txt_data = read_txt_file(txt_file_path)

                    for i, row in df.iterrows():
                        if row['name'] == folder_name:
                            df.at[i, 'Titreşim'] = txt_data.get('Titreşim', None)
                            df.at[i, 'Bant hızı (m/dk)'] = txt_data.get('Bant hızı (m/dk)', None)
                            df.at[i, 'Yonga boyutu (mm)'] = txt_data.get('Yonga boyutu (mm)', None)
                            df.at[i, 'Yükseklik(cm)'] = txt_data.get('Yükseklik(cm)', None)

    df.to_csv(csv_path, index=False, encoding='utf-8')

if __name__ == "__main__":
    csv_path = 'segmentation_results.csv'
    parent_folder = r'C:\Users\ranag\Downloads\Görüntüler-20240813T122831Z-001\Görüntüler'
    update_csv_with_txt_info(csv_path, parent_folder)
