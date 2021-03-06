import argparse
import time

from streamProcessor import StreamProcessor

#Main function that calls the generator processor class
def main(fileName, timeout):
    print("Initiated data stream processor. Please wait...")

    exe = StreamProcessor(fileName, timeout)
    exe.runStreamProcessor()

#Parsing specified, in case python script is called directly instead of through the shell script.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script is used to spawn 10 processes that is used to find the word \"FiCo\" in a given input file.")
    parser.add_argument(
        "filename", help="Specifies the name of the file.", type=str)
    parser.add_argument(
        "-t", "--timeout", default=60, help="Specifies timeout in seconds for each process. If left blank it defaults to 60 seconds", type=int)
    args = parser.parse_args()
    fileName = args.filename
    timeout = args.timeout
    main(fileName, timeout)
