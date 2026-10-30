"""
Ghost File Organizer with local Ollama AI.

Requirements:
1. Install Ollama: https://docs.ollama.com/linux
2. Download a model, for example: ollama run llama3.2:1b
3. Run: python3 ghost_ai_organizer.py

The AI receives only each filename, not the file contents.
Files are not moved until you type YES.
"""

import json
import os
import shutil
import urllib.error
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"
CATEGORIES = ["Images", "Documents", "Videos", "Audio", "Python", "Archives", "Others"]


def ask_local_ai(filename):
    prompt = (
        "You are a file organizer. Choose exactly one category from this list: "
        + ", ".join(CATEGORIES)
        + ". Decide using only the filename and its extension. "
        "Reply with only the category name. Filename: "
        + filename
    )

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
        category = result.get("response", "").strip()
        for valid_category in CATEGORIES:
            if category.lower() == valid_category.lower():
                return valid_category
        return "Others"
    except urllib.error.URLError:
        print("Could not connect to Ollama. Is Ollama installed and running?")
        raise


def organize_files(folder_path):
    folder_path = os.path.abspath(os.path.expanduser(folder_path))
    if not os.path.isdir(folder_path):
        print("Ghost says: Folder not found!")
        return

    plan = []
    print("\n👻 Local AI is examining filenames. Please wait...\n")

    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)
        if not os.path.isfile(source):
            continue
        try:
            category = ask_local_ai(filename)
        except Exception as error:
            print("AI error:", error)
            print("Stopping without moving files.")
            return

        destination_folder = os.path.join(folder_path, category)
        destination = os.path.join(destination_folder, filename)
        if os.path.exists(destination):
            print("Skipped (file already exists):", filename)
            continue
        plan.append((source, destination, category))
        print(f"  {filename} -> {category}/")

    if not plan:
        print("Ghost says: No files need organizing.")
        return

    answer = input("\nMove these files? Type YES to confirm: ").strip()
    if answer != "YES":
        print("👻 Cancelled. No files were moved.")
        return

    moved = 0
    for source, destination, category in plan:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        try:
            shutil.move(source, destination)
            moved += 1
            print(f"👻 Moved: {os.path.basename(source)} -> {category}/")
        except OSError as error:
            print(f"Could not move {os.path.basename(source)}: {error}")

    print(f"\nThe Ghost has finished! Files moved: {moved}")


def main():
    print("=" * 38)
    print("   GHOST FILE ORGANIZER — LOCAL AI 👻")
    print("=" * 38)
    print(f"Model: {MODEL}")
    folder = input("Enter a folder path (example: ~/GhostTest): ").strip()
    organize_files(folder)


if __name__ == "__main__":
    main()
