#: E231
a = (1,2)
#: E231
a[b1,:]
#: E231
a = [{'a':''}]
#: Okay
a = (4,)
b = (5, )
c = {'text': text[5:]}

result = {
    'key1': 'value',
    'key2': 'value',
}
#: Okay
print(f"{x:0.{digits:d}f}")
#: Okay
print(f'{x:{y:{z:02}}}')
#: Okay
print(f"{a[lower:upper]}")
