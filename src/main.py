from src.kmp_algorithm import print_kmp_result

def main():
    print("KMP Algorithm")
    print("Assignment 2 - Lexical Analysis")
    print("-" * 35)

    text = input("Enter the text: ").strip()
    pattern = input("Enter the pattern: ").strip()

    if text == "" or pattern == "":
        print("Error: text and pattern cannot be empty.")
        return

    print_kmp_result(text, pattern)


if __name__ == "__main__":
    main()