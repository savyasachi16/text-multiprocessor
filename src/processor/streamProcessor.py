import concurrent.futures
import os
import sys
import time


class StreamProcessor:
    def __init__(self, fileName, timeout):
        self.fileName = fileName
        self.timeout = timeout*100
        self.result = []

#Method to check if given string matches required string
    def checkString(self, input):
        if input == "FiCo":
            return True
        return False

#Method to calculate the execution time
    def execTime(self, startTime):
        endTime = time.perf_counter()
        return int((endTime-startTime)*100)

#Main process method that gets called 10 times
    def proc(self, startIndex):
        try:
            idx = startIndex                #Index that goes 10 steps ahead on every iteration
            pid = os.getpid()               #Extract process ID of current process
            bytesRead = 0                   #Number of bytes read
            startTime = time.perf_counter() #Execution start time for the current process
            
            fileObj = open(self.fileName, 'r')
            fileObj.seek(idx)               #Move the file pointer to the start index
            while True:
                temp = fileObj.read(4)      #Extract 4 bytes from the file
                bytesRead += 4
                if temp == '' or len(temp) != 4:    # Assuming input file is limited in size, temp will be empty if end of file is reached
                    fileObj.close()
                    return [pid, self.timeout, bytesRead, "FAILURE"]

                elif self.execTime(startTime) >= self.timeout:      #If execution time exceeds timeout
                    fileObj.close()
                    return [pid, self.timeout, bytesRead, "TIMEOUT"]

                elif self.checkString(temp):                        #If given string is found
                    fileObj.close()
                    return [pid, self.execTime(startTime), bytesRead, "SUCCESS"]
                idx += 10
                fileObj.seek(idx)
        except:
            return [pid, self.execTime(startTime), bytesRead, "FAILURE"]    #If any exeception is hit

    def displayResults(self):
        self.result = sorted(self.result, key=lambda l: l[1], reverse=True) #Sort results according to elapsed time
        totalTime = 0
        totalBytes = 0
        print("PID      Elapsed Time        Byted Read      Status")
        for i in self.result:
            print(f"{i[0]}          {i[1]}          {i[2]}          {i[3]}")
            if i[3] == "SUCCESS":
                totalTime += i[1]
                totalBytes += i[2]
        try:
            print(
                f"Average Bytes Read/Millisecond for Successful Processes = {totalBytes//totalTime} bytes/ms")
        except:
            print(
                f"Average Bytes Read/Millisecond for Successful Processes = 0 bytes/ms")

    def runStreamProcessor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            processes = [executor.submit(self.proc, i) for i in range(10)]      #Spawn 10 processes and set its start index to i
        for f in concurrent.futures.as_completed(processes):                    #Wait for process termination and store result
            self.result.append(f.result())
        self.displayResults()
