import os

file_path = r'C:\Users\Godhane computer\Documents\data_visualization_project\jsondata.json'

if os.path.isfile(file_path):
    print(f'File found: {file_path}')
else:
    print(f'File not found: {file_path}')
