#!/usr/bin/python3

import xml.etree.ElementTree as ET
import sys

def main(argv):
    """ import filedata"""
    tree = ET.parse(argv[1])
    root = tree.getroot()
    
    """ loop through the filedata and compare start and end with top and bottom"""
    for POINT in root.findall('POINT'):
        topHZ = float(POINT.find('TOP_HZ').text)
        bottomHZ = float(POINT.find('BOTTOM_HZ').text)
        startF0 = float(POINT.find('F0_START').text)
        endF0 = float(POINT.find('F0_END').text)
	    
        
        if startF0 > topHZ or startF0 < bottomHZ:
            root.remove(POINT)
        elif endF0 > topHZ or endF0 < bottomHZ:
            root.remove(POINT)
	
    """ write to file"""	    
    tree.write(argv[2])
    
if __name__ == "__main__":
    main(sys.argv)
			
			
	    
	    
	    

