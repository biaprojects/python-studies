class Biblioteca:
    def __init__(self):
        self.acervo = {}
        self.usuarios = {}

    def __str__(self):
        return f"Biblioteca com {len(self.acervo)} livros e {len(self.usuarios)} usuários."

    def adicionar_livro(self, livro):
        if livro.codigo in self.acervo:
            raise ValueError("Livro já presente no acervo")
        self.acervo[livro.codigo] = livro

    def cadastrar_usuario(self, usuario):
        if usuario.cpf in self.usuarios:
            raise ValueError("Usuário já cadastrado")
        self.usuarios[usuario.cpf] = usuario

    def emprestar(self, cpf, codigo_livro):
        if cpf in self.usuarios and codigo_livro in self.acervo:
            self.usuarios[cpf].emprestar_livro(self.acervo[codigo_livro])
        else:
            if cpf not in self.usuarios:
                raise ValueError("Usuário não encontrado")
            if codigo_livro not in self.acervo:
                raise ValueError("Livro não presente no acervo")

    def devolver_livro(self, cpf, codigo_livro):
        if cpf in self.usuarios and codigo_livro in self.acervo:
            self.usuarios[cpf].devolver_livro(codigo_livro)
        else:
            if cpf not in self.usuarios:
                raise ValueError("Usuário não encontrado")
            if codigo_livro not in self.acervo:
                raise ValueError("Livro não presente no acervo")