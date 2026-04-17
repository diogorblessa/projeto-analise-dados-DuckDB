# DER - Modelo Dimensional (Bloco 7)

Fonte canonica do diagrama dimensional do Bloco 7 em Mermaid ER.

## Fonte editavel (Mermaid)

```mermaid
erDiagram
    dim_tempo ||--o{ fato_item_pedido : sk_tempo
    dim_cliente ||--o{ fato_item_pedido : sk_cliente
    dim_produto ||--o{ fato_item_pedido : sk_produto
    dim_localidade ||--o{ fato_item_pedido : sk_localidade
    dim_status ||--o{ fato_item_pedido : sk_status
    dim_categoria ||--o{ dim_produto : sk_categoria

    fato_item_pedido {
        INT sk_tempo FK
        INT sk_cliente FK
        INT sk_produto FK
        INT sk_localidade FK
        INT sk_status FK
        VARCHAR pedido_id "DD"
        INT qtd "M"
        DECIMAL valor_unit "M"
        DECIMAL desconto_pct "M"
        DECIMAL valor_bruto "D"
        DECIMAL desconto_valor "D"
        DECIMAL receita_liquida "M"
        DECIMAL avaliacao "S"
    }

    dim_tempo {
        INT sk_tempo PK
        DATE data_pedido UK
        INT ano
        INT mes
        INT trimestre
        VARCHAR dia_semana
    }

    dim_cliente {
        INT sk_cliente PK
        VARCHAR cliente_id UK
    }

    dim_produto {
        INT sk_produto PK
        VARCHAR produto UK
        INT sk_categoria FK
    }

    dim_categoria {
        INT sk_categoria PK
        VARCHAR categoria UK
    }

    dim_localidade {
        INT sk_localidade PK
        CHAR uf UK
        VARCHAR regiao
    }

    dim_status {
        INT sk_status PK
        VARCHAR status UK
        VARCHAR grupo_status
    }
```

## Legenda de chaves e metricas

- `PK`: `dim_tempo.sk_tempo`, `dim_cliente.sk_cliente`, `dim_produto.sk_produto`, `dim_categoria.sk_categoria`, `dim_localidade.sk_localidade`, `dim_status.sk_status`
- `FK` na fato: `sk_tempo`, `sk_cliente`, `sk_produto`, `sk_localidade`, `sk_status`
- `FK` hierarquia: `dim_produto.sk_categoria -> dim_categoria.sk_categoria`
- `DD`: `fato_item_pedido.pedido_id`
- `M`: `qtd`, `valor_unit`, `desconto_pct`, `receita_liquida`
- `D`: `valor_bruto`, `desconto_valor`
- `S`: `avaliacao`

SK = surrogate key | NK = natural key | DD = dimensao degenerada
