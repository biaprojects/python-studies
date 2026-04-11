ANO = 2025

class Livro:
    def __init__(self, titulo, autor, ano, codigo):
        if ano > ANO:
            raise ValueError("Ano de publicação não pode ser no futuro!")
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo

    def __str__(self):
        return f"{self.titulo}, do autor {self.autor} - Código: {self.codigo}"