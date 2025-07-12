def categorize_files(files):
    categories = {}
    for file in files:
        # Extract extension after last dot, lowercase for uniformity
        if "." in file:
            ext = file[file.rfind("."):].lower()
        else:
            ext = "No Extension"
        categories[ext] = categories.get(ext, []) + [file]
    return categories

def show_summary(categories):
    print("\n=== File Categories Summary ===")
    for ext, flist in categories.items():
        print(f"{ext} : {len(flist)} file(s)")
        for f in flist:
            print(f"  - {f}")
    print()

def main():
    files = []
    print("=== Mini File Organizer ===")
    print("Enter file names (type 'done' to finish):")
    while True:
        filename = input("File name: ").strip()
        if filename.lower() == "done":
            break
        if filename:
            files.append(filename)
        else:
            print("❌ Filename cannot be empty.")

    if not files:
        print("No files entered.")
        return

    categories = categorize_files(files)
    show_summary(categories)

if __name__ == "__main__":
    main()
