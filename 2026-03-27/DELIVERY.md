# 🔢 MRR Reverse Engineer

**Data:** 27 Março 2026  
**Estilo:** Data Dense 📊  
**Categoria:** Business/Calculadoras  
**Streak:** 55 noites! 🔥

---

## 💡 Porquê Isto?

A maioria dos founders pensa "para a frente": tenho X visitantes, converto Y%, ganho Z. Mas quando defines um **objectivo de MRR**, precisas de pensar **ao contrário**.

**O problema que resolve:**
- "Quero chegar a $10K MRR, mas quanto tráfego preciso?"
- "Vale mais melhorar conversão ou reduzir churn?"
- "Quanto tempo vai demorar realisticamente?"

**Inspiração:**
- Artigo Indie Hackers: "$0 to $62k MRR in three months"
- DEV.to: "How to Actually Hit $10K MRR in 2026"
- Discussões sobre realistic timelines vs hype

---

## 🎯 O Que Faz

### Inputs
- Target MRR ($)
- ARPU (preço médio)
- Visitor → Trial rate
- Trial → Paid rate
- Monthly churn
- Current MRR (opcional)
- Current visitors (opcional)

### Outputs

**Primary Metrics:**
- Customers needed (com colour coding)
- Monthly visitors required
- Effective conversion rate
- Monthly churn loss ($)
- Time to goal
- Customer LTV

**Formula Breakdown:**
- Mostra toda a matemática transparentemente
- Passo a passo de como os números se calculam

**Funnel Requirements:**
- Tabela com visitors → trials → customers
- "To reach goal" vs "Monthly to maintain"

**Sensitivity Analysis:**
- O que acontece se melhorares cada métrica 10%
- Highlight na que tem mais impacto

**Timeline Scenarios:**
- Se tiveres 1K, 5K, 10K, 25K, 50K visitors/mês
- Quanto tempo demora em cada cenário
- Tags de dificuldade (EASY/MEDIUM/HARD)

**Bottleneck Detection:**
- Identifica automaticamente o maior problema
- Dá sugestões específicas para resolver

**Monthly Milestones:**
- Projecção mês a mês até ao objectivo
- Mostra churned vs added customers

---

## 🎨 Estilo: Data Dense

**Porquê este estilo:**
- Ferramenta de análise = muitos números
- Founders querem ver os dados, não decoração
- Transparência nos cálculos gera confiança
- Estética de terminal/Bloomberg

**Características aplicadas:**
- Monospace font para números
- Tabelas densas com borders
- Colour coding funcional (verde/amarelo/vermelho)
- Muito pouco whitespace
- Zero elementos decorativos
- Headers uppercase, small

**Referências:**
- Bloomberg Terminal
- Grafana dashboards
- Financial spreadsheets

---

## 🔧 Detalhes Técnicos

- **Zero dependências** - vanilla JS
- **Presets** - $1K, $5K, $10K, $50K goals
- **Responsive** - funciona em mobile
- **Real-time** - recalcula em cada input

**Fórmulas implementadas:**
```
customers_needed = target_mrr / arpu
monthly_churn_loss = customers_needed × churn_rate
trials_needed = monthly_churn_loss / trial_to_paid_rate
visitors_needed = trials_needed / visitor_to_trial_rate
ltv = arpu / churn_rate
time_to_goal = customers_to_add / net_monthly_growth
```

---

## 📁 Ficheiros

```
overnight/2026-03-27/
├── index.html       # Aplicação completa
└── DELIVERY.md      # Este ficheiro
```

---

## 🚀 Como Usar

1. Define o teu objectivo de MRR
2. Input das tuas taxas actuais (ou usa presets)
3. Vê exactamente o que precisas
4. Identifica o teu bottleneck
5. Testa melhorias com sensitivity analysis

---

## 💭 Notas

Esta ferramenta força a **honestidade** sobre timelines. Muitos founders sonham com $10K MRR mas não fazem as contas do que isso realmente implica em termos de tráfego e conversões.

A sensitivity analysis é particularmente útil: às vezes melhorar 10% no trial-to-paid tem mais impacto que duplicar tráfego.

**Próximos passos possíveis:**
- Exportar análise como PDF
- Comparar múltiplos cenários side-by-side
- Integrar com Stripe para dados reais
- Add LTV/CAC analysis
