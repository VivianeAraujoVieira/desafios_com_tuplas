
""" Crie um programa que tenha uma tupla única  com nomes de produtos  e seus respectivos preços , na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular. """

produtos = ('shampoo', 7.80, 'sabonetes', 2.50, 'contonetes', 1.80, 'álcool',7.20, 'lencinhos', 5.00 )

print('-'*60)
print(f'{"LISTA":^60}')
print('-'*60)

for p in range(0, len(produtos)):
    if p % 2==0:
        print(f"{produtos[p]:.<40}", end='')
    else:
        print(f"R${produtos[p]:>5}")

    