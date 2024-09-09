# bankUI: Sistema de Gerenciamento de Conta Bancária

Este é um sistema simples de **Gerenciamento de Conta Bancária** desenvolvido em Python 3.9, implementando funcionalidades básicas como **depósito**, **saque** e **extrato** (histórico de transações). O sistema utiliza uma interface baseada em texto, onde os usuários podem realizar essas operações em um ambiente simulado.

O objetivo deste projeto é fornecer um ponto de partida simples para o aprendizado e prototipação de operações bancárias, oferecendo uma estrutura básica de CRUD (Create, Read, Update, Delete) para o gerenciamento de contas.

## Funcionalidades

- **Depósito**: Adiciona dinheiro ao saldo da conta.
- **Saque**: Permite retirar dinheiro da conta, com verificações de saldo disponível, limites de saque e o número máximo de saques.
- **Extrato**: Exibe todas as transações realizadas na conta, incluindo depósitos e saques.
- **Interface Amigável**: Em caso de operações falhadas (ex: valor de saque inválido, saldo insuficiente), o sistema pergunta se o usuário deseja tentar novamente ou voltar ao menu principal.
- **Interface Baseada em Texto**: Simples e fácil de usar diretamente pelo terminal.

## Como Começar

### Pré-requisitos

- Python 3.9 ou superior
- Um terminal ou linha de comando

### Executando o Programa

1. Clone este repositório:
   ```bash
   git clone https://github.com/vitorshaft/bankUI.git
   ```

2. Navegue até o diretório do projeto:
    ```bash
    cd bankUI
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

### Versão 1.2 (Segunda Alteração)
- Fluxo aprimorado para tentativas de operação:

- - Foi implementado um fluxo que, em caso de falha (como saldo insuficiente, valor de saque inválido ou número de saques excedido), questiona o usuário se ele deseja tentar a operação novamente ou retornar ao menu principal. Isso melhora a experiência do usuário, permitindo corrigir rapidamente o erro sem voltar ao menu inicial.

### Implementação Antiga:
O programa retornava diretamente ao menu após uma falha na operação de saque ou depósito.
Nova Implementação:
Agora, após um erro, o sistema pergunta:
```python
tentar_novamente = input("Deseja tentar novamente? (s/n): ")
if tentar_novamente.lower() != 's':
    break
```

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