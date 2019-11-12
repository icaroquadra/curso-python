# Class by: Léo Willian Kölln, Software Architect
# Student: Ícaro Quadra, Developer JR. at: Rentcars.com


# I will start with the the 5th class, with we see the PEP-8 documentation one style guideline for Python
#     first of all the link to the guide https://www.python.org/dev/peps/pep-0008/
#     lets see the basics:
#         Comments, Declarations e Indentation


# Comments:


# now you can noticed the '#' is how to start comments
try_not_do_that = 'it'  # is not a good way to make your's comments


# Declarations:


regular_variables = 'lowercase, separated by underscores'
CONSTANTS_VARIABLES = ['all variables can be modified', 'real constants don\'t exist', 'to indicate one "constant"',
                       'uppercase, separated by underscores']


# Functions and Methods:


def function_names():

    print('like variables should be lowercase, separated by underscores',
          'and', 'two line blanks before and after', 'and need four blank spaces')


# Class:


class ClassName:

    print('camelcase')


# -----------------------------------------------------------------------------------------------------------------------
# Operations
# Add, Divide, Multiply, Subtract
#

print('add result \n', 2 + 2)
# 4
print('subtract and multiplication \n', 50 - 5*6)
# 20
print('parentheses to group \n', (50 - 5*6) / 4)
# 5.0


# Division


print('divisions return float \n', 8 / 5)
# 1.6 division always return float
print('float \n', 17 / 3)
# 5.666666666666667
print('discard after the dot \n', 17 // 3)
# 5 discard after the dot
print('the rest \n', 17 % 3)
# 2 rest of divisor

# its is possible to put the results direct in a variable
results = (50 - 5*6) / 4
print('result direct in a variable \n', results)

# you can use the operators directly in the variables
print('plus of two variables \n', results + results)


# Strings


# use \ to skip
string = 'Python \''
# strings can be repeated by the * and concat by +
print(string * 2 + ' is cool')
# accesses the indice of one string by put [number of indice]
print('first indice of string', string[0])
# from other side
print('the indice acceses by other side', string[-3])
# acceses just the interval
print('interval', string[0:2])

# strings are immutable
# lets go to the exercises
