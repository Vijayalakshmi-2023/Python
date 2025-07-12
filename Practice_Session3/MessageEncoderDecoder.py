def encode_message(message):
    ascii_codes = []
    for char in message:
        ascii_codes.append(str(ord(char)))  # Convert char to ASCII code string
    return " ".join(ascii_codes)

def decode_message(ascii_string):
    chars = []
    for code in ascii_string.split():
        try:
            chars.append(chr(int(code)))  # Convert ASCII code back to char
        except ValueError:
            return "❌ Invalid ASCII codes detected."
    return "".join(chars)

def main():
    while True:
        print("\n=== Message Encoder/Decoder ===")
        print("1. Encode message to ASCII")
        print("2. Decode ASCII to message")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            msg = input("Enter message to encode: ")
            encoded = encode_message(msg)
            print(f"Encoded ASCII:\n{encoded}")

        elif choice == "2":
            ascii_input = input("Enter ASCII codes separated by spaces: ")
            decoded = decode_message(ascii_input)
            print(f"Decoded message:\n{decoded}")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
