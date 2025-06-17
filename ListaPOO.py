class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel: bool = True):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == False:
            print("O livro não está disponível para empréstimo!")
        else:
            self.disponivel = False
            print("Livro emprestado com sucesso!")

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print("Livro devolvido com sucesso!")
        else:
            print("Livro não foi emprestado!")

    def obter_info(self):
        if self.disponivel == True:
            disponibilidade = "Sim"
        else:
            disponibilidade = "Não"
        return f"Título: {self.titulo}\nano de lançamento: {self.ano_publicacao}\nDisponível: {disponibilidade}"


class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                return False
            return True

    def obter_info(self):
        for livro in self.lista_livros:
            return f"Livro: {livro.titulo}"
            


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao,edicao, disponivel: bool = True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.edicao = edicao

    def atualizar_edicao(self):
        if self.edicao <= 0:
            return "edição indisponivel"
        else:
            self.edicao += 1

    def restringir_emprestimo(self,dias:int = 0):
        if self.ano_publicacao <=2000:
            return "A revista pode ser emprestada até sete dias!"
        else:
            return f"A revista pode ser emprestada até {dias} dias!"

    def obter_info(self):
        if self.disponivel == True:
            disponibilidade = "Sim"
        else:
            disponibilidade = "Não"
        return f"Título: {self.titulo}\nEdição: {self.edicao}\nano de lançamento: {self.ano_publicacao}\nDisponível: {disponibilidade}"

class Biblioteca:
    def __init__(self):
        self.items = {}

    def adicionar_item(self,item):
        if item.titulo in self.items:
            print("O item já existe na biblioteca!")
        else:
            self.items[item.titulo] = item
            print(f"Item '{item.titulo}' adicionado à biblioteca com sucesso.")

    def remover_item(self,item):
        if item.titulo not in self.items:
            print("O item não existe na biblioteca!")
        else:
            print(f"Item '{item.titulo}' deletado da biblioteca com sucesso.")
            del self.items[item.titulo]

    def listar_items_disponiveis(self):
        for item in self.items.values():
            if item.disponivel:
                print(f"Titulo do item: {item.titulo}")

    def contar_itens_emprestados(self):
        contador = 0
        for item in self.items.values():
            if not item.disponivel:
                contador+=1
                print(f"Quantidade de items emprestados no momento: {contador}")


class RelatorioBiblioteca:


    def __init__(self, biblioteca: Biblioteca):



        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self) :

        if not self.biblioteca.items:
            return "A biblioteca está vazia. Nenhum item para relatar."


        partes_relatorio = ["=== RELATÓRIO COMPLETO DE ITENS ==="]
        for item in self.biblioteca.items.values():
            partes_relatorio.append(item.obter_info())
            partes_relatorio.append("-" * 30)

        return "\n".join(partes_relatorio)


livro1 = ItemBiblioteca("Percy Jackson e o ladrão de raios", 2008)
livro2 = ItemBiblioteca("Percy Jackson e o Mar de Monstros", 2012)

colecao1 = ColecaoLivros("Percy Jackson", 1998, False)
colecao1.adicionar_livro(livro1)
colecao1.adicionar_livro(livro2)
colecao1.obter_info()

revista1 = Revista("Turma da monica",1990, 230)
print(revista1.obter_info())
revista1.atualizar_edicao()
print(revista1.obter_info())

print(revista1.restringir_emprestimo(20))

bibliotecaDoDorivas = Biblioteca()

bibliotecaDoDorivas.adicionar_item(livro1)
bibliotecaDoDorivas.adicionar_item(livro1)
bibliotecaDoDorivas.adicionar_item(colecao1)
bibliotecaDoDorivas.remover_item(livro2)

bibliotecaDoDorivas.listar_items_disponiveis()
bibliotecaDoDorivas.contar_itens_emprestados()

relatorio = RelatorioBiblioteca(bibliotecaDoDorivas)
print(relatorio.gerar_relatorio_completo())
