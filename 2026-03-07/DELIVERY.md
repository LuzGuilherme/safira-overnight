# 🛡️ VibeGuard — Security Scanner for AI-Generated Code

**Data:** 2026-03-07  
**Estilo:** Industrial Dark 🌙  
**Categoria:** Security / Developer Tools  
**Tempo:** ~1.5 horas

---

## 🎯 O que é

**VibeGuard** é um serviço de security scanning especializado em código gerado por AI (Claude, GPT, Cursor, etc.). A premissa é simples: LLMs escrevem código rápido, mas também escrevem vulnerabilidades rápido.

### Porquê isto?

1. **Timing perfeito:** "Vibe coding" explodiu em 2025-2026. Milhares de indie hackers estão a lançar apps construídas 90%+ por AI.

2. **Problema real:** LLMs são treinados em código público — incluindo código vulnerável. Padrões comuns:
   - Hardcoded API keys
   - SQL injection via string concatenation
   - Auth bypass por race conditions
   - CORS wildcard policies
   - Debug endpoints em produção

3. **Ideia validada:** Guilherme aprovou "AI Security Scanner para Vibe-Coded Apps" na sessão de 2026-01-29.

4. **Mercado existente:** Snyk, SonarQube, etc. existem, mas nenhum é posicionado especificamente para o nicho de "AI-generated code".

---

## ✨ Features do MVP

### Landing Page completa:
- **Hero** com scanner interactivo (demo mode)
- **Estatísticas** de social proof
- **Secção de problema** — educação sobre riscos
- **Features** — como funciona
- **Sample Report** — visualização de um scan real
- **Pricing** — modelo freemium ($0 / $29 / $99)

### Elementos técnicos:
- Design system consistente (Industrial Dark)
- Responsivo (mobile-ready)
- Interactividade (smooth scroll, demo scan)
- Copy persuasivo focado em dor

---

## 🎨 Escolha de Estilo

**Industrial Dark** foi escolhido porque:
1. Target audience são developers/indie hackers
2. Segurança pede seriedade e confiança
3. Não era usado há 3 semanas (desde 2026-02-19)
4. Referências: Vercel, Linear, Railway

Cores: 
- Background: #0a0a0a
- Accent: #22c55e (verde — segurança/sucesso)
- Danger: #ef4444 (vermelho — vulnerabilidades)

---

## 💡 Próximos Passos (se Guilherme quiser avançar)

### Validação rápida:
1. Post no Twitter/X sobre o problema
2. Landing page com waitlist
3. Fazer 5-10 scans manuais como "beta"

### MVP técnico:
1. Integração GitHub OAuth
2. Clone + scan básico (grep para patterns comuns)
3. Usar GPT/Claude para análise mais profunda
4. Gerar relatório automático

### Monetização:
- Free: 3 scans/mês (public repos)
- Pro: $29/mês (unlimited, private repos, CI/CD)
- Team: $99/mês (compliance, team features)

---

## 📁 Ficheiros

```
/root/clawd/overnight/2026-03-07/
├── index.html      # Landing page completa
└── DELIVERY.md     # Este ficheiro
```

---

## 🔗 Links

- **GitHub Pages:** https://luzguilherme.github.io/safira-overnight/2026-03-07/
- **Referências de design:** Vercel, Linear, Snyk

---

## 🏷️ Tags

`security` `developer-tools` `ai` `vibe-coding` `saas` `b2b`

---

*Construído por Safira 🌙*
