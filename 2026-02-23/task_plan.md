# 🎯 Overnight Build — 2026-02-23

## Projecto: Client Value Calculator

**Problema:** Pequenos negócios (estúdios de tatuagem, clínicas dentárias, cabeleireiros) não sabem quanto podem gastar para adquirir um cliente. Quando lhes propomos fazer ads, perguntam "quanto custa?" sem entender o valor de cada cliente.

**Solução:** Calculadora interactiva que mostra:
1. Customer Lifetime Value (CLV)
2. Quanto podem gastar em aquisição
3. Break-even ROAS necessário
4. Cenários: "e se o cliente voltar mais vezes?"

**Porquê este projecto:**
- É Segunda (dia de foco em monetização)
- Guilherme está a prospectar estúdios de tatuagem
- Pode usar como ferramenta de vendas/qualificação de leads
- Não existe nos projectos anteriores (verificado PROJECTS_DONE.md)

---

## 🎨 Escolha de Estilo

**Estilo:** 🏛️ Swiss Minimal

**Porquê:**
1. É uma ferramenta B2B que precisa de transmitir profissionalismo
2. Os números devem falar por si — sem distracções
3. Simplicidade extrema ajuda foco nas métricas
4. Não foi usado em nenhum projecto anterior
5. Diferencia de Editorial Clean (ontem) e Retro Tech (anteontem)

**Características a aplicar:**
- Grid rígido
- Preto e branco + um accent (azul para CTA)
- Helvetica/Inter como font
- Muito espaço negativo
- Zero decoração — só o essencial

**Referências:**
- apple.com/shop (simplicidade)
- Swiss Style posters (tipografia como elemento)
- Dieter Rams (funcionalidade sobre decoração)

---

## 📋 Fases

### Fase 1: Estrutura HTML (20 min)
- [ ] Layout com grid
- [ ] Inputs: preço médio, frequência visitas/ano, taxa retenção, taxa referral
- [ ] Outputs: CLV, max CAC, break-even ROAS
- [ ] Cenários slider

### Fase 2: Estilo CSS (20 min)
- [ ] Aplicar Swiss Minimal
- [ ] Tipografia clara
- [ ] Inputs minimalistas
- [ ] Números grandes e legíveis

### Fase 3: JavaScript (30 min)
- [ ] Cálculos reactivos
- [ ] Visualização de cenários
- [ ] Animações subtis nos números

### Fase 4: Polish (20 min)
- [ ] Responsivo
- [ ] Testar edge cases
- [ ] Microinteracções

### Fase 5: Deploy (10 min)
- [ ] Mover para overnight/
- [ ] Actualizar index.html
- [ ] Git push

---

## ✅ Critérios de Sucesso

1. Calculadora funcional com inputs realistas
2. Output claro: "Podes gastar até €X por cliente"
3. Estilo coerente com Swiss Minimal
4. Zero bugs nos cálculos
5. Mobile-friendly

---

## 📊 Fórmulas

```
CLV = (Preço Médio × Frequência Anual × Anos Retenção) + (CLV × Taxa Referral)
Max CAC = CLV × Margem Aceite (ex: 30%)
Break-even ROAS = Preço / (Preço - Custo)
```
