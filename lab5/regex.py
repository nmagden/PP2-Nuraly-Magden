#ex1
import re

def match_pattern(input_string):
    pattern = re.compile(r'a*b*')
    match = pattern.fullmatch(input_string)
    return bool(match)

def main():
    try:
        input_string = input("Enter a string: ")
        result = match_pattern(input_string)

        if result:
            print("The string matches the pattern.")
        else:
            print("The string does not match the pattern.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
#ex2
import re

def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)
    return bool(match)

def main():
    try:
        input_string = input("Enter a string: ")

        result = match_pattern(input_string)
        
        if result:
            print("The input string matches the pattern.")
        else:
            print("The input string does not match the pattern.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#ex3
import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    return matches

def main():
    try:
        input_string = input("Enter a string: ")

        sequences = find_sequences(input_string)

        if sequences:
            print("Sequences found:")
            for seq in sequences:
                print(seq)
        else:
            print("No sequences found in the input string.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#ex4
import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    return matches

def main():
    try:
        input_string = input("Enter a string: ")

        sequences = find_sequences(input_string)

        if sequences:
            print("Sequences found:")
            for seq in sequences:
                print(seq)
        else:
            print("No sequences found in the input string.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
