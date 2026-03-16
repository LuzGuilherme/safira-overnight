# 🚀 Launch Checklist Generator

**Data:** 2026-03-16  
**Estilo:** Industrial Dark 🌙  
**Categoria:** Ferramentas/Indie Hackers  
**Tempo:** ~1.5 horas

---

## O que é?

Um gerador de checklists de lançamento customizadas por tipo de produto. Indie hackers e makers frequentemente esquecem tasks críticas no dia de lançamento. Esta ferramenta gera uma checklist completa e interactiva baseada no tipo de produto.

**6 tipos de produto suportados:**
- 💻 SaaS Product
- 📱 Mobile App
- 🧩 Chrome Extension
- 📚 Info Product (cursos, ebooks)
- ⚡ API / Dev Tool
- 📧 Newsletter

---

## Porquê isto?

**1. Problema real e validado:**
- "I always forget something on launch day" é queixa comum no r/indiehackers
- Product Hunt, Hacker News, Reddit... cada plataforma tem nuances
- Checklists existentes são genéricas demais ou pagas

**2. Tendência actual:**
- HN Show está cheio de dev tools e indie maker resources
- "Ship fast" culture precisa de guardrails
- Context Gateway e GitAgent mostram foco em tooling prático

**3. Útil para o Guilherme:**
- Pode usar para futuros lançamentos
- Cada tipo de produto tem conhecimento curado
- Shareable com comunidade indie

---

## Features

### Core
- **6 tipos de produto** com checklists específicas
- **3 fases por tipo:** Pre-Launch, Launch Day, Post-Launch
- **Tags de prioridade:** Critical, Important, Optional
- **Progress tracking** com barra visual
- **Persistência via URL** — pode partilhar ou voltar mais tarde

### Interacção
- Click para marcar/desmarcar
- Copy as Markdown para exportar
- Reset para começar de novo
- Share link com progresso incluído

### UX
- Collapsible phases
- Progress por fase
- Toast notifications
- Mobile responsive

---

## Stack Técnico

- HTML/CSS/JS puro (zero dependencies)
- CSS Variables para theming
- LocalStorage-free (tudo no URL)
- Space Grotesk + JetBrains Mono

---

## Decisões de Design

**Por que Industrial Dark?**
- 9 dias desde último uso (mais antigo no ciclo)
- Fits developer/maker audience
- Night-friendly (launch prep à noite é comum)
- Professional feel para ferramenta séria

**Por que 6 tipos específicos?**
- Baseado nos lançamentos mais comuns no indie space
- Cada tipo tem nuances próprias (App Store vs Chrome Store vs HN)
- Evitei "Other/Generic" para forçar value específico

**Por que URL-based persistence?**
- Shareability (pode enviar link com progresso)
- No privacy concerns (nada server-side)
- Bookmarkable progress

---

## Conteúdo das Checklists

Cada checklist foi curada baseada em:
- Best practices de lançamentos bem sucedidos
- Erros comuns documentados em post-mortems
- Timing específico (ex: PH às 00:01 PST)
- Platform-specific requirements

**Exemplos de insights incluídos:**
- "Developers judge tools by docs quality" (API)
- "Submit 2-3 days early for review buffer" (Mobile)
- "HN is THE place for dev tools" (API)
- "Devs hate credit card upfront" (API free tier)

---

## Potencial de Expansão

**Se converter em produto:**
1. Add Notion/Linear export
2. Team collaboration (shared checklist)
3. Custom checklist builder
4. Email reminders for tasks
5. Integration with PH/HN submission

---

## URLs

- **Live:** https://luzguilherme.github.io/safira-overnight/2026-03-16/
- **Source:** /root/clawd/overnight/2026-03-16/

---

## Screenshot

```
┌─────────────────────────────────────────────┐
│    🚀 Launch Checklist Generator            │
│    Stop forgetting critical launch tasks    │
├─────────────────────────────────────────────┤
│  [💻 SaaS] [📱 Mobile] [🧩 Chrome]          │
│  [📚 Info] [⚡ API]   [📧 Newsletter]       │
├─────────────────────────────────────────────┤
│  ████████████░░░░░ 67%                      │
│  12 / 18 tasks completed                    │
├─────────────────────────────────────────────┤
│  🔧 Pre-Launch                    8/12      │
│  ├─ [x] Landing page live         CRITICAL  │
│  ├─ [x] Payment tested            CRITICAL  │
│  └─ [ ] Demo video                OPTIONAL  │
├─────────────────────────────────────────────┤
│  🚀 Launch Day                    4/6       │
│  └─ ...                                     │
└─────────────────────────────────────────────┘
```

---

*Built overnight by Safira 🌙*
