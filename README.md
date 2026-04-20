# Case TechShop - Análise de Dados com DuckDB e ferramentas de IA

## 📋 Sobre

A TechShop é um e-commerce de eletrônicos e periféricos que cresceu de 3 para 13 estados atendidos em dois anos, com registros migrados de dois sistemas legados e histórico parcialmente preenchido por fornecedor externo. Este repositório contém a análise end-to-end solicitada: diagnóstico de qualidade, tratamento, SQL analítico em DuckDB, análise de negócio para expansão regional, auditoria de script legado, modelagem dimensional e insight livre. O artefato principal é `notebooks/case_techshop.ipynb`, com todas as 7 questões respondidas e auditadas.

---

## 📚 Síntese do projeto

### Questões respondidas

| Questão | Tema 
|---|---|
| Q1 | Diagnóstico de qualidade de dados 
| Q2 | Tratamento e limpeza
| Q3 | SQL analítico (4 queries DuckDB in-memory)
| Q4 | Análise de negócio: expansão para a região Sul
| Q5 | Debug de script legado
| Q6 | Modelagem dimensional (esquema estrela) 
| Q7 | Insight livre: correlação desconto x receita

### Principais descobertas (Questões 1 - 7)

**Q1/Q2 - Qualidade de dados:** `12` achados catalogados (DI-001 a DI-012), incluindo `25` registros sem `cliente_id`, `10` linhas duplicadas, `5` registros com `qtd <= 0`, `6` produtos com `valor_unit` com razão exata de `10x` entre si (erro de cadastro por deslocamento de vírgula decimal), `20` datas em formato não padrão e `8` registros com status com capitalização inconsistente. Todos os achados foram tratados com decisão justificada e registrada em `memory-bank/decisions.md`. O dataset tratado tem `1.183 linhas × 13 colunas` (`data/interim/ecommerce_tratado.csv`).

**Q3 - SQL:** 4 queries DuckDB in-memory sobre o dataset tratado, cada uma com arquivo `.sql` reproduzível. Achados:
- a) três monitores e duas impressoras formam o top 5 de receita líquida nos últimos 90 dias; a receita é puxada por ticket médio alto, não por volume;
- b) `Periféricos` tem a maior taxa de cancelamento/devolução e `59` pedidos não concluídos no ano (maior volume absoluto), enquanto `Monitores` combina liderança de receita com segunda maior taxa (`20,88%`). O cruzamento expõe o principal risco operacional da base;
- c) `42` dos `200` clientes identificados qualificam como recorrentes com `3+` meses consecutivos de compra (`21,0%`); o cliente de maior receita no grupo (`C108`) tem ticket médio de `R$ 1.519,18/pedido` com apenas `7` pedidos. Recorrência moderada de ticket alto supera recorrência frequente de ticket baixo;
- d) SC lidera ticket médio por UF (`R$ 1.134,71`) com volume moderado (`59` pedidos entregues), enquanto SP concentra `28,3%` do volume total mas ocupa o `6º` lugar em ticket (`R$ 758,95`).

**Q4 - Negócio:** Recomendação `prosseguir com ressalvas` para expansão na região Sul. O achado dominante é a heterogeneidade interna entre estados: SC lidera com ticket médio de `R$ 1.122,54`, seguido de PR com `R$ 729,15` e RS com `R$ 582,92`, amplitude de `1,93×`. Uma campanha única Sul-agregado sacrificaria margem em SC sem resolver RS. O Sul apresenta desempenho comparável ao restante do país em cancelamento (`17,60%` vs `18,74%`) e avaliação (`3,87` vs `3,93`). A análise foi elaborada com `5` KPIs e `6` limitações explicitadas; base de `250` pedidos no período é pequena para mensurar efeito de campanha.

**Q5 - Debug:** Dois erros graves identificados no script legado `scripts/analise_crescimento.py`: (1) status inválidos com capitalização errada (`"Entregue"`, `"Devolvido"`) inflam a receita calculada, pois nenhum pedido é filtrado corretamente; (2) o cálculo de crescimento YoY usa como base o primeiro mês de cada categoria individualmente (base móvel), tornando a comparação entre categorias impossível e os percentuais exibidos à diretoria sem sentido.

**Q6 - Modelagem:** Esquema estrela com `1` tabela fato (`fato_pedidos`) e `5` dimensões: `dim_tempo`, `dim_cliente`, `dim_localidade`, `dim_produto` e `dim_status`. A escolha do modelo estrela em vez do snowflake se justifica pela estrutura do dataset: o raw é flat, cada linha representa um pedido com um único produto, sem relacionamentos multi-produto que exigissem normalização adicional. `categoria` já convive com `produto` na mesma entidade lógica; criar uma dimensão separada para ela (como exige o snowflake) adicionaria um join sem simplificar nenhuma análise relevante para este case. O resultado é um modelo com o menor número possível de joins para as consultas analíticas esperadas: receita por categoria, por UF, por mês e por status. Diagrama SVG disponível em `artifacts/diagrams/`.

**Q7 - Insight:** Correlação de Spearman entre `desconto_pct` e receita por cliente resulta em `ρ=+0,009`, correlação praticamente nula. A hipótese "desconto se paga em volume" não encontra suporte nos dados de 2024. Clientes sem desconto registram receita média de `R$ 697,86`; com desconto de `11%` a `20%`, de `R$ 798,41`. A diferença existe mas não segue padrão monotônico com o percentual de desconto.

---

## 📁 Estrutura do Projeto

```
projeto-analise-dados-DuckDB/
│
├── notebooks/
│   └── case_techshop.ipynb        # Entrega principal: Q1 a Q7
│
├── data/
│   ├── raw/
│   │   └── ecommerce_vendas.csv   # Dataset bruto, imutável
│   └── interim/
│       └── ecommerce_tratado.csv  # Dataset tratado (saída de Q2): 1.183 × 13
│
├── sql/
│   ├── q3_a_top5_receita.sql      # Top 5 produtos por receita líquida (90 dias)
│   ├── q3_b_taxas_categoria.sql   # Cancelamento/devolução por categoria
│   ├── q3_c_clientes_recorrentes.sql  # Clientes com 3+ meses consecutivos
│   └── q3_d_ticket_uf.sql         # Ticket médio por UF (entregues)
│
├── scripts/
│   └── analise_crescimento.py     # Script legado auditado em Q5
│
├── artifacts/
│   ├── diagrams/
│   │   ├── DER_MODELO_DIMENSIONAL_BLOCO_7.svg  # Diagrama do esquema estrela
│   │   └── DER_MODELO_DIMENSIONAL_BLOCO_7.md   # Documentação textual do modelo
│   ├── figures/
│   │   └── imagem_grafico_receita_tota_por_categoria_crescimento_YoY.jpg  # Gráfico auditado Q5
│   └── q7_desconto_receita.png    # Gráfico dispersão desconto x receita
│
├── docs/
│   ├── PRD.md                     # Fonte normativa: escopo, padrões e aceite
│   ├── instrucoes_desafio.md      # Enunciado original do case
│
├── memory-bank/
│   ├── active-context.md          # Foco atual e ponteiros de continuidade
│   ├── question-status.md         # Status de Q1 a Q7
│   ├── decisions.md               # 10 decisões técnicas e de negócio documentadas
│   ├── data-issues.md             # Catálogo de 12 achados de qualidade (DI-001..DI-012)
│   ├── handoff.md                 # Histórico de encerramento por questão
│   └── review-checklist.md        # Checklist persistente de aceite (61 critérios)
│
├── .claude/
│   ├── agents/                    # business-reporter.md, code-reviewer.md
│   ├── commands/                  # comandos rápidos para ações que se repetem
│   ├── rules/                     # regras e boas práticas para o desenvolvimento do projeto
│   ├── skills/                    # skills necessárias para o desenvolvimento do projeto
│   └── settings.json              # Permissões e hooks versionados
│
├── CLAUDE.md                      # Política persistente de operação para IA neste workspace
├── pyproject.toml                 # Manifesto canônico de dependências
├── uv.lock                        # Lockfile reproduzível
└── requirements.txt               # Interface de compatibilidade para pip
```

---

## 🏗️ Arquitetura do Projeto

O projeto é organizado em quatro camadas:

**Dados**
- `data/raw/` recebe o CSV exportado do sistema legado e permanece imutável durante toda a análise.
- `data/interim/` guarda o dataset tratado gerado em Q2, que é o insumo único de Q3 a Q7.

**Análise**
- `notebooks/case_techshop.ipynb` é o artefato central: cada questão segue a sequência `[MD explicação] -> [CODE] -> [MD análise]`, garantindo que toda afirmação seja rastreável ao output imediatamente anterior.
- `sql/q3_*.sql` armazena as `4` queries de Q3 como arquivos reproduzíveis. O notebook as carrega e executa via DuckDB in-memory; não há banco de dados externo.
- `scripts/analise_crescimento.py` é o insumo legado auditado em Q5. Ele não é executado na análise; é examinado como artefato.

**Artefatos**
- `artifacts/diagrams/` contém o diagrama SVG do modelo dimensional (Q6) e sua documentação textual.
- `artifacts/figures/` e `artifacts/q7_desconto_receita.png` registram os gráficos gerados e referenciados nas análises.

**Documentação normativa**
- `docs/PRD.md` define escopo, padrões e critérios de aceite. Prevalece sobre qualquer outro arquivo em caso de divergência.
- `memory-bank/` é a fonte de verdade operacional persistente: registra decisões, achados de qualidade, status por questão e histórico da revisão formal. Não é documentação descritiva; é o rastreio vivo do projeto.
- `CLAUDE.md` define as políticas de operação para sessões assistidas por IA.

---

## 🤖 Operação com o Claude Code

Este projeto foi desenvolvido com assistência do Claude Code (Anthropic). Esta seção responde às três perguntas que o avaliador verificará em devolutiva.

### Como a IA foi usada

O Claude Code atuou em três papéis complementares, definidos em `.claude/agents/`:

- `@business-reporter`: tradução de achados técnicos em linguagem de negócio, sínteses executivas e recomendações rastreáveis (usado em Q1, Q4 e Q7).
- `@code-reviewer`: revisão ad hoc de células `[CODE]` e queries SQL, com foco em achados acionáveis, sem substituir o fluxo formal de revisão.
- Skills canônicos em `.claude/skills/`: cada questão tem um skill dedicado (`diagnosticar`, `tratar`, `consultar-sql`, `analisar-negocio`, `encontrar-erro`, `modelar-dimensional`, `insight-livre`) com critérios de aceite explícitos do PRD. Os skills `revisar-questao` e `revisao-final` conduzem a auditoria formal.

A IA não definiu a estrutura do projeto nem tomou decisões sem registro. Toda escolha não trivial foi documentada em `memory-bank/decisions.md` com motivo, impacto e fonte rastreável.

### Como os resultados foram validados

A validação seguiu três camadas:

1. **Rastreabilidade célula a célula:** cada afirmação no `[MD análise]` precisa de output visível na célula `[CODE]` imediatamente anterior. Achados sem evidência visível foram registrados como `open findings` e corrigidos antes do fechamento da questão.

2. **Auditoria formal por questão:** o skill `/revisar-questao` audita cada bloco contra os critérios do PRD e registra achados em `memory-bank/review-checklist.md`. Somente após auditoria sem achados abertos a questão avança para `done`.

3. **Auditoria global:** `/revisao-final all --auditar` e `--corrigir` foram executados ao final, cobrindo `31` células do notebook e `61` critérios de aceite. O resultado geral é PASS, com `1` ressalva ambiental aberta (RF-004: `Restart & Run All` não revalidado após Q7 por limitação do ambiente Windows; o `nbconvert --execute` histórico foi bloqueado por `PermissionError WinError 5`).

Números de Q4 foram cross-checados diretamente contra `data/interim/ecommerce_tratado.csv`. Números de Q7 foram verificados contra o output visível da célula antes de serem aceitos na narrativa. Os `2` erros de Q5 foram identificados por leitura do código legado e confirmados por execução controlada.

### Por que essa arquitetura foi adotada

O projeto opera com um conjunto de problemas recorrentes em análise assistida por IA: (1) a IA pode gerar afirmações plausíveis mas sem suporte nos dados; (2) sessões longas perdem contexto entre conversas; (3) sem separação clara de papéis, a IA tende a expandir escopo silenciosamente.

A arquitetura responde a cada problema:

- `memory-bank/` resolve a continuidade entre sessões: `active-context.md` e `question-status.md` são lidos no início de cada sessão; `handoff.md` registra o estado ao encerrar. Não há dependência de memória implícita.
- A separação `[MD explicação] -> [CODE] -> [MD análise]` impede que a narrativa extrapole o output: a regra de rastreabilidade é estrutural, não opcional.
- Skills com critérios de aceite do PRD limitam o escopo de cada fluxo: a IA sabe exatamente o que precisa entregar e o que não é seu papel.
- `decisions.md` com campos `override_of` e `aprovacao` garante que nenhuma decisão da IA redefina silenciosamente o contrato normativo do projeto.

### `.claude/`

Contém a configuração completa de governança para trabalho assistido por IA:

- `rules/`: regras persistentes aplicadas a todo o repositório (`project-globals.md`, `analysis-writing.md`) e regras escopadas por caminho (`code-style.md`, `sql-conventions.md`, `visualization.md`, `notebook-base.md`).
- `skills/`: workflows canônicos por questão, cada um com `SKILL.md` (passos) e `reference.md` (critérios detalhados de aceite do PRD).
- `agents/`: agentes de apoio especializados em saída ou revisão ad hoc. Não substituem skills; complementam com síntese executiva e revisão de código.
- `commands/`: slash-commands de navegação rápida para abertura e encerramento de sessão.
- `settings.json`: permissões e hooks versionados, auditáveis como qualquer outro arquivo do projeto.

### `memory-bank/`

Fonte de verdade operacional persistente. Cada arquivo tem papel específico:

- `active-context.md`: ponto de entrada por sessão; foco atual, skill ativo e próximo marco.
- `question-status.md`: status de Q1 a Q7 (`not_started`, `in_progress`, `review`, `done`).
- `decisions.md`: `10` decisões documentadas (DT-001 a DT-008, Q4-001, Q4-002) com motivo, impacto e fonte.
- `data-issues.md`: catálogo dos `12` achados de qualidade (DI-001 a DI-012) com evidência e tratamento aplicado.
- `review-checklist.md`: `61` critérios de aceite com estado PASS/FAIL e histórico de achados aplicados ou encerrados.
- `handoff.md`: histórico de encerramento por questão; permite retomar qualquer sessão sem dependência de memória implícita.

---

## 🛠️ Tecnologias e Ferramentas

| Tecnologia | Versão mínima | Propósito no projeto |
|---|---|---|
| Python | `≥ 3.11` | Linguagem principal do notebook e dos scripts |
| DuckDB | `≥ 1.0` | Motor SQL in-memory para as 4 queries de Q3 e consultas analíticas |
| pandas | `≥ 2.0` | Leitura, tratamento e manipulação do dataset |
| NumPy | `≥ 1.24` | Cálculo de correlação de Spearman (Q7) e operações numéricas |
| Matplotlib | `≥ 3.7` | Geração dos gráficos de Q5 e Q7 |
| Seaborn | `≥ 0.13` | Visualização do gráfico de dispersão de Q7 |
| Jupyter | `≥ 1.0` | Ambiente de execução do notebook |
| ipykernel | `≥ 6.25` | Kernel Python para o Jupyter no VS Code |
| uv | - | Gerenciamento de ambiente e dependências; gera `uv.lock` reproduzível |
| Claude Code | - | Assistência em análise, revisão e síntese executiva; governança via `.claude/` |

---

## 🚀 Como Usar

### Instalação

**Fluxo principal com `uv`:**

1. Instale `uv` se ainda não estiver disponível:

   ```bash
   python -m pip install uv
   ```

2. Na raiz do repositório, sincronize o ambiente:

   ```bash
   uv sync
   ```

3. Valide os imports e o acesso ao dataset:

   ```bash
   uv run python -c "import pandas, numpy, duckdb, matplotlib, seaborn; print('imports ok')"
   uv run python -c "from pathlib import Path; print(Path('data/raw/ecommerce_vendas.csv').exists())"
   ```

### Execução

1. No VS Code, selecione o interpretador da `.venv` criada por `uv`.
2. Abra `notebooks/case_techshop.ipynb` sem mover o arquivo de posição.
3. Use o mesmo interpretador como kernel do notebook.
4. Execute `Restart & Run All`.

Os paths do notebook são relativos ao diretório `notebooks/` (`../data/raw/ecommerce_vendas.csv`, `../data/interim`, `../sql`). Execute pelo Jupyter no VS Code para preservar esse contexto.

**Fallback com `pip` em Windows com App Control:**

Se o Windows bloquear módulos compilados dentro da `.venv` com erro do tipo `Uma política de Controle de Aplicativo bloqueou este arquivo`, use um Python global aprovado pela máquina:

```bash
python -m pip install -r requirements.txt
python -c "import pandas, numpy, duckdb, matplotlib, seaborn; print('imports ok')"
python -c "from pathlib import Path; print(Path('data/raw/ecommerce_vendas.csv').exists())"
```

Depois, no VS Code, selecione esse interpretador global e use-o como kernel do notebook. Os paths do projeto não precisam mudar para esse fallback.

---

