# Backlog — Tek Token

Um item por PR, ramo `local/TK-TNNN-slug`. Cada item é um título de nível 3 dentro do módulo, no formato que o [painel central](https://samalencar.github.io/painel-central/#token) lê. Marcar `[x]` na linha de status quando o critério de aceite for atendido.

Fases: 0 fundação; 1 MVP de registro de PI; 2 licenciamento e orçamento 5D auditado, sem captação; 3 crowdfunding em conformidade com a CVM 88; 4 consolidação. Item jurídico, regulatório, financeiro ou tributário só gera decisão provisória em [DUVIDAS.md](DUVIDAS.md).

## Fundação

### TK-T001 — Árvore de diretórios com esqueleto .md por módulo

- Entregável: `docs/ESTRUTURA.md`
- Critério de aceite: pastas dos módulos M1 a M4 e de docs criadas, cada arquivo planejado existe como esqueleto que aponta o item que o preenche; docs/ESTRUTURA.md mostra a árvore; links internos verdes
- Depende de: nenhuma
- Fase: 0
- Status: [x] (26/10/2026)

### TK-T002 — Esboço do README para o lado da oferta e o lado da demanda

- Entregável: `README.md`
- Critério de aceite: README com seções para engenheiros e incorporadores (oferta) e para investidores e auditores (demanda), aviso de que não é oferta de valores mobiliários nem aconselhamento, e mapa dos módulos com links
- Depende de: TK-T001
- Fase: 0
- Status: [x] (26/10/2026)

### TK-T003 — Convenções do repositório

- Entregável: `docs/CONVENCOES.md`
- Critério de aceite: regras de citação (código, edição e item, sem copiar texto), formato de decisão provisória, idioma pt-BR, o que é fora de escopo (software, stack, infraestrutura) e como marcar conteúdo não verificado
- Depende de: TK-T001
- Fase: 0
- Status: [x] (27/10/2026)

### TK-T004 — Glossário inicial

- Entregável: `docs/GLOSSARIO.md`
- Critério de aceite: termos de RWA, IP-NFT, security token, escrow, tranche, BIM 4D e 5D, IFC, QTO, BDI, PSAV, KYC e PLD/FT definidos em linguagem simples, com a fonte de cada termo regulatório
- Depende de: TK-T003
- Fase: 0
- Referências: ISO 19650; ISO 16739-1
- Status: [x] (28/10/2026)

### TK-T005 — Catálogo de fontes oficiais

- Entregável: `docs/FONTES.md`
- Critério de aceite: lista das fontes primárias por código, data e link oficial com data de acesso: resoluções CVM, Lei 6.385/1976, Lei 14.478/2022, Resoluções BCB 519 a 521/2025, Lei 9.613/1998, LGPD, Lei 9.610/1998, ISO 19650, ISO 16739-1; o objeto de cada ato conferido na fonte
- Depende de: TK-T003
- Fase: 0
- Referências: Resolução CVM 88/2022; Lei 14.478/2022; ISO 19650
- Status: [x] (29/10/2026)

### TK-T006 — Relação com os repositórios Tekto

- Entregável: `docs/RELACAO-TEKTO.md`
- Critério de aceite: tabela do que o Tek Token consome de tek-calc (orçamento e cálculo), tek-docs (normas), tek-catalog (materiais e preços), tek-studio e tek-model (IFC), sem decisão de arquitetura
- Depende de: TK-T001
- Fase: 0
- Status: [x] (30/10/2026)

### TK-T007 — Registro de riscos inicial

- Entregável: `docs/RISCOS.md`
- Critério de aceite: riscos regulatório, jurídico, técnico de projeto, de orçamento, de obra, de contraparte, de reputação e de dados, cada um com causa, efeito, dono provisório e mitigação de negócio
- Depende de: TK-T005
- Fase: 0
- Status: [ ]

## M1 — Tokenização de PI

### TK-T008 — Visão do M1 e personas do lado da oferta

- Entregável: `m1-tokenizacao-pi/README.md`
- Critério de aceite: problema, proposta de valor, personas (engenheiro autor, escritório, incorporador licenciado) e jornada resumida, sem promessa de rendimento
- Depende de: TK-T002
- Fase: 1
- Status: [ ]

### TK-T009 — Autoria e direitos sobre projeto de engenharia

- Entregável: `m1-tokenizacao-pi/autoria-e-direitos.md`
- Critério de aceite: enquadramento provisório de direito autoral sobre projeto (Lei 9.610/1998, artigo e inciso citados), relação com ART e RRT e com titularidade do contratante; pontos para advogado em DUVIDAS
- Depende de: TK-T005
- Fase: 1
- Referências: Lei 9.610/1998; Lei 6.496/1977
- Status: [ ]

### TK-T010 — Pacote de evidência de autoria do modelo IFC

- Entregável: `m1-tokenizacao-pi/evidencia-autoria-ifc.md`
- Critério de aceite: lista dos elementos que provam autoria e integridade de uma versão do modelo (hash do arquivo, metadados IFC, responsável técnico, data, estado do contêiner de informação), sem definir tecnologia
- Depende de: TK-T008
- Fase: 1
- Referências: ISO 16739-1; ISO 19650-1
- Status: [ ]

### TK-T011 — Modelos de licenciamento do IP-NFT

- Entregável: `m1-tokenizacao-pi/modelos-licenciamento.md`
- Critério de aceite: tipos de licença (uso único, multiuso, exclusiva, derivação, adaptação a terreno) com direitos, limites, responsabilidade técnica e remuneração do autor; cada regra jurídica marcada como provisória
- Depende de: TK-T009
- Fase: 1
- Referências: Lei 9.610/1998
- Status: [ ]

### TK-T012 — Ciclo de vida do IP-NFT

- Entregável: `m1-tokenizacao-pi/ciclo-vida-ip-nft.md`
- Critério de aceite: estados e transições (rascunho, registrado, licenciado, revisado, substituído, revogado) e regra para nova versão do modelo, com quem aprova cada passo
- Depende de: TK-T010, TK-T011
- Fase: 1
- Referências: ISO 19650-1
- Status: [ ]

### TK-T013 — Regras de produto do MVP de registro de PI

- Entregável: `m1-tokenizacao-pi/regras-produto-registro.md`
- Critério de aceite: critérios de aceite de um projeto para registro, verificação mínima do autor, o que o MVP faz e não faz, métricas de sucesso
- Depende de: TK-T012
- Fase: 1
- Status: [ ]

### TK-T014 — Quando um IP-NFT pode ser valor mobiliário

- Entregável: `m1-tokenizacao-pi/enquadramento-regulatorio-ip-nft.md`
- Critério de aceite: análise provisória com o Parecer de Orientação CVM 40/2022 e a Lei 6.385/1976 (art. 2º): o que manteria o IP-NFT como licença e o que o transformaria em contrato de investimento coletivo; decisão em DUVIDAS
- Depende de: TK-T005, TK-T011
- Fase: 1
- Referências: Parecer de Orientação CVM 40/2022; Lei 6.385/1976
- Status: [ ]

## M2 — Orçamento BIM 5D

### TK-T015 — Visão do M2

- Entregável: `m2-orcamento-5d/README.md`
- Critério de aceite: papel do orçamento 5D na plataforma (base da captação e das tranches), limites de precisão e o que fica com o tek-calc e o tek-catalog
- Depende de: TK-T006
- Fase: 2
- Status: [ ]

### TK-T016 — Requisitos de informação do modelo para orçamento

- Entregável: `m2-orcamento-5d/requisitos-informacao-modelo.md`
- Critério de aceite: nível de informação necessária por disciplina para extrair quantitativos (classes IFC, propriedades, unidades), citado por código e item, sem copiar norma
- Depende de: TK-T015
- Fase: 2
- Referências: ISO 19650-1; ISO 7817-1; ISO 16739-1
- Status: [ ]

### TK-T017 — Fluxo de orçamento 5D do IFC ao orçamento paramétrico

- Entregável: `m2-orcamento-5d/fluxo-orcamento-5d.md`
- Critério de aceite: fluxo em etapas (recebimento do IFC, validação, quantitativos, composição, preço, BDI, revisão, congelamento da versão) com papéis, entradas, saídas e critério de passagem de cada etapa
- Depende de: TK-T016
- Fase: 2
- Referências: ISO 19650-2
- Status: [ ]

### TK-T018 — Fontes de preço e referências de custo

- Entregável: `m2-orcamento-5d/fontes-de-preco.md`
- Critério de aceite: fontes aceitas (SINAPI, CUB da NBR 12721, cotações, tek-catalog), regra de data-base, reajuste e registro da origem de cada preço
- Depende de: TK-T017
- Fase: 2
- Referências: NBR 12721; Decreto 7.983/2013
- Status: [ ]

### TK-T019 — BDI, encargos e contingência

- Entregável: `m2-orcamento-5d/bdi-contingencia.md`
- Critério de aceite: regras de produto para BDI, encargos e reserva de contingência, com faixas só citadas de fonte oficial e decisão provisória em DUVIDAS
- Depende de: TK-T018
- Fase: 2
- Referências: Decreto 7.983/2013
- Status: [ ]

### TK-T020 — Fluxo de auditoria do orçamento 5D

- Entregável: `m2-orcamento-5d/auditoria-orcamento-5d.md`
- Critério de aceite: trilha de auditoria (quem revisa, o que confere, tolerâncias, amostragem, ART do orçamentista e do revisor independente) e parecer que libera o orçamento para uma oferta
- Depende de: TK-T017, TK-T019
- Fase: 2
- Referências: ISO 19650-2
- Status: [ ]

### TK-T021 — Mudanças e versões do orçamento

- Entregável: `m2-orcamento-5d/mudancas-e-versoes.md`
- Critério de aceite: regra para revisão do modelo, aditivo e reorçamento depois da oferta, com efeito nas tranches e aviso ao investidor
- Depende de: TK-T020
- Fase: 2
- Status: [ ]

## M3 — Tokenomics e crowdfunding

### TK-T022 — Visão do M3 e personas do lado da demanda

- Entregável: `m3-tokenomics-crowdfunding/README.md`
- Critério de aceite: personas (investidor de varejo, investidor qualificado, auditor, incorporador captador), jornada da oferta e limites do que a plataforma promete
- Depende de: TK-T002
- Fase: 3
- Status: [ ]

### TK-T023 — Tokenomics do hub de PI

- Entregável: `m3-tokenomics-crowdfunding/tokenomics-ip.md`
- Critério de aceite: fluxos de valor do IP-NFT (taxa de registro, taxa de licença, repasse ao autor), sem token especulativo e sem promessa de valorização; decisão provisória em DUVIDAS
- Depende de: TK-T011, TK-T014
- Fase: 3
- Status: [ ]

### TK-T024 — Estrutura do security token da oferta imobiliária

- Entregável: `m3-tokenomics-crowdfunding/estrutura-security-token.md`
- Critério de aceite: alternativas de direito representado (participação em SPE, dívida, receita) com prós, contras e enquadramento provisório; nenhuma escolhida como final
- Depende de: TK-T032
- Fase: 3
- Referências: Resolução CVM 88/2022; Parecer de Orientação CVM 40/2022
- Status: [ ]

### TK-T025 — Cronograma 4D e definição de marco físico

- Entregável: `m3-tokenomics-crowdfunding/marcos-4d.md`
- Critério de aceite: como um marco é definido no modelo 4D (pacote de serviço, percentual físico, evidência exigida), critérios de medição e de aceite
- Depende de: TK-T017
- Fase: 3
- Referências: ISO 19650-2
- Status: [ ]

### TK-T026 — Escrow e liberação por tranches ligada a marcos 4D

- Entregável: `m3-tokenomics-crowdfunding/escrow-e-tranches.md`
- Critério de aceite: fluxo de liberação (pedido de medição, vistoria, laudo com ART, conferência com o modelo 4D, aprovação, liberação), papéis e prazos, sem definir tecnologia
- Depende de: TK-T025
- Fase: 3
- Status: [ ]

### TK-T027 — Exceções do escrow: atraso, disputa e devolução

- Entregável: `m3-tokenomics-crowdfunding/excecoes-escrow.md`
- Critério de aceite: regras para marco não atingido, divergência de medição, paralisação, cancelamento da oferta e devolução aos investidores, citando os dispositivos da CVM 88 aplicáveis
- Depende de: TK-T026, TK-T032
- Fase: 3
- Referências: Resolução CVM 88/2022
- Status: [ ]

### TK-T028 — Direitos e informações ao investidor

- Entregável: `m3-tokenomics-crowdfunding/direitos-investidor.md`
- Critério de aceite: o que o investidor recebe antes e depois da oferta (informações essenciais, relatórios de obra, prestação de contas), conforme a CVM 88, por item
- Depende de: TK-T032
- Fase: 3
- Referências: Resolução CVM 88/2022
- Status: [ ]

### TK-T029 — Mercado secundário e transferência dos tokens

- Entregável: `m3-tokenomics-crowdfunding/mercado-secundario.md`
- Critério de aceite: o que a regra atual permite para revenda dos tokens e o que fica proibido, com decisão provisória em DUVIDAS
- Depende de: TK-T032, TK-T034
- Fase: 3
- Referências: Resolução CVM 88/2022
- Status: [ ]

### TK-T030 — Modelo de receita da plataforma

- Entregável: `m3-tokenomics-crowdfunding/modelo-receita.md`
- Critério de aceite: fontes de receita (taxas de registro, licença, sucesso da captação, auditoria) com conflitos de interesse apontados; valores só como hipótese provisória
- Depende de: TK-T023, TK-T024
- Fase: 3
- Status: [ ]

## M4 — Governança e conformidade

### TK-T031 — Visão do M4

- Entregável: `m4-governanca-conformidade/README.md`
- Critério de aceite: mapa dos regimes que tocam a plataforma (CVM, BCB, COAF, ANPD, conselhos profissionais) e qual módulo cada um afeta
- Depende de: TK-T005
- Fase: 1
- Status: [ ]

### TK-T032 — Mapa de conformidade com a Resolução CVM 88

- Entregável: `m4-governanca-conformidade/mapa-cvm-88.md`
- Critério de aceite: tabela por capítulo e artigo da CVM 88 (registro da plataforma, limites de captação e por investidor, informações essenciais, desistência, publicidade, vedações) com a regra de produto correspondente e o status de cada uma
- Depende de: TK-T005
- Fase: 3
- Referências: Resolução CVM 88/2022
- Status: [ ]

### TK-T033 — Tokenização sob a CVM

- Entregável: `m4-governanca-conformidade/tokenizacao-cvm.md`
- Critério de aceite: leitura provisória do Parecer de Orientação CVM 40/2022 e de outros atos CVM sobre tokens, com o que se aplica ao IP-NFT e ao security token
- Depende de: TK-T032
- Fase: 3
- Referências: Parecer de Orientação CVM 40/2022
- Status: [ ]

### TK-T034 — Lei 14.478/2022 e regras do BCB para PSAV

- Entregável: `m4-governanca-conformidade/ativos-virtuais-bcb.md`
- Critério de aceite: quando a plataforma seria ou dependeria de prestadora de serviços de ativos virtuais (Lei 14.478/2022, art. 5º, e Resoluções BCB 519 a 521/2025), incluindo a exclusão do art. 1º, parágrafo único, para ativos que são valores mobiliários
- Depende de: TK-T005
- Fase: 3
- Referências: Lei 14.478/2022; Resoluções BCB 519, 520 e 521/2025
- Status: [ ]

### TK-T035 — KYC e prevenção à lavagem de dinheiro

- Entregável: `m4-governanca-conformidade/kyc-pld.md`
- Critério de aceite: obrigações de identificação, registro e comunicação (Lei 9.613/1998, arts. 9º a 11; Resolução CVM 50/2021; COAF) e quem as cumpre em cada arranjo
- Depende de: TK-T032, TK-T034
- Fase: 3
- Referências: Lei 9.613/1998; Resolução CVM 50/2021
- Status: [ ]

### TK-T036 — LGPD e dados em registro imutável

- Entregável: `m4-governanca-conformidade/lgpd.md`
- Critério de aceite: regra de que nenhum dado pessoal vai a registro imutável, bases legais por tratamento e direitos do titular (Lei 13.709/2018, por artigo)
- Depende de: TK-T005
- Fase: 1
- Referências: Lei 13.709/2018
- Status: [ ]

### TK-T037 — Notas tributárias provisórias

- Entregável: `m4-governanca-conformidade/tributacao-provisoria.md`
- Critério de aceite: lista de perguntas tributárias para o contador (licença de PI, rendimento do investidor, receita da plataforma), sem afirmar alíquota nem regime
- Depende de: TK-T024, TK-T030
- Fase: 3
- Status: [ ]

### TK-T038 — Governança da plataforma

- Entregável: `m4-governanca-conformidade/governanca-plataforma.md`
- Critério de aceite: papéis, comitês, alçadas, segregação de funções e política de conflito de interesses quando a Tekto é autora, orçamentista ou originadora
- Depende de: TK-T020, TK-T026
- Fase: 3
- Status: [ ]

### TK-T039 — Auditoria independente e responsabilidade técnica

- Entregável: `m4-governanca-conformidade/auditoria-e-responsabilidade.md`
- Critério de aceite: quem audita orçamento e medição, exigência de ART de cada parecer, independência do auditor e registro das evidências
- Depende de: TK-T020, TK-T026
- Fase: 3
- Referências: Lei 6.496/1977
- Status: [ ]

### TK-T040 — Matriz de responsabilidades da oferta

- Entregável: `m4-governanca-conformidade/matriz-raci.md`
- Critério de aceite: matriz RACI da oferta ponta a ponta, do registro do IFC à última tranche
- Depende de: TK-T038, TK-T039
- Fase: 3
- Status: [ ]

## Roadmap e consolidação

### TK-T041 — Roadmap por fases

- Entregável: `docs/ROADMAP.md`
- Critério de aceite: fases do MVP de registro de PI até o crowdfunding em conformidade com a CVM 88, com entregas de negócio e marcos de decisão do Samuel em cada fase
- Depende de: TK-T013, TK-T020, TK-T026, TK-T032
- Fase: 4
- Referências: Resolução CVM 88/2022
- Status: [ ]

### TK-T042 — Critérios de entrada e saída de cada fase

- Entregável: `docs/CRITERIOS-FASES.md`
- Critério de aceite: critério objetivo de avançar ou parar em cada fase (regulatório, técnico, comercial), com dono provisório
- Depende de: TK-T041
- Fase: 4
- Status: [ ]

### TK-T043 — Revisão do registro de riscos

- Entregável: `docs/RISCOS.md`
- Critério de aceite: riscos atualizados com o que os módulos M1 a M4 encontraram, cada risco ligado ao item ou dúvida que o trata
- Depende de: TK-T040
- Fase: 4
- Status: [ ]

### TK-T044 — Glossário consolidado

- Entregável: `docs/GLOSSARIO.md`
- Critério de aceite: todos os termos usados nos módulos estão no glossário, com fonte
- Depende de: TK-T040
- Fase: 4
- Status: [ ]

### TK-T045 — Requisitos de negócio para o repositório técnico

- Entregável: `docs/REQUISITOS-NEGOCIO.md`
- Critério de aceite: lista numerada de requisitos de negócio e regras de produto para o repositório técnico, sem arquitetura, stack ou infraestrutura
- Depende de: TK-T041
- Fase: 4
- Status: [ ]

### TK-T046 — Pontos para especialistas

- Entregável: `docs/PONTOS-PARA-ESPECIALISTAS.md`
- Critério de aceite: lista do que precisa de advogado de mercado de capitais, contador e engenheiro auditor antes de qualquer oferta real, ligada às dúvidas abertas
- Depende de: TK-T043
- Fase: 4
- Status: [ ]
