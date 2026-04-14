# 🌙 Overnight Build — 2026-04-14

## Projecto
**PR Stack Architect**

Ferramenta para decompor uma feature grande em PRs pequenos e sequenciais, respeitando dependências e controlando risco por stack.

## Porque este projecto
Durante a pesquisa nocturna apareceram sinais fortes de foco em **qualidade de shipping** e workflows de equipa:
- HN: discussão sobre *GitHub Stacked PRs*
- HN: incidente de supply-chain em plugins WordPress (reforça necessidade de mudança incremental e auditável)
- Product Hunt feed: várias tools operacionais verticais (execução > ideia)

Isto encaixa no perfil do Guilherme: shipping rápido, mas com disciplina técnica.

## Estilo escolhido
**Swiss Minimal 🏛️**

### Justificação
- Ferramenta de planeamento: pede clareza e hierarquia, não “efeitos”.
- Interface neutra para leitura rápida de trade-offs (impacto, esforço, risco, dependências).
- Diferente dos estilos muito usados recentemente (Industrial/Data Dense/Playful).

### Referências de estilo (fase de pesquisa)
- apple.com (páginas produto, hierarquia limpa)
- posters Swiss style (grid e tipografia funcional)
- dashboards minimalistas com foco em legibilidade

## Funcionalidades
1. **Adicionar backlog técnico** com impacto, esforço, risco e dependência.
2. **Validação de dependências** (ID existente obrigatório).
3. **Topological sort** para respeitar ordem de execução.
4. **Quebra automática em PR stacks** (até ~8 pontos por PR, isolamento de itens high-risk quando possível).
5. **KPIs rápidos**: número de PRs, lead time estimado, risco total.
6. **Modo demo** para testar imediatamente.

## Testes feitos
- ✅ Sem itens: mensagem de orientação
- ✅ Dependência inválida: bloqueio com alerta
- ✅ Dependências cíclicas: detecção e erro explícito
- ✅ Dataset demo: gera plano multi-PR consistente
- ✅ Responsivo (desktop/mobile)

## Ficheiros
- `index.html` — app completa (HTML/CSS/JS)

## Resultado
Build pronto em:
`/root/clawd/overnight/2026-04-14/`
