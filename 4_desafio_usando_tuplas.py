

""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9.

b) Em que posição foi digitado o primeiro valor 3.

c) Quais foram os números pares. """

valores = (int(input("Informe o primeiro valor: ")),
           int(input("Informe o segundo valor: ")),
           int(input("informe o terceiro valor: ")),
           int(input("Informe o quarto valor: " )))

print(f"Todos o valores são esses: {valores}")
print(f"O valor 9 aparece {valores.count(9)} vezes")
print(f"O valor 3 esta na {valores.index(3)}ª posição")





