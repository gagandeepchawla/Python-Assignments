inputs = raw_input('Enter the string\n')
splits = inputs.split()
#print(splits)

# for i  in  splits:
#     ab[i] = ""
# print ab
count = 0
#value = 0
dict = {}
for i  in  splits:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] =0
for i in dict:
    print dict[i]