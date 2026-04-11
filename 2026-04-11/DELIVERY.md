# 🌙 Overnight Build — 2026-04-11

## Projecto
**Complexity Guard — Technical Debt Radar**

## O que é
Uma ferramenta local (single-page app) para equipas técnicas avaliarem rapidamente risco de dívida técnica com base em métricas simples:
- code churn
- complexidade ciclomática
- cobertura em falta
- duplicação
- lead time
- regressões por mês

Gera automaticamente:
1. **Health Score (0-100)**
2. **Nível de risco** (Healthy / Attention / High Risk)
3. **3 KPIs** (Complexity Pressure, Shipping Risk, Refactor Priority)
4. **Plano de sprint accionável**
5. **Ranking de hotspots para refactor**

## Pesquisa usada (Fase 1)
- **Hacker News / Show HN:** vários projectos de tooling para developers
- **Product Hunt feed:** destaque para “Complexity Indicator”
- **Reddit (r/SideProject, r/indiehackers):** bloqueado por network security neste ambiente

## Estilo escolhido
**Industrial Dark 🌙**

### Justificação
- Público-alvo: developers / tech leads
- Contexto de uso: dashboards/ferramentas técnicas
- Prioridade: legibilidade de métricas e sensação “ops/devtool”
- Encaixa no STYLE_LIBRARY para ferramentas técnicas e análise

## Não-duplicação
Não repete directamente projectos recentes:
- não é priorização de features (LadderRank)
- não é scanner de segurança (Trust Gap Scanner)
- não é triagem de incidentes (Incident Triage Board)

É uma ferramenta nova focada em **qualidade de código + dívida técnica**.

## Ficheiros
- `/root/clawd/overnight/2026-04-11/index.html`
- `/root/clawd/overnight/2026-04-11/DELIVERY.md`

## Resultado
Pronto para abrir em browser via:
`https://luzguilherme.github.io/safira-overnight/2026-04-11/`
