# dict style
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple']) # get apple from dict

# module style
import mystuff

mystuff.apple() # get apple from the module
print(mystuff.tangerine) # same thing, it's just a variable


# class style
from mystuff2 import MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)
