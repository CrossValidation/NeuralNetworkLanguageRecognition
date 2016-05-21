# coding=utf-8
import os
import csv
from NeuralNetworkLanguageRecognition.wordAndValue import wordAndValue

class Encoder(object):
    '''
    classdocs
    '''
    dict = {"&": "00000",
            "a": "00001",
            "b": "00010",
            "c": "00011",
            "d": "00100",
            "e": "00101",
            "f": "00110",
            "g": "00111",
            "h": "01000",
            "i": "01001",
            "j": "01010",
            "k": "01011",
            "l": "01100",
            "m": "01101",
            "n": "01110",
            "o": "01111",
            "p": "10000",
            "q": "10001",
            "r": "10010",
            "s": "10011",
            "t": "10100",
            "u": "10101",
            "v": "10110",
            "x": "10111",
            "w": "11000",
            "y": "11001",
            "z": "11010",
            "à": "11011",
            "è": "11100",
            "ì": "11101",
            "ò": "11110",
            "ù": "11111"           
                        }
    firstReadTraining = True
    trainingDataset = {}
    firstReadValidation = True
    validationDataset = {}
    valueEncoded = []
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def translateWord(self, word):
        i = 0
        wordOutput = ""
        if len(word) <= 10:
            while i<10:
                #x = dict.get(word[i], "pippo")
                #if  x == 'pippo':
                    #print(word[i])
                if(i < len(word)):
                    try:
                        wordOutput = wordOutput + self.dict[word[i]] #encode word
                    except KeyError:
                        wordOutput = "default"
                else:
                    wordOutput = wordOutput + self.dict['&'] #add padding
                i += 1
        return(wordOutput)
        
    def getWord(self, type, offset, n): #type is either training or validation
        self.valueEncoded[:] = []
        if type== 0:
            if self.firstReadTraining == True: 
                self.firstReadTraining = False
                file_path = os.path.join(os.path.dirname(__file__), "./dataset/training_dataset.csv")            
                with open(file_path, 'r') as csvfile:
                    reader = csv.DictReader(csvfile,delimiter=';')
                    for index,row in enumerate(reader):  
                        self.trainingDataset[index] =  modelWordValue = wordAndValue(row[None][0],row[None][1]) 
                        if index >= offset and index < offset + n:
                            #encoded=self.translateWord(row[None][0])
                            self.valueEncoded.append(wordAndValue(self.translateWord(row[None][0]), row[None][1]))
            else:
                while offset <= offset + n:
                    self.valueEncoded.append(wordAndValue(self.translateWord(self.trainingDataset[offset].getWord()), self.trainingDataset[offset].getValue()))
                    offset = offset + 1
        if type== 1:
            if self.firstReadValidation == True: 
                self.firstReadValidation = False
                file_path = os.path.join(os.path.dirname(__file__), "./dataset/validation_dataset.csv")            
                with open(file_path, 'r') as csvfile:
                    reader = csv.DictReader(csvfile,delimiter=';')
                    for index,row in enumerate(reader):  
                        self.validationDataset[index] =  modelWordValue = wordAndValue(row[None][0],row[None][1]) 
                        if index >= offset and index < offset + n:
                            #encoded=self.translateWord(row[None][0])
                            self.valueEncoded.append(wordAndValue(self.translateWord(row[None][0]), row[None][1]))
            else:
                while offset <= offset + n:
                    self.valueEncoded.append(wordAndValue(self.translateWord(self.validationDataset[offset].getWord()), self.validationDataset[offset].getValue()))
                    offset = offset + 1