# 🎁 Entrega Nocturna — 28 Janeiro 2026

## 💡 Idea Tracker

Uma aplicação para capturar e organizar as tuas ideias de negócio/projectos.

---

### 🚀 Como usar

1. **Abrir no browser:**
   ```
   file:///root/clawd/overnight/2026-01-28/idea-tracker.html
   ```
   Ou simplesmente: clica duas vezes no ficheiro

2. **Adicionar uma ideia:**
   - Clica em "Nova Ideia" (ou Ctrl+N)
   - Preenche o título e descrição
   - Avalia: Esforço, Potencial de Receita, Match com Skills
   - O score é calculado automaticamente!

3. **Gerir ideias:**
   - Filtrar por estado (Ideia → Pesquisando → Validando → Construindo → Lançado)
   - Ordenar por Score, Data, Potencial ou Esforço
   - Pesquisar por texto
   - Editar ou apagar a qualquer momento

---

### 📊 O Score

Fórmula: `(Potencial × 2) + (Skills × 1.5) - Esforço`

- **Verde (≥8):** Excelente oportunidade
- **Amarelo (5-7.9):** Potencial interessante
- **Cinza (<5):** Talvez não valha a pena

Quanto maior o score, melhor a relação esforço/retorno!

---

### ✨ Funcionalidades

| Feature | ✅ |
|---------|---|
| Dark theme | ✅ |
| Adicionar/Editar/Apagar | ✅ |
| Filtrar por estado | ✅ |
| Ordenar (score/data/potencial/esforço) | ✅ |
| Pesquisar | ✅ |
| Score automático | ✅ |
| Estatísticas no topo | ✅ |
| Dados guardados localmente | ✅ |
| Mobile responsive | ✅ |
| Português | ✅ |

---

### 💾 Dados

Os dados ficam guardados no `localStorage` do browser — não precisas de servidor.

**Nota:** Se limpares os dados do browser, perdes as ideias. Para backup, podes exportar manualmente via consola:
```javascript
copy(localStorage.getItem('ideas'))
```

---

### 🔮 Ideias para o futuro

Se gostares, posso adicionar:
- [ ] Export para JSON/CSV
- [ ] Tags personalizadas
- [ ] Notas/comentários por ideia
- [ ] Histórico de alterações
- [ ] Sync com Obsidian

---

**Tempo de desenvolvimento:** ~45 minutos
**Testado:** ✅ Funciona perfeitamente

Bom dia! ☀️

— Safira ✨
