# Relação com os repositórios Tekto

O que o Tek Token espera receber dos outros repositórios da Tekto, definido na TK-T006. Este arquivo descreve só **o que** é consumido e para qual regra de produto. **Como** a integração acontece (formato de troca, serviço, contrato inteligente) é decisão do repositório técnico separado e não entra aqui (ver [convenções](CONVENCOES.md), seção 2). Nada aqui é oferta de valores mobiliários, recomendação de investimento ou aconselhamento jurídico (ver o [README](../README.md)).

## 1. Situação conferida em 30/10/2026

Os cinco repositórios abaixo são privados; o Tek Token é público. Por isso este arquivo não tem link para o conteúdo deles e descreve cada um só pelo propósito declarado no próprio README, lido em 2026-10-30.

| Repositório | Propósito declarado | O que existe hoje que interessa ao Tek Token |
| --- | --- | --- |
| tek-calc | Acervo de cálculos de engenharia civil, rastreável às normas ABNT NBR; cada rotina devolve o valor e os passos, e o memorial sai em Markdown | Verificações estruturais (concreto armado pela NBR 6118) com memorial rastreável. **Não há orçamento** nem composição de custo |
| tek-docs | Base de conhecimento teórico: memoriais, métodos construtivos, materiais, especificações, fluxo BIM e laudos, com índice de normas sem o texto da ABNT | Fichas de método construtivo e de material, padrões BIM e modelos de BEP, índice de normas citadas |
| tek-catalog | Catálogo de materiais e produtos da construção, com ficha escrita e IFC 4.3 por item genérico | Itens com classe IFC e dimensões validadas. **Preço de mercado está fora do escopo** do catálogo nesta fase |
| tek-model | Modelo neutro e IFC 4.3, com identificador no formato do IFC (`IfcGloballyUniqueId`) em cada elemento | Elementos identificados de forma estável, resultados de cálculo ligados ao elemento; exportação de quantitativos ainda planejada, não feita |
| tek-studio | Software interno que reúne as disciplinas; a IA conversa com o engenheiro e todo cálculo vem de um núcleo determinístico, com registro de cada chamada | Trilha de auditoria das chamadas de ferramenta e propostas de alteração do modelo com norma citada |

## 2. O que o Tek Token consome

Cada linha diz o insumo, de onde ele deve vir e qual regra de produto do Tek Token depende dele. "Hoje" resume a seção 1.

| Insumo | Origem prevista | Usado em | Hoje |
| --- | --- | --- | --- |
| Modelo IFC do projeto, com identificador estável por elemento | tek-model (camada neutra) e tek-studio (onde o projeto é feito) | M1: evidência de autoria e versão do modelo (TK-T010); M2: base do orçamento 5D (TK-T016, TK-T017) | Existe o identificador por elemento; o pacote de evidência ainda é regra a definir na TK-T010 |
| Quantitativos por elemento (áreas, volumes, contagens) | tek-model | M2: levantamento de quantidades do orçamento (TK-T017) | Planejado no tek-model, não feito |
| Memorial de cálculo com norma, edição e item | tek-calc | M2: prova de que o projeto orçado foi verificado; M4: documentação do dossiê de auditoria (TK-T020) | Existe para os cálculos estruturais já implementados |
| Especificação técnica e método construtivo | tek-docs | M2: descrição do serviço em cada linha do orçamento (TK-T017); M3: definição do que é um marco físico concluído (TK-T025) | Existe parcialmente; cobertura cresce com o backlog do tek-docs |
| Material ou produto genérico, com classe IFC | tek-catalog | M2: ligação entre elemento do modelo e insumo da composição de custo (TK-T018) | Existe para os primeiros itens; sem preço |
| Preço de referência e composição de custo | **Sem origem definida** (D-011) | M2: fontes de preço, BDI e contingência (TK-T018, TK-T019) | Nenhum repositório Tekto tem preço nem composição |
| Cronograma físico ligado ao modelo (4D) | **Sem origem definida** (D-011) | M3: marcos físicos e liberação de tranches (TK-T025, TK-T026) | Nenhum repositório Tekto tem cronograma |
| Registro de quem fez cada cálculo ou alteração | tek-studio | M4: trilha de auditoria e responsabilidade técnica (TK-T020, TK-T036) | Existe o registro das chamadas de ferramenta |

## 3. O que o Tek Token não pede aos outros repositórios

- Nenhum dado de cliente, empreendimento real, valor de captação ou dado pessoal (D-007, D-008).
- Nenhuma mudança de escopo nos outros repositórios: se uma regra do Tek Token precisar de algo que eles não fazem, isso vira dúvida aqui e, se o Samuel aprovar, item no backlog do repositório dono.
- Nenhuma decisão de formato, protocolo ou ferramenta de integração (fica no repositório técnico).

## 4. Consequência para o backlog

O M2 (orçamento 5D) e o M3 (marcos 4D) dependem de dois insumos que nenhum repositório Tekto produz hoje: preço com composição de custo e cronograma físico. Até a D-011 ser decidida, os itens TK-T018, TK-T019, TK-T025 e TK-T026 descrevem a regra de produto e a fonte oficial de referência, sem supor que algum repositório já entrega esses dados.
