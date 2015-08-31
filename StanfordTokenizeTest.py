__author__ = 'hz'
from nltk.tokenize.stanford import StanfordTokenizer
import os

# os.environ['STANFORD_POSTAGGER'] = '.\jars'

text = "Python.com is a good website."
s = StanfordTokenizer().tokenize( text )

print( s )