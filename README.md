# Tek Token

Base de conhecimento, hub de governança e especificação de produto de uma plataforma dupla da Tekto:

1. **Hub de propriedade intelectual (PI):** registro de autoria e licenciamento de projetos de engenharia em OpenBIM/IFC, representados como IP-NFT.
2. **Crowdfunding imobiliário de alta precisão:** captação com security tokens, apoiada em orçamento paramétrico BIM 5D, com escrow e liberação de recursos em tranches ligadas a marcos físicos do cronograma BIM 4D.

## Aviso importante

- **Este repositório é só documentação de planejamento.** Nada aqui é oferta pública, oferta privada, convite, solicitação ou anúncio de valores mobiliários, tokens ou qualquer investimento. Não há empreendimento, valor de captação nem retorno esperado neste repositório (D-008).
- **Não é recomendação de investimento nem aconselhamento jurídico, contábil ou tributário.** Toda regra legal, regulatória, financeira ou tributária aqui é decisão provisória, registrada em [docs/DUVIDAS.md](docs/DUVIDAS.md), até revisão do Samuel e de profissionais habilitados.
- **Fora do escopo:** arquitetura de software, stack de desenvolvimento, código da plataforma e infraestrutura de deploy. Isso fica num repositório técnico separado. Aqui ficam regras de negócio, conformidade regulatória, tokenomics e regras de produto.
- Normas e atos oficiais são citados por código e item (por exemplo, Resolução CVM 88/2022, Lei 14.478/2022, ISO 19650). O texto das normas não é copiado.

## Para quem é este repositório

### Lado da oferta: engenheiros, escritórios e incorporadores

Quem produz o projeto e quem quer construir.

| Pergunta | Onde está (ou vai estar) |
| --- | --- |
| Como registro a autoria de um projeto IFC? | [M1 — README](m1-tokenizacao-pi/README.md), [evidência de autoria](m1-tokenizacao-pi/evidencia-autoria-ifc.md), [regras do MVP](m1-tokenizacao-pi/regras-produto-registro.md) |
| Que direitos tenho sobre o projeto e como licencio? | [autoria e direitos](m1-tokenizacao-pi/autoria-e-direitos.md), [modelos de licenciamento](m1-tokenizacao-pi/modelos-licenciamento.md), [ciclo de vida do IP-NFT](m1-tokenizacao-pi/ciclo-vida-ip-nft.md) |
| O que meu modelo precisa ter para ser orçado em 5D? | [requisitos de informação](m2-orcamento-5d/requisitos-informacao-modelo.md), [fluxo de orçamento 5D](m2-orcamento-5d/fluxo-orcamento-5d.md) |
| Como um empreendimento vira oferta e como recebo os recursos? | [marcos 4D](m3-tokenomics-crowdfunding/marcos-4d.md), [escrow e tranches](m3-tokenomics-crowdfunding/escrow-e-tranches.md), [exceções](m3-tokenomics-crowdfunding/excecoes-escrow.md) |
| Que responsabilidade técnica assumo? | [auditoria e responsabilidade](m4-governanca-conformidade/auditoria-e-responsabilidade.md), [matriz RACI](m4-governanca-conformidade/matriz-raci.md) |

### Lado da demanda: investidores e auditores

Quem avalia o risco e quem confere os números.

| Pergunta | Onde está (ou vai estar) |
| --- | --- |
| De onde vem o orçamento e quem o auditou? | [auditoria do orçamento 5D](m2-orcamento-5d/auditoria-orcamento-5d.md), [fontes de preço](m2-orcamento-5d/fontes-de-preco.md), [BDI e contingência](m2-orcamento-5d/bdi-contingencia.md) |
| Quando e como o dinheiro sai do escrow? | [escrow e tranches](m3-tokenomics-crowdfunding/escrow-e-tranches.md), [marcos 4D](m3-tokenomics-crowdfunding/marcos-4d.md) |
| O que acontece se a obra atrasar ou parar? | [exceções do escrow](m3-tokenomics-crowdfunding/excecoes-escrow.md), [mudanças e versões do orçamento](m2-orcamento-5d/mudancas-e-versoes.md) |
| Que direitos e informações o token dá? | [estrutura do security token](m3-tokenomics-crowdfunding/estrutura-security-token.md), [direitos do investidor](m3-tokenomics-crowdfunding/direitos-investidor.md), [mercado secundário](m3-tokenomics-crowdfunding/mercado-secundario.md) |
| Qual regra regulatória vale e quem a cumpre? | [mapa da CVM 88](m4-governanca-conformidade/mapa-cvm-88.md), [tokenização na CVM](m4-governanca-conformidade/tokenizacao-cvm.md), [ativos virtuais e BCB](m4-governanca-conformidade/ativos-virtuais-bcb.md), [KYC e PLD](m4-governanca-conformidade/kyc-pld.md), [LGPD](m4-governanca-conformidade/lgpd.md) |
| Como a plataforma evita conflito de interesses? | [governança da plataforma](m4-governanca-conformidade/governanca-plataforma.md), [riscos](docs/RISCOS.md) |

## Módulos

| Módulo | Conteúdo | Lado principal |
| --- | --- | --- |
| [M1 — Tokenização de PI](m1-tokenizacao-pi/README.md) | autoria, evidência, licenças e ciclo de vida do IP-NFT | oferta |
| [M2 — Orçamento BIM 5D](m2-orcamento-5d/README.md) | do IFC ao orçamento paramétrico auditado | oferta e auditores |
| [M3 — Tokenomics e crowdfunding](m3-tokenomics-crowdfunding/README.md) | security token, escrow, tranches por marco 4D, receita | demanda |
| [M4 — Governança e conformidade](m4-governanca-conformidade/README.md) | CVM, BCB, PLD/FT, LGPD, tributação, governança | os dois |

A árvore completa de arquivos e o item que preenche cada um estão em [docs/ESTRUTURA.md](docs/ESTRUTURA.md). Fases do produto, do MVP de registro de PI ao crowdfunding em conformidade com a CVM 88: [docs/ROADMAP.md](docs/ROADMAP.md) (TK-T041).

## Relação com outros repositórios Tekto

O Tek Token só descreve regras e fluxos. Cálculo vem do tek-calc, normas e especificações do tek-docs, materiais do tek-catalog e modelos IFC do tek-studio e do tek-model. Preço de referência e cronograma físico ainda não têm origem definida em nenhum repositório Tekto (D-011). O detalhe fica em [docs/RELACAO-TEKTO.md](docs/RELACAO-TEKTO.md) (TK-T006).

## Como acompanhar

- Fila de trabalho: [docs/BACKLOG.md](docs/BACKLOG.md) (IDs TK-T001, TK-T002, ...), um item por PR.
- Dúvidas e decisões provisórias: [docs/DUVIDAS.md](docs/DUVIDAS.md).
- Painel: [painel central da Tekto](https://samalencar.github.io/painel-central/#token).
- Checagem local: `npx --yes markdownlint-cli2 "**/*.md"` e `python3 scripts/verificar.py` (links internos, formato do backlog e das dúvidas). O script só confere a documentação deste repositório.

## Licença

Ainda não escolhida (ver D-001 em [docs/DUVIDAS.md](docs/DUVIDAS.md)). Até a decisão, nenhuma licença é concedida.
