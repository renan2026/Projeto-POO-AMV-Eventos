class Motorista:
    def __init__(self, id_motorista, nome, cpf, cnh):
        self.id = id_motorista
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh

    def cadastrar(self, nome, cpf, cnh):
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh
        print(f"Motorista {self.nome} cadastrado com sucesso.")

    def atualizar(self, nome=None, cpf=None, cnh=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if cnh:
            self.cnh = cnh
        print(f"Dados do motorista {self.id} atualizados.")


class Veiculo:
    def __init__(self, id_veiculo, placa, modelo, capacidade):
        self.id = id_veiculo
        self.placa = placa
        self.modelo = modelo
        self.capacidade = capacidade

    def cadastrar(self, placa, modelo, capacidade):
        self.placa = placa
        self.modelo = modelo
        self.capacidade = capacidade
        print(f"Veículo {self.placa} cadastrado.")

    def atualizar(self, placa=None, modelo=None, capacidade=None):
        if capacidade is not None and capacidade <= 0: # Modificado para aceitar apenas números positivos
            raise ValueError("A capacidade deve ser um número positivo.")
        if placa is not None:
            self.placa = placa
        if modelo is not None:
            self.modelo = modelo
        if capacidade is not None:
            self.capacidade = capacidade
        print(f"Veículo {self.id} atualizado.")


class MaterialCozinha:
    def __init__(self, id_material, nome, tipo, descricao):
        self.id = id_material
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao

    def cadastrar(self, nome, tipo, descricao):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        print(f"Material {self.nome} cadastrado.")

    def atualizar(self, nome=None, tipo=None, descricao=None):
        if nome:
            self.nome = nome
        if tipo:
            self.tipo = tipo
        if descricao:
            self.descricao = descricao
        print(f"Material {self.id} atualizado.")


class ItemEntrega:
    def __init__(self, id_item, quantidade, material):
        self.id = id_item
        self.quantidade = quantidade
        self.material = material

    def adicionar(self, qtd):
        if qtd <= 0: # Modificado para aceitar apenas números positivos
            raise ValueError("A quantidade a ser adicionada deve ser positiva.") # Não aceita numero negativo
        self.quantidade += qtd
        print(f"Adicionados {qtd} itens. Total atual: {self.quantidade}")
    def remover(self, qtd):
        if qtd <= 0:
            raise ValueError("A quantidade a ser removida deve ser positiva.")
        if qtd > self.quantidade:
            raise ValueError("Não é possível remover mais itens do que a quantidade disponível.")
        self.quantidade -= qtd
        print(f"Removidos {qtd} itens. Total restante: {self.quantidade}")


class Evento:
    def __init__(self, id_evento, data, destino, motorista=None, veiculo=None):
        self.id = id_evento
        self.data = data
        self.destino = destino
        self.status = "Pendente"
        self.motorista = motorista
        self.veiculo = veiculo
        self.itens = []

    def criar(self):
        self.status = "Criado"
        print(f"Evento {self.id} para {self.destino} foi criado.")

    def finalizar(self):
        self.status = "Finalizado"
        print(f"Evento {self.id} finalizado.")

    def cancelar(self):
        self.status = "Cancelado"
        print(f"Evento {self.id} cancelado.")

    def adicionar_item(self, item):
        self.itens.append(item)


# --- Teste de Funcionalidade ---
if __name__ == "__main__":
    # 1. Criar Motorista e Veículo
    m1 = Motorista(1, "Carlos Silva", "123.456.789-00", "ABC12345")
    v1 = Veiculo(1, "ABC-1234", "Kombi", 1200.0)

    # 2. Criar Material e Item de Entrega
    mat1 = MaterialCozinha(1, "Panela Industrial", "Inox", "Panela 50L")
    item1 = ItemEntrega(101, 5, mat1)
    item1.adicionar(10)

    # 3. Criar e gerir o Evento
    ev1 = Evento(1, "2026-10-15", "Cozinha Comunitária Centro", m1, v1)
    ev1.adicionar_item(item1)
   
    ev1.criar()
    print(f"Status atual do evento: {ev1.status}")
   
    ev1.finalizar()
    print(f"Status atual do evento: {ev1.status}")