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
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def translateWord(self, word):
        i = 0
        wordOutput = ""
        word = word.decode('utf-8')
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
        
    def getWord(self, type, offset, n): #type is either training or validation
        self.valueEncoded[:] = []
        if type== 0:
            if self.firstReadTraining == True: 
                self.firstReadTraining = False
                file_path = os.path.join(os.path.dirname(__file__), "dataset/training_dataset.csv")            
                with open(file_path, 'r') as csvfile:
                    reader = csv.DictReader(csvfile,delimiter=';')
                    for index,row in enumerate(reader):  
                        rowprova = row[None][0].decode('utf-8')
                        self.trainingDataset[index] =  modelWordValue = wordAndValue(row[None][0],row[None][1]) 
                        if index >= offset and index < offset + n:
                            #encoded=self.translateWord(row[None][0])
                            self.valueEncoded.append(wordAndValue(self.translateWord(row[None][0]), row[None][1]))
            else:
                index_training = offset
                while index_training <= offset + n:
                    self.valueEncoded.append(wordAndValue(self.translateWord(self.trainingDataset[index_training].getWord()), self.trainingDataset[index_training].getValue()))
                    index_training = index_training + 1
        if type == 1:          
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
                index_training = offset
                while index_training <= offset + n:
                    self.valueEncoded.append(wordAndValue(self.translateWord(self.validationDataset[index_training].getWord()), self.validationDataset[index_training].getValue()))
                    index_training = index_training + 1
        return self.valueEncoded