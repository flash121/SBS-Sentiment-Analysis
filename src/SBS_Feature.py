'''
Created on 2013-12-3
Sentence Based Feature Extraction Class based on SBSDriveBased Function
@author: yfeng
'''
from SBSDriver import SBSDriverBase

class SBS_Feature_Extraction(SBSDriverBase):
    '''
    @summary:  simple version: without specify homepath
    @param SBS_corpus: sentence based corpus
    @param SBS_feature: sentence based features
    @param sentiment: sentiment words
    @author: yfeng
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    def __str__(self):
        '''
        @summary: print information of class
        @note: pass
        '''
        pass
    def __iter__(self):
        '''
        @summary: iterate each sentence's structure
        '''
        pass
    def structureExtraction(self):
        '''
        @summary: extract structure of sentence
        '''
        pass 
    def sentimentExtraction(self):
        '''
        @summary: extract sentiment feature 
        '''
        pass
    