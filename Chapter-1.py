'''
Practice stuff from Chapter 1
I decided not to do some trivially easy stuff like assigning variables.
I've done a ton of that before and I know how that works.
'''

print(int('99'))# Works

print(int('99.99'))# Does not work

print(float('99.99'))# Works

print(int(float('99.99')))# Works, prints 99

foo = 'hello'
print(foo*5)#hellohellohellohellohello
# How useful is this? IDK but it works

bar = 5 + (1 + 3 * 4) / 2# 11.5
