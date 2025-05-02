import os

working_dir = "C:/Unpacked"
output_file = os.pat.join(working_dir, "FileList.txt")

folders = ["DriveBeyondHorizon", "Engine"]

if os.path.exist(output_file):
    os.remove(output_file)
    

with open(output_file, 'a', encoding = 'utf-8') as f:
    for folder in folders:
        folder_path = os.path.join(working_dir, folder)
        
        if not os.path.exists(folder_path):
            print(f" Folder '{folder}' not found! Skipping...")
            continue
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                abs_path_fixed = abs_path.replace("\\", "/")
                
                relative_path = os.path.relpath(abs_path, start = folder_path).replace("\\","/")
                virtual_path = f"../../../{folder}/{relative_path}" 
                
                f.write(f"{abs_path_fixed} {virtual_path}\n")
                
print("All files written to FileList.txt")
