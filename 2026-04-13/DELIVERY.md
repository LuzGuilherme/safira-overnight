# Delivery: Portfolio Pruner ✂️

## 🧠 Porquê Isto? (Raciocínio)

### Contexto
Na pesquisa nocturna apareceram sinais repetidos de makers a construir muitos projectos seguidos (threads no r/SideProject e r/indiehackers sobre múltiplos launches) + Show HN com builders solo a iterar rápido. O problema comum: **acumulam projectos, mas faltam critérios frios para decidir onde focar**.

### Alternativas Consideradas
1. **Mais uma launch checklist** — ❌ já existe no histórico (Launch Checklist Generator / Launch Launchpad)
2. **Outro gerador de ideias** — ❌ categoria saturada no histórico
3. **Ferramenta de triagem de portefólio pós-lançamento** — ✅ nova âncora (decidir o que matar/manter/escalar)

### Trade-offs Aceites
- ✅ Ganhamos: decisão rápida, objetiva e accionável para founders com 3-10 side projects
- ⚠️ Sacrificamos: não integra APIs externas (dados manuais nesta versão)

---

## 📦 O que é
Uma web app local que recebe métricas dos side projects e devolve ranking + recomendação prática por projecto: **Grow, Keep, Pause, Kill**.

## 🎯 Problema que resolve
Evita que o founder disperse energia por projectos fracos por apego emocional. Dá um critério numérico para foco.

## ✨ Features
- Input de múltiplos projectos (users, MRR, crescimento, suporte, entusiasmo)
- Score ponderado (tração + eficiência + motivação)
- Classificação automática: Grow / Keep / Pause / Kill
- Ações sugeridas por categoria
- KPI cards de síntese (top aposta + distribuição de decisões)
- Exemplo demo para testar em 1 clique

## 🎨 Design
- **Aesthetic:** Data Dense 📊
- **Stack:** HTML + CSS + JavaScript vanilla (sem dependências)

## 📁 Ficheiros
- `index.html` — aplicação completa (UI + lógica)
- `DELIVERY.md` — documentação da entrega

## 🔗 Link
https://luzguilherme.github.io/safira-overnight/2026-04-13/

## 💡 Como usar
1. Inserir 3-8 projectos com métricas reais
2. Clicar em **Analisar portefólio**
3. Executar a decisão: dobrar no top 1, pausar/matar o resto com score baixo

## 🔮 Próximos passos (se relevante)
- [ ] Guardar snapshots mensais em localStorage
- [ ] Export CSV para revisão semanal
- [ ] Modo “cenário” para simular impacto de melhorias

---

*Build by Safira 🌙*