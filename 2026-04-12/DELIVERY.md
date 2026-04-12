# 🌙 Overnight Delivery — 2026-04-12

## Projecto
**Inbox Heatmap — Message Triage Planner**

URL: https://luzguilherme.github.io/safira-overnight/2026-04-12/

## O que é
Ferramenta local (sem API) para transformar uma lista caótica de mensagens num plano de resposta accionável:
- Classifica mensagens por urgência (Urgente / Em breve / Pode esperar)
- Estima tempo mínimo de resposta
- Sugere batching por canal para reduzir context switching
- Dá ETA de resposta por mensagem

## Pesquisa antes de construir
### Hacker News (Show HN)
- “Depsly – CLI to see dependency impact”
- “MCP vs CLI for browser automation”
- “Git why – log agent reasoning trace”

### Product Hunt Feed
- InboxJoy - Filter Noise from Social DMs
- Tidy for Group Chats
- SummAgent

### Reddit
- Tentativa em r/SideProject e r/indiehackers bloqueada por anti-bot/rate-limit nesta sessão.

**Insight aplicado:** há tração clara em produtos que reduzem ruído e ajudam triagem de mensagens/conversas.

## Estilo escolhido
**Playful / Friendly 🎭** (de `data/STYLE_LIBRARY.md`)

**Porquê este estilo:**
- Produto focado em uso diário e approachable
- Não é ferramenta enterprise hardcore
- Precisa de transmitir leveza para reduzir stress de inbox overload

## Como usar
1. Colar mensagens (uma por linha): `canal | pessoa | mensagem`
2. Escolher modo do dia (focus/normal/meeting-heavy)
3. Definir minutos disponíveis nas próximas 2h
4. Clicar “Gerar plano de triagem”

## Qualidade
- Testado em cenários mistos (cliente urgente, bug produção, mensagens low-priority)
- Interface responsiva e cálculo 100% local
- Sem dependências externas

## Ficheiros
- `overnight/2026-04-12/index.html`
- `overnight/2026-04-12/DELIVERY.md`
