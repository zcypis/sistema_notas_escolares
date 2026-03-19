# Sistema de Gestão de notas Academicas

Sistema de gerenciamento dados academicos via terminal, desenvolvido em Python puro. Permite registrar alunos, ver notas, acompanhar desempenho e manter os dados entre sessões — sem nenhuma dependência externa.

---

## Funcionalidades

- Registrar aluno com nome e notas personalizadas
- Buscar aluno pelo nome
- Listar todos os alunos com média e situação
- Cálculo automático de desempenho
- Dados salvos automaticamente em `dados_alunos.json`

---

## Critério de desempenho

| Média        | Situação        |
|--------------|-----------------|
| 6.0 a 10.0   | Aprovado      |
| 4.0 a 5.9    | Recuperação   |
| 0.0 a 3.9    | Reprovado     |

---

## Estrutura do projeto

```
sistema_notas_escolares/
- main.py            # Menu interativo e loop principal
- validadores.py     # Validação de nome, nota e lista de notas
- processadores.py   # Lógica de negócio: registrar, buscar, listar
- helpers.py         # Leitura e tratamento de input do usuário
- dados.py           # Persistência: carregar e salvar em JSON
- dados_alunos.json         # Banco de dados local (gerado automaticamente)
- .gitignore
- README.md
```

---

## Como usar

### Pré-requisitos
- Python 3.10 ou superior

### Executando o projeto

```bash
git clone https://github.com/zcypis/sistema_notas_escolares.git
cd Gestao_Academica
python main.py
```

### Menu principal

```
=== SISTEMA DE ALUNOS ===
[1] - Registrar aluno
[2] - Buscar aluno
[3] - Listar todos
[4] - Sair
```

---

## Arquitetura

O projeto segue o princípio de **separação de responsabilidades** — cada módulo tem uma função clara e independente:

| Módulo | Responsabilidade |
|---|---|
| `validadores.py` | Garante que os dados recebidos são válidos antes de qualquer processamento |
| `processadores.py` | Contém a lógica principal do sistema |
| `helpers.py` | Gerencia a leitura de inputs do usuário com tratamento de erros |
| `dados.py` | Abstrai o carregamento e salvamento no arquivo JSON |
| `main.py` | Orquestra os módulos e exibe o menu ao usuário |

---

## Tecnologias

- Python 3.10+
- Somente biblioteca padrão — `json`
- Sem dependências externas

---

## Autor

**Guilherme Xavier**
- GitHub: [@zcypis](https://github.com/zcypis)
- Email: guilhermexavie3@gmail.com