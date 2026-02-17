# 🤖 AI Agent ROI Calculator

## Objectivo
Criar uma calculadora interactiva que ajuda empresas a estimar o ROI de implementar um agente AI vs manter processos manuais/humanos.

## Porquê isto?
- Trend actual: AI agents em alta (Reddit r/SideProject mostra virtual offices com AI agents como top post)
- Alinhado com interesses do Guilherme (AI, automação, indie hacking)
- Potencial monetização: Lead magnet para serviços de AI, ou produto standalone
- Útil para o próprio Guilherme vender serviços de setup de agentes

## Funcionalidades
1. **Input Section**
   - Tipo de tarefa (customer support, data entry, research, etc.)
   - Volume mensal (emails, tickets, horas)
   - Custo actual (salário ou custo por tarefa)
   - Tempo médio por tarefa

2. **Cálculos**
   - Custo estimado do AI agent (setup + mensal)
   - Horas economizadas por mês
   - Payback period (meses até ROI positivo)
   - Savings anuais

3. **Output Visual**
   - Comparação lado a lado: Human vs AI
   - Gráfico de break-even
   - Timeline de ROI
   - Botão para exportar/partilhar

## Design Direction
**Aesthetic:** Industrial/Utilitarian + Tech
- **Cores:** Dark theme (#0a0a0a background), accent verde (#10b981)
- **Font:** Space Grotesk (headings), Inter para números (legibilidade)
- **Layout:** Grid funcional, labels claros, números grandes
- **Vibe:** Dashboard de engenharia, não marketing fluff

## Fases
1. [ ] Estrutura HTML + CSS base
2. [ ] Inputs interactivos com validação
3. [ ] Lógica de cálculo JavaScript
4. [ ] Visualização de resultados
5. [ ] Polish: animações, responsivo

## Critérios de Sucesso
- Funciona sem erros em mobile e desktop
- Cálculos fazem sentido matematicamente
- Design distintivo, não AI slop
- Útil e shareable
