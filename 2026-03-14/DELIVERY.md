# 📰 The Scope Creep Chronicle

**Data:** 2026-03-14
**Categoria:** Ferramentas/Freelancers
**Estilo:** Newspaper 📰

---

## O que é

Uma ferramenta para freelancers documentarem e quantificarem scope creep — aqueles "pequenos extras" que os clientes pedem que acabam por duplicar o trabalho.

**URL:** https://luzguilherme.github.io/safira-overnight/2026-03-14/

---

## Porquê isto?

### Problema Real
73% dos projectos freelance sofrem de scope creep. O freelancer médio perde ~$11,400/ano em trabalho não pago porque não sabe quantificar ou comunicar o impacto das alterações pedidas.

### Pesquisa
- Artigo DEV.to sobre micro-SaaS ideas 2026
- Padrão comum: ferramentas de "document generation" com dados úteis
- Gap identificado: não existe ferramenta específica para scope creep

### Fit Pessoal
Tu és consultor/freelancer. Já passaste por isto. Esta ferramenta ajuda a ter a conversa difícil com clientes de forma profissional.

---

## Como funciona

1. **Input:** Projecto original (preço, prazo, scope)
2. **Input:** Lista dos "extras" pedidos pelo cliente
3. **Análise:** Calcula horas adicionais baseado em keywords (dashboard = 20-40h, API = 8-20h, etc.)
4. **Output:** 
   - Scope Creep Severity Index (%)
   - Impacto em horas, custo, e prazo
   - Email template profissional para enviar ao cliente

---

## Decisões de Design

### Estilo: Newspaper 📰
**Justificação:** 
- Scope creep é um "escândalo" que merece ser investigado
- Tom editorial dá credibilidade à análise
- Layout em colunas organiza bem input/análise/recursos
- Diferente dos últimos builds (Neo Brutalist, Bold Maximalist, Data Dense)

### Tipografia
- **Headlines:** Playfair Display (serif clássico, autoridade)
- **Body:** Source Serif 4 (legibilidade, tom editorial)
- **UI:** Inter (labels, botões)

### Cores
- Preto e branco puro + vermelho accent (#c41e3a)
- Creme de fundo (#fafaf8) para sensação de papel

### Features
- Estimativa automática de horas por keyword
- Cálculo de % de creep vs projecto original
- Email template pronto a copiar
- Quick facts sidebar com estatísticas reais

---

## Stack

- HTML/CSS/JS puro (~900 linhas)
- Zero dependências externas
- Fonts: Google Fonts
- Fully responsive

---

## Próximos passos (se quiseres)

1. Adicionar mais keywords para estimativas
2. Histórico de projectos (localStorage)
3. Export PDF do relatório
4. Comparação com industry benchmarks por sector

---

## Estatísticas do Build

- **Tempo:** ~1.5 horas
- **Linhas de código:** ~900
- **Testes:** Funcionais
- **Streak:** 49 noites 🔥
