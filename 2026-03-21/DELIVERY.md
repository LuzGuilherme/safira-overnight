# Delivery: Ramen Profitability Calculator 🍜

## 🧠 Porquê Isto? (Raciocínio)

### Contexto
Pesquisa nocturna em recursos de micro-SaaS e indie hackers. O artigo do dev.to sobre "Actually Useful Micro-SaaS Ideas (2026 Edition)" mencionava calculadoras financeiras como ferramentas populares. O conceito de "ramen profitable" — ter receita suficiente para cobrir despesas básicas e trabalhar full-time no projecto — é fundamental na cultura indie hacker.

### Alternativas Consideradas
1. **Proposal Builder para Freelancers** — ❌ Requer templates complexos e mais tempo
2. **Market Research Report Generator** — ❌ Dependente de APIs externas
3. **Ramen Profitability Calculator** — ✅ Auto-contido, útil imediatamente, alinhado com interesses do Guilherme (side hustles)

### Trade-offs Aceites
- ✅ Ganhamos: Ferramenta prática e imediatamente útil, cálculos em tempo real, sem dependências externas
- ⚠️ Sacrificamos: Não tem persistência (localStorage), não exporta relatórios

---

## 📦 O que é
Uma calculadora interactiva que ajuda indie hackers a descobrir quando podem abandonar o emprego e dedicar-se 100% ao seu projecto. Calcula o "ramen profitability threshold" — o ponto onde a receita recorrente cobre as despesas básicas de vida.

## 🎯 Problema que resolve
Todo indie hacker sonha em largar o emprego. Mas quando é seguro fazê-lo? Esta ferramenta responde:
- Quão perto estou de "ramen profitable"?
- Quantos meses até lá chegar (com diferentes cenários de crescimento)?
- Se largar hoje, quanto tempo aguento com as minhas poupanças?

## ✨ Features
- **Progress Tracker:** Percentagem visual até ramen profitability
- **Expense Breakdown:** 7 categorias de despesas (renda, comida, utilities, etc.)
- **3 Cenários:** Pessimista, Realista, Optimista — com datas estimadas
- **Runway Calculator:** Quantos meses de poupanças se largares HOJE
- **Safety Buffer:** Configura quantos meses de buffer queres antes de saltar
- **Tips Section:** Conselhos práticos para acelerar o processo
- **Real-time Updates:** Todos os valores actualizam instantaneamente

## 🎨 Design
- **Aesthetic:** Data Dense 📊 — Layout denso com muita informação, ideal para dashboards financeiros
- **Stack:** HTML5, CSS3, Vanilla JavaScript (zero dependências)
- **Fonts:** JetBrains Mono (números), Inter (texto)
- **Colors:** Dark theme com verde/amarelo/vermelho para estados

## 📁 Ficheiros
- `ramen-calculator.html` — Aplicação completa (single file, ~40KB)

## 🔗 Link
https://luzguilherme.github.io/safira-overnight/2026-03-21/ramen-calculator.html

## 💡 Como usar
1. Preenche as tuas despesas mensais (renda, comida, etc.)
2. Introduz o teu MRR actual e taxa de crescimento esperada
3. Define as tuas poupanças e buffer de segurança desejado
4. Vê instantaneamente quando podes "saltar"

## 🔮 Próximos passos (se relevante)
- [ ] localStorage para guardar dados entre sessões
- [ ] Export para PDF com o plano
- [ ] Gráfico de projecção MRR vs tempo
- [ ] Integração com Stripe para MRR automático

---

*Built by Safira 🌙 • 21 Março 2026 • 01:30-02:15 UTC*
