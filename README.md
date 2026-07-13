# Copa do Mundo em Dicionários — Desempenho do Brasil

Trabalho final da disciplina de Estrutura de Dados (AED). Sistema que modela o
desempenho da Seleção Brasileira nas Copas do Mundo usando **dicionários**
como estrutura central de armazenamento e consulta.

## Estrutura do repositório

```
copa-brasil-ryckson/
├── copa_brasil.py              # backend em Python (versão terminal)
├── copa_brasil_ipywidgets.py   # mesma lógica, com interface ipywidgets p/ Google Colab
├── front/                      # vitrine visual estática (HTML/CSS/JS)
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

> O front em `front/` é apenas uma vitrine visual do projeto (JavaScript puro,
> roda no navegador). A lógica avaliada — dicionários, funções, robustez —
> está em `copa_brasil.py`.

## Modelagem dos dados

O sistema usa três dicionários como estrutura central:

| Dicionário            | Chave                                | Por que essa chave                                                   |
|------------------------|---------------------------------------|------------------------------------------------------------------------|
| `copas_brasil`         | `ano` (int)                           | Único e imutável — identifica a edição da Copa                        |
| `artilheiros_brasil`   | `nome` (str)                          | Único neste conjunto de dados                                         |
| `partidas_brasil`      | `(ano, fase, adversario)` (tupla)     | Chave composta: o mesmo adversário pode aparecer em anos/fases diferentes, então só a combinação dos três garante unicidade |

Estruturas compostas usadas: dicionário de dicionários (`copas_brasil`,
`artilheiros_brasil`) e dicionário com chave-tupla (`partidas_brasil`).

## Funcionalidades implementadas

**Consulta**
- Listar todas as participações do Brasil em Copas
- Ver detalhes de uma Copa específica
- Listar eliminações
- Listar partidas cadastradas

**Análise**
- Listar títulos conquistados
- Ranking de artilheiros
- Comparar duas Copas lado a lado

**Modificação**
- Cadastrar nova Copa
- Atualizar dados de uma Copa existente
- Cadastrar partida
- Remover partida

O programa trata chave inexistente, opção inexistente no menu e entrada
inválida (texto onde se espera número) sem quebrar.

## Como executar

### Versão terminal (`copa_brasil.py`)

Requer apenas Python 3, sem bibliotecas externas.

```bash
python copa_brasil.py
```

Também funciona colado em uma célula do Google Colab (o `input()` funciona
normalmente lá).

### Versão com interface no Google Colab (`copa_brasil_ipywidgets.py`)

1. Abra o [Google Colab](https://colab.research.google.com).
2. Cole o conteúdo do arquivo `copa_brasil_ipywidgets.py` em uma célula.
3. Execute a célula — a interface com abas (Consultas, Análises, Copas,
   Partidas) aparece logo abaixo.

### Front estático (`front/`)

Não precisa de servidor nem instalação.

1. Baixe ou clone o repositório.
2. Abra `front/index.html` diretamente no navegador (duplo clique ou
   arrastar para uma aba).

Os dados dessa versão ficam em memória no navegador e reiniciam a cada
recarregamento da página.

## Relatório de uso de IA

Ferramenta utilizada: Claude (Anthropic), para apoio na estruturação do
código, geração de exemplos de interface e revisão de organização.

Escrevi a lógica principal baseada em dicionários e estruturas de dados em Python, com uma pequena interface para melhor visualização, além de modificar e ajustar os estilos visuais do front-end no arquivo `script.js`. Realizei testes manuais inserindo dados inválidos no terminal para garantir o tratamento de erros e testei exaustivamente a integração de código via Git para solucionar conflitos de mesclagem entre o ambiente local e o GitHub. No processo, aprendi a resolver conflitos complexos de versionamento e a estruturar melhor dados aninhados para buscas rápidas.
