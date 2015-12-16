__author__ = 'hz'
from practnlptools.tools import Annotator

text = "Disclosed is an organic light-emitting diode (OLED) display panel. An OLED display panel includes a plurality of signal lines and a thin film transistor formed on a substrate, an interlayer insulating layer, a first electrode, a bank, an organic light-emitting layer, a second electrode, a first passivation layer, an organic layer, a second passivation layer and a barrier film, wherein the bank is formed to completely cover the interlayer insulating layer, and an inclination formed by side surfaces of the bank and the interlayer insulating layer is made to be gradual."

# text = "Disclosed is an organic light-emitting diode (OLED) display panel."
# semantic role labelling
text = 'Unlike the classic PPP technique, in our new approach, the ionospheric-free linear combination is not used.'
annotator = Annotator()
result = annotator.getAnnotations( text )["srl"]

print( type(result) )
print( result )
