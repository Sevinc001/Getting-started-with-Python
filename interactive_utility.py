"""
Interactive Data Processor Utility.
Demonstrates: Loop protocols, Exception Handling, and Tracking Extremums.
Author: Sevinc Zaur Qasimova
"""

def run_data_processor():
    """Prompts user for numbers until 'done' is typed, then analyzes inputs."""
    largest = None
    smallest = None

    print("--- Interactive Statistics Processor Started ---")
    print("Enter numbers to analyze, or type 'done' to finish.\n")

    while True:
        user_input = input("Enter a number: ").strip()
        
        if user_input.lower() == "done":
            break
            
        # Ignore custom comment strings in the input stream
        if user_input.startswith("#"):
            continue

        try:
            current_num = int(user_input)
        except ValueError:
            print("[Error] Invalid input. Please enter a valid integer.")
            continue

        # Algorithmic tracking of maximum and minimum values
        if largest is None or current_num > largest:
            largest = current_num
            
        if smallest is None or current_num < smallest:
            smallest = current_num

    print("\n--- Execution Finished ---")
    print(f"Maximum Value Registered: {largest}")
    print(f"Minimum Value Registered: {smallest}")


if __name__ == "__main__":
    run_data_processor()
