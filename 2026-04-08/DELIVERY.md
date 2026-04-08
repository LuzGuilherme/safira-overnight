# 🌙 Overnight Build — 2026-04-08

## Projecto
**Storage Exit Calculator**

Ferramenta interactiva para founders compararem o custo de armazenamento entre:
- Dropbox Business / Google Workspace (situação actual)
- AWS S3, Cloudflare R2, Backblaze B2 (alternativas object storage)

Inclui:
- Inputs de storage, egress, pedidos API e tamanho de equipa
- Custo mensal actual vs melhor alternativa
- Poupança mensal e anual
- Breakdown detalhado por provider
- Recomendação automática

---

## Pesquisa (antes de construir)

### Reddit
- r/SideProject RSS: discussão activa sobre projectos não-AI e produtos com utilidade real
- r/indiehackers RSS: foco em operações práticas para founders

### Hacker News
- Show HN incluía projecto com tese clara: **"Stop paying for Dropbox/Google Drive, use your own S3 bucket instead"**
- Sinal forte de dor real: custos recorrentes de ferramentas infra aparentemente “simples”

### Product Hunt
- A homepage estava protegida por Cloudflare durante fetch automático (403), por isso baseei trend validation em Reddit + HN hoje.

---

## Escolha e escopo

- **Evitei duplicados** de `PROJECTS_DONE.md` (não havia calculadora focada em *storage stack migration* / FinOps para creators/founders).
- **Escopo 1–2h:** um único HTML self-contained, sem dependências externas.
- **Categoria:** Business / FinOps / Founder Utility.

---

## Estilo escolhido

**Swiss Minimal 🏛️**

### Porquê
- Tema de decisão financeira pede clareza e credibilidade, não gimmicks.
- Hierarquia tipográfica + grelha limpa ajuda leitura rápida de números.
- Fit directo com a library para ferramentas sérias de decisão.

---

## Testes feitos

- Vários cenários de input (0 TB, valores altos, mudança de stack actual, equipa 1+)
- Recalculo em tempo real sem refresh
- Verificação de formatação monetária e cálculo anual
- Validação de layout mobile e desktop

---

## Ficheiros criados
- `/root/clawd/overnight/2026-04-08/index.html`
- `/root/clawd/overnight/2026-04-08/DELIVERY.md`

