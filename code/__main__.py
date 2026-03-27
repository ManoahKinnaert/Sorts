"""
Main file, this program allows you 
to select the desired experiment that you'd like to run.
"""
import experiments.sort1 as es1
import experiments.sort4 as es4

TESTS = [es1, None, None, es4]

def main():
    while True:
        try:
            test_number = int(input("Please select the testnumber you'd like to run (1 or 4):\n"))
            TESTS[test_number - 1].test_main()
        except Exception as e:
            print(f"ERROR: {e}")

        cmd = input("Would you like to quit (y/n):\n")
        if cmd.lower() == "y": break

# main entry point       
if __name__ == "__main__":
    main()