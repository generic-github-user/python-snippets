#!/usr/bin/env python
# coding: utf-8

# ### Prime Number Generator
# 
# Prints out a list of prime numbers in the specified range.

# In[ ]:





# In[2]:


for i in range(2, 50):
    for j in range(2, round(i**(1/2))):
        if i % j == 0:
            break
    else:
        print(i)


# ### Flatten Nested List
# 
# Convert an irregular ordered list of lists and/or values to a shallow sequence of values.
# 
# Source: https://stackoverflow.com/a/14491059/10940584

# In[3]:


def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item

list(flatten([[[1, 2, 3], [4, 5]], 6]))


# ## String Manipulation

# ### Title Case

# In[10]:


def title(text, ignore=['in', 'the', 'of', 'with', 'or', 'and']):
    return ' '.join(w[0].upper()+w[1:] if w not in ignore else w for w in text.split(' '))

title('trends in machine learning')


# In[9]:


def makelist(items):
    return ', '.join(items[:-1])+', and '+items[-1]

makelist(list('xyz'))


# In[41]:


def subdivide(num, parts):
    result = []
#     while num>0:
    factor = max(1/p for p in parts)
    parts = [int(p*factor) for p in parts]
    num *= factor
    parts.sort(reverse=True)
    for p in parts:
#             while num>p:
        if num >= p:
            x = num // p
            result.append((p/factor, x))
            num -= p * x
    if num:
        print(f'Remainder of {round(num/factor, 4)}')
    return result


# In[59]:


# test = 'thing'
# test.pop()


# In[66]:


def plural(a, b, prepend=False):
    if b != 1:
        if a[-1] == 'y':
            a = a[:-1] + 'ies'
        elif a[-1] != 's':
            a += 's'
    if prepend:
        a = f'{b} {a}'
    return a


# In[74]:


values = [
    [100, '$100 bill'],
    [50, '$50 bill'],
    [20, '$20 bill'],
    [10, '$10 bill'],
    [5, '$5 bill'],
    [1, '$1 bill'],
    [0.25, 'quarter'],
    [0.10, 'dime'],
    [0.05, 'nickel'],
    [0.01, 'penny']
]
nums, labels = list(zip(*values))
c = subdivide(12.34, nums)
print(nums)
makelist(['{} x {}'.format(int(b[1]), labels[nums.index(b[0])]) for b in c])


# In[75]:


makelist([plural(labels[nums.index(b[0])], int(b[1]), True) for b in c])


# In[76]:


def change(amount):
    c = subdivide(amount, nums)
    return makelist([plural(labels[nums.index(b[0])], int(b[1]), True) for b in c])

print(change(378.22))


# In[42]:


# TODO: flood fill

