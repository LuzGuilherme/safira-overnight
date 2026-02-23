# 🎁 Client Value Calculator

**Data:** 2026-02-23
**Categoria:** Business/Calculadora
**Tempo:** ~2 horas

---

## 📋 O Que É

Calculadora interactiva que ajuda pequenos negócios (estúdios de tatuagem, clínicas, cabeleireiros) a entender:

1. **Customer Lifetime Value (CLV)** — Quanto vale realmente cada cliente
2. **Custo Máximo de Aquisição** — Quanto podem gastar em ads por cliente
3. **Break-even ROAS** — ROAS mínimo para não perder dinheiro
4. **Cenários** — E se melhorarem retenção ou referrals?

---

## 🎯 Para Que Serve

**Use case principal:** Ferramenta de vendas para prospecção de clientes.

Quando falas com um estúdio de tatuagem que pergunta "quanto custa fazer ads?", mostras esta calculadora:
- Preenches os valores do negócio deles
- Mostras que cada cliente vale €X ao longo do tempo
- Explicas que podem gastar até €Y para adquirir cada cliente
- Propões uma campanha dentro desse budget

**Resultado:** Conversa mais educada, cliente entende o valor, tu ganhas credibilidade.

---

## 🎨 Escolha de Estilo

**Estilo:** 🏛️ Swiss Minimal

**Porquê:**
1. É uma ferramenta B2B — precisa de transmitir profissionalismo
2. Os números devem falar por si — sem distracções visuais
3. Simplicidade extrema ajuda foco nas métricas
4. Diferencia dos projectos anteriores (Editorial Clean, Retro Tech)

**Características aplicadas:**
- Grid rígido de 2 colunas
- Preto, branco e um accent azul (#0066ff)
- Inter como font principal
- Muito espaço negativo
- Zero elementos decorativos
- Inputs minimalistas com apenas underline

**Referências usadas:**
- apple.com (product pages)
- Dieter Rams philosophy: "Less, but better"
- Swiss International Style posters

---

## 🔧 Como Funciona

### Inputs
- Preço médio por serviço (€)
- Custo por serviço (€)
- Visitas por ano (slider 1-24)
- Anos de retenção (slider 1-10)
- Taxa de referral (slider 0-100%)

### Outputs
- **Receita Total:** preço × visitas × anos
- **CLV:** (preço - custo) × visitas × anos × (1 + referral%)
- **Max CAC:** CLV × 30% (margem de segurança)
- **Break-even ROAS:** preço / margem

### Cenários
- Actual (valores inseridos)
- +1 Ano de retenção
- +10% taxa de referral

---

## 📊 Exemplo Real (Estúdio de Tatuagem)

**Inputs:**
- Preço médio: €150
- Custo: €30
- Visitas/ano: 2
- Retenção: 4 anos
- Referrals: 30%

**Outputs:**
- CLV: €1,248
- Max CAC: €374
- Break-even ROAS: 1.25x

**Insight:** "Podes gastar até €374 para adquirir cada cliente novo!"

---

## 🚀 Link

**GitHub Pages:** https://luzguilherme.github.io/safira-overnight/2026-02-23/

---

## ✅ Critérios de Sucesso

- [x] Calculadora funcional
- [x] Output claro e actionable
- [x] Estilo Swiss Minimal consistente
- [x] Mobile-friendly (testado)
- [x] Zero bugs nos cálculos
- [x] Cenários úteis
