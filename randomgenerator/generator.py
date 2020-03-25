import random

class RandomGenerator:

    def writetoFile(self, fileName, string):
        fileObj = open(fileName, 'a')
        fileObj.write(string)
        fileObj.close()

    def generateString(self):
        result = []
        for _ in range(1000000):
            randASCII = random.randrange(65, 123)
            while(randASCII in range(91, 97)):
                randASCII = random.randrange(65, 123)
            result.append(chr(randASCII))
        return ''.join(result)

    def runGenerator(self, fileName, sizeInMB):
        for i in range(sizeInMB):
            string = self.generateString()
            self.writetoFile(fileName, string)