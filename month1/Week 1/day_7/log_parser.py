from pathlib import Path

def count_contents(target_directory):
    path = Path(target_directory)
    if not path.is_dir():
        print(f"Error: The path '{target_directory}' is not a valid directory.")
        return
    file_count = 0
    dir_count = 0

    for item in path.iterdir():
        if item.is_file():
            file_count += 1
        elif item.is_dir():
            dir_count += 1

    print(f"Analysis of: {path.absolute()}")
    print(f"Files: {file_count}")
    print(f"Folders: {dir_count}")
    print(f"Total items: {file_count + dir_count}")

count_contents('.')