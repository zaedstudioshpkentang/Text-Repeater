def repeat_text(text, count, mode):
    if mode == "List":
        repeated_text = '\n'.join([text for _ in range(count)])
    elif mode == "Inline":
        repeated_text = text * count
    else:
        repeated_text = "Invalid mode"
    return repeated_text

def main():
    
    text = input("Enter the text to be repeated: ")
    count = int(input("Enter how many times to repeat: "))
    print("Choose display mode:")
    print("1. List")
    print("2. Inline")
    mode_choice = input("Enter choice (1 or 2): ")

    if mode_choice == "1":
        mode = "List"
    elif mode_choice == "2":
        mode = "Inline"
    else:
        mode = "Invalid"
        
    result = repeat_text(text, count, mode)
    
    print("Result:")
    print(result)

if __name__ == "__main__":
    main()