import re
type_in=str(input("Type whatever you want: "))
lremoval_pattern=r'^0+'
tremoval_pattern=r'0+$'
lzero_removal=re.sub(lremoval_pattern,"",type_in)
tzero_removal=re.sub(tremoval_pattern,"",lzero_removal)
print(tzero_removal)