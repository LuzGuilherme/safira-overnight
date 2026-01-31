# BigIdeasDB Portugal — Improvements Log

> Actualizações ao dashboard de oportunidades baseadas em dados do Portal da Queixa

---

## 🚀 2026-01-31 — Live Scraper + Validation Score

### O que foi implementado

#### 1. Live Scraper (`/root/clawd/scripts/bigideas_scraper.py`)

Script Python para extracção automática de dados do Portal da Queixa:

**Funcionalidades:**
- Scraping de 8 categorias principais (logística, telecom, público, beleza, mobiliário, pets, tech, finanças)
- Extracção de marcas, subcategorias e queixas recentes
- Detecção de tendências comparando com dados anteriores
- Baseline dos dados oficiais do Barómetro 2025

**Output (em `/root/clawd/data/bigideas/`):**
- `complaints.json` — Dados raw do scraping
- `trends.json` — Análise de tendências e alertas
- `opportunities.json` — Oportunidades com Validation Scores
- `last_scrape.json` — Metadata do último scrape
- `dashboard_data.js` — Dados formatados para injectar no HTML

**Uso:**
```bash
# Scrape completo (com rate limiting)
python3 /root/clawd/scripts/bigideas_scraper.py

# Modo rápido (só gera dados, sem HTTP requests)
python3 /root/clawd/scripts/bigideas_scraper.py --quick
```

---

#### 2. Validation Score System

Sistema de pontuação (0-100) para priorizar oportunidades de negócio:

| Componente | Peso | Critério |
|------------|------|----------|
| **Volume** | 0-25 pts | Número de queixas no sector (mais = mais oportunidade) |
| **Tendência** | 0-25 pts | Crescimento YoY (>50% = 25 pts, >30% = 22 pts...) |
| **Build Ease** | 0-25 pts | Tempo estimado de desenvolvimento (≤1 sem = 25 pts) |
| **Competição** | 0-25 pts | Menos concorrência = mais pontos |

**Escalas de cor:**
- 🟢 **80-100**: Excelente (verde)
- 🔵 **60-79**: Bom (azul)
- 🟠 **40-59**: Médio (laranja)
- 🔴 **<40**: Baixo (vermelho)

---

### Ranking Actual (31 Jan 2026)

| # | Oportunidade | Score | Destaque |
|---|--------------|-------|----------|
| 🥇 | Assistente para Cancelar Serviços | **91/100** | Build rápido + baixa competição |
| 🥈 | Monitor de Insolvências PT | **86/100** | Zero competição + tendência forte |
| 🥉 | Verificador de Lojas Online PT | **83/100** | Tendência +51.9% + baixa competição |
| 4 | Comparador de Operadoras | 76/100 | Alta competição baixa score |
| 5 | Directory Clínicas Estéticas | 75/100 | Tendência forte (+52.5%) |
| 6 | Tracker de Encomendas | 72/100 | Volume alto mas competição média |
| 7 | Bot de Apoio IHRU/AIMA | 71/100 | Build complexo baixa score |
| 8 | Pet Services Marketplace | 57/100 | Volume baixo + build complexo |

---

### Alterações ao Dashboard

1. **Novo CSS** para Validation Scores:
   - Círculos de score com gradiente visual
   - Breakdown dos 4 componentes em cada card
   - Destaque visual para top 3 (bordas coloridas)

2. **Top 3 Ranking** no topo da secção de oportunidades

3. **Legenda explicativa** no final da secção

4. **Badges actualizados** com medalhas (#1, #2, #3)

---

### Ficheiros Modificados/Criados

```
/root/clawd/
├── scripts/
│   └── bigideas_scraper.py         # NOVO - Scraper Python
├── data/
│   └── bigideas/
│       ├── complaints.json         # NOVO - Dados scraping
│       ├── trends.json             # NOVO - Tendências
│       ├── opportunities.json      # NOVO - Oportunidades com scores
│       ├── last_scrape.json        # NOVO - Metadata
│       └── dashboard_data.js       # NOVO - JS para dashboard
└── overnight/
    └── 2026-01-31/
        ├── bigideas-portugal.html  # EDITADO - Com Validation Scores
        └── IMPROVEMENTS.md         # NOVO - Esta documentação
```

---

### Próximos Passos (Sugestões)

1. **Automatizar scrape diário** via cron
2. **Adicionar histórico** para ver evolução dos scores
3. **Notificações** quando um sector "aquece" (>40% crescimento)
4. **API endpoint** para consumir dados em tempo real
5. **Filtros no dashboard** (por score, sector, tempo de build)

---

*Implementado por Safira • 31 Janeiro 2026*
