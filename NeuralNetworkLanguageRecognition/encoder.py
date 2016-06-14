# coding=utf-8
import os
import csv
from NeuralNetworkLanguageRecognition.wordAndValue import wordAndValue
from string import lower

class Encoder(object):
    '''
    classdocs
    '''
    dict = {"&".decode('utf-8'): "00000",
            "a".decode('utf-8'): "00001",
            "b".decode('utf-8'): "00010",
            "c".decode('utf-8'): "00011",
            "d".decode('utf-8'): "00100",
            "e".decode('utf-8'): "00101",
            "f".decode('utf-8'): "00110",
            "g".decode('utf-8'): "00111",
            "h".decode('utf-8'): "01000",
            "i".decode('utf-8'): "01001",
            "j".decode('utf-8'): "01010",
            "k".decode('utf-8'): "01011",
            "l".decode('utf-8'): "01100",
            "m".decode('utf-8'): "01101",
            "n".decode('utf-8'): "01110",
            "o".decode('utf-8'): "01111",
            "p".decode('utf-8'): "10000",
            "q".decode('utf-8'): "10001",
            "r".decode('utf-8'): "10010",
            "s".decode('utf-8'): "10011",
            "t".decode('utf-8'): "10100",
            "u".decode('utf-8'): "10101",
            "v".decode('utf-8'): "10110",
            "x".decode('utf-8'): "10111",
            "w".decode('utf-8'): "11000",
            "y".decode('utf-8'): "11001",
            "z".decode('utf-8'): "11010",
            "à".decode('utf-8'): "11011",
            "è".decode('utf-8'): "11100",
            "ì".decode('utf-8'): "11101",
            "ò".decode('utf-8'): "11110",
            "ù".decode('utf-8'): "11111"           
                        }
    firstReadTraining = True
    trainingDataset = {}
    firstReadValidation = True
    validationDataset = {}
    valueEncoded = []
    

    def __init__(self, k):
        self.k = k
        self.max = 9592
        file_path = os.path.join(os.path.dirname(__file__), "dataset/final_dataset.csv")            
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            for index,row in enumerate(reader):
                self.valueEncoded.append(wordAndValue(self.translateWord(row[None][0]), row[None][1], row[None][0]))

        
    def translateWord(self, word):
        i = 0
        wordOutput = ""
        word = word.decode('utf-8')
        word = word.lower()
        if len(word) <= 10:
            while i<10:
                if(i < len(word)):
                    try:
                        wordStr = word[i]
                        wordOutput = wordOutput + self.dict[wordStr.lower()] #encode word
                    except Exception as e:
                        print(e)
                        
                        print (word)
                        wordOutput = "default"
                        print (word[i])
                else:
                    wordOutput = wordOutput + self.dict['&'] #add padding
                i += 1
        return(wordOutput)
        
    def getTesting(self, numIter):
        testingSet = []
        for testingElement in range((numIter-1)*int(self.max/self.k), numIter*int(self.max/self.k)+1):
            testingSet.append(self.valueEncoded[testingElement])
        return testingSet
    
    def getTraining(self, numIter):
        trainingSet = []
        if numIter > 1:
            for trainingElement in range(0, (numIter-1)*int(self.max/self.k)):
                trainingSet.append(self.valueEncoded[trainingElement])
        if numIter < self.k:
            for trainingElement in range((numIter)*int(self.max/self.k), self.max):
                trainingSet.append(self.valueEncoded[trainingElement])    
        return trainingSet
            
            