# coding=utf-8
'''
Created on 12/mag/2016

@author: lorenzo
'''

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

    def __init__(self):
        '''
        Constructor
        '''
        
    def translateWord(self,word="Hello"):
        i = 0
        wordOutput = ""
        if len(word) <= 10:
            while (i<10):
                if(i < len(word)):
                    wordOutput = wordOutput + self.dict[word[i]]
                else:
                    wordOutput = wordOutput + self.dict['&']
                i += 1
        print(wordOutput)
                
            
            
        
        
        
        
        