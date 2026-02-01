---
title: AI Video Dubbing SaaS
created: 2026-01-29
tags:
  - idea
  - side-hustle
  - ai
  - saas
status: exploring
potential: 8
effort: 7
skills: 5
problem: "Criadores querem expandir para outros idiomas mas dubbing profissional custa milhares"
solution: "SaaS que auto-traduz + faz lip-sync com voz AI"
market: "YouTubers, course creators, SaaS com tutoriais"
---

# AI Video Dubbing SaaS

## Problem
Criadores de conteúdo querem expandir audiência para outros idiomas, mas:
- Legendas têm baixa conversão
- Dubbing profissional custa €2000+ por vídeo
- Qualidade de ferramentas amadoras é fraca

## Solution
Plataforma que automatiza:
1. Transcrição (Whisper)
2. Tradução (Claude/GPT)
3. Voice cloning (ElevenLabs/Fish Audio)
4. Lip sync (Wav2Lip/SadTalker)

## Market
- YouTubers com >100k subs
- Course creators (Udemy, Teachable)
- SaaS com video tutorials
- Agências de marketing

## Technical Stack
- **Transcrição:** Whisper API
- **Tradução:** Claude API
- **TTS:** ElevenLabs (voice cloning)
- **Lip Sync:** Wav2Lip ou SadTalker
- **Frontend:** Next.js
- **Backend:** Python + FastAPI
- **Queue:** Redis + Celery

## Pricing
- Starter: $29/mês (5 vídeos)
- Pro: $99/mês (20 vídeos)
- Agency: $199/mês (50 vídeos)

## Competition
- Rask AI
- HeyGen
- Papercup

> [!warning] Challenges
> - Lip sync ainda não é perfeito
> - Voice cloning precisa de samples
> - Custos de API podem ser altos

## Next Steps
- [ ] Testar pipeline completo manualmente
- [ ] Calcular unit economics
- [ ] Validar com 3 criadores

## Notes
Ideia surgiu no briefing de 2026-01-29. ^origin
