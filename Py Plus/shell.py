import sys
from basic import PyPlusInterpreter

def main():
    interpreter = PyPlusInterpreter()

    print("Beta 1. 2. 1, V 1. 1. 1")

    while True:
        try:
            # Read input from the user
            input_text = input("Py Plus+ >> ")

            # Evaluate the input using the PyPlus interpreter
            result = interpreter.eval(input_text)

            # Print the result
            print(result)

        except EOFError:
            # Exit gracefully on Ctrl+D (EOF)
            print("\nExiting PyPlus shell.")
            break
        except Exception as e:
            # Print any exceptions that occur during evaluation
            print("Error:", e)

if __name__ == "__main__":
    main()

import sys
from basic import PyPlusInterpreter

def execute_file(file_path):
    interpreter = PyPlusInterpreter()

    try:
        # Read the contents of the file
        with open('test.pyplus', 'r') as file:
            code = file.read()

        # Evaluate the code using the PyPlus interpreter
        result = interpreter.eval(code)

        # Print the result
        print(result)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 2:
        print("Usage: python shell.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if file_path.endswith(".pyplus"):
        execute_file(file_path)
    else:
        print("Error: PyPlus files must have a '.pyplus' extension.")

if __name__ == "__main__":
    main()