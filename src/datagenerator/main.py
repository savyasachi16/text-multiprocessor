import time
import argparse
from generator import RandomGenerator


def main(fileName, fileSize):
    startTime = time.perf_counter()

    print("Initiated random stream generator...")
    exe = RandomGenerator()
    exe.runGenerator(fileName, fileSize)

    endTime = time.perf_counter()
    print(f'Execution comepleted in {round(endTime-startTime,2)} second(s)')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script is used to generate random stream of alphabets in a text file.")
    parser.add_argument(
        "filename", help="Specifies the name of the file.", type=str)
    parser.add_argument(
        "filesize", help="Specifies the size of the file in MB", type=int)
    args = parser.parse_args()
    fileName = args.filename
    fileSize = args.filesize
    main(fileName, fileSize)
