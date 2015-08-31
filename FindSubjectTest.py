__author__ = 'hz'
from nltk.tree import ParentedTree
from nltk.parse import stanford
import nltk
from nltk.tree import Tree
import SAO

text = 'the least squares theory applied something to estimate smoothed pseudo-distances'

text = 'Resulting ZTDs can be characterized by mean standard deviations of 6-10 mm, ' \
       'but still remaining large biases up to 20 mm due to missing precise models in the software.'
text = 'I saw a dog chasing a cat.'
text = 'Resulting ZTDs can be characterized by mean standard deviations of 6-10 mm, but still ' \
       'remaining large biases up to 20 mm due to missing precise models in the software.'
# sao_system = SAO.SAOSystem()
#
# sao_paser = SAO.SAOParserCore()
#
# tree = sao_paser.getParserTree( text )
# print( tree )

parser = stanford.StanfordParser( model_path="englishPCFG.ser.gz" )

##### raw_parse_sents: parameter:['','']
sentences = parser.raw_parse_sents( nltk.sent_tokenize( text ) )

paser_tree = None

for line in sentences:
    for sentence in line:
        paser_tree = sentence

paser_tree.draw()
# print( paser_tree[0] )

sao_system = SAO.SAOSystem()
print( sao_system._SAOSystem__findSubject( paser_tree[0]))