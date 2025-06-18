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
                self.disponivel= False
            else:
                self.disponivel=True

    def obter_info(self):
        informacoes = [f"Informações da {self.titulo}: "]
        for livro in self.lista_livros:
            informacoes.append(f"Título: {livro.titulo}\nano de lançamento: {livro.ano_publicacao}\nDisponível: {livro.disponivel}")

        return f"{"\n\n".join(informacoes)}"
            


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
        self.disponiveis = 0
        self.emprestados = 0
        self.relacao = ""

    def gerar_relatorio_completo(self) :

        if not self.biblioteca.items:
            return "A biblioteca está vazia. Nenhum item para relatar."


        partesRelatorio = ["\nRelatório: "]
        for item in self.biblioteca.items.values():
            partesRelatorio.append(item.obter_info())
            partesRelatorio.append("-" * 30)

        return "\n".join(partesRelatorio)

    def gerar_relatorio_disponibilidade(self):
        partesRelatorio = ["Relatório de itens disponiveis:"]
        contadorDisponiveis = 0
        for item in self.biblioteca.items.values():
            if item.disponivel:
                contadorDisponiveis+=1
                partesRelatorio.append(item.titulo)
        self.disponiveis = contadorDisponiveis
        return f"{"\n".join(partesRelatorio)}\nQuantidade de itens disponiveis: {contadorDisponiveis}"

    def gerar_relatorio_emprestimo(self):
        partesRelatorio = ["\nRelatório de itens emprestados: "]
        for item in self.biblioteca.items.values():
            if not item.disponivel:
                self.emprestados += 1
                partesRelatorio.append(item.titulo)
        self.relacao = f"{self.disponiveis}/{self.emprestados}"
        return f"{"\n".join(partesRelatorio)}\nRelação dos itens disponiveis/emprestados: {self.relacao}"



livro1 = ItemBiblioteca("Percy Jackson e o ladrão de raios", 2008)
livro2 = ItemBiblioteca("Percy Jackson e o Mar de Monstros", 2012)

colecao1 = ColecaoLivros("Coleção Percy Jackson", 1998, True)
colecao1.adicionar_livro(livro1)
colecao1.adicionar_livro(livro2)
print(colecao1.obter_info())

revista1 = Revista("Turma da monica",1990, 230)

revista1.atualizar_edicao()




bibliotecaDoDorivas = Biblioteca()
bibliotecaDoDorivas.adicionar_item(livro1)
bibliotecaDoDorivas.adicionar_item(livro2)
bibliotecaDoDorivas.adicionar_item(colecao1)
bibliotecaDoDorivas.adicionar_item(revista1)


livro1.emprestar()

relatorio = RelatorioBiblioteca(bibliotecaDoDorivas)
print(relatorio.gerar_relatorio_completo())
print(relatorio.gerar_relatorio_disponibilidade())
print(relatorio.gerar_relatorio_emprestimo())