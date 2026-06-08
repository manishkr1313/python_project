import os
import shutil

#folder path you want to organize
folder_path = input("Enter the folder path you want to organize: ")
# os.getcwd() # current working directory

#file type mappimg
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': [ '.js', '.html', '.css'],
    'Others': [],
    'excel': ['.xlsx', '.xls'],
    'powerpoint': ['.pptx', '.ppt']  
}

#create folders if they don't exist
for folder in file_types.keys(): # create folders for each file type
    folder_dir = os.path.join(folder_path, folder) # create folder path
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)# create folder if it doesn't exist

#organize files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename) # create file path
    
#skip folders
    if os.path.isdir(file_path):
        continue
    
    #get file extension
    # print(os.path.splitext(filename))
    file_ext = os.path.splitext(filename)[1].lower() # get file extension and convert to lowercase
    
    for folder, extensions in file_types.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(folder_path, folder, filename)) # move file to corresponding folder
            break
     
print("Files organized successfully! ✅") 