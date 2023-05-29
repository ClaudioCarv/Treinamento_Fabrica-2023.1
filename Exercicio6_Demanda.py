class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def imprimir_informacoes(self):
        print("Informações do Livro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.num_paginas}")



meu_livro = Livro("One Piece Volume 102", "Eichiro Oda", "202\n")
meu_livro.imprimir_informacoes()
meu_livro2 = Livro("Berserk Volume 5", "Kentaro Miura", "240" )
meu_livro2.imprimir_informacoes()
