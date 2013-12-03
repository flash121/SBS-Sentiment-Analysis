'''
Created on 2013-12-3

@author: yfeng


SBS_Driver: contains initial parameters & inital driver for model & useful basic functions

'''
import gensim
import numpy
import scipy.sparse.lil_matrix

class SBSDriverBase(object):
    '''
    @param homepath: default: "..\\data\\"
    @param storepath: default: "..\\features\\"
    @param corpus: coding strategy
    @param dict: dictionary generated from source in homepath
    @author: yfeng
    @contact: gaoyfeng2010@hotmail.com
    @version: 0.0.1
    '''

    def __init__(self,homepath="..\\data\\",storepath="..\\features\\"):
        '''
        Constructor
        @todo: load data
        @todo: generated dictionary
        @todo: generated sparse lili_matrix
        '''
        self.homepath=homepath
        self.storepath=storepath
        pass
    def SBSload(self):
        '''
        @summary: load that from specify directory
        @todo: if directory not exist, then create
        @todo: if directory no file, return error
        @todo: load all files
        '''
        pass
    def SBSGenerateDictionary(self):
        '''
        @summary: generated dictionary
        @todo: generted dictionary
        @keyword gensim, dictionary       
        '''
        pass
    def SBS_lilsparse(self):
        '''
        @summary: lili-sparse matrix to store words relation
        @todo: construct relation
        '''
        pass