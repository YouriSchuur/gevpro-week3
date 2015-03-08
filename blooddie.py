#!/usr/bin/python3

import sys
import json
from collections import namedtuple

""" create a namedtuple"""
Language = namedtuple("language", "name, classification")

def blooddie(language):
    blood = language[2].split()
    die = language[3].split()
    return [True for word in blood if word in die]

def main():
    """ open file"""
    open_file = open("blood-die.json", "r")
    filedata = json.load(open_file)
    
    """ create resultslist and append to resultslist"""
    resultslist = []
    [resultslist.append(Language(language[0], language[1])) for language in filedata if blooddie(language)]
    [print(result.name, "|", result.classification) for result in resultslist]

if __name__ == '__main__':
    main()
