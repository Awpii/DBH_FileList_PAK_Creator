import os

#working dir shit
working_dir = "C:/Unpacked"
output_file = "C:/Unpacked/FileList.txt"

#scan folder
folders = ["DriveBeyondHorizon", "Engine"]

#clear output file
if os.path.exists(output_file):
    os.remove(output_file)
    
#Open file in append
with open(output_file, 'a') as f:
    for folder in folders:
        folder_path = os.path.join(working_dir, folder)
        
        if not os.path.exists(folder_path):
            print(f"Warning: Folder '{folder}' not found. Skipping...")
            continue
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                absolute_path = os.path.join(root, file).replace("\\", "/")
                relative_path = os.path.relpath(root, folder_path).replace("\\", "/")
                virtual_path = f"../../{folder}/{relative_path}/{file}"
                
                f.write(f"{absolute_path} {virtual_path}\n")
    
print("FileList.txt created with all files from the defined folders")
