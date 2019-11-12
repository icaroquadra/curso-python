# Experimentos:
#     Experimente retirar end=' ' das chamadas a print().
#     Experimente o código age = input("How old are you? ").
#     O que acontece caso seja usado o código print("How old are you?" , input())?


print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
