# 🌙 Overnight Build — 2026-03-31

## Projecto
**Global Meeting Overlap Planner**

Ferramenta para equipas remotas encontrarem rapidamente horários de reunião com maior sobreposição entre fusos horários.

## Porque este projecto?
Durante a pesquisa nocturna:
- **Hacker News Show** mostrava tools de scheduling/timezones para equipas distribuídas.
- **Product Hunt feed** tinha vários lançamentos orientados a produtividade e colaboração global.
- No **r/SideProject**, havia sinais de fadiga com “mais um AI wrapper”, o que reforça utilidade prática não-AI.

Escolhi construir algo:
- útil no dia-a-dia de founders/remote teams,
- rápido de validar,
- sem dependências externas,
- com execução clara em 1-2 horas.

## Estilo escolhido
**Swiss Minimal 🏛️**

### Justificação
- O produto é utilitário e funcional (não “marketing page”).
- O estilo Swiss favorece **clareza, grid rígido e legibilidade**, ideal para matriz de horários.
- Evita ruído visual e ajuda a tomar decisões rápidas.

## Features implementadas
- Adicionar membros com:
  - nome,
  - fuso horário,
  - horário de trabalho local.
- Matriz 24h (UTC) com conversão por membro.
- Cobertura por hora (percentagem da equipa disponível).
- Indicadores automáticos:
  - nº de slots perfeitos (100%),
  - melhor hora UTC.
- **Top 5 slots recomendados**.
- Botão **demo** com equipa distribuída (Lisboa, NY, Índia, Japão).
- Layout responsive.

## Stack
- HTML + CSS + JavaScript (vanilla)
- Sem build step, sem libs externas.

## Ficheiros
- `/root/clawd/overnight/2026-03-31/index.html`
- `/root/clawd/overnight/2026-03-31/DELIVERY.md`

## Nota
Projecto novo (não duplicado com os já existentes em `PROJECTS_DONE.md`).
Categoria: **Produtividade / Remote Collaboration**.