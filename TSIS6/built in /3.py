s = input(str)
t = s[::-1]
if hash(s) == hash(t):
    print('Palindrom')
else:
    print('Not Palindrom')
