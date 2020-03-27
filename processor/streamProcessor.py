import multiprocessing
import os
import sys


class StreamProcessor:
    def __init__(self, fileName, timeout):
        self.fileName = fileName
        self.timeout = timeout
        self.result = []

    def checkString(self, input):
        if input == "FiCo":
            return True
        return False

    def proc(self, startIndex):
        fileObj = open(self.fileName, 'r')
        idx = startIndex
        fileObj.seek(idx)
        try:
            while True:
                temp = fileObj.read(4)
                if self.checkString(temp):
                    fileObj.close()
                    print("SUCCESS")
                    return
                idx += 10
                fileObj.seek(idx)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            fileObj.close()
            print("FAILURE")
            return

    def displayResults(self):
        pass
    """
    The parent collects the results of each worker and writes a report to stdout for each worker sorted 
    in descending order by [elapsed]: [elapsed] [byte_cnt] [status]
    A final line of output will show the average bytes read per time unit in a time unit of your choice 
    where failed/timeout workers will not report stats. 11 lines of output total to stdout.
    """

    def runStreamProcessor(self):
        processes = []
        for i in range(5):
            p = multiprocessing.Process(target=self.proc, args=(i,))
            p.start()
            processes.append(p)
        for process in processes:
            process.join(60)
            print("Killed Process")
