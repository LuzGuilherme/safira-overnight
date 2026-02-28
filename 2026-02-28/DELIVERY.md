# 🚢 Ship or Sink — Overnight Build (2026-02-28)

## O que é?
Um countdown público e "brutal" para lançar side projects. Define um deadline, partilha publicamente, e enfrenta a vergonha se falhares.

## Porquê isto?

### O Problema Real
Vi no Reddit r/SideProject que as pessoas têm "graveyards of half-built things". O problema não é ter ideias — é **shipar**. A procrastinação mata mais side projects que a falta de skills.

### A Solução
Pressão social. Quando partilhas um deadline publicamente, tens mais probabilidade de o cumprir. "Ship or Sink" é um accountability partner impiedoso.

### Inspiração
- Posts como "The tools that actually helped me ship"
- O facto de que 80% dos side projects morrem antes de lançar
- O conceito de "build in public" mas aplicado a deadlines

## Features

1. **Set Deadline** — Nome do projecto + data/hora de lançamento
2. **Live Countdown** — Dias, horas, minutos, segundos
3. **Shame Mode** — Se passares o deadline, tudo fica VERMELHO
4. **Brutal Quotes** — Mensagens motivacionais (nada de fluff)
5. **Share Link** — URL com parâmetros para partilhar publicamente
6. **Ship Button** — Marca como lançado e celebra
7. **Stats** — Quantos dias demoraste, se foi a tempo ou não

## Design

### Estilo: Neo Brutalist 🔲

**Porquê Neo Brutalist:**
- Comunica urgência e seriedade
- Não é "bonito" — é funcional e impactante
- Diferencia-se de todas as apps "soft" de produtividade
- O público-alvo (devs, indie hackers) aprecia estética bold

**Elementos usados:**
- Amarelo vibrante (#FFE600) como background principal
- Bordas grossas pretas (4px)
- Tipografia monospace (Space Mono)
- Zero gradientes, sombras flat
- Layout directo, sem decoração

**Referências consultadas:**
- brutalistwebsites.com
- Indie games UI
- 90s web aesthetic

## Tech Stack
- HTML5, CSS3, Vanilla JavaScript
- Nenhuma dependência externa (exceto Google Fonts)
- Funciona 100% client-side
- URL params para sharing (stateless)

## Como Usar
1. Abre a página
2. Dá nome ao teu projecto
3. Define o deadline
4. Clica "Start Countdown"
5. Partilha o link publicamente
6. Quando lançares, clica "I SHIPPED IT!"

## Potencial de Expansão

### Versão SaaS (se validar):
- Accounts para histórico de projectos
- Notificações por email/SMS
- Integração com Twitter/X para auto-post
- Leaderboard público de "shippers"
- Badges/achievements

### Monetização:
- Freemium: 1 projecto grátis, mais = pago
- Team plans para startups
- API para integração com outras tools

## URL
https://luzguilherme.github.io/safira-overnight/2026-02-28/

## Notas de Construção
- Tempo de build: ~45 minutos
- Testado: setup form, countdown, URL params
- Não testado: shame mode (requer deadline passado)
