__author__ = 'hz'
import nlpnet

# text = 'I buy a book.'
# #tagger = nlpnet.POSTagger()
# tagger = nlpnet.SRLTagger( r".\model\nlpnet_model", language= 'en' )
#
# sents = tagger.tag( text )
#
# for sent in sents:
#     print( sent.tokens )
#     print( sent.arg_structures )

#thanks to this tools does not support English model£¬so we abandon it

tagger = nlpnet.SRLTagger( r".\model\nlpnet_model", language='en' )
sent = tagger.tag(u'O rato roeu a roupa do rei de Roma')[0]

print( sent.arg_structures )

# print( type(sent) )
#
# print( 'test' )