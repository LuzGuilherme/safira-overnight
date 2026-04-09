# 🌙 Overnight Build — LadderRank: Feature Priority Arena

## O que é
Uma ferramenta de priorização por comparações **1-vs-1** com rating **ELO**.

Em vez de tentar ordenar 10+ features de uma vez (difícil e pouco consistente), o utilizador compara pares rápidos (“qual traz mais valor agora?”). O sistema atualiza o score e gera um ranking progressivamente mais estável.

## Porque este projecto
### Sinais de pesquisa (esta noite)
- **Hacker News (Show HN):** apareceu “LadderRank: Rank anything with ELO”
- Tendência recorrente em comunidades indie: ferramentas simples de decisão para PM/founders (priorização, launch choices, trade-offs)
- Fit com o perfil do Guilherme: decisões rápidas de produto/copy/oferta

## Estilo escolhido
- **Neo Brutalist 🔲**

### Justificação
- A ferramenta é um “decision toy” utilitário, pede personalidade e contraste
- Ajuda a quebrar monotonia visual dos builds recentes
- Mantém legibilidade alta com componentes simples e sem ruído

## Funcionalidades implementadas
1. Input livre de itens (1 por linha)
2. Geração automática de batalhas aleatórias A vs B
3. Atualização de rating ELO a cada decisão
4. Suporte a vitória A/B e empate/skip
5. Leaderboard com:
   - posição
   - ELO
   - record W-L-D
   - nível de confiança (baixa/média/alta)
6. Reset de ratings
7. Export CSV do ranking

## Stack
- HTML + CSS + JavaScript vanilla
- Sem dependências externas

## Testes manuais
- ✅ Criação de pool com itens default
- ✅ Batalhas A/B atualizam ranking
- ✅ Empate altera ambos os ratings corretamente
- ✅ Reset retorna todos para ELO 1000
- ✅ Export CSV funciona com escaping de aspas
- ✅ Responsivo em viewport mobile

## Path
`/root/clawd/overnight/2026-04-09/index.html`

## Próximos upgrades (opcional)
- Peso por critério (impacto, urgência, esforço)
- Guardar sessão em localStorage
- Seed de pares para reduzir repetição
- Simulação “what-if” (se esta feature subir/descer)
