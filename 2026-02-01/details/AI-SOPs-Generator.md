---
title: AI SOPs Generator
created: 2026-01-29
tags:
  - idea
  - side-hustle
  - ai
  - b2b
status: exploring
potential: 7
effort: 5
skills: 7
problem: "PMEs gastam horas a documentar processos internos (SOPs)"
solution: "Tool que grava demonstrações e gera SOPs automáticos com screenshots"
market: "PMEs, consultores, onboarding teams"
---

# AI SOPs Generator

## Problem
Pequenas e médias empresas perdem tempo enorme a:
- Documentar processos internos
- Criar manuais de onboarding
- Manter SOPs atualizados

## Solution
Ferramenta que:
1. Grava screen + voz enquanto demonstras o processo
2. Transcreve com Whisper
3. Extrai screenshots automáticos
4. Gera documento estruturado com Claude
5. Exporta para Notion/Confluence/Google Docs

## Market
- PMEs (10-200 funcionários)
- Consultoras de processos
- HR/Onboarding teams
- Franchises

## Technical Stack
- **Screen recording:** Browser extension ou Electron
- **Transcrição:** Whisper
- **Screenshot:** Puppeteer/system APIs
- **Geração:** Claude API
- **Export:** APIs do Notion/Confluence

## Pricing
- Free: 3 SOPs/mês
- Pro: $29/mês per seat
- Team: $19/mês per seat (5+ seats)

## Competition
- Scribe
- Tango
- Loom (parcialmente)

> [!tip] Diferenciador
> Output é documento editável, não apenas vídeo.
> Integração directa com ferramentas existentes.

## Next Steps
- [ ] Testar com Scribe para benchmark
- [ ] Protótipo com screen recording manual
- [ ] Validar com 2-3 PMEs

## Notes
Boa sinergia com skills de programação que já temos.
