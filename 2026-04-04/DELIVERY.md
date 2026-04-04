# 💀 The Pre-Mortem Machine

**Data:** 2026-04-04  
**Categoria:** Business/Risk Assessment  
**Estilo:** Retro Tech ⚡  
**Tempo de build:** ~1.5 horas

---

## 🎯 O Que É

Uma ferramenta interactiva que aplica a técnica de **Pre-Mortem** (desenvolvida por Gary Klein) para indie hackers e fundadores identificarem riscos ANTES de falharem.

O conceito: "Viaja ao futuro onde o teu projecto falhou. Aprende porquê."

---

## 💡 Porquê Isto?

**Problema real:**
- Fundadores são optimistas por natureza (têm de ser)
- Mas isso cria pontos cegos para riscos óbvios
- A maioria das startups falha por razões previsíveis
- Post-mortems são úteis, mas chegam tarde demais

**A técnica Pre-Mortem:**
- Criada por Gary Klein (psicólogo cognitivo)
- Usado por empresas como Google, Amazon, McKinsey
- Inverte a perspectiva: em vez de "como ter sucesso?", perguntas "como falhámos?"
- Quebra o groupthink e revela riscos que ninguém queria mencionar

**Porque não existe versão interactiva:**
- A maioria das ferramentas de pre-mortem são templates estáticos
- Não há personalização por tipo de projecto
- Zero orientação sobre mitigações

---

## ✨ Features

### Input Personalizado
- Nome do projecto
- Tipo (SaaS, Mobile, API, Marketplace, etc.)
- Timeline de lançamento
- Tamanho da equipa
- Status de funding
- Mercado-alvo

### Análise Inteligente
- Selecciona riscos relevantes baseado nos inputs
- Calcula probabilidade personalizada
- Agrupa por categoria (Market, Tech, Team, Resources, Timing)

### 6 Categorias de Risco
1. **Market** — Problema errado, mercado saturado, timing
2. **Tech** — Technical debt, scaling, security
3. **Team** — Burnout, conflitos, contratações
4. **Resources** — Runway, distribuição, dependências
5. **Timing** — Demasiado cedo/tarde
6. **Execution** — Scope creep, foco

### Output Actionable
- Cenário de falha detalhado (narrativa realista)
- 3-4 estratégias de mitigação por risco
- Risk meter global
- Survival rate estimado
- Export para Markdown

### UX Retro Tech
- Estética terminal/sci-fi
- Scanlines e glow effects
- Animação de "simulação" durante processamento
- Cards expansíveis para detalhes
- Mobile responsive

---

## 🎨 Justificação do Estilo

**Retro Tech ⚡** escolhido porque:
1. O conceito de "viajar ao futuro" combina com sci-fi
2. Visual de terminal/radar para análise de riscos
3. Não foi usado desde 2026-03-20 (variedade)
4. Destaca-se dos últimos builds (Editorial Clean, Neo Brutalist, Data Dense)

**Elementos usados:**
- Cores: Cyan/Pink néon, verde/vermelho para status
- Fonts: Orbitron (títulos), Space Mono (texto)
- Grid background com linhas de scan
- Glow effects e animações
- Bordas sharp (2px)

---

## 📊 Base de Dados de Riscos

**18 cenários de falha únicos** organizados por categoria:

| Categoria | Riscos |
|-----------|--------|
| Market | No Real Problem, Crowded Market, Wrong Audience, Timing Disaster |
| Tech | Technical Debt, Scale Wall, Integration Hell, Security Breach |
| Team | Founder Burnout, Co-Founder Conflict, Hiring Mistakes, Scope Creep |
| Resources | Runway Crash, Distribution Black Hole, Key Person Dependency |
| External | Platform Risk, Regulatory Surprise, Copycat Attack |

Cada risco tem:
- Trigger conditions (tipo, timeline, team, funding, market)
- Cenário narrativo (100-150 palavras)
- 4 mitigações actionable

---

## 🧪 Como Testar

1. Abrir `index.html` no browser
2. Preencher formulário com projecto real ou fictício
3. Ver animação de "simulação"
4. Explorar riscos (clicar para expandir)
5. Exportar report (botão "Copy Report")
6. Testar diferentes combinações de inputs

**Cenários de teste sugeridos:**
- Solo founder, SaaS, bootstrapped, esta semana
- Equipa pequena, marketplace, seed funded, este quarter
- API developer tool, enterprise B2B, série A

---

## 📁 Ficheiros

```
/root/clawd/overnight/2026-04-04/
├── index.html      # Aplicação completa (HTML/CSS/JS)
└── DELIVERY.md     # Este ficheiro
```

---

## 🔗 Links

- **Live:** https://luzguilherme.github.io/safira-overnight/2026-04-04/
- **Inspiração:** [Gary Klein - PreMortem](https://www.gary-klein.com/premortem)

---

## 💭 Notas

Este build foi inspirado pela técnica de pre-mortem, uma das ferramentas de decision-making mais poderosas que existe. A ideia é simples mas contra-intuitiva: assumir que o projecto já falhou e trabalhar de trás para a frente para descobrir porquê.

Para indie hackers que costumam estar sozinhos e não têm uma equipa para fazer devil's advocate, esta ferramenta pode ser o "co-founder pessimista" que faz as perguntas difíceis.

*"The best time to fix a failure is before it happens."*
