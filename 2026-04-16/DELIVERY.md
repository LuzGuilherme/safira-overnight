# 🌙 Overnight Build — 2026-04-16

## Projecto
**Focus Runway Planner 🌿**

Ferramenta para founders estimarem dois limites críticos ao mesmo tempo:
1. **Runway financeiro** (meses até ficar sem margem)
2. **Runway cognitivo** (semanas até saturação por stress + context switching)

URL: https://luzguilherme.github.io/safira-overnight/2026-04-16/

---

## Pesquisa rápida (fontes)
- **Hacker News / Show HN:** tendências em tooling para produtividade de builders e pressão cognitiva
- **Reddit (r/SideProject, r/indiehackers):** acesso directo bloqueado por 403 nesta sessão nocturna, então usei sinais de discussão já reflectidos em HN sobre burnout/foco e shipping stress
- **Product Hunt:** tema recorrente de ferramentas para workflow/ship velocity

---

## Escolha e escopo
Evitei duplicados de projectos já feitos (prioritizers, checklists de launch, scorecards clássicos).

Ângulo novo: **combinar dinheiro + energia mental** numa única decisão operacional.

Escopo mantido para 1-2 horas:
- Inputs essenciais (savings, burn, foco, stress, switching, fase)
- Cálculo instantâneo
- Diagnóstico visual
- Plano de acção automático

---

## Estilo escolhido
**Organic Soft 🌿**

### Porquê este estilo?
O tema é burnout/sustentabilidade de execução. Um visual agressivo iria contra o objectivo. Organic Soft comunica calma, clareza e gestão sustentável de ritmo.

---

## Features entregues
- Calculadora de **runway financeiro**
- Estimativa de **runway cognitivo** com penalização por stress + switching + fase do projecto
- Veredicto em 3 estados:
  - Zona estável
  - Atenção
  - Risco alto
- Recomendações dinâmicas orientadas à acção
- Preset conservador para simulação rápida
- Layout responsive e standalone (sem dependências)

---

## QA / testes
- Testado fluxo principal (inputs default)
- Testado cenário de risco (burn alto + stress alto)
- Testado cenário estável (burn baixo + stress baixo)
- Testado preset + recálculo
- Validado render mobile/desktop (layout fluido)

Sem erros JS no fluxo principal.

---

## Ficheiros criados
- `/root/clawd/overnight/2026-04-16/index.html`
- `/root/clawd/overnight/2026-04-16/DELIVERY.md`

