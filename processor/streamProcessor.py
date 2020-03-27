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
        fileObj = open(self.fileName, 'r')

        idx = startIndex
        fileObj.seek(idx)
        pid = os.getpid()
        bytesRead = 0
        startTime = time.perf_counter()

        try:
            while True:
                temp = fileObj.read(4)
                bytesRead += 4
                if self.execTime(startTime) >= self.timeout:
                    fileObj.close()
                    return [pid, self.timeout, bytesRead, "TIMEOUT"]

                elif self.checkString(temp):
                    fileObj.close()
                    return [pid, self.execTime(startTime), bytesRead, "SUCCESS"]
                idx += 10
                fileObj.seek(idx)
        except:
            fileObj.close()
            return [pid, self.execTime(startTime), bytesRead, "FAILURE"]
            return

    def displayResults(self):
        self.result = sorted(self.result, key=lambda l: l[1])
        totalTime = 0
        totalBytes = 0
        print("PID      Elapsed Time        Byted Read      Status")
        for i in self.result:
            print(f"{i[0]}          {i[1]}          {i[2]}          {i[3]}")
            if i[3] == "SUCCESS":
                totalTime += i[1]
                totalBytes += i[2]
        print(
            f"Average Bytes Read/Millisecond for Successful Processes = {totalBytes//totalTime} Bytes/ms")

    """
    The parent collects the results of each worker and writes a report to stdout for each worker sorted 
    in descending order by [elapsed]: [elapsed] [byte_cnt] [status]
    A final line of output will show the average bytes read per time unit in a time unit of your choice 
    where failed/timeout workers will not report stats. 11 lines of output total to stdout.
    """

    def runStreamProcessor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            processes = [executor.submit(self.proc, i) for i in range(10)]

        for f in concurrent.futures.as_completed(processes):
            self.result.append(f.result())
        self.displayResults()
