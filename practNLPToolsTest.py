__author__ = 'hz'
from practnlptools.tools import Annotator

text = 'the absolute receiver position and its clock offset in a second adjustment.'
# text = "We present the new MAP3 algorithms to perform static precise point positioning (PPP) " \
#        "from multifrequency and multisystem GNSS observations"
text = "MAP3 represents a two-step strategy in which the least squares theory is applied twice " \
       "to estimate smoothed pseudo-distances, initial phase ambiguities, and slant ionospheric delay " \
       "first, and the absolute receiver position and its clock offset in a second adjustment."
# text = "The interest-only securities were priced at 35 1/2 to yield 10.72 %."
# text = "Rami Eid is studying at Stony Brook University in NY."
text = 'the boy picked up a coin in the road and handed it to a policeman'
text = 'theory is applied twice.'

text = "I saw a dog chasing a cat."

text = 'Resulting ZTDs can be characterized by mean standard deviations of 6-10 mm, but still ' \
       'remaining large biases up to 20 mm due to missing precise models in the software.'

# semantic role labelling
annotator = Annotator()
result = annotator.getAnnotations( text )["srl"]

print( type(result) )
print( result )