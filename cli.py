

import sys
from backend import Placeholder

def main():
    p = Placeholder()
    
    print("Welcome!")
    print("Type 'exit' or 'quit' to end the program.")
    
    while True:
        q = input("\nQ: ")
        
        if q.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        try:
            to_output = p.output(q)
            print(to_output)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()