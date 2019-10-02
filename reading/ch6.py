#%%

def tax(subtotal):
    return subtotal * 0.08875


#%%

def set_a():
    a = 10
    print('the value of a:', a)

a = 20
print('Initially the value of a', a)
set_a()
print('finally the value of a', a)
#%%

l = [4, 7, 2, 6]

for num in l:
    print(num*2)

#%%
x = 'hello'
type(x)

'hello'+'world'

#%%
len('hello world')

str(2)+'hello'
#%%

def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

words = ['hello', 'world']
double(words)

double('abstraction')
#%%
