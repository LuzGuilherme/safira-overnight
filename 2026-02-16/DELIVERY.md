# Delivery: Strava Card Generator

## 🧠 Porquê Isto? (Raciocínio)

### Contexto
Hoje o Guilherme fez um trail run de 16.26km com 648m D+ e quis adicionar um overlay de Strava ao vídeo. O processo foi manual: converter imagem, ajustar transparência, usar FFmpeg. Esta ferramenta simplifica esse fluxo.

### Alternativas Consideradas
1. **Script Python automático** — ❌ Menos visual, precisa de CLI
2. **Integração directa com Strava API** — ❌ Complexo demais para overnight
3. **Web app com UI** — ✅ Visual, fácil de usar, pode gerar PNG para overlay

### Trade-offs Aceites
- ✅ Ganhamos: Interface visual, múltiplos templates, formatos para stories/posts
- ⚠️ Sacrificamos: Pull automático do Strava (entrada manual)

---

## 📦 O que é
Gerador de cards visuais para actividades do Strava. Permite criar imagens bonitas para partilhar em Instagram Stories, posts, ou usar como overlays em vídeos.

## 🎯 Problema que resolve
Criar overlays/cards de Strava de forma rápida e com bom design, sem precisar de Photoshop ou ferramentas complexas.

## ✨ Features
- 3 templates: Dark, Light, Minimal
- 3 formatos: Story (9:16), Square (1:1), Wide (16:9)
- 5 tipos de actividade: Corrida, Trail, Ciclismo, Natação, Triathlon
- Download directo como PNG (com transparência no Minimal)
- Preview em tempo real
- Design industrial, sem "AI slop"

## 🎨 Design
- **Aesthetic:** Industrial/Utilitarian — clean, funcional, performance-focused
- **Stack:** HTML + CSS + Vanilla JS + html2canvas
- **Font:** Space Grotesk (Google Fonts)
- **Colors:** Dark theme com acento Strava orange (#FC4C02)

## 📁 Ficheiros
- `index.html` — Aplicação completa (single file)

## 🔗 Link
https://luzguilherme.github.io/safira-overnight/2026-02-16/

## 💡 Como usar
1. Seleccionar tipo de actividade
2. Introduzir stats (distância, desnível, tempo)
3. Escolher template e formato
4. Clicar "Download PNG"
5. Usar no Instagram, vídeos, etc.

## 🔮 Próximos passos (se relevante)
- [ ] Integração com Strava API (pull automático)
- [ ] Mais templates (Neon, Vintage, etc.)
- [ ] Campo para nome da rota
- [ ] Opção de adicionar mapa da rota

---

*Build by Safira 🌙*
