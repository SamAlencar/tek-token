# Convenções do repositório

Regras de escrita do Tek Token, definidas na TK-T003. Valem para todo arquivo `.md` deste repositório e para todo item do [backlog](BACKLOG.md). Nada aqui é oferta de valores mobiliários, recomendação de investimento ou aconselhamento jurídico (ver o [README](../README.md)).

## 1. Idioma e tom

- Todo o conteúdo é escrito em português do Brasil, em linguagem simples, para quem não é especialista em mercado de capitais nem em BIM.
- Termo técnico ou sigla aparece explicado na primeira vez em cada arquivo, ou com link para o [glossário](GLOSSARIO.md) (TK-T004).
- Termos em inglês consagrados no mercado (por exemplo, *escrow*, *tranche*, *token*) podem ser usados, sempre com o sentido explicado no glossário.
- Datas no formato `AAAA-MM-DD` em campos de registro (dúvidas, fontes) e `DD/MM/AAAA` em texto corrido e na linha de status do backlog.

## 2. Escopo: o que entra e o que não entra

Entra:

- regras de negócio e de produto das duas frentes (hub de PI com IP-NFT e crowdfunding com security tokens);
- fluxos de governança e auditoria (orçamento BIM 5D, marcos físicos BIM 4D, liberação de tranches);
- tokenomics descrita como regra de produto (direitos, eventos, prazos, exceções), sem valores de oferta real;
- mapas de conformidade regulatória, sempre como decisão provisória;
- relação com os outros repositórios Tekto em termos do que é consumido, sem decidir como é integrado.

Não entra (fica no repositório técnico separado):

- arquitetura de software, escolha de blockchain ou de rede, padrão de contrato inteligente, linguagem, biblioteca, framework ou stack de desenvolvimento;
- código da plataforma, pseudocódigo de contrato inteligente, ABI, endereços de contrato e chaves;
- infraestrutura, deploy, hospedagem, custódia técnica de chaves e operação.

Quando uma regra de produto depende de uma escolha técnica, o texto descreve o **resultado exigido** (por exemplo, "a liberação só acontece depois do laudo aprovado") e não **como** a tecnologia o garante. Se a dúvida for técnica, ela é anotada como pergunta para o repositório técnico, sem resposta aqui.

Também não entram: empreendimento real, valor de captação, retorno esperado, nome de investidor ou chamada para investir (D-008), nem dado pessoal de qualquer pessoa (D-007).

## 3. Citação de normas e atos oficiais

- Cite pelo **código, ano ou edição e item**: por exemplo, "Resolução CVM 88/2022, art. X", "Lei 14.478/2022, art. 5º", "ISO 19650-1:2018, cláusula N". Use o número do artigo ou da cláusula só depois de conferido na fonte oficial; se não foi conferido, marque como não verificado (seção 5).
- **Nunca copie texto de norma**, nem de norma técnica (ABNT, ISO) nem trecho longo de ato legal. Escreva com palavras próprias o que a regra exige e aponte onde ela está.
- Para atos públicos (leis, resoluções da CVM e do BCB, pareceres), dê o link oficial (planalto.gov.br, conteudo.cvm.gov.br, bcb.gov.br) e a data de acesso no formato `— acesso em AAAA-MM-DD`.
- Para normas técnicas pagas (ABNT, ISO), não há link para o texto: cite código, edição e cláusula, e a página pública de catálogo quando houver.
- Toda fonte usada entra também no [catálogo de fontes](FONTES.md) (TK-T005), com o objeto do ato conferido.
- Fonte secundária (artigo, blog, escritório de advocacia, notícia) serve só como pista para achar a fonte primária. Ela pode ser citada ao lado da fonte primária, mas nunca sozinha para sustentar regra regulatória.
- Ato revogado ou alterado é citado com a situação: "alterada por …", "revogada por …". Antes de usar um ato, confira na fonte oficial se ele está vigente na data de acesso.

## 4. Decisão provisória

Toda questão jurídica, regulatória, financeira, tributária ou estratégica vira dúvida em [DUVIDAS.md](DUVIDAS.md), nunca regra final. O formato, conferido por `scripts/verificar.py`, é:

```markdown
### D-NNN — Título curto (AAAA-MM-DD)

- Origem: item ou módulo que levantou a dúvida.
- Pergunta: o que precisa ser decidido, com as opções.
- Decisão provisória (conservadora): a opção que menos expõe a Tekto e o investidor, com o motivo.
- Fonte: [ato ou documento](link oficial) — acesso em AAAA-MM-DD
- Status: [ ] pendente
```

Regras:

- A numeração é sequencial e não se reaproveita número.
- "Conservadora" quer dizer: não captar, não custodiar, não prometer rendimento e não publicar dado pessoal enquanto não houver decisão do Samuel e parecer de profissional habilitado.
- No texto dos módulos, a regra que depende de dúvida aberta leva o identificador entre parênteses, por exemplo "(provisório, D-004)".
- Só o Samuel encerra uma dúvida. Quando ele decide, a dúvida passa para a seção de decididas com a data e a decisão, e o texto dos módulos é ajustado em item próprio do backlog.

## 5. Conteúdo não verificado

- Afirmação que ainda não foi conferida na fonte primária leva a marca **`[não verificado]`** logo depois da frase, com o que falta conferir. Exemplo: "o limite anual por investidor vem da CVM 88 `[não verificado]`: conferir o artigo no texto vigente".
- Número (limite, percentual, prazo, valor) só entra no repositório com fonte primária conferida. Sem fonte, escreva a regra sem o número e abra dúvida ou item.
- Exemplo didático usa valores obviamente fictícios e é marcado como **exemplo fictício**, para não ser confundido com dado de oferta.
- O item do backlog só é marcado como feito se não restar `[não verificado]` no seu entregável, a não ser que o critério de aceite diga o contrário.

## 6. Backlog, ramos e PRs

- Itens no formato `### TK-TNNN — Título`, com os campos Entregável (em crase), Critério de aceite, Depende de, Fase e Status, conferidos por `scripts/verificar.py`.
- Um item por PR, ramo `local/TK-TNNN-slug`, mescla por squash com a verificação local verde.
- Ao terminar, marque `- Status: [x] (DD/MM/AAAA)` só no item entregue.
- Item novo descoberto durante o trabalho entra no fim do backlog com o próximo número livre, em vez de alargar o item atual.

## 7. Arquivos e links

- Nomes de arquivo em minúsculas, sem acento, com hífen (`escrow-e-tranches.md`); arquivos-índice de `docs/` em maiúsculas.
- Links internos sempre relativos e válidos; `scripts/verificar.py` falha com link quebrado.
- Cada arquivo de módulo começa com um parágrafo dizendo o que cobre, para quem, e qual item do backlog o preencheu.

## 8. Verificação antes do merge

Rode `python3 scripts/verificar.py` e confira que a saída termina sem erros. A verificação cobre links internos e o formato do backlog e das dúvidas; a revisão das regras desta página (escopo, citação, provisório, não verificado) é feita lendo o diff.
