---
name: vexter-historia-marca
description: Use SEMPRE que pedirem texto, post, carrossel, legenda, roteiro, proposta, apresentação, site ou material institucional da Vexter Intelligence, ou perguntarem sobre história, nome, logo, cores ou posicionamento. Define o padrão de feed e guarda a logo oficial.
---

# Vexter Intelligence: história, significado e identidade

Fonte oficial: documento de Lucas Benício Souza (sócio), 21/10/2026, em `references/historia_e_identidade.md`. Leia-o quando a tarefa envolver história, significado, tom institucional ou narrativa de marca. Ele prevalece sobre qualquer texto antigo.

## Resumo rápido
- **Essência:** transformar informação em inteligência e inteligência em direção para o negócio.
- **Lema:** "Inteligência que transforma dados em direção para o negócio."
- **Assinatura:** Contabilidade. Estratégia. Tecnologia. Evolução.
- **Nome:** VEX = visão e estratégia; TER = estrutura e execução; INTELLIGENCE = inteligência aplicada. **A divisão VEX/TER é interpretação conceitual da marca; nunca afirmar que é a origem etimológica oficial.**
- **Símbolo:** estética executiva, minimalista e tecnológica. Geometria (visão multidimensional: contábil, fiscal, financeira, operacional, tributária, estratégica), linhas finas (precisão, integração), diagonais ascendentes (movimento, direção, futuro), simplicidade.
- **Cores:** preto #000000 (autoridade), grafite #1B1B1B (profundidade), dourado #C8A34D (valor, excelência; uso moderado), branco #FFFFFF (clareza), cinza-claro #F5F5F5 (organização). Apoio: dourado claro #DDBE7A e dourado escurecido #A8832F (só no tema claro, para contraste).
- **Tipografia:** títulos Poppins 600/700; corpo Inter 400/500/600 (embutidas em `assets/fonts`, licença OFL).
- **Atributos:** confiança, inteligência, estratégia, tecnologia, evolução.
- **Foco setorial:** Transporte e Logística (principal) e Agronegócio; atende também Comércio, Indústria e Serviços.
- **Perfil:** @somosvexter.

## Regras
1. **Logo:** nunca recriar, redesenhar ou aplicar filtros. Só redimensionar mantendo a proporção, usando `assets/`:
   - `logo_transparente_cores_originais.png`: fundos claros.
   - `logo_transparente_fundo_escuro.png`: fundos preto ou grafite (texto em dourado claro).
   - `simbolo_transparente.png`: só o símbolo, para composições grandes.
2. **Proporção de cores:** peças institucionais e comerciais com preto e dourado predominando; relatórios, propostas técnicas e dashboards com branco e cinza-claro predominando e dourado só nos destaques.
3. **Sem fatos inventados:** não criar datas de fundação, número de clientes, cases, depoimentos ou resultados. Se faltar dado, perguntar ou omitir.
4. **Sem travessões** em textos e artes (o script bloqueia).
5. **Tom:** técnico, estratégico e consultivo, sem jargão sem explicação e sem promessa de economia garantida ("reduza X% de imposto"). Conteúdo tributário ou normativo leva fonte, data e indicação de que exige validação técnica por um sócio antes de publicar (publicidade do profissional contábil segue o Código de Ética do CFC).
6. **SPIN Selling obrigatório em TODO material** (posts, carrosséis, legendas, roteiros, e-mails, scripts de WhatsApp e ligação, propostas, site). Ver a seção "Estrutura SPIN".

## Estrutura SPIN (aplicar sempre)
| Etapa | Função | Carrossel | Legenda | Script / e-mail / proposta |
|---|---|---|---|---|
| **S** Situação | Contexto que o decisor reconhece | Capa | Abertura | Pergunta de situação (regime, porte, operação) |
| **P** Problema | Dor concreta | 1 a 2 slides | Contexto | Pergunta de problema (o que incomoda hoje) |
| **I** Implicação | Custo de não agir (margem, caixa, autuação, tempo) | 1 a 2 slides | Contexto | Pergunta de implicação (o que isso causa) |
| **N** Necessidade de solução | O próprio leitor conclui o valor; Vexter como caminho | Slide final + CTA | CTA | Pergunta de necessidade (o que mudaria se resolvido) |

Regras: nunca abrir pelo serviço da Vexter; Implicação sem números inventados (só dado com fonte ou exemplo declarado como hipotético); a oferta aparece só na etapa N. Antes de entregar, marcar no rascunho qual slide ou parágrafo cumpre cada etapa.

## Fluxo para criar posts ou carrosséis
1. Ler `references/padrao_feed.md`.
2. Definir **um** tema para a série inteira (`escuro`, `grafite` ou `claro`).
3. Montar o roteiro SPIN e escrever os slides como JSON (`tipo`: capa, texto, lista, dado ou cta; máximo 5 itens por slide de lista; `<b>` em 1 a 3 palavras do título para o destaque dourado).
4. Gerar: `python scripts/feed_template.py serie.json saida/` (ou `render_series` + `make_grid` em Python). O script valida o padrão, embute fontes e logo, ajusta o texto à área segura e avisa se precisou reduzir mais de 15%.
5. Abrir `_grade.png` e conferir o checklist do padrão de feed.
6. Escrever a legenda na estrutura fixa do padrão.

## Referência já aprovada
Sequência "história da marca" em 3 feeds (1/3 Quem somos, 2/3 A marca, 3/3 Nosso foco): as 3 imagens formam um panorama, com o símbolo no centro e a lâmina diagonal estendida como linha dourada atravessando as 3. Esse panorama é composição especial e não sai do template padrão; os textos de cores e símbolo seguem o documento de referência.
