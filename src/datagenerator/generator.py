##This class is used to generate the random stream of data and store it into a text file.

import random


class RandomGenerator:
    #Method that writes a string to the file and closes it.
    def writetoFile(self, fileName, string):
        fileObj = open(fileName, 'a')
        fileObj.write(string)
        fileObj.close()

    #Method that generates a pseudorandom string of size 1MB.
    def generateString(self):
        result = []
        for _ in range(1000000):
            randASCII = random.randrange(65, 123)

            #Keep generating randASCII values until it is only an alphabet and not a special character.
            while(randASCII in range(91, 97)):
                randASCII = random.randrange(65, 123)
            result.append(chr(randASCII))
        return ''.join(result)

    #Wrapper method
    def runGenerator(self, fileName, sizeInMB):
        for i in range(sizeInMB):
            string = self.generateString()
            self.writetoFile(fileName, string)
