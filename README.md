# Tek Token

Base de conhecimento, hub de governança e especificação de produto de uma plataforma dupla da Tekto:

1. **Hub de propriedade intelectual (PI):** registro de autoria e licenciamento de projetos de engenharia em OpenBIM/IFC, representados como IP-NFT.
2. **Crowdfunding imobiliário de alta precisão:** captação com security tokens, apoiada em orçamento paramétrico BIM 5D, com escrow e liberação de recursos em tranches ligadas a marcos físicos do cronograma BIM 4D.

## Aviso importante

- **Este repositório é só documentação de planejamento.** Nada aqui é oferta pública, oferta privada, convite, solicitação ou anúncio de valores mobiliários, tokens ou qualquer investimento.
- **Não é recomendação de investimento nem aconselhamento jurídico, contábil ou tributário.** Toda regra legal, regulatória, financeira ou tributária aqui é decisão provisória, registrada em [docs/DUVIDAS.md](docs/DUVIDAS.md), até revisão do Samuel e de profissionais habilitados.
- **Fora do escopo:** arquitetura de software, stack de desenvolvimento, código da plataforma e infraestrutura de deploy. Isso fica num repositório técnico separado. Aqui ficam regras de negócio, conformidade regulatória, tokenomics e regras de produto.
- Normas e atos oficiais são citados por código e item (por exemplo, Resolução CVM 88, Lei 14.478/2022, ISO 19650). O texto das normas não é copiado.

## Módulos

- **M1** — Tokenização de PI (IP-NFT)
- **M2** — Orçamento BIM 5D
- **M3** — Tokenomics e crowdfunding
- **M4** — Governança e conformidade regulatória

## Como acompanhar

- Fila de trabalho: [docs/BACKLOG.md](docs/BACKLOG.md) (IDs TK-T001, TK-T002, ...), um item por PR.
- Dúvidas e decisões provisórias: [docs/DUVIDAS.md](docs/DUVIDAS.md).
- Checagem local: `npx --yes markdownlint-cli2 "**/*.md"` e `python3 scripts/verificar.py` (links internos, formato do backlog e das dúvidas). O script só confere a documentação deste repositório.

## Licença

Ainda não escolhida (ver D-001 em [docs/DUVIDAS.md](docs/DUVIDAS.md)). Até a decisão, nenhuma licença é concedida.
