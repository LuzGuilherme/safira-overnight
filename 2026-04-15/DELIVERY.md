# 🌙 Overnight Build — 2026-04-15

## Projecto
**Name Stress Test**  
Ferramenta para founders compararem nomes de startup de forma rápida com scoring heurístico (clareza, memorabilidade, pronúncia, diferenciação e risco de confusão).

## Inspiração (Fase de Pesquisa)
- **Hacker News / Show HN:** vários launches de tooling prático e rápido para makers (incluindo ferramentas de naming/positioning em discussão).
- **Reddit r/indiehackers:** histórico de posts tipo *"Show IH"* com forte foco em validação de nome e branding inicial.
- **Product Hunt:** tendência contínua de micro-ferramentas para founders com feedback imediato.

## Porque isto?
- Naming é uma dor real no início de qualquer side project.
- É um problema **rápido de resolver** com heurísticas locais (sem APIs externas).
- Mantém escopo de 1-2h com output útil e testável no browser.

## Estilo Escolhido
**Bold Maximalist 🎨**

### Justificação de fit
- A fase de naming pede energia, experimentação e criatividade.
- O estilo cria sensação de "laboratório de ideias" em vez de ferramenta corporativa rígida.
- Diferencia visualmente dos últimos dias (Swiss Minimal / Data Dense / Playful).

## Features Entregues
1. Input de 3-10 nomes (1 por linha)
2. Score 0-100 por nome com breakdown de critérios
3. "Top pick" automático com justificação curta
4. Tabela comparativa completa
5. Chips visuais de risco/qualidade
6. Gerador de variações automáticas
7. Persistência local via `localStorage`

## Ficheiros
- `overnight/2026-04-15/index.html`
- `overnight/2026-04-15/DELIVERY.md`

## Limitações conhecidas
- Não consulta trademark/domain em tempo real (heurístico offline).
- Scoring é orientativo; decisão final deve incluir validação legal/comercial.

## Como testar rapidamente
1. Abrir `index.html`
2. Clicar em **Usar exemplo**
3. Confirmar que aparece ranking, vencedor e tabela
4. Clicar em **Gerar variações** e validar refresh automático do ranking
