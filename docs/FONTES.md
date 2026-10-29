# Catálogo de fontes oficiais

Lista das fontes primárias que o Tek Token usa, preenchida na TK-T005. Serve para quem escreve os módulos (saber qual ato citar e onde ele está) e para quem audita o repositório (conferir que cada regra aponta para uma fonte oficial). Cada linha traz o código do ato, a data, o link oficial, a data de acesso e o objeto do ato com palavras próprias, conferido na própria fonte. Regras de citação em [CONVENCOES.md](CONVENCOES.md).

Nada aqui é oferta de valores mobiliários, recomendação de investimento ou aconselhamento jurídico (ver o [README](../README.md)). Este catálogo diz **o que cada ato trata**; o que ele exige da plataforma é analisado nos itens dos módulos, sempre como decisão provisória em [DUVIDAS.md](DUVIDAS.md).

## Como usar e manter

- Antes de citar um artigo, abra o link oficial e confira a redação vigente; o catálogo registra só a situação na data de acesso.
- Ato alterado aparece com as alterações conhecidas na data de acesso; ato revogado sai da tabela principal e vai para a seção de histórico, com o ato que o revogou.
- Fonte nova usada em qualquer módulo entra aqui no mesmo PR.
- Norma técnica paga (ABNT, ISO) entra só com código, edição, estágio e página pública de catálogo, nunca com texto.

## 1. Mercado de valores mobiliários (CVM)

| Ato | Data | Objeto conferido na fonte | Situação na data de acesso | Usado em |
| --- | --- | --- | --- | --- |
| [Lei 6.385/1976](https://www.planalto.gov.br/ccivil_03/leis/l6385.htm) | 1976-12-07 | Organiza o mercado de valores mobiliários e cria a CVM. O art. 2º lista o que é valor mobiliário, incluindo, no inciso IX, os contratos de investimento coletivo ofertados publicamente | Em vigor, texto compilado | M1 (TK-T014), M3, M4 (TK-T032, TK-T033) |
| [Resolução CVM 88/2022](https://conteudo.cvm.gov.br/legislacao/resolucoes/resol088.html) | 2022-04-27 (DOU 2022-04-28) | Regula a oferta pública de valores mobiliários de sociedades empresárias de pequeno porte, com dispensa de registro, feita por plataforma eletrônica de investimento participativo; revogou a Instrução CVM 588/2017 | Em vigor, alterada pelas Resoluções CVM 158/2022 e 226/2025; usar o texto consolidado | M3 (TK-T022 a TK-T029), M4 (TK-T032) |
| [Resolução CVM 50/2021](https://conteudo.cvm.gov.br/legislacao/resolucoes/resol050.html) | DOU 2021-09-02 | Prevenção à lavagem de dinheiro e ao financiamento do terrorismo e da proliferação de armas de destruição em massa (PLD/FTP) no mercado de valores mobiliários; revogou a Instrução CVM 617/2019 | Em vigor, alterada pelas Resoluções CVM 179/2023 e 245/2026; tem nota explicativa própria | M4 (TK-T035) |
| [Parecer de Orientação CVM 40/2022](https://conteudo.cvm.gov.br/legislacao/pareceres-orientacao/pare040.html) | 2022-10-11 (DOU 2022-10-14) | "Os CriptoAtivos e o Mercado de Valores Mobiliários": orientação da CVM sobre quando um criptoativo é valor mobiliário e quais regras se aplicam a ele | Em vigor (parecer de orientação, não é norma com artigos) | M1 (TK-T014), M4 (TK-T033) |

Acesso: CVM, páginas das resoluções e do parecer — acesso em 2026-10-29. Planalto, Lei 6.385/1976 — acesso em 2026-10-29.

## 2. Ativos virtuais (Lei 14.478/2022 e Banco Central)

| Ato | Data | Objeto conferido na fonte | Situação na data de acesso | Usado em |
| --- | --- | --- | --- | --- |
| [Lei 14.478/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14478.htm) | 2022-12-21 | Diretrizes para a prestação de serviços de ativos virtuais e para a regulação das prestadoras (PSAV); cria o crime de fraude com ativos virtuais, valores mobiliários ou ativos financeiros no Código Penal e altera a Lei 7.492/1986 e a Lei 9.613/1998. O art. 1º, parágrafo único, exclui da lei os ativos que representam valores mobiliários sujeitos à Lei 6.385/1976 | Em vigor | M4 (TK-T034, TK-T035) |
| [Decreto 11.563/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/D11563.htm) | 2023-06-13 | Regulamenta a Lei 14.478/2022 e dá ao Banco Central a competência de regular os serviços de ativos virtuais e de autorizar e supervisionar as PSAV; o art. 3º repete que não se aplica a ativos que são valores mobiliários | Em vigor | M4 (TK-T034) |
| [Resolução BCB 519/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=519) | 2025-11-10 (DOU 2025-11-11) | Processos de autorização para funcionar de corretoras de câmbio, corretoras e distribuidoras de títulos e valores mobiliários e sociedades prestadoras de serviços de ativos virtuais | Em vigor (não revogada nem cancelada no buscador do BCB) | M4 (TK-T034) |
| [Resolução BCB 520/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=520) | 2025-11-10 (DOU 2025-11-11) | Constituição e funcionamento das sociedades prestadoras de serviços de ativos virtuais e prestação desses serviços por outras instituições autorizadas pelo BCB | Em vigor; versão 2 no buscador, alterada pela Resolução BCB 589/2026 (dispositivos com vigência a partir de 2026-10-01 e de 2027-01-01) | M4 (TK-T034) |
| [Resolução BCB 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) | 2025-11-10 (DOU 2025-11-11) | Altera as Resoluções BCB 277, 278 e 279/2022 (mercado de câmbio, Lei 14.286/2021) para incluir no mercado de câmbio atividades ou operações das PSAV, com base no art. 7º, inciso V, da Lei 14.478/2022 | Em vigor (não revogada nem cancelada no buscador do BCB) | M4 (TK-T034) |

Acesso: Planalto — acesso em 2026-10-29. Buscador de normas do BCB (dados de assunto, publicação e situação) — acesso em 2026-10-29.

## 3. Prevenção à lavagem de dinheiro e proteção de dados

| Ato | Data | Objeto conferido na fonte | Situação na data de acesso | Usado em |
| --- | --- | --- | --- | --- |
| [Lei 9.613/1998](https://www.planalto.gov.br/ccivil_03/leis/l9613.htm) | 1998-03-03 | Crimes de lavagem ou ocultação de bens, direitos e valores, prevenção do uso do sistema financeiro para esses crimes e criação do COAF; o art. 9º lista quem tem dever de identificar clientes, manter registros e comunicar operações, lista que a Lei 14.478/2022 ampliou para incluir as PSAV | Em vigor, texto compilado | M4 (TK-T035) |
| [Lei 13.709/2018 (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) | 2018-08-14 | Lei Geral de Proteção de Dados Pessoais: tratamento de dados pessoais, inclusive em meio digital, por pessoa física ou jurídica, pública ou privada; altera o Marco Civil da Internet | Em vigor, com alterações (entre elas a Lei 13.853/2019) | M4 (TK-T036), D-007 |

Acesso: Planalto — acesso em 2026-10-29.

## 4. Propriedade intelectual e responsabilidade técnica

| Ato | Data | Objeto conferido na fonte | Situação na data de acesso | Usado em |
| --- | --- | --- | --- | --- |
| [Lei 9.610/1998](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm) | 1998-02-19 | Lei de Direitos Autorais: altera, atualiza e consolida a legislação sobre direitos de autor e direitos conexos | Em vigor | M1 (TK-T009, TK-T011) |
| [Lei 6.496/1977](https://www.planalto.gov.br/ccivil_03/leis/l6496.htm) | 1977-12-07 | Institui a Anotação de Responsabilidade Técnica (ART) em obras e serviços de engenharia, arquitetura e agronomia; a ART define os responsáveis técnicos e é feita no CREA | Em vigor | M1 (TK-T009), M2 (TK-T020), M4 (TK-T039) |

Acesso: Planalto — acesso em 2026-10-29.

## 5. Orçamento de obras

| Ato | Data | Objeto conferido na fonte | Situação na data de acesso | Usado em |
| --- | --- | --- | --- | --- |
| [Decreto 7.983/2013](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7983.htm) | 2013-04-08 | Regras e critérios para o orçamento de referência de obras e serviços de engenharia pagos com recursos da União (custos de referência, composições, BDI). Para o Tek Token, vale só como referência de boa prática de orçamento, porque a plataforma não trata de obra pública | Sem marca de revogação na página do Planalto. O preâmbulo cita a Lei 8.666/1993, hoje substituída pela Lei 14.133/2021; usar o decreto só como referência metodológica | M2 (TK-T018, TK-T019) |

Acesso: Planalto — acesso em 2026-10-29.

## 6. Normas técnicas de BIM e IFC (só catálogo)

| Norma | Edição | Assunto (título oficial resumido) | Estágio ISO em 2026-10-28 | Adoção ABNT | Usado em |
| --- | --- | --- | --- | --- | --- |
| [ISO 19650-1](https://www.iso.org/standard/68078.html) | 2018 | Gestão da informação com BIM: conceitos e princípios | 90.92, a ser revisada | ABNT NBR ISO 19650-1:2022 (Versão Corrigida 2:2025) | M1 (TK-T010, TK-T012), M2 (TK-T016) |
| [ISO 19650-2](https://www.iso.org/standard/68080.html) | 2018 | Gestão da informação com BIM: fase de entrega dos ativos | 90.92, a ser revisada | ABNT NBR ISO 19650-2:2022 (Versão Corrigida 2:2025) | M2 (TK-T017, TK-T020) |
| [ISO 19650-3](https://www.iso.org/standard/75109.html) | 2020 | Gestão da informação com BIM: fase operacional dos ativos | 90.92, a ser revisada | ABNT NBR ISO 19650-3:2025 | Referência geral |
| [ISO 19650-4](https://www.iso.org/standard/78246.html) | 2022 | Gestão da informação com BIM: troca de informação | 60.60, publicada | ABNT NBR ISO 19650-4:2025 (situação não lida no catálogo ABNT) | Referência geral |
| [ISO 19650-5](https://www.iso.org/standard/74206.html) | 2020 | Abordagem voltada à segurança para a gestão da informação | 90.93, confirmada | ABNT NBR ISO 19650-5:2025 | Referência geral |
| [ISO 19650-6](https://www.iso.org/standard/82705.html) | 2025 | Informações de saúde e segurança | 60.60, publicada | ABNT NBR ISO 19650-6:2026 | Referência geral |
| [ISO 16739-1](https://www.iso.org/standard/84123.html) | 2024 | Industry Foundation Classes (IFC) para troca de dados na construção e na gestão de facilidades: esquema de dados (substituiu a edição de 2018) | 60.60, publicada | Sem adoção ABNT registrada aqui | M1 (TK-T010), M2 (TK-T016) |
| [ISO 7817-1](https://www.iso.org/standard/82914.html) | 2024 | BIM, nível de informação necessária: conceitos e princípios (partes 2 e 3 em elaboração) | 60.60, publicada | Sem adoção ABNT registrada aqui | M2 (TK-T016) |

Acesso: [catálogo do ISO/TC 59/SC 13](https://www.iso.org/committee/49180/x/catalogue/) e páginas de cada norma — acesso em 2026-10-28 e 2026-10-29. Edições e situação ABNT da série 19650 vêm da leitura do [ABNT Catálogo](https://www.abntcatalogo.com.br/) de 2026-10-28 registrada no Tek Team (`pesquisa/iso-19650-visao-geral.md`). Para o IFC, a buildingSMART mantém as [especificações públicas do esquema](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/), que servem de apoio à ISO 16739-1.

## 7. Pendências de conferência

Fontes previstas no backlog que ainda não entram nas tabelas, porque o objeto ou a edição não foi conferido numa fonte primária:

| Fonte | Item que precisa | O que falta |
| --- | --- | --- |
| ABNT NBR 12721 (custos unitários de construção, base do CUB) | TK-T018 | Edição vigente e título oficial no ABNT Catálogo (leitura no portal, fora das rotinas) |
| ABNT NBR ISO 19650-4:2025 | Referência geral | Situação no ABNT Catálogo |
| Resoluções CVM 158/2022, 226/2025, 179/2023 e 245/2026 | TK-T032, TK-T035 | Objeto de cada alteração; por ora basta usar o texto consolidado da CVM 88 e da CVM 50 |
| Atos do COAF, da ANPD e do CONFEA citados nos módulos | TK-T031, TK-T035, TK-T036, TK-T039 | Entram quando o item que os usa for feito |

## Histórico

| Ato | Situação | Substituído por |
| --- | --- | --- |
| Instrução CVM 588/2017 | Revogada | Resolução CVM 88/2022 |
| Instrução CVM 617/2019 | Revogada | Resolução CVM 50/2021 |
| ISO 16739-1:2018 | Retirada (95.99) | ISO 16739-1:2024 |
