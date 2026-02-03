# 🔍 Landing Page Auditor

## O que é
Uma ferramenta de auditoria de landing pages que ajuda a identificar problemas de conversão de forma estruturada.

## Porquê este projecto
Esta noite criei a ideia "AI-Landing-Page-Auditor" (Priority Score: 15.0) durante a pesquisa nocturna. Vi no Reddit que alguém vendeu auditorias manuais a $29 cada. Este MVP demonstra o conceito.

## Como funciona
1. Introduz o URL da landing page
2. Percorre a checklist de 20 pontos divididos em 5 categorias:
   - 📝 Copy & Messaging (25 pts)
   - 🎨 Visual Design (20 pts)
   - 🎯 Call-to-Action (25 pts)
   - 🛡️ Trust & Proof (15 pts)
   - 📱 Mobile & Technical (15 pts)
3. Vê o score em tempo real (0-100)
4. Recebe grade (A-F) e lista de issues prioritárias
5. Exporta relatório em texto

## Fit com o Guilherme
- Background PPC = conhece conversão melhor que ninguém
- Pode usar para auditar páginas de clientes
- Base para possível side hustle (€19/auditoria ou €29/mês)

## Próximos passos (se quiser desenvolver)
1. Adicionar AI Vision para análise automática de screenshots
2. Integrar PageSpeed API para métricas técnicas
3. Criar versão SaaS com Stripe checkout
4. Validar: oferecer 3 auditorias grátis no r/Entrepreneur

## Stack
- HTML/CSS/JS puro (zero dependências)
- Design dark mode com gradientes
- Responsivo
- Export para ficheiro de texto

## Link
https://luzguilherme.github.io/safira-overnight/2026-02-03/landing-page-auditor.html

---

# ₿ BTC Decision Dashboard

## O que é
Dashboard pessoal para análise de Bitcoin — agrega dados de preço, indicadores técnicos e sentimento de mercado para ajudar a tomar decisões mais informadas.

## Porquê este projecto
Pedido directo do Guilherme. Quer uma plataforma pessoal que combine:
- Histórico de preço
- Fear & Greed Index
- Indicadores técnicos
- Análise agregada

## Funcionalidades
- **Preço actual** em EUR com variação 24h (via CoinGecko)
- **Fear & Greed Index** com gauge visual (via Alternative.me)
- **Gráfico histórico** com tabs 7D/30D/90D/1A
- **Indicadores técnicos:**
  - RSI (14) — detecta oversold/overbought
  - MA50 vs Preço — tendência curta
  - MA200 vs Preço — tendência longa (bull/bear)
  - Volatilidade (30D)
- **Níveis de preço:** Máximo/Mínimo 365D, distância do ATH
- **Variação histórica:** 7D, 30D, 365D
- **Sinal agregado:** Combina todos os indicadores para mostrar Zona Favorável/Neutra/Cautela
- **Auto-refresh:** Actualiza a cada 60 segundos

## APIs usadas (todas grátis, sem key)
- CoinGecko API — preço e histórico
- Alternative.me — Fear & Greed Index

## Stack
- HTML/CSS/JS puro
- Chart.js para gráficos
- Design dark mode Bitcoin-themed
- Zero dependências externas além de Chart.js

## Link
https://luzguilherme.github.io/safira-overnight/2026-02-03/btc-dashboard.html

---
*Pedido do Guilherme | Build #8*
*Tempo: ~30 minutos*
