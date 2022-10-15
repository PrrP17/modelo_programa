import modelo


class_av = modelo


vingadores = class_av.Filme('vingadores - guerra infinita', 2018, 160)

vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
f'- Duração: {vingadores.duracao}' f'- Likes: {vingadores.likes}')

atlanta = class_av.Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
f'- Temporadas: {atlanta.temporadas}' f'- Likes: {atlanta.likes}')

