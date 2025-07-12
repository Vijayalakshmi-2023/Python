def star_square(size):
    print("\nStar Square Pattern:")
    for _ in range(size):
        print("* " * size)

def right_triangle(size):
    print("\nRight Triangle Pattern:")
    for i in range(1, size + 1):
        print("* " * i)

def number_triangle(size):
    print("\nNumber Triangle Pattern:")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    while True:
        print("\n=== Pattern Generator ===")
        print("1. Star Square")
        print("2. Right Triangle")
        print("3. Number Triangle")
        print("4. Exit")

        choice = input("Choose a pattern (1-4): ").strip()

        if choice == "4":
            print("👋 Goodbye!")
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid choice. Try again.")
            continue

        try:
            size = int(input("Enter pattern size (positive integer): "))
            if size <= 0:
                print("❌ Size must be positive.")
                continue
        except ValueError:
            print("❌ Please enter a valid integer.")
            continue

        if choice == "1":
            star_square(size)
        elif choice == "2":
            right_triangle(size)
        elif choice == "3":
            number_triangle(size)

if __name__ == "__main__":
    main()
