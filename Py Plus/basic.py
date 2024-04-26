# basic.py

import sys

class PyPlusInterpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, code):
        lines = code.split('\n')
        output = []

        for line in lines:
            tokens = line.split()

            if len(tokens) == 0:
                continue

            command = tokens[0]
            if command == 'print':
                if len(tokens) >= 2:
                    text = " ".join(tokens[1:])
                    output.append(self.colorize(text))
                else:
                    output.append("")

            elif command == 'set':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = var_value
                    output.append(f"Set variable '{var_name}' to '{var_value}'")
                else:
                    output.append("\033[31mError: 'set' command requires a variable name and a value.\033[0m")

            elif command == 'let':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = self.eval_expression(var_value)
                    output.append(f"Let variable '{var_name}' be '{self.variables[var_name]}'")
                else:
                    output.append("\033[31mError: 'let' command requires a variable name and an expression.\033[0m")

            elif command == 'include':
                if len(tokens) >= 2:
                    file_path = tokens[1]
                    try:
                        with open(file_path, 'r') as file:
                            included_code = file.read()
                        included_output = self.eval(included_code)
                        output.append(included_output)
                    except FileNotFoundError:
                        output.append(f"\033[31mError: File '{file_path}' not found.\033[0m")
                else:
                    output.append("\033[31mError: 'include' command requires a file path.\033[0m")

            elif command == 'insert':
                if len(tokens) >= 3:
                    list_name = tokens[1]
                    value = " ".join(tokens[2:])
                    if list_name not in self.variables:
                        self.variables[list_name] = []
                    self.variables[list_name].append(value)
                    output.append(f"Inserted '{value}' into list '{list_name}'")
                else:
                    output.append("\033[31mError: 'insert' command requires a list name and a value.\033[0m")

            elif command == '<import>':
                if len(tokens) >= 2:
                    module_name = tokens[1]
                    try:
                        __import__(module_name)
                        output.append(f"Imported module '{module_name}' successfully.")
                    except ImportError:
                        output.append(f"\033[31mError: Failed to import module '{module_name}'.\033[0m")
                else:
                    output.append("\033[31mError: '<import>' command requires a module name.\033[0m")

            elif command == '<from>':
                if len(tokens) >= 3:
                    module_name = tokens[1]
                    class_name = tokens[2]
                    try:
                        imported_module = __import__(module_name)
                        imported_class = getattr(imported_module, class_name)
                        self.classes[class_name] = imported_class
                        output.append(f"Imported class '{class_name}' from module '{module_name}' successfully.")
                    except ImportError:
                        output.append(f"\033[31mError: Failed to import class '{class_name}' from module '{module_name}'.\033[0m")
                    except AttributeError:
                        output.append(f"\033[31mError: Module '{module_name}' does not contain class '{class_name}'.\033[0m")
                else:
                    output.append("\033[31mError: '<from>' command requires a module name and a class name.\033[0m")

            elif command == 'loop':
                if len(tokens) >= 3:
                    loop_var = tokens[1]
                    loop_range = tokens[2]
                    loop_code = " ".join(tokens[3:])
                    try:
                        loop_range = eval(loop_range)
                        for loop_value in loop_range:
                            self.variables[loop_var] = loop_value
                            loop_result = self.eval(loop_code)
                            output.append(loop_result)
                    except Exception as e:
                        output.append(f"\033[31mError in 'loop' command: {e}\033[0m")
                else:
                    output.append("\033[31mError: 'loop' command requires a loop variable, a loop range, and code to execute.\033[0m")

            elif command == 'dev':
                if len(tokens) >= 2:
                    dev_code = " ".join(tokens[1:])
                    try:
                        dev_result = eval(dev_code)
                        output.append(str(dev_result))
                    except Exception as e:
                        output.append(f"\033[31mError in 'dev' command: {e}\033[0m")
                else:
                    output.append("\033[31mError: 'dev' command requires code to execute.\033[0m")

            elif command == 'variable':
                if len(tokens) >= 2:
                    var_name = tokens[1]
                    if var_name in self.variables:
                        var_value = self.variables[var_name]
                        output.append(f"Variable '{var_name}' is '{var_value}'")
                    else:
                        output.append(f"\033[31mError: Variable '{var_name}' not found.\033[0m")
                else:
                    output.append("\033[31mError: 'variable' command requires a variable name.\033[0m")

            elif command == 'class':
                if len(tokens) >= 2:
                    class_name = tokens[1]
                    class_code = " ".join(tokens[2:])
                    self.classes[class_name] = class_code
                    output.append(f"Defined class '{class_name}'")
                else:
                    output.append("\033[31mError: 'class' command requires a class name and class code.\033[0m")

            elif command == 'int':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = int(tokens[2])
                    self.variables[var_name] = var_value
                    output.append(f"Set variable '{var_name}' to {var_value}")
                else:
                    output.append("\033[31mError: 'int' command requires a variable name and an integer value.\033[0m")

            elif command == 'main':
                # Process 'main' command (if needed)
                output.append("Main function declaration")

            elif command == 'object':
                # Process 'object' command (if needed)
                output.append("Object declaration")

            elif command == 'def':
                # Process 'def' command (if needed)
                output.append("Function definition")

            elif command == 'lix':
                # Process 'lix' command (if needed)
                output.append("Lix command")

            elif command == 'noc':
                # Process 'noc' command (if needed)
                output.append("Noc command")

            elif command == 'cap':
                # Process 'cap' command (if needed)
                output.append("Cap command")

            elif command == 'sys.print':
                if len(tokens) >= 2:
                    text = " ".join(tokens[1:])
                    output.append(self.colorize(text))
                else:
                    output.append("")

            elif command == 'sys.set':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = var_value
                    output.append(f"System set '{var_name}' to '{var_value}'")
                else:
                    output.append("\033[31mError: 'set' command requires a variable name and a value.\033[0m")

            elif command == 'sys.let':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = var_value
                    output.append(f"System let '{var_name}' to '{var_value}'")
                else:
                    output.append("\033[31mError: 'let' command requires a variable name and an expression.\033[0m")

            elif command == 'def':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = var_value
                    output.append(f"{var_name} syntax has created!")
                else:
                    output.append("\033[31mError: def command requires to make a syntax.]")

            elif command == 'End Code;':
                if len(tokens) >= 3:
                    var_name = tokens[1]
                    var_value = " ".join(tokens[2:])
                    self.variables[var_name] = var_value
                    output.append(f"End here....")
                else:
                    output.append("\101[31mError: End command don't allow any variable next to the command.]")

            elif command == 'end':
                break

        return "\n".join(output)

    def eval_expression(self, expression):
        # For now, simply return the expression as is
        return expression

    def colorize(self, text):
        # Replace color formatting markers with ANSI escape codes
        text = text.replace("[green]", "\033[32m")
        text = text.replace("[red]", "\033[31m")
        text = text.replace("[yellow]", "\033[33m")
        text = text.replace("[blue]", "\033[34m")
        text = text.replace("[reset]", "\033[0m")
        return text

def run(filename):
    interpreter = PyPlusInterpreter()

    try:
        # Read the contents of the file
        with open(filename, 'r') as file:
            code = file.read()

        # Evaluate the code using the PyPlus interpreter
        result = interpreter.eval(code)

        # Print the result
        print(result)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: python basic.py run <filename>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "run":
        filename = sys.argv[2]
        run(filename)
    else:
        print("Error: Invalid command. Use 'run' to execute a PyPlus file.")

if __name__ == "__main__":
    main()
