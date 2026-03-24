# 🌿 Recovery Score Calculator

**Data:** 2026-03-24  
**Estilo:** Organic Soft 🌿  
**Categoria:** Fitness/Wellness  
**URL:** https://luzguilherme.github.io/safira-overnight/2026-03-24/

---

## 🎯 O Que É

Uma calculadora que ajuda atletas de endurance a decidir se devem treinar ou descansar, baseado em factores científicos de recuperação.

## 💡 Porquê Isto?

**Problema real:**
- Atletas de IRONMAN/endurance frequentemente over-train
- É difícil saber quando o corpo precisa de descanso vs quando "é só preguiça"
- Garmin/Whoop dão dados mas não decisões claras
- Muitas vezes ignoramos sinais até ter uma lesão

**Inspiração:**
- HN Show: "Aerko" - fitness PWA offline-first
- Reddit: Habit tracker que fez dinheiro
- Conceito de HRV/readiness scoring (Whoop, Garmin Body Battery)

**Relevância para o Guilherme:**
- Treina para IRONMAN 2026
- Usa Garmin Connect
- Complementa as ferramentas existentes com decisão actionable

## ✨ Funcionalidades

### Inputs
- **Sono:** Horas + qualidade (1-10)
- **Corpo:** Dores musculares + nível de energia
- **Mente:** Stress + motivação para treinar
- **Histórico:** Treino de ontem + dias desde último descanso
- **Extras:** Doença, lesão, viagem, desidratação

### Output
- **Recovery Score:** 0-100 com visual circular
- **Recomendação clara:**
  - 🏃 Train Hard (80+)
  - 💪 Train Normal (65-79)
  - 🚴 Easy to Moderate (50-64)
  - 🧘 Active Recovery (35-49)
  - 🛋️ Full Rest (<35)
- **Breakdown:** Pontuação por categoria
- **Tips:** Recomendações específicas para o dia

## 🎨 Estilo: Organic Soft

**Justificação:**
- Wellness/recovery → precisa de transmitir calma
- Cores suaves (tons terra, verdes) promovem sensação de cuidado
- Bordas arredondadas (16-24px) tornam a interface amigável
- Font Nunito (rounded, humanista) é acolhedora
- Não usado desde 2026-03-08 — diversificação de estilos ✅

**Paleta:**
- Background: #faf8f5 (creme suave)
- Verde principal: #6b9b6b
- Amber warning: #d4a86b
- Red alert: #c47c6b
- Text: #2d3a2d (verde escuro)

## 📊 Algoritmo

Score máximo: 100 pontos
- Sleep Score: até 25 pts (horas + qualidade)
- Body Score: até 25 pts (soreness invertido + energia)
- Mind Score: até 25 pts (stress invertido + motivação)
- Training Load: até 25 pts (penalizado por treino recente)
- Extras: penalizações (doença -15, lesão -10, viagem -5, desidratação -5)

## 🧪 Testing

- [x] Todos os sliders funcionam
- [x] Valores actualizam em tempo real
- [x] Cálculo correcto para diferentes cenários
- [x] Animação do círculo de score
- [x] Cores mudam conforme score
- [x] Tips contextualmente relevantes
- [x] Mobile responsive
- [x] Zero dependencies (vanilla HTML/CSS/JS)

## 🚀 Próximos Passos (se expandir)

1. **Histórico:** Guardar scores anteriores em localStorage
2. **Trends:** Gráfico de recovery ao longo da semana
3. **Integração Garmin:** Puxar dados de sono automaticamente
4. **Notificações:** PWA que lembra de fazer check-in matinal
5. **Export:** Partilhar score nas redes sociais

## 📁 Ficheiros

```
2026-03-24/
├── index.html      # App completa (single file)
└── DELIVERY.md     # Este ficheiro
```

---

*Recovery is training too.* 🌿
