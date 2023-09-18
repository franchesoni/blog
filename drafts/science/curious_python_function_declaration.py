
# I wanted to modify an existing recursive function, but I wanted to keep its workings. Let's say I had this function:

def fun(number):
  if number < 10:
    return fun(number+1)
  return number

print('-'*30)
number = 3
output = fun(number)
print(f'input = {number}')
print(f'fun output = {output}')

# And suppose now I want to return another number if the input is five, something like:

def fun2(number):
  if number == 5:
    return 20
  else:
    return fun(number)

print('-'*30)
number = 3
output = fun2(number)
print(f'input = {number}')
print(f'fun2 output = {output}')

print('-'*30)
number = 5
output = fun2(number)
print(f'input = {number}')
print(f'fun2 output = {output}')

# but when doing this, I am passing through 5 without returning 20! One solution is implementing the logic inside the function:

def fun3(number):
  if number == 5:
    return 20
  else:  # initial function logic here
    return fun3(number+1)

print('-'*30)
number = 3
output = fun3(number)
print(f'input = {number}')
print(f'fun3 output = {output}')

# which is not nice if we have to rewrite all the logic and the logic is long. Then we can think about a hack: 

fun4 = fun  # init fun4 as original recursion
fun4 = lambda number: fun4(number) if number != 5 else 20  # set fun4 to original recursion if number is not 5 and return 20 if number is 5

# the idea of this hack is to set

def fun4(number):  # the exact copy of fun but with another name
  if number < 10:
    return fun4(number+1)
  return number

# and then
def fun4(number):
  if number != 5:
    return fun4(number)  # here using the original recursive implementaiton
  else:
    return 20


# But this of course doesn't work. On the second definition the first definition is forgotten. If passing the first definition as another function (as in fun2) it doesn't work as required. When trying this we get a RecursionError (because we created an eternal loop).


print('-'*30)
number = 3
print(f'input = {number}')
try:
    output = fun4(number)
except RecursionError:
    print('RecursionError !')
print(f'fun4 output = {output}')

# So, how to do this?
  
#askstackoverflow
