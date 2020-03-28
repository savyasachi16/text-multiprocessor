import concurrent.futures
import os
import sys
import time


class StreamProcessor:
    def __init__(self, fileName, timeout):
        self.fileName = fileName
        self.timeout = timeout*100
        self.result = []

    def checkString(self, input):
        if input == "FiCo":
            return True
        return False

    def execTime(self, startTime):
        endTime = time.perf_counter()
        return int((endTime-startTime)*100)

    def proc(self, startIndex):
        try:

            idx = startIndex
            pid = os.getpid()
            bytesRead = 0
            startTime = time.perf_counter()

            fileObj = open(self.fileName, 'r')
            fileObj.seek(idx)
            
            fileObj = open(self.fileName, 'r')
            fileObj.seek(idx)
            while True:
                temp = fileObj.read(4)
                bytesRead += 4
                if temp == '' or len(temp) != 4:    # Assuming input is limited
                    fileObj.close()
                    return [pid, self.timeout, bytesRead, "FAILURE"]

                elif self.execTime(startTime) >= self.timeout:
                    fileObj.close()
                    return [pid, self.timeout, bytesRead, "TIMEOUT"]

                elif self.checkString(temp):
                    fileObj.close()
                    return [pid, self.execTime(startTime), bytesRead, "SUCCESS"]
                idx += 10
                fileObj.seek(idx)
        except:
            return [pid, self.execTime(startTime), bytesRead, "FAILURE"]

    def displayResults(self):
        self.result = sorted(self.result, key=lambda l: l[1], reverse=True)
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
            processes = [executor.submit(self.proc, i) for i in range(10)]
        for f in concurrent.futures.as_completed(processes):
            self.result.append(f.result())
        self.displayResults()
