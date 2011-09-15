#!/usr/bin/env python

"""
A simple utility script for helping me develop solutions to the project euler problems. For more information about project eueler visit projecteuler.net

Commands: 

gen [filename] [problem] - generates a file name "filename," and puts the description of the "problem" specified in a docstring at the top of the file. Example usage - util problem1.py 1
"""

import urllib2
import argparse
from BeautifulSoup import BeautifulSoup

euler_problems_url = "http://www.projecteuler.net/index.php?section=problems&id="


########################################
#####             Parse           ######
########################################

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

#gen command
parser_gen = subparser.add_parser("gen")
parser_gen.add_argument("filename")
parser_gen.add_argument("problem_number", type=int)

args = parser.parse_args()

##########################################

url = "%s%d" % (euler_problems_url, args.problem_number)
site = urllib2.urlopen(url)

source = site.read()
soup = BeautifulSoup(source)
source = soup.find('div', role='problem')
text = source.getText()

newfile = file(args.filename, 'w')
newfile.write('"""' + '\n' + text + '\n\n' + url + '\n'  + '"""')
newfile.close()
