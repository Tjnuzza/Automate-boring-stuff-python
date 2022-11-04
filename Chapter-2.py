# Chapter 2 stuff
# Flow control (if statements and loops)
# I feel like I understand this but I had a thought while reading
# I wonder if I can do a SQL injection / bobby tables type of error?

foo = True
while(foo):
    print('Enter a statement: ')
    bar = input()
    print(bar)
    if bar == 'break':
        print('Goodbye')
        break
    # Let's see if I can enter something like 'break#' and exit the loop
# Doesn't look like this kind of attack works
# Inputs are sanitized, which is kind of what I expected
