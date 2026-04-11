LIMITE_ALUNO = 3
LIMITE_PROFESSOR = 5

class Usuario:
    def __init__(self, nome, cpf, livros_emprestados):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = livros_emprestados if livros_emprestados else []

    def __str__(self):
        if self.livros_emprestados:
            return f"{self.nome} está com {len(self.livros_emprestados)} livros"
        else:
            return f"{self.nome} não pegou nenhum livro emprestado"

    def emprestar_livro(self, livro):
        self.livros_emprestados.append(livro)

    def devolver_livro(self, codigo):
        for livro in self.livros_emprestados:
            if livro.codigo == codigo:
                self.livros_emprestados.remove(livro)
                return
        raise ValueError("Esse livro não está com este usuário!")

    def limite_emprestimos(self):
        raise NotImplementedError("Subclasses devem informar o limite")


class Aluno(Usuario):
    def __init__(self, nome, cpf, livros_emprestados=None):
        super().__init__(nome, cpf, livros_emprestados)

    def limite_emprestimos(self):
        return LIMITE_ALUNO

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < LIMITE_ALUNO:
            self.livros_emprestados.append(livro)
        else:
            raise ValueError("Limite de empréstimos excedidos")


class Professor(Usuario):
    def __init__(self, nome, cpf, livros_emprestados=None):
        super().__init__(nome, cpf, livros_emprestados)

    def limite_emprestimos(self):
        return LIMITE_PROFESSOR

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < LIMITE_PROFESSOR:
            self.livros_emprestados.append(livro)
        else:
            raise ValueError("Limite de empréstimos excedidos")
