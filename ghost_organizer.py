import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".odt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".ogg", ".m4a"],
    "Python": [".py"],
    "Archives": [".zip", ".tar", ".gz", ".7z"],
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_files(folder_path):
    folder_path = os.path.abspath(os.path.expanduser(folder_path))

    if not os.path.isdir(folder_path):
        print("Ghost says: Folder not found!")
        return

    print("\n👻 The Ghost is checking your files...")
    planned_moves = []

    # Only check files directly inside the selected folder.
    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)
        if not os.path.isfile(source):
            continue

        category = get_category(filename)
        target_folder = os.path.join(folder_path, category)
        destination = os.path.join(target_folder, filename)

        if os.path.exists(destination):
            print("Skipped (file already exists):", filename)
            continue

        planned_moves.append((source, destination, category))

    if not planned_moves:
        print("Ghost says: No files need organizing.")
        return

    print("\nFiles that will be moved:")
    for source, destination, category in planned_moves:
        print(f"  {os.path.basename(source)} -> {category}/")

    answer = input("\nMove these files? Type yes to confirm: ").strip().lower()
    if answer != "yes":
        print("👻 Cancelled. No files were moved.")
        return

    moved = 0
    for source, destination, category in planned_moves:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        try:
            shutil.move(source, destination)
            print(f"👻 Moved: {os.path.basename(source)} -> {category}/")
            moved += 1
        except OSError as error:
            print(f"Could not move {os.path.basename(source)}: {error}")

    print(f"\nThe Ghost has finished! Files moved: {moved}")


def main():
    print("=" * 34)
    print("      GHOST FILE ORGANIZER 👻")
    print("=" * 34)
    folder = input("Enter a folder path (example: ~/GhostTest): ").strip()
    organize_files(folder)


if __name__ == "__main__":
    main()
