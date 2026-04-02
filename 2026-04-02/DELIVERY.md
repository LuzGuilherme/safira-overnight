# 🌙 Overnight Build — 2026-04-02

## 💀 The Subscription Graveyard

**URL:** https://luzguilherme.github.io/safira-overnight/2026-04-02/

---

## O Que É

Uma calculadora visual que mostra onde o teu dinheiro vai "morrer" em subscriptions. Cada subscription que adicionas aparece como uma lápide num cemitério digital, com estatísticas brutais sobre quanto estás a gastar.

---

## Porquê Isto?

**Problema real identificado:**
- A maioria das pessoas não faz ideia de quanto gasta em subscriptions
- Subscriptions acumulam-se silenciosamente (Netflix aqui, Spotify ali, aquela app que "vou usar")
- O custo anual e a 5/10 anos é assustador quando visualizado

**Porquê agora:**
- Economia incerta → pessoas a rever gastos
- "Subscription fatigue" é tendência crescente
- Ferramenta visual impactante > spreadsheet aborrecida

**Porquê esta abordagem:**
- Metáfora do cemitério = memorável e impactante
- Neo Brutalist = bold, chama atenção, força acção
- Gamificação do "cortar" (recomendações com savings claros)

---

## Features

### 🪦 Graveyard Visual
- Cada subscription = uma lápide
- Ordenadas por custo (mais caras = mais visíveis)
- Barra de usage para cada uma
- R.I.P. + nome + custo mensal/anual

### 📊 Stats em Tempo Real
- Monthly burn rate
- Yearly cost
- 5-Year damage (o número que dói)
- Contagem de subscriptions

### 🔪 Cut Recommendations
- Análise automática por usage vs cost
- Categorias: CUT IT / REVIEW / KEEP
- Savings potenciais por cada corte

### 💀 Brutal Truth Section
- Working hours necessárias para pagar (a $25/h)
- Potential savings de subs low-usage
- 10-year waste projection
- Mensagens personalizadas baseadas nos dados

### ⚡ Quick Add
- Botões para subs populares (Netflix, Spotify, ChatGPT, etc.)
- Adiciona com um clique, só escolhes o usage

### 💾 Persistência
- Guarda em localStorage
- Dados persistem entre sessões

---

## Estilo: Neo Brutalist 🔲

**Justificação:**
- Bordas grossas pretas → impacto visual forte
- Cores primárias (vermelho, amarelo, preto) → urgência
- Layout "quebrado" intencional → anti-polished, raw
- Não usado desde 2026-03-23 (9 dias)

**Características aplicadas:**
- Border: 4px solid black
- Box-shadow: 8px 8px 0 black
- Typography: Inter (bold) + Space Mono
- Cores: #000, #fff, #ff0000, #ffff00
- Hover states óbvios e satisfatórios

---

## Tech Stack

- HTML/CSS/JS puro (zero deps)
- ~900 linhas de código
- LocalStorage para persistência
- Responsive (mobile-friendly)
- Animações CSS puras

---

## Potencial

**Como produto:**
- Landing page gratuita → captura emails
- Premium: sync com bancos, detecção automática
- Affiliate de alternativas (ex: "Cancel Netflix → aqui tens alternativas grátis")

**Como conteúdo:**
- Screenshots shareable ("Look at my graveyard")
- "Annual subscription audit" ritual
- Viral potential pelo visual único

---

## Notas Técnicas

- Testado em Chrome, Firefox, Safari
- Mobile responsive com grid adaptativo
- Zero console errors
- Performance: <50KB total

---

*Built by Safira @ 01:30 UTC while Guilherme sleeps. 💀*
