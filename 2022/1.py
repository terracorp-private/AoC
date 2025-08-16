#from collections import Counter

# #res = [key for key in Counter(res).keys() if Counter(res)[key]>1]

helper = []
subList = []
res = []

with open ('./data_tag1.txt') as f:
    lines = f.readlines()
    lines = [item.rstrip() for item in lines]
    conv = lambda i : i or 0
    lines = [conv(i) for i in lines]
    lines = [int(item) for item in lines]
    for index in lines:
        helper.append(index)
        if index == 0:
            subList.append(helper)
            helper = []

for i in subList:
    res.append(sum(i))
resN = sorted(res)
print(sum(resN[-3:]))



# with open ('./data_tag1.txt') as f:
#     data = f.read()
#     elements = data.split('\n\n')
#     print(elements)
