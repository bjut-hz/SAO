import nltk

text = "We present the new MAP3 algorithms to perform static precise point positioning (PPP) " \
       "from multifrequency and multisystem GNSS observations. MAP3 represents a two-step strategy " \
       "in which the least squares theory is applied twice to estimate smoothed pseudo-distances, " \
       "initial phase ambiguities, and slant ionospheric delay first, and the absolute receiver position " \
       "and its clock offset in a second adjustment. Unlike the classic PPP technique, in our new approach, " \
       "the ionospheric-free linear combination is not used. The combination of signals from different " \
       "satellite systems is accomplished by taking into account the receiver inter-system bias. " \
       "MAP3 has been implemented in MATLAB and integrated within a complete PPP software developed on site " \
       "and named PCube. We test the MAP3 performance numerically and contrast it with other external PPP programs. " \
       "In general, MAP3 positioning accuracy with low-noise GPS dual-frequency observations is about 2.5 cm in 2-h" \
       " observation periods, 1 cm in 10 h, and 7 mm after 1 day. " \
       "This means an improvement in the accuracy in short observation periods of at least 7 mm with respect to" \
       " the other PPP programs. The MAP3 convergence time is also analyzed and some results obtained from real " \
       "triple-frequency GPS and GIOVE observations are presented."

sentences = nltk.sent_tokenize( text )
print( sentences )

words = []
for sent in sentences:
   # words.append( nltk.word_tokenize( sent ) )
   print( nltk.word_tokenize(sent))



# tags = []
# for tokens in words:
#    tags.append( nltk.pos_tag( tokens ) )
#
# print( tags )
#
# ners = nltk.ne_chunk( tags )