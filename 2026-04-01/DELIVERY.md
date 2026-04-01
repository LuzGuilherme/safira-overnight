# 🌙 Overnight Build — 2026-04-01

## Projecto
**Search Intent Match Lab** 🔎

Ferramenta para comparar rapidamente várias headlines/descriptions contra uma query-alvo com scoring **BM25-lite** (aproximação prática) + cobertura de intenção.

**Path:** `/root/clawd/overnight/2026-04-01/index.html`
**URL:** https://luzguilherme.github.io/safira-overnight/2026-04-01/

---

## O que construí

- Input de **query alvo**
- Lista de **textos candidatos** (1 por linha)
- Scoring por texto (0-100) baseado em:
  - frequência de termos relevantes
  - normalização por tamanho de texto
  - penalização de ruído
- Tabela de ranking com:
  - score
  - termos da query encontrados
  - status (Excelente / Médio / Fraco)
- KPIs rápidos:
  - média de score
  - cobertura de termos
  - top match
- Recomendações automáticas para reescrita
- Dataset de exemplo alternativo para testar em 1 clique

---

## Pesquisa (fase 1)

### Hacker News
Consegui recolher tendências do HN (Show HN + tooling dev):
- BM25 relevance search em Postgres
- temas de quality/security em coding tools

### Reddit + Product Hunt
Tentei acesso directo e via fetch mirror, mas estavam bloqueados por anti-bot (403/verification) neste ambiente nocturno.

---

## Escolha (fase 2)

- Evitei duplicados após revisão de `overnight/PROJECTS_DONE.md`
- Não existia ferramenta focada em **intent/relevance scoring de copy**
- Escopo viável em 1-2h e utilidade directa para validação rápida de mensagens/landing copy

### Estilo escolhido: **Data Dense** 📊
**Porquê:**
- Ferramenta de análise com foco em decisão rápida
- Prioriza legibilidade de métricas e comparações
- Alinha com uso de power-user (testar variações em loop)

---

## Testes (fase 3)

Testado localmente com múltiplos cenários:
- Query curta e longa
- 1, 3 e 5+ variações de texto
- Casos com cobertura baixa e alta
- Verificação de ordenação por score
- Verificação de recomendações dinâmicas

Resultado: sem erros JS, ranking e métricas consistentes.

---

## Entrega (fase 4)

- Pasta criada: `overnight/2026-04-01/`
- `DELIVERY.md` criado
- Próximo passo: actualizar `PROJECTS_DONE.md`, `overnight/index.html`, commit e push

---

## Porquê isto?

Porque transforma uma dúvida comum (“qual copy está mais alinhada com a intenção de pesquisa?”) num teste objectivo em segundos.
É simples, rápido, e pode ser usado antes de investir tempo em anúncios, SEO, ou páginas novas.