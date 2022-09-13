import re
input_var=input("type any phrase: ")

#pattern_forconversion=r'(:|8|;|x)\('
#pattern_forchange=r':)|8)|x)|;)'

eyes = [r":", r";", r"8", r"x"]

for e in eyes:
    pattern_forconversion=e+r'\('
    pattern_forchange=e+r')'
    input_var=re.sub(pattern_forconversion,pattern_forchange,input_var)

print(input_var)
