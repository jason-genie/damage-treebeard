import shutil, os
# files = ['file1.txt', 'file2.txt', 'file3.txt']
# os.mkdir('bitbucket_output') # creates new folder
current_dir = os.getcwd() # gets directory
files = os.listdir(current_dir)
print(current_dir)
print(files)

for f in files:
    if (f == "client") or (os.path.isdir(current_dir)): continue # skips all files that are not folders
    source_dir = fr"{current_dir}\{f}"
    destination_dir = fr"{current_dir}\bitbucket_output\{f}"
    shutil.copytree(source_dir, destination_dir)

for f in files:
    if os.path.isfile(current_dir) == False: continue # skips all files that are folders
    shutil.copy(f, 'bitbucket_output')

# specifically for 'client' folder
client_dir = f'{current_dir}\client\django_tasks_client'
files = os.listdir(client_dir)

for f in files:
    if f == "node_modules": continue
    if os.path.isdir(client_dir): # if 'f' is a folder
        source_dir = fr"{client_dir}\{f}"
        destination_dir = fr"{current_dir}\bitbucket_output\client\{f}"

        shutil.copytree(source_dir, destination_dir)
    else:
        shutil.copy(f, 'bitbucket_output\client')
