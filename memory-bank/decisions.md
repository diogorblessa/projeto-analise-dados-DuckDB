# Decisions

Decisões técnicas e de negócio com justificativa. Registre apenas escolhas não triviais e overrides explícitos quando existirem.

## Schema
| id | data | escopo | decisao | motivo | impacto | fonte | status | override_of | aprovacao |
|---|---|---|---|---|---|---|---|---|---|

Status: `proposed`, `accepted`, `rejected`, `superseded`.

`override_of`: use `-` em decisões comuns; preencha com o item do PRD quando houver override explícito.
`aprovacao`: use `-` em decisões comuns; preencha com aprovador ou fonte de aprovação quando `override_of` estiver preenchido.

Decisões comuns documentam interpretação e continuidade operacional. Só um registro `accepted` com `override_of` e `aprovacao` explícitos ajusta o item referenciado do PRD.

## Registros

_vazio — template pré-execução, nenhuma decisão registrada ainda._
