__author__ = 'hz'

from nltk.parse import stanford
import nltk
from nltk.tree import Tree

# text = 'MAP3 represents a two-step strategy in which the least squares theory is ' \
#        'applied twice to estimate smoothed pseudo-distances, initial phase ambiguities, ' \
#        'and slant ionospheric delay first, and the absolute receiver position and its clock ' \
#        'offset in a second adjustment.'


text = 'the least squares theory applied something to estimate smoothed pseudo-distances'
# text = 'the absolute receiver position and its clock offset in a second adjustment.'
# text = 'the least squares theory applied something to estimate smoothed pseudo-distances'
parser = stanford.StanfordParser( model_path="englishPCFG.ser.gz" )

sentences = parser.raw_parse_sents( nltk.sent_tokenize( text ) )
print( type( sentences ) )

test = None

for line in sentences:
    for sentence in line:
        test = sentence
        print(sentence)
        sentence.draw()
