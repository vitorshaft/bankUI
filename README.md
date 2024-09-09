# bankUI: Sistema de Gerenciamento de Conta Bancária

Este é um sistema simples de **Gerenciamento de Conta Bancária** desenvolvido em Python 3.9, implementando funcionalidades básicas como **depósito**, **saque** e **extrato** (histórico de transações). O sistema utiliza uma interface baseada em texto, onde os usuários podem realizar essas operações em um ambiente simulado.

O objetivo deste projeto é fornecer um ponto de partida simples para o aprendizado e prototipação de operações bancárias, oferecendo uma estrutura básica de CRUD (Create, Read, Update, Delete) para o gerenciamento de contas.

## Funcionalidades

- **Depósito**: Adiciona dinheiro ao saldo da conta.
- **Saque**: Permite retirar dinheiro da conta, com verificações de saldo disponível, limites de saque e o número máximo de saques.
- **Extrato**: Exibe todas as transações realizadas na conta, incluindo depósitos e saques.
- **Interface Baseada em Texto**: Simples e fácil de usar diretamente pelo terminal.

## Como Começar

### Pré-requisitos

- Python 3.9 ou superior
- Um terminal ou linha de comando

### Executando o Programa

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```

3. Execute o programa:
    ```bash
    python main.py
    ```

## Uso

Ao executar o programa, um menu será apresentado com as seguintes opções:
```
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
```

O usuário pode interagir com o sistema escolhendo uma das opções e seguindo as instruções fornecidas.

## Atualizações
### Versão 1.1 (Primeiras Alterações)
- Melhoria no Gerenciamento do Histórico de Transações:

- - A variável extrato, que anteriormente era implementada como uma string concatenada, foi alterada para uma lista que armazena as transações. Isso permite um gerenciamento mais eficiente e escalável do histórico de transações.

### Implementação Antiga:
```python
extrato = ""
extrato += f"Depósito: R$ {valor:.2f}\n"
```

### Nova Implementação
```python
extrato = ""
extrato += f"Depósito: R$ {valor:.2f}\n"
```