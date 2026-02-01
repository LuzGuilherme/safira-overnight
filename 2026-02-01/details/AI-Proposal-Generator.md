---
title: AI Proposal Generator
created: 2026-01-30
tags:
  - idea
  - side-hustle
  - ai
  - b2b
  - saas
  - ppc
  - marketing
status: exploring
potential: 8
effort: 4
skills: 9
problem: "Consultores e agências gastam 3-5 horas a criar cada proposta comercial"
solution: "AI que gera propostas profissionais a partir de briefing"
market: "Consultores, Agências de marketing, Freelancers B2B"
---

# AI Proposal Generator

## Problem
Consultores e agências perdem tempo enorme com propostas:

- **3-5 horas** por proposta bem estruturada
- **Copy-paste** de templates antigos
- **Inconsistência** entre propostas
- **Personalização** demora mas é crucial para fechar
- **Win rate** baixo porque propostas são genéricas

> [!note] Fonte
> Mencionado em análise de micro-SaaS trends como "AI-powered proposal generator for consultants - not trying to replace entire workflow, just making one painful task way easier"

> [!tip] BYOK Trend (2026-01-31)
> **Bring Your Own Key** está a crescer como modelo de negócio:
> - Utilizador usa a própria API key (Claude, GPT, Gemini)
> - Não há custos de AI para o SaaS
> - Pricing mais baixo possível
> - Exemplos: Nano-Slides, Git AutoReview
> 
> **Aplicação aqui:** Oferecer tier "BYOK" a $9/mês (só software, user paga AI directamente). Tier managed a $29/mês para quem quer simplicidade.

## Solution
**SaaS que gera propostas profissionais:**

1. **Input simples:**
   - Nome do cliente + sector
   - Problema/necessidade
   - Serviços a propor
   - Budget range (opcional)

2. **Output completo:**
   - Proposta PDF profissional
   - Executive summary
   - Scope detalhado
   - Timeline
   - Pricing breakdown
   - T&Cs standard

3. **Personalização inteligente:**
   - Analisa website do cliente (scraping)
   - Adapta linguagem ao sector
   - Inclui case studies relevantes
   - Customiza design por tipo de serviço

## Porque alinhado com Guilherme
- ✅ **Conhece a dor** — faz propostas PPC
- ✅ **Pode ser primeiro utilizador** — usa no próprio trabalho
- ✅ **Network de agências** — potencial early adopters
- ✅ **Skills de marketing** — sabe promover
- ✅ **MVP rápido** — pode ser simples no início

## Features MVP
1. Template de proposta de marketing/PPC
2. Input: cliente + briefing + serviços
3. Output: Proposta PDF (1 design)
4. Estimativa de tempo/budget automática

## Features Futuras
- Múltiplos templates por indústria
- Integração CRM (HubSpot, Pipedrive)
- Tracking de propostas (abriu, não abriu)
- Follow-up automático
- Analytics de win rate

## Technical Stack
- **Frontend:** Next.js
- **Backend:** Python/FastAPI
- **AI:** Claude API para texto
- **PDF:** WeasyPrint ou similar
- **Scraping:** Para análise de cliente

## Pricing
| Tier | Preço | Propostas/mês |
|------|-------|---------------|
| Starter | $29/mês | 10 propostas |
| Pro | $79/mês | 50 propostas |
| Agency | $199/mês | Unlimited |

## Competition
| Tool | Foco | Gap |
|------|------|-----|
| Proposify | Proposal software | Não gera conteúdo |
| PandaDoc | Docs + e-sign | Genérico |
| Qwilr | Proposals web | Caro, não é AI |
| Better Proposals | Templates | Manual |

**Oportunidade:** Nenhum é verdadeiramente AI-first para geração de conteúdo.

## Validation
- [ ] Criar landing page
- [ ] Partilhar com network de agências
- [ ] 5 entrevistas com consultores
- [ ] MVP funcional em 1 semana

## Challenges
- Qualidade do output (precisa ser realmente bom)
- Diferentes sectores = diferentes templates
- Pricing vs value (quanto vale poupar 3h?)

## Notes
**Prós:**
- MVP simples (pode começar com 1 template)
- Guilherme pode usar/testar pessoalmente
- Mercado claro (consultores/agências)
- $29/mês é impulso buy

**Contras:**
- Competição eventual (fácil de copiar)
- Dependência de qualidade AI
- Pode ser feature de outro produto

---

*Ideia encontrada em análise de trends micro-SaaS — 2026-01-30*
