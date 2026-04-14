# Project Globals

Regras globais do case TechShop. Aplicadas a todo o repositório, independente do caminho tocado.

## Evidência e rastreabilidade
- Nunca invente dados, métricas ou conclusões sem evidência visível no notebook.
- Toda afirmação analítica deve ser rastreável a um output visível.
- Números, percentuais e valores monetários entre crases em markdown.

## Estrutura do notebook
- Padrão de células: `[MD explicacao] -> [CODE] -> [MD analise]`.
- Exceção: Q6 pode ser markdown-only com diagrama.
- Conteúdo final fica no `.ipynb`; scripts `.py` e `.sql` são insumo reproduzível.

## Linguagem e nível
- Português brasileiro para conteúdo, inglês para nomes de arquivo.
- Nível: analista pleno, raciocínio explícito, escolhas fundamentadas, sem jargão desnecessário.

## Dados e SQL
- SQL exclusivamente via DuckDB in-memory; nunca conectar banco externo.
- `data/raw/` é imutável; saídas tratadas vão em `data/interim/`.

## Premissas e clarificação
- Declare a premissa relevante quando ambiguidade de escopo, métrica, fonte ou pergunta puder mudar a resposta.
- Se a ambiguidade alterar o resultado esperado, peça clarificação em vez de escolher silenciosamente.
- Se precisar assumir algo para avançar, torne a premissa explícita e mantenha a decisão reversível.
- Se houver caminho mais simples e igualmente aderente ao PRD, sinalize antes de expandir a solução.

## Simplicidade e escopo cirúrgico
- Prefira o menor conjunto de mudanças que responda à questão pedida com rastreabilidade.
- Notebook e SQL devem permanecer explícitos e auditáveis; helper local só é aceitável com repetição real e ganho claro.
- Não introduza parametrização, utilitário transversal, framework ou camada genérica sem necessidade comprovada.
- Prefira etapas claras e legíveis a compactação, "esperteza" ou flexibilidade especulativa.
- Toque apenas arquivos, células e trechos necessários para a tarefa atual.
- Não reescreva comentário, formatação, narrativa ou código adjacente apenas para "melhorar" o contexto.
- Remova somente imports, variáveis, passos ou arquivos que a sua própria mudança tornou órfãos.
- Se notar problema não relacionado, registre ou mencione; não corrija silenciosamente no mesmo movimento.

## Execução orientada a verificação
- Em tarefa não trivial, explicite `objetivo`, `artefato esperado` e `como verificar`.
- Verifique com sinal concreto: output visível, resultado SQL, checklist, diff ou outro artefato auditável.
- Se a verificação não puder ser concluída, diga o que faltou e qual risco permanece.
- Prefira ciclos curtos de implementar, verificar e reportar a mudanças abertas sem critério de conclusão.
