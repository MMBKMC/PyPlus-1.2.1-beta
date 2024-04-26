# pyplus_cli.py

import sys

# Define the version number of PyPlus
VERSION = "1.2.1"
BETA = "1.1.1"
def show_version():
    print(f"PyPlus version:{VERSION}")
    print(f"Beta:{BETA}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python pyplus_cli.py --version")
        sys.exit(1)

    option = sys.argv[1]
    if option == "--version":
        show_version()
    else:
        print("Unknown option. Use '--version' to display the PyPlus version.")

if __name__ == "__main__":
    main()
