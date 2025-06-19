
# 🐞 Ouvidoria BESOURO VERMELHO

Sistema de ouvidoria simples e interativo, desenvolvido em Python com integração a banco de dados MySQL. Permite o registro, visualização, busca e exclusão de manifestações dos usuários.

> Projeto desenvolvido por:
> - Naytson Pimentel da Silva  
> - Edson Pedro da Rocha Silva  
> - Eddie Yago Gabriel dos Santos Sátiro  
> - Guilherme Natã Meirelles Jung  

---

## 📁 Estrutura de Arquivos

```
📦 OuvidoriaBesouroVermelho
├── menu.py            # Arquivo principal com menu e navegação
├── ouvidoria.py       # Funções relacionadas à manipulação das manifestações
├── operacoesbd.py     # Conexão e operações com o banco de dados
└── README.md          # Este arquivo
```

---

## ▶️ Como Executar

1. Configure o MySQL com um banco chamado `ouvidoriabesourovermelhov2` e uma tabela `ouvidoria` com os seguintes campos:
```sql
CREATE TABLE ouvidoria (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nomeusuario VARCHAR(100),
    tipomanifestacao INT,
    manifestacao TEXT
);
```

2. Execute o programa principal:
```bash
python menu.py
```

---

## 📌 menu.py

Este é o **arquivo principal** do projeto. Ele exibe o menu de ações da ouvidoria e redireciona as escolhas do usuário para as funções apropriadas.

### Funcionalidades:

- 📋 **Listar manifestações** (por tipo ou todas)
- ➕ **Criar nova manifestação** (Elogio, Sugestão ou Reclamação)
- 🔢 **Exibir quantidade total de manifestações**
- 🔍 **Pesquisar manifestação pelo código**
- ❌ **Excluir manifestação**
- 🚪 **Sair do sistema**

---

## 🧠 ouvidoria.py

Arquivo que contém **todas as funções operacionais** para manipular as manifestações no banco de dados.

### Funções principais:

- `criarManifestacao()`: Insere uma nova manifestação (Elogio, Sugestão ou Reclamação)
- `listarTodos()`: Lista todas as manifestações cadastradas
- `listarManifestacao()`: Lista apenas manifestações de um tipo específico
- `pesquisarManifestacoes()`: Busca uma manifestação pelo seu código
- `excluirManifestacao()`: Remove uma manifestação específica
- `contadorManifestacoes()`: Exibe a quantidade total de manifestações

---

## 💾 operacoesbd.py

Módulo responsável por **todas as operações de banco de dados**, com tratamento de exceções.

### Principais funções:

- `criarConexao()`: Conecta ao banco MySQL
- `encerrarConexao()`: Fecha a conexão
- `insertNoBancoDados()`: Insere dados com segurança
- `listarBancoDados()`: Lista dados com base em uma query
- `atualizarBancoDados()`: Atualiza registros
- `excluirBancoDados()`: Remove registros do banco

---

## 🛡️ Segurança e Boas Práticas

✅ Uso de **prepared statements** para evitar SQL Injection  
✅ Tratamento de erros nas operações com o banco de dados  
✅ Separação clara entre interface (menu), lógica (funções) e acesso ao banco  

---

## 📚 Tecnologias

- Python 3
- MySQL
- Biblioteca `mysql-connector-python`

---

## 📦 Exemplo de Manifestação

```
Código: 1
Nome: João da Silva
Tipo: Sugestão
Manifestação: Poderiam melhorar o tempo de resposta.
```

---

## 📩 Contato

Caso queira contribuir ou tenha sugestões:

📧 naytson.ai@gmail.com

---
