# Stream Processor

Stream Processor is a Python Project that when run, can spawn 10 child processes that searches a random input data stream for the word \"FiCo".

On the first iteration of each of the process:

The first process checks 4 bytes of data starting from index = 0 of the file.

The next process checks 4 bytes of data starting from index = 1 of the file.

The third process checks 4 bytes of data starting from index = 3 of the file.

...

The final process checks 4 bytes of data starting from index = 9 of the file.

On the next iteration, each of process' moves to index+10, as the strings starting from the first 10 indexes need not be checked again. So on the second iteration:

The first process checks 4 bytes of data starting from index = 10 of the file.

The first process checks 4 bytes of data starting from index = 11 of the file.

...

The final process checks 4 bytes of data starting from index = 19 of the file.

This way, each of the 10 child processes check for the required string without checking substrings that are already processed, but ensuring that all substrings are parallely checked for efficient execution.


## Preequisites and Installation

You need to ensure that Python 3 is installed on your system.

## Usage

### Running the Stream Processor
Navigate to the bin folder:
```bash
cd bin
```
Run the start.sh script to begin exection of the stream processor:
```bash
./start.sh <yourfilehere> -t 100
```
OR
```bash
./start.sh <yourfilehere> --timeout 100
```
where 'youfilehere' is the file path, or file name if it is present in the same directlory. '100' is the time out of each process in seconds.

Additionally, you can also run the script without providing the process timeout:
```bash
./start.sh <yourfilehere>
```
This would set the default timeout value of 60 seconds.


### Running the Data Generator
Navigate to the bin folder:
```bash
cd bin
```
Run the generateData.sh script to begin execution of the data generator:
```bash
./generateData.sh <yourfilehere> <filesizeMB>
```
where 'youfilehere' is the file path, or file name if it is to be placed in the same directory. 'filesizeMB' is the size of the file in MB.


## Sample Output for Stream Processing
PID      Elapsed Time        Byted Read      Status
29492          6000          13877856        TIMEOUT
29495          6000          12936620        TIMEOUT
29496          6000          13844380        TIMEOUT
29493          6000          14558312        TIMEOUT
29498          6000          12976528        TIMEOUT
29494          6000          12800816        TIMEOUT
29497          4039          8162900         SUCCESS
29491          1569          3007928         SUCCESS
29493          682           1238452         SUCCESS
29492          372           643320          SUCCESS
Average Bytes Read/Millisecond for Successful Processes = 1959 bytes/ms


## License

[MIT](https://choosealicense.com/licenses/mit/)
