#!./.venv/bin/python

print(5+5)

print(5-2)

A='{} {}'.format('hello', 'python')
print(A)

# put  member name together

name=['taro', 'hanako', 'daisuke']
birth=[1980, 1985, 1992]
address=['tokyo','osaka','kyoto']


NUM_USER=len(name)
for index in range(NUM_USER):
    #print('{} {} {}'.format(name[index], birth[index], address[index]))
    print(f'{name[index]}, {birth[index]}, {address[index]}')


taro=('taro',1980,'tokyo')
print(f'{taro[0]},{taro[1]},{taro[2]}')
