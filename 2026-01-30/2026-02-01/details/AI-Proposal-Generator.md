# AI Proposal Generator

## 🎯 Problema
Consultores e agências perdem tempo enorme a criar propostas comerciais.

**Dores específicas:**
- 3-5 horas por proposta bem estruturada
- Copy-paste de templates antigos
- Inconsistência entre propostas
- Personalização demora mas é crucial para fechar
- Win rate baixo porque propostas são genéricas

> **Fonte:** Análise de micro-SaaS trends — "AI-powered proposal generator for consultants - not trying to replace entire workflow, just making one painful task way easier"

## 📈 Trends Relevantes
**BYOK (Bring Your Own Key)** está a crescer como modelo de negócio:
- Utilizador usa a própria API key (Claude, GPT, Gemini)
- Não há custos de AI para o SaaS
- Pricing mais baixo possível
- Exemplos: Nano-Slides, Git AutoReview

**Aplicação aqui:** Tier "BYOK" a $9/mês (só software). Tier managed a $29/mês para quem quer simplicidade.

## 💡 Solução

**Input:**
- Nome do cliente + sector
- Problema/necessidade
- Serviços a propor
- Budget range (opcional)

**Output:**
- Proposta PDF profissional
- Executive summary
- Scope detalhado
- Timeline
- Pricing breakdown
- T&Cs standard

**Diferencial:**
- Analisa website do cliente (scraping)
- Adapta linguagem ao sector
- Inclui case studies relevantes
- Customiza design por tipo de serviço

## 📊 Scores
| Dimensão | Score | Justificação |
|----------|-------|--------------|
| Market   | 6/10  | Competição existe mas nenhum é AI-first |
| Demand   | 8/10  | Dor real, consultores pagam por produtividade |
| Effort   | 8/10  | MVP simples (1 template), 1-2 semanas |
| Skills   | 9/10  | Guilherme faz propostas PPC, conhece a dor |
| Revenue  | 8/10  | SaaS subscription claro, BYOK reduz custos |
| Interest | 7/10  | Útil e aplicável ao próprio trabalho |

**Score Final: 7.75 — BUILD IT 🟢**

## 🏢 Competidores
| Tool | Foco | Gap |
|------|------|-----|
| Proposify | Proposal software | Não gera conteúdo |
| PandaDoc | Docs + e-sign | Genérico, não AI |
| Qwilr | Proposals web | Caro, não é AI |
| Better Proposals | Templates | Manual, sem AI |

**Oportunidade:** Nenhum é verdadeiramente AI-first para geração de conteúdo.

## 👤 Target Market
- **Consultores independentes** — $29-79/mês, precisam parecer profissionais
- **Agências de marketing** — $79-199/mês, volume alto de propostas
- **Freelancers B2B** — $29/mês, impulse buy

## 💰 Monetização
| Tier | Preço | Inclui |
|------|-------|--------|
| BYOK | $9/mês | Software only, user paga AI |
| Starter | $29/mês | 10 propostas/mês |
| Pro | $79/mês | 50 propostas/mês |
| Agency | $199/mês | Unlimited |

## 🛠️ Tech Stack
- **Frontend:** Next.js
- **Backend:** Python/FastAPI
- **AI:** Claude API para texto
- **PDF:** WeasyPrint ou similar
- **Outros:** Scraping para análise de cliente

## 🎯 Features MVP
- [ ] Template de proposta de marketing/PPC
- [ ] Input: cliente + briefing + serviços
- [ ] Output: Proposta PDF (1 design)
- [ ] Estimativa de tempo/budget automática

## 🚀 Features Futuras
- Múltiplos templates por indústria
- Integração CRM (HubSpot, Pipedrive)
- Tracking de propostas (abriu, não abriu)
- Follow-up automático
- Analytics de win rate

## ✅ Validação
1. [ ] Criar landing page simples
2. [ ] Partilhar com network de agências
3. [ ] 5 entrevistas com consultores
4. [ ] MVP funcional em 1 semana

## 🔗 Sinergia Contigo
- ✅ **Conhece a dor** — faz propostas PPC no trabalho
- ✅ **Primeiro utilizador** — pode testar no próprio trabalho
- ✅ **Network de agências** — potencial early adopters
- ✅ **Skills de marketing** — sabe promover
- ✅ **MVP rápido** — pode começar simples

## ⚠️ Challenges
- Qualidade do output (precisa ser realmente bom)
- Diferentes sectores = diferentes templates
- Pricing vs value (quanto vale poupar 3h?)

## 📝 Notas

**Prós:**
- MVP simples (pode começar com 1 template)
- Pode usar/testar pessoalmente
- Mercado claro (consultores/agências)
- $29/mês é impulse buy

**Contras:**
- Competição eventual (fácil de copiar)
- Dependência de qualidade AI
- Pode ser feature de outro produto

---
*Fonte: r/microsaas trends + análise pessoal — 2026-01-30*
