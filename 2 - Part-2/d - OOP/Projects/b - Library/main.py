from entities.book import Livro
from entities.library import Biblioteca
from entities.user import Aluno, Professor

# Rodando testes
print("Rodando testes")
print()

# criando livros
livro1 = Livro("As Crônicas de Nárnia", "C.S. Lewis", 1950, "L001")
livro2 = Livro("Cristianismo puro e simples", "C.S.Lewis", 1952, "L002")
livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "L003")
livro4 = Livro("A Revolução dos Bichos", "George Orwell", 1945, "L004")
livro5 = Livro("Dom Casmurro", "Machado de Assis", 1899, "L005")
livro6 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, "L006")

print(f"{livro1}\n{livro2}\n{livro3}\n{livro4}\n{livro5}\n{livro6}")
print()

# criando usuarios
aluno = Aluno("João da Silva", "12345678900")
professor = Professor("Maria Souza", "98765432100")

print(f"{aluno}\n{professor}")
print()

# criando biblioteca
bib = Biblioteca()

print(bib)
print()

# cadastrando livros e usuarios
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_livro(livro3)
bib.adicionar_livro(livro4)
bib.adicionar_livro(livro5)
bib.adicionar_livro(livro6)

print(bib)
print()

bib.cadastrar_usuario(aluno)
bib.cadastrar_usuario(professor)

print(bib)
print()

# fazendo emprestimos
bib.emprestar("12345678900", "L001")  # Aluno pega 1º livro
bib.emprestar("12345678900", "L002")  # Aluno pega 2º livro
bib.emprestar("12345678900", "L003")  # Aluno pega 3º livro

print(aluno)
print()

bib.emprestar("98765432100", "L004")  # Professor pega 1º livro
bib.emprestar("98765432100", "L005")  # Professor pega 2º livro
bib.emprestar("98765432100", "L006")  # Professor pega 3º livro

print(professor)
print()


# devolvendo livro
bib.devolver_livro("12345678900", "L002")  # Aluno devolve um livro

print(aluno)
print()

# verificando estado atual
print(bib)  # Quantidade de livros e usuários
print([str(l) for l in aluno.livros_emprestados])  # Livros com o aluno
print([str(l) for l in professor.livros_emprestados])  # Livros com o professor