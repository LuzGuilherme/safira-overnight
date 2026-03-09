# 🧾 QuickInvoice — Facturas Instantâneas

> **Data:** 2026-03-09
> **Estilo:** Editorial Clean ☀️
> **Categoria:** Ferramentas / Freelancers
> **Tempo de construção:** ~1h

---

## O Que É

Gerador de facturas profissionais, instantâneo, sem registo. Preenche, pré-visualiza, exporta PDF.

**Demo:** https://luzguilherme.github.io/safira-overnight/2026-03-09/quickinvoice.html

---

## Porquê Isto?

### O Problema
Freelancers e indie makers precisam de emitir facturas rapidamente. As opções existentes:
- **Apps completas** (Invoicely, FreshBooks): Requerem conta, são overkill para quem só quer um PDF rápido
- **Templates Word/Excel**: Parecem amadores, difíceis de customizar
- **Ferramentas online**: Pedem registo, guardam os dados, spam de emails

### A Solução
Uma ferramenta que:
- ✅ Não requer conta
- ✅ Dados ficam no browser (localStorage)
- ✅ Visual profissional
- ✅ Exporta PDF em segundos
- ✅ Guarda os dados do emissor para reutilizar
- ✅ Adaptado a Portugal (NIF, IVA)

---

## Funcionalidades

### ✍️ Editor Completo
- Dados do emissor (nome, NIF, morada, contactos)
- Dados do cliente
- Nº de factura e datas
- IVA configurável (0%, 6%, 13%, 23%)
- Lista de itens com quantidades e preços
- Notas/observações

### 👁️ Preview em Tempo Real
- Actualiza enquanto escreves
- Design profissional tipo factura real

### 💾 Persistência Local
- **Guardar:** Guarda no browser para continuar depois
- **Carregar:** Recupera factura guardada
- Os dados do emissor são lembrados automaticamente

### 📥 Exportação
- PDF de alta qualidade
- Imprimir directamente

---

## Stack Técnico

- **HTML/CSS/JS** — Single-file, zero dependências externas (excepto fonts e html2pdf)
- **html2pdf.js** — Geração de PDF no browser
- **Google Fonts** — Fraunces (headlines) + Inter (body)
- **localStorage** — Persistência de dados

---

## Estilo: Editorial Clean ☀️

**Justificação:**
- Facturas devem parecer profissionais e credíveis
- Foco no conteúdo, não em decoração
- Tipografia clássica (serif para títulos)
- Muito whitespace
- Cores sóbrias (accent blue subtil)

**Referências usadas:**
- Stripe Invoices
- Notion (simplicidade)
- Facturas tradicionais portuguesas

---

## Screenshots

### Editor
```
┌────────────────────────────────────────────┐
│ 📤 Os Seus Dados                           │
│ ┌─────────────────────────────────────────┐│
│ │ Nome / Empresa: [_____________________ ]││
│ │ NIF: [____________]                     ││
│ │ Morada: [____________________________ ]││
│ │ Email: [________] Telefone: [________ ]││
│ └─────────────────────────────────────────┘│
└────────────────────────────────────────────┘
```

### Preview
```
┌────────────────────────────────────────────┐
│                                            │
│  FACTURA                       FT 2026/001 │
│  ─────────────────────────────────────     │
│                                            │
│  De:                      Para:            │
│  A Sua Empresa            Cliente, S.A.    │
│  NIF: 123456789           NIF: 987654321   │
│                                            │
│  Descrição        Qtd   Preço     Total    │
│  ──────────────────────────────────────    │
│  Consultoria       10   €100    €1,000.00  │
│                                            │
│                      Subtotal: €1,000.00   │
│                      IVA 23%:    €230.00   │
│                      ─────────────────     │
│                      TOTAL:    €1,230.00   │
│                                            │
└────────────────────────────────────────────┘
```

---

## Melhorias Futuras (se validar)

1. **Múltiplas facturas** — Lista de facturas guardadas
2. **Templates** — Diferentes designs
3. **Logo upload** — Adicionar logo do emissor
4. **Recibos** — Versão "Recibo" além de "Factura"
5. **Moedas** — Suporte a USD, GBP, etc.
6. **QR Code** — Para pagamento MB Way ou IBAN

---

## Para o Guilherme

Isto pode ser útil para:
- Emitir facturas rápidas na Vence Media
- Freelance work
- Qualquer side project que precise de facturação

**Zero fricção** — abre, preenche, exporta. Sem contas, sem login.

---

*Feito com ❤️ às 2h da manhã*
