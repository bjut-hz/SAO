__author__ = 'hz'

from nltk.tag import *
import os

# os.environ['STANFORD_MODELS'] = '.\jars'
# os.environ['STANFORD_POSTAGGER'] = '.\jars'

# StanfordPOSTagger Test
st = StanfordPOSTagger("english-bidirectional-distsim.tagger")
result = st.tag("Rami Eid is studying at Stony Brook University in NY".split())
print( result )

#StanfordNERTagger Test
st_ner_tagger = StanfordNERTagger("english.all.3class.distsim.crf.ser.gz")
result = st_ner_tagger.tag( 'Rami Eid is studying at Stony Brook University in NY'.split() )
print( result )