class Livro:
    def __init__(self, titulo, autor, genero, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numero_paginas = numero_paginas

    def informacoes(self):
        return f"""
            Titulo: {self.titulo}
            Autor: {self.autor}
            Gênero: {self.genero}
            Número de Páginas: {self.numero_paginas}
        """
    def analise_paginas(self):
        if self.numero_paginas > 350:
            return f"O livro {self.titulo} é longo"
        else:
            return f"O livro {self.titulo} não é longo"
        
livro1 = Livro(titulo= "Senhor dos Aneis - As duas torres", autor="JRR Tolkien", genero="Aventura", numero_paginas= 450)

print(livro1.informacoes())
print(livro1.analise_paginas())