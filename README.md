This script creates a FileList.txt that the UnrealPak.exe utility uses to list all the files that you're going to add into the .pak file.

The command below is used to move the defined files in the FileList.txt as the ones to add into the .pak file.
 
cd "C:\Program Files\Epic Games\UE_5.2\Engine\Binaries\Win64" 
UnrealPak.exe "C:\Unpacked\{name-of-the-pak-file.pak}" -Create="C:\Unpacked\FileList.txt" -Sign="C:\Program Files\Epic Games\UE_5.2\Engine\Binaries\Win64\{key-file}"
