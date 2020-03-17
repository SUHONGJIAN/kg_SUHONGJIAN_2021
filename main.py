# Python solution to check whether one-to-one character mapping exists from one string to another string.
import sys
from collections import defaultdict


class Solution(object):
    def check1v1Mapping(self, s1, s2):
        '''
        >>> check1v1Mapping("abc", "bcd")
        True
        '''
        if len(s1) != len(s2):
            return False
        mappingDict = defaultdict(str)
        # For each character pair of (s1, s2), check whether one-to-one mapping exists and return False if exists one-to-many.
        for char1, char2 in zip(s1, s2):
            if mappingDict[char1] and mappingDict[char1] != char2:
                return False
            else:
                mappingDict[char1] = char2
        return True


class InputError(Exception):
    '''
    Custom Exception: raise when the number of command line arguments is not what expected
    '''
    def __init__(self, inputsSize):
        self.inputsSize = inputsSize
        
        
class MainProcess(object):
    def main(self):
        '''
        >>> python main.py 123 321
        True
        '''
        try:
            if len(sys.argv) != 3:
                raise InputError(len(sys.argv) - 1)
            s1, s2 = sys.argv[1], sys.argv[2]
            result = Solution().check1v1Mapping(s1, s2)
            print(result)
        except InputError as error:
            print("Oops! That was invalid command line arguments[inputs size: " + str(error.inputsSize) + " -> shout be 2]. Try it again.")

MainProcess().main()