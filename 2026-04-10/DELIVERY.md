# 🌙 Overnight Build — Trust Gap Scanner 🛡️

## O que é
Uma ferramenta standalone para founders SaaS avaliarem **prontidão de segurança/compliance** em menos de 5 minutos.

Transforma 12 controlos base (MFA, backups, incident response, vendors, etc.) em:
- **Score 0-100**
- **Grade A-F**
- **Tabela de riscos prioritários**
- **Plano de remediação de 30 dias** exportável

## Porque este projecto
### Sinais de pesquisa (esta noite)
- **Hacker News / Show HN:** projectos ligados a auditoria/compliance (SOC2 reports scoring)
- **Product Hunt:** tendência de produtos AI com camada de governance/trust
- **Reddit r/SideProject:** foco crescente em tools que ajudam a ir de “hack” para “produto vendável”

### Tese
Muitos founders constroem rápido, mas perdem deals quando surge due diligence básica de segurança. Um “security readiness scanner” resolve dor real, com utilidade imediata para pré-venda B2B.

## Estilo escolhido
- **Newspaper / Editorial Classic 📰**

### Justificação
- Tema de credibilidade/risco pede visual sóbrio e factual
- Hierarquia editorial melhora leitura de checklist + relatório
- Contraste com estilos recentes (Neo Brutalist / Swiss / Data Dense)

## Funcionalidades implementadas
1. Checklist de 12 controlos com pesos
2. Score percentual + grade A-F
3. Indicador visual de progresso
4. Tabela de riscos detectados (nível + impacto)
5. Plano automático de 30 dias
6. Presets rápidos (MVP cedo / SaaS maduro)
7. Copiar resumo para clipboard
8. Export TXT do relatório

## Stack
- HTML + CSS + JavaScript vanilla
- Sem dependências

## Testes manuais
- ✅ Score recalcula conforme checks marcados
- ✅ Grade e label mudam por thresholds
- ✅ Riscos ordenam por criticidade
- ✅ Presets aplicam cenários esperados
- ✅ Reset limpa avaliação
- ✅ Export TXT gera ficheiro válido
- ✅ Layout responsivo em mobile

## Path
`/root/clawd/overnight/2026-04-10/index.html`

## Próximos upgrades (opcional)
- Benchmarks por tipo de SaaS (B2B, health, fintech)
- Modo “cliente enterprise” com requisitos extra
- Evidências anexáveis por controlo
- Save/load via localStorage
