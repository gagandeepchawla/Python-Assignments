from __future__ import print_function
inputs = raw_input('Enter the string\n')
splits = inputs.split()
dict = {}
for i  in  splits:
    if i in dict:
        if len(i)>=2:
            del dict[i]

    else:
        dict[i]=0

for i in sorted(dict):
    print (i,end = " ")
