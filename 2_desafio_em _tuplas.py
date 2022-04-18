
""" Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campionato Brasileiro de Futebol, 
na ordem de colocação. depois mostre:
a)Apenas os 5 primeiros colocados.
b)Os últimos 4 colocados da tabela.
c)Uma lista com os times em ordem alfabética.
d)Em que posição esta o time do flamengo."""


times = ('São paulo', 'Coritiba', 'Corinthias', 'Atlético-MG', 'Ceará-SC', 'Avai', 'Cuiabá', 'Bragantino', 
'Juventude', 'Flamengo', 'Atlético-GO', 'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'América-MG', 
'Botafogo', 'Internacional','Goias','Atlético-PR\n')

print('=' *40)

print(f'Tabela de classificação do campionato Brasileiro em 2022: {times}\n')

print(f'Os cinco primeiros colocados foram: {times[:5]}\n')

print(f'Os últimos 4 colocados foram: {times[16:]}\n')

print(f'Sua tabela em ordem alfabética: {sorted(times)}\n')

print(f"A posição do flamendo é: {times.index('Flamengo')+1}ª posição\n")

print('=' *40)

