# Estrutura do repositório

Árvore de arquivos `.md` do Tek Token, criada na TK-T001. Cada arquivo nasce como esqueleto e é preenchido pelo item do [backlog](BACKLOG.md) indicado na tabela. A estrutura cobre só negócio, produto, tokenomics, governança e conformidade; arquitetura de software, stack e infraestrutura ficam no repositório técnico separado.

## Árvore

```text
tek-token/
├── README.md
├── docs/
│   ├── BACKLOG.md
│   ├── CONVENCOES.md
│   ├── CRITERIOS-FASES.md
│   ├── DUVIDAS.md
│   ├── ESTRUTURA.md
│   ├── FONTES.md
│   ├── GLOSSARIO.md
│   ├── PONTOS-PARA-ESPECIALISTAS.md
│   ├── RELACAO-TEKTO.md
│   ├── REQUISITOS-NEGOCIO.md
│   ├── RISCOS.md
│   └── ROADMAP.md
├── m1-tokenizacao-pi/
│   ├── README.md
│   ├── autoria-e-direitos.md
│   ├── ciclo-vida-ip-nft.md
│   ├── enquadramento-regulatorio-ip-nft.md
│   ├── evidencia-autoria-ifc.md
│   ├── modelos-licenciamento.md
│   └── regras-produto-registro.md
├── m2-orcamento-5d/
│   ├── README.md
│   ├── auditoria-orcamento-5d.md
│   ├── bdi-contingencia.md
│   ├── fluxo-orcamento-5d.md
│   ├── fontes-de-preco.md
│   ├── mudancas-e-versoes.md
│   └── requisitos-informacao-modelo.md
├── m3-tokenomics-crowdfunding/
│   ├── README.md
│   ├── direitos-investidor.md
│   ├── escrow-e-tranches.md
│   ├── estrutura-security-token.md
│   ├── excecoes-escrow.md
│   ├── marcos-4d.md
│   ├── mercado-secundario.md
│   ├── modelo-receita.md
│   └── tokenomics-ip.md
├── m4-governanca-conformidade/
│   ├── README.md
│   ├── ativos-virtuais-bcb.md
│   ├── auditoria-e-responsabilidade.md
│   ├── governanca-plataforma.md
│   ├── kyc-pld.md
│   ├── lgpd.md
│   ├── mapa-cvm-88.md
│   ├── matriz-raci.md
│   ├── tokenizacao-cvm.md
│   └── tributacao-provisoria.md
└── scripts/
    └── verificar.py
```

## Módulos

- **M1** — [Tokenização de PI](../m1-tokenizacao-pi/README.md): autoria e licenciamento de projetos OpenBIM/IFC como IP-NFT (lado da oferta).
- **M2** — [Orçamento BIM 5D](../m2-orcamento-5d/README.md): orçamento paramétrico a partir do IFC e sua auditoria.
- **M3** — [Tokenomics e crowdfunding](../m3-tokenomics-crowdfunding/README.md): security token, escrow e tranches por marco 4D (lado da demanda).
- **M4** — [Governança e conformidade](../m4-governanca-conformidade/README.md): CVM, BCB, PLD/FT, LGPD, tributação e governança.

## Arquivo por item

| Arquivo | Item(ns) do backlog |
| --- | --- |
| [README.md](../README.md) | TK-T002 |
| [docs/BACKLOG.md](BACKLOG.md) | fila e dúvidas (todas as execuções) |
| [docs/CONVENCOES.md](CONVENCOES.md) | TK-T003 |
| [docs/CRITERIOS-FASES.md](CRITERIOS-FASES.md) | TK-T042 |
| [docs/DUVIDAS.md](DUVIDAS.md) | fila e dúvidas (todas as execuções) |
| [docs/ESTRUTURA.md](ESTRUTURA.md) | TK-T001 |
| [docs/FONTES.md](FONTES.md) | TK-T005 |
| [docs/GLOSSARIO.md](GLOSSARIO.md) | TK-T004, TK-T044 |
| [docs/PONTOS-PARA-ESPECIALISTAS.md](PONTOS-PARA-ESPECIALISTAS.md) | TK-T046 |
| [docs/RELACAO-TEKTO.md](RELACAO-TEKTO.md) | TK-T006 |
| [docs/REQUISITOS-NEGOCIO.md](REQUISITOS-NEGOCIO.md) | TK-T045 |
| [docs/RISCOS.md](RISCOS.md) | TK-T007, TK-T043 |
| [docs/ROADMAP.md](ROADMAP.md) | TK-T041 |
| [m1-tokenizacao-pi/README.md](../m1-tokenizacao-pi/README.md) | TK-T008 |
| [m1-tokenizacao-pi/autoria-e-direitos.md](../m1-tokenizacao-pi/autoria-e-direitos.md) | TK-T009 |
| [m1-tokenizacao-pi/ciclo-vida-ip-nft.md](../m1-tokenizacao-pi/ciclo-vida-ip-nft.md) | TK-T012 |
| [m1-tokenizacao-pi/enquadramento-regulatorio-ip-nft.md](../m1-tokenizacao-pi/enquadramento-regulatorio-ip-nft.md) | TK-T014 |
| [m1-tokenizacao-pi/evidencia-autoria-ifc.md](../m1-tokenizacao-pi/evidencia-autoria-ifc.md) | TK-T010 |
| [m1-tokenizacao-pi/modelos-licenciamento.md](../m1-tokenizacao-pi/modelos-licenciamento.md) | TK-T011 |
| [m1-tokenizacao-pi/regras-produto-registro.md](../m1-tokenizacao-pi/regras-produto-registro.md) | TK-T013 |
| [m2-orcamento-5d/README.md](../m2-orcamento-5d/README.md) | TK-T015 |
| [m2-orcamento-5d/auditoria-orcamento-5d.md](../m2-orcamento-5d/auditoria-orcamento-5d.md) | TK-T020 |
| [m2-orcamento-5d/bdi-contingencia.md](../m2-orcamento-5d/bdi-contingencia.md) | TK-T019 |
| [m2-orcamento-5d/fluxo-orcamento-5d.md](../m2-orcamento-5d/fluxo-orcamento-5d.md) | TK-T017 |
| [m2-orcamento-5d/fontes-de-preco.md](../m2-orcamento-5d/fontes-de-preco.md) | TK-T018 |
| [m2-orcamento-5d/mudancas-e-versoes.md](../m2-orcamento-5d/mudancas-e-versoes.md) | TK-T021 |
| [m2-orcamento-5d/requisitos-informacao-modelo.md](../m2-orcamento-5d/requisitos-informacao-modelo.md) | TK-T016 |
| [m3-tokenomics-crowdfunding/README.md](../m3-tokenomics-crowdfunding/README.md) | TK-T022 |
| [m3-tokenomics-crowdfunding/direitos-investidor.md](../m3-tokenomics-crowdfunding/direitos-investidor.md) | TK-T028 |
| [m3-tokenomics-crowdfunding/escrow-e-tranches.md](../m3-tokenomics-crowdfunding/escrow-e-tranches.md) | TK-T026 |
| [m3-tokenomics-crowdfunding/estrutura-security-token.md](../m3-tokenomics-crowdfunding/estrutura-security-token.md) | TK-T024 |
| [m3-tokenomics-crowdfunding/excecoes-escrow.md](../m3-tokenomics-crowdfunding/excecoes-escrow.md) | TK-T027 |
| [m3-tokenomics-crowdfunding/marcos-4d.md](../m3-tokenomics-crowdfunding/marcos-4d.md) | TK-T025 |
| [m3-tokenomics-crowdfunding/mercado-secundario.md](../m3-tokenomics-crowdfunding/mercado-secundario.md) | TK-T029 |
| [m3-tokenomics-crowdfunding/modelo-receita.md](../m3-tokenomics-crowdfunding/modelo-receita.md) | TK-T030 |
| [m3-tokenomics-crowdfunding/tokenomics-ip.md](../m3-tokenomics-crowdfunding/tokenomics-ip.md) | TK-T023 |
| [m4-governanca-conformidade/README.md](../m4-governanca-conformidade/README.md) | TK-T031 |
| [m4-governanca-conformidade/ativos-virtuais-bcb.md](../m4-governanca-conformidade/ativos-virtuais-bcb.md) | TK-T034 |
| [m4-governanca-conformidade/auditoria-e-responsabilidade.md](../m4-governanca-conformidade/auditoria-e-responsabilidade.md) | TK-T039 |
| [m4-governanca-conformidade/governanca-plataforma.md](../m4-governanca-conformidade/governanca-plataforma.md) | TK-T038 |
| [m4-governanca-conformidade/kyc-pld.md](../m4-governanca-conformidade/kyc-pld.md) | TK-T035 |
| [m4-governanca-conformidade/lgpd.md](../m4-governanca-conformidade/lgpd.md) | TK-T036 |
| [m4-governanca-conformidade/mapa-cvm-88.md](../m4-governanca-conformidade/mapa-cvm-88.md) | TK-T032 |
| [m4-governanca-conformidade/matriz-raci.md](../m4-governanca-conformidade/matriz-raci.md) | TK-T040 |
| [m4-governanca-conformidade/tokenizacao-cvm.md](../m4-governanca-conformidade/tokenizacao-cvm.md) | TK-T033 |
| [m4-governanca-conformidade/tributacao-provisoria.md](../m4-governanca-conformidade/tributacao-provisoria.md) | TK-T037 |
