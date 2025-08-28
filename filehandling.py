<<<<<<< HEAD
# file_handling_assignment.py

def file_read_write():
    """Reads input.txt, modifies it, and writes to output.txt"""
    try:
        with open("input.txt", "r") as f:
            content = f.read()

        # Modify content (convert to uppercase)
        modified_content = content.upper()

        with open("output.txt", "w") as f:
            f.write(modified_content)

        print("✅ File has been read and modified content written to output.txt")

    except FileNotFoundError:
        print("❌ input.txt was not found. Please create it first.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def error_handling_lab():
    """Asks user for a filename and handles errors"""
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n📂 File Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"❌ The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def main():
    while True:
        print("\n===== File Handling & Exception Handling Assignment =====")
        print("1. File Read & Write Challenge 🖋️")
        print("2. Error Handling Lab 🧪")
        print("3. Exit ❌")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            file_read_write()
        elif choice == "2":
            error_handling_lab()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
=======
# file_handling_assignment.py

def file_read_write():
    """Reads input.txt, modifies it, and writes to output.txt"""
    try:
        with open("input.txt", "r") as f:
            content = f.read()

        # Modify content (convert to uppercase)
        modified_content = content.upper()

        with open("output.txt", "w") as f:
            f.write(modified_content)

        print("✅ File has been read and modified content written to output.txt")

    except FileNotFoundError:
        print("❌ input.txt was not found. Please create it first.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def error_handling_lab():
    """Asks user for a filename and handles errors"""
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n📂 File Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"❌ The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def main():
    while True:
        print("\n===== File Handling & Exception Handling Assignment =====")
        print("1. File Read & Write Challenge 🖋️")
        print("2. Error Handling Lab 🧪")
        print("3. Exit ❌")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            file_read_write()
        elif choice == "2":
            error_handling_lab()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
>>>>>>> b7bf494611744c21b6072f9e00e96b27ada8c8ff
