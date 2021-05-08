import os
os.chdir('./MyData')
file_names = os.listdir()
total_files = (len(file_names))
new_name = 201
files = 0

print(os.listdir())
print('total', total_files)

print(file_names)
while total_files != files:
    print(os.listdir())
    os.renames(file_names[files], str(new_name)+'.jpg')
    new_name += 1
    files += 1
    print(new_name)
    print(files)
