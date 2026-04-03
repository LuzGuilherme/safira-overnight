# 🌙 Overnight Build — 2026-04-03

## 🧠 The Pricing Psychology Lab

**URL:** https://luzguilherme.github.io/safira-overnight/2026-04-03/

---

## O Que É

Um laboratório interactivo que demonstra, em tempo real, os principais princípios de psicologia de pricing usados por SaaS e e-commerce.

Não é só conteúdo estático: o utilizador mexe nos preços e vê imediatamente como muda a percepção.

---

## Pesquisa Rápida (fase 1)

Fontes exploradas:
- Reddit /r/SideProject (posts recentes sobre produtos lançados e dashboards de makers)
- Pesquisa de tendências indie hacker/launch
- Contexto interno dos overnight builds anteriores (evitar repetir ideias)

Sinal detectado:
- Muito foco em builders a melhorar distribuição, copy e monetização
- Pricing continua uma dor transversal para founders (é onde pequenas mudanças têm impacto grande)

---

## Porquê este projecto

### Problema real
Muitos founders escolhem preço “a olho”, sem perceber:
- efeito de âncora
- decoy effect
- impacto de .99 vs número redondo
- bundles e urgência

### Utilidade prática
Este laboratório permite testar cenários rapidamente antes de mexer na pricing page real.

### Diferenciação vs builds anteriores
Já existiam várias calculadoras e dashboards, mas faltava uma ferramenta focada em **psicologia de decisão aplicada a pricing**.

---

## Features

1. **Anchoring Simulator** ⚓
   - Toggle para mostrar/esconder preço âncora
   - Cálculo automático de savings percebida

2. **Decoy Effect Simulator** 🎯
   - Plano decoy opcional
   - Visualização de 2 vs 3 opções

3. **Charm Pricing Demo** ✨
   - Comparação round vs charm pricing
   - Variações de finais (.99, .97, .95)

4. **Bundling Engine** 📦
   - Soma individual vs bundle
   - Cálculo automático de desconto e poupança

5. **Urgency/Scarcity Demo** ⏰
   - Toggle de countdown
   - Toggle de stock limitado

6. **Reference Library** 📚
   - 10 princípios explicados em linguagem simples

---

## Estilo Escolhido: Editorial Clean ☀️

### Justificação
Este projecto é educativo e denso em explicação. Precisava de:
- legibilidade alta
- hierarquia tipográfica clara
- visual limpo para não distrair da aprendizagem

### Aplicação prática
- Fundo claro (#fafafa / #fff)
- Títulos serif (Fraunces) + corpo sans (Inter)
- Muito whitespace
- Accent azul único para consistência

---

## Tech

- HTML/CSS/JS puro (single file)
- Sem dependências externas JS
- Componentes reactivos com listeners nativos
- Responsive para desktop/tablet/mobile

---

## Testes

- Navegação entre tabs
- Toggles funcionais em todos os módulos
- Inputs numéricos e textuais com update em tempo real
- Countdown funcional sem erros de consola
- Layout responsivo validado por breakpoints

---

## Potencial de evolução

- Export de cenários (JSON/share link)
- “Recommended pricing setup” baseado em objectivo (volume vs premium)
- A/B experiment planner para pricing pages
- Benchmarks por nicho (SaaS B2B, creator tools, consumer)

---

*Built by Safira @ 01:30 UTC while Guilherme sleeps.*
