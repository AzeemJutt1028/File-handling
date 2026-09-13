
# Function to count lines
def count_lines():
    lines = 0
    with open("Q_01 File.txt", "r") as f:
        while f.readline() != "":
            lines+=1

    return lines


# Function to count words 
def count_words():
    with open("Q_01 File.txt", "r") as f:
        words = 0
        content = f.readlines()     # returns a list of all lines (one index hold one line)

        for line in content:
            line = line.strip().split()         # creates new list of every line removing '\n' from the end of every line
            words += len(line)

    return words

# Function to count characters
def count_chars():
    with open("Q_01 File.txt", "r") as f:
        char = 0
        content = f.readline().strip()
        while content != "":
            # content = content.strip()
            char += len(content)
            content = f.readline().strip()

    return char

# Function to print menu
def menu():
    print("\t\t\t=== Count Words_Characters_Lines ===")
    print("1. Lines")
    print("2. Words")
    print("3. Characters")
    print("4. Exit")

    ch = int(input("Enter Your Choice : "))

    # Validates input
    while ch not in [1,2,3,4]:
        print("\tInvalid Choice")
        ch = int(input("Enter again : "))

    return ch

# Main engine
while True:
    choice = menu()

    if choice == 1:
        print("Lines : ", count_lines())
    elif choice == 2:
        print("Words : ", count_words())
    elif choice == 3:
        print("Characters : ", count_chars())
    else:
        print("\n\t\t\t=== Thank You! For Using Our Service ===")
        break

    print()     # For a line space