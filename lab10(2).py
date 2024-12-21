import os

current_directory = os.listdir('.')
print("Вміст поточного каталогу:")
for item in current_directory:
    print(item)

f_files = [item for item in current_directory if item.startswith('f')]
print("\nФайли, що починаються з літери 'f':")
print(f_files)
