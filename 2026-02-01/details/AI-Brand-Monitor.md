---
title: AI Brand Monitor
created: 2026-01-31
tags:
  - idea
  - side-hustle
  - ai
  - b2b
  - saas
  - marketing
status: exploring
potential: 9
effort: 6
skills: 8
problem: "Marcas não sabem como aparecem nas respostas de ChatGPT, Perplexity, Claude"
solution: "Dashboard que monitoriza menções da marca em AI responses"
market: "Empresas, Agências de marketing, Brand managers"
---

# AI Brand Monitor

## Problem
Com AI a substituir Google para muitas pesquisas, marcas têm um novo problema:

- **Não sabem** como aparecem nas respostas de ChatGPT/Perplexity/Claude
- **Não conseguem medir** visibilidade em AI vs competidores
- **Não têm alertas** quando AI diz algo errado sobre eles
- **SEO tradicional** não funciona para optimizar para AI

> [!note] Validação
> Startup "Mentions" fez **$0 → $62k MRR em 3 meses** com produto similar.
> Target para 2026: $100k MRR.
> Fonte: Indie Hackers (Janeiro 2026)

## Solution
**SaaS que monitoriza presença da marca em AI:**

1. **Tracking contínuo:**
   - Queries relevantes ao negócio
   - Comparação com competidores
   - Histórico de mudanças

2. **Dashboard:**
   - Score de visibilidade AI
   - Sentiment das respostas
   - Comparação temporal

3. **Alertas:**
   - Quando AI diz algo incorrecto
   - Quando competidor ganha visibilidade
   - Mudanças significativas

4. **Insights:**
   - Como melhorar presença em AI
   - Que conteúdo criar para ser citado
   - Gaps vs competidores

## Porque alinhado com Guilherme
- ✅ **Marketing adjacent** — não é PPC mas é da área
- ✅ **B2B SaaS** — receita recorrente
- ✅ **Timing perfeito** — mercado emergente, pouca competição
- ✅ **Skills relevantes** — entende de marcas e visibilidade
- ✅ **Validado** — já há startup com $62k MRR

## MVP Features
1. Input: nome da marca + 5 queries relevantes
2. Scrape respostas de ChatGPT/Perplexity (1x por dia)
3. Dashboard simples com score e menções
4. Alerta por email se mudança >20%

## Technical Stack
- **Frontend:** Next.js
- **Backend:** Python/FastAPI
- **Scraping:** Playwright para AI interfaces
- **DB:** Supabase
- **Alertas:** Resend/email

## Pricing
| Tier | Preço | Queries | Competidores |
|------|-------|---------|--------------|
| Starter | $49/mês | 10 queries | 2 |
| Pro | $149/mês | 50 queries | 5 |
| Agency | $399/mês | Unlimited | 20 |

## Competition
| Tool | Status | Gap |
|------|--------|-----|
| Mentions.ai | $62k MRR | Líder atual |
| Peec.ai | Early | Menos features |
| Manual | Comum | Não escala |

**Oportunidade:** Mercado novo, só 2-3 players, muito espaço.

## Challenges
- Scraping de AI interfaces pode mudar
- Rate limits das plataformas AI
- Definir "visibilidade" de forma consistente

## Next Steps
- [ ] Validar interesse com 5 empresas/agências
- [ ] MVP manual (scrape + spreadsheet)
- [ ] Landing page para waitlist

---

*Ideia encontrada em pesquisa Indie Hackers — 2026-01-31*
*Alta prioridade pelo timing e validação de mercado*
