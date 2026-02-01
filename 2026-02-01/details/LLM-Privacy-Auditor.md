---
title: LLM Privacy Auditor
created: 2026-01-29
tags:
  - idea
  - side-hustle
  - ai
  - security
  - privacy
  - b2b
status: exploring
potential: 8
effort: 6
skills: 6
problem: "Empresas não sabem que dados sensíveis os funcionários enviam para AI tools"
solution: "Proxy que audita e alerta sobre dados enviados para LLMs"
market: "Enterprise IT, Security teams, Compliance officers"
---

# LLM Privacy Auditor

## Problem
Com a explosão de AI tools (ChatGPT, Claude, Copilot, Cursor):
- **Funcionários copiam código, emails, dados de clientes** para LLMs
- **IT não tem visibilidade** sobre o que é enviado
- **Compliance nightmare** — GDPR, HIPAA, SOC2
- **Data leaks acidentais** são inevitáveis

> [!important] Trending on HN (validação forte!)
> "Sherlock" - A MitM proxy to see what your LLM tools are sending
> **215 pontos, 119 comentários** (30 Jan 2026) — demanda clara!
> Link: github.com/jmuncor/sherlock

## Solution
**SaaS/On-prem que audita tráfego para LLMs:**

1. **Proxy Layer:** Interceta requests para OpenAI, Anthropic, etc.
2. **Data Classification:** Detecta PII, código, credentials, dados sensíveis
3. **Policy Engine:** Bloqueia ou alerta baseado em regras
4. **Dashboard:** Visibilidade total para IT/Security
5. **Reports:** Compliance reports para auditorias

### Features Chave
- **Shadow AI Discovery** — descobre que AI tools estão a ser usados
- **Data Loss Prevention** — bloqueia envio de dados sensíveis
- **Audit Trail** — log completo para compliance
- **Anomaly Detection** — alerta padrões suspeitos

## Market
| Segmento | Dor | Budget |
|----------|-----|--------|
| Enterprises (500+) | Compliance, data loss | $5K-50K/ano |
| Mid-market (50-500) | Visibility, control | $1K-5K/ano |
| Regulated industries | HIPAA, SOC2, GDPR | Premium pricing |

**TAM:** $2B+ (AI security market growing 30%/year)

## Technical Stack
- **Proxy:** mitmproxy, custom TLS interception
- **Classification:** Fine-tuned models para PII detection
- **Backend:** Go/Rust (performance crítica)
- **Dashboard:** React + charts
- **Deploy:** Docker, Kubernetes, on-prem option

## Pricing
- **Starter:** $99/mês — até 50 users, basic policies
- **Business:** $499/mês — até 500 users, advanced features
- **Enterprise:** Custom — on-prem, SSO, dedicated support

## Competition
| Tool | Foco | Gap |
|------|------|-----|
| Nightfall AI | DLP geral | Não específico para LLMs |
| Lakera | LLM security | Foco em prompt injection |
| Open source (Sherlock) | Dev tool | Não é enterprise-ready |

> [!tip] Oportunidade
> Mercado novo, poucos players established, enterprises precisam AGORA.

## Challenges
- [ ] Complexidade técnica (TLS interception)
- [ ] Enterprise sales cycle longo
- [ ] Precisa de credibilidade/trust
- [ ] Competição vai aparecer rápido

## Validation Ideas
- Criar versão open source primeiro (like Sherlock)
- Ganhar traction na comunidade dev
- Converter para paid enterprise features

## Next Steps
- [ ] Estudar Sherlock (github.com/jmuncor/sherlock)
- [ ] Testar com setup básico no nosso VPS
- [ ] Landing page para enterprise waitlist
- [ ] Contactar 5 security professionals para feedback

## Notes
**Prós:**
- Mercado quente (AI security)
- B2B = higher ACV
- Pode começar como open source

**Contras:**
- Mais técnico que outros projectos
- Enterprise sales é diferente
- Precisa de investimento em credibilidade

---

*Ideia encontrada via Hacker News Show HN (210 pontos) — 2026-01-29*
