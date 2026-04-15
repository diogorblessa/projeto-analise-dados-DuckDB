# Case TechShop - Analise de Dados com DuckDB

Repositorio do case tecnico da TechShop com foco em diagnostico de qualidade, tratamento, SQL analitico, analise de negocio, auditoria de script legado e modelagem dimensional. O artefato principal e o notebook [notebooks/case_techshop.ipynb](notebooks/case_techshop.ipynb).

## Entregaveis

- `notebooks/case_techshop.ipynb`: entrega principal com Q1 a Q7.
- `README.md`: visao geral, execucao e estrutura.
- `pyproject.toml`: manifesto canonico de dependencias do projeto.
- `uv.lock`: lockfile reproduzivel gerado por `uv`.
- `requirements.txt`: caminho compativel para instalacao com `pip`.
- `sql/q3_*.sql`: queries reproduziveis de Q3.
- `scripts/analise_crescimento.py`: insumo legado auditado em Q5.
- `artifacts/`: figuras e diagramas referenciados na entrega.

## Estrutura

- `data/raw/`: dataset bruto imutavel.
- `data/interim/`: saidas tratadas e artefatos intermediarios reproduziveis.
- `docs/PRD.md`: contrato normativo do projeto.
- `docs/instrucoes_desafio.md`: enunciado original e contexto historico.
- `.claude/`: regras, skills, agentes e configuracao de governanca para trabalho assistido por IA.
- `memory-bank/`: unica continuidade operacional persistente do projeto.
- `state/`: scratch efemero da sessao; nao e fonte de verdade.

## Ambiente e dependencias

O projeto agora usa `uv` como fluxo principal porque ele centraliza o manifesto em `pyproject.toml`, gera `uv.lock` versionado e reduz divergencia entre maquinas. `requirements.txt` continua no repositorio como interface de compatibilidade para quem ainda usa `pip` ou trabalha em ambientes mais restritos.

Importante: `uv` melhora velocidade e reprodutibilidade, mas nao corrige por si so bloqueios de App Control no Windows. Se a maquina bloquear modulos binarios dentro da `.venv`, o fallback operacional continua sendo usar um Python global aprovado e instalar as dependencias com `pip`.

## Execucao padrao com `uv`

1. Instale `uv` se ele ainda nao estiver disponivel no sistema.

   ```bash
   python -m pip install uv
   ```
2. Na raiz do repositorio, sincronize o ambiente:

   ```bash
   uv sync
   ```

3. Valide os imports e o acesso ao dataset:

   ```bash
   uv run python -c "import pandas, numpy, duckdb, matplotlib, seaborn; print('imports ok')"
   uv run python -c "from pathlib import Path; print(Path('data/raw/ecommerce_vendas.csv').exists())"
   ```

4. No VS Code, selecione o interpretador da `.venv` criada por `uv`.
5. Abra `notebooks/case_techshop.ipynb` sem mover o arquivo e use o mesmo interpretador como kernel.
6. Rode `Restart & Run All`.

Os paths do notebook foram escritos relativos a `notebooks/` (`../data/raw/ecommerce_vendas.csv`, `../data/interim`, `../sql`). Execute o notebook pelo Jupyter no VS Code para preservar esse contexto.

## Fallback com `pip` em Windows restrito

Se o Windows bloquear modulos compilados na `.venv` com erro do tipo `Uma politica de Controle de Aplicativo bloqueou este arquivo`, use um Python global aprovado pela maquina:

```bash
python -m pip install -r requirements.txt
python -c "import pandas, numpy, duckdb, matplotlib, seaborn; print('imports ok')"
python -c "from pathlib import Path; print(Path('data/raw/ecommerce_vendas.csv').exists())"
```

Depois, no VS Code, selecione esse interpretador global e use-o tambem como kernel do notebook. O notebook e os paths do projeto nao precisam mudar para esse fallback.

## Governanca

- `docs/PRD.md` e a unica norma humana de escopo, padroes e aceite.
- `CLAUDE.md` e a politica persistente de operacao para IA dentro deste workspace.
- `docs/playbook_subagentes.md` consolida quando usar `@code-reviewer` e `@business-reporter`, com templates curtos de invocacao.
- `memory-bank/active-context.md` e `memory-bank/question-status.md` sao a porta de entrada para retomar sessoes.
- `memory-bank/review-checklist.md` concentra o estado persistente da revisao.
- `README.md` e apenas descritivo; status vivo do trabalho deve existir em `memory-bank/`.

## Referencias

- PRD: [docs/PRD.md](docs/PRD.md)
- Enunciado: [docs/instrucoes_desafio.md](docs/instrucoes_desafio.md)
- Playbook de subagents: [docs/playbook_subagentes.md](docs/playbook_subagentes.md)
- Notebook principal: [notebooks/case_techshop.ipynb](notebooks/case_techshop.ipynb)
- DuckDB: <https://duckdb.org/docs/>
- uv docs: <https://docs.astral.sh/uv/>
