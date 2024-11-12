import json

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

    def to_dict(self):
        return {
            "dataVenda": self.__dataVenda,
            "produtos": [produto.to_dict() for produto in self.__produtos]
        }

    @staticmethod
    def salvar_vendas(vendas, arquivo="vendas.json"):
        try:
            with open(arquivo, "w") as file:
                json.dump([venda.to_dict() for venda in vendas], file, indent=4)
                print("Vendas salvas com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar vendas: {e}")

    @staticmethod
    def carregar_vendas(arquivo="vendas.json"):
        vendas = []
        try:
            with open(arquivo, "r") as file:
                vendas_data = json.load(file)
                for venda_data in vendas_data:
                    venda = Venda(venda_data["dataVenda"])
                    for produto_data in venda_data["produtos"]:
                        produto = Produto(
                            produto_data["nome"],
                            produto_data["preco"],
                            produto_data["quantidade"]
                        )
                        venda.get_produtos().append(produto)
                    vendas.append(venda)
            print("Vendas carregadas com sucesso.")
        except FileNotFoundError:
            print("Arquivo de vendas não encontrado, começando uma nova venda.")
        except Exception as e:
            print(f"Erro ao carregar vendas: {e}")
        return vendas
