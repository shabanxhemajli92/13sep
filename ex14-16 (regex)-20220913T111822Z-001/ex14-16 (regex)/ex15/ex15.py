from nis import match
import re
input_function=input("type in to check if its math: ")
pattern_tomatch=r'\d\s*(\+|\*|-|%|\/)\s*\d'
input_checker=re.search(pattern_tomatch,input_function)
if input_checker==None:
    print(False)
else:
    print(True)    
   