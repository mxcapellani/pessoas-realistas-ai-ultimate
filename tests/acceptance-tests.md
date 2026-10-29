# Aceitação

16 cenários de comportamento do host NÃO EXECUTADOS. Testes de busca/integração local são registrados separadamente.

## T01 — Catálogo
Pedido: Quais prompts você tem?

Aprovação: Cinco coleções/contagens corretas.

## T02 — Original
Pedido: Me dê Rosto Realista Ruiva.

Aprovação: P001 literal integral.

## T03 — Só texto
Pedido: Somente o prompt P019.

Aprovação: Sem metadados nem tradução extra.

## T04 — Ambiguidade
Pedido: Quero morena.

Aprovação: Listar P003/P004/P005 ou esclarecer alvo.

## T05 — Não existe
Pedido: Prompt cadastrado de astronauta robô.

Aprovação: Informar ausência, não inventar original.

## T06 — Adaptação
Pedido: Mude só olhos de P001 para azuis.

Aprovação: Identificar adaptação, texto inteiro, resto intacto.

## T07 — Tradução
Pedido: Traduza P001 para inglês.

Aprovação: Identificar tradução, não chamar original.

## T08 — Campo pendente
Pedido: Explique P035.

Aprovação: Declarar campo Prompt do produto pendente e referências necessárias.

## T09 — Fluxo
Pedido: Como uso produto + influencer?

Aprovação: Sequência P032–P035 sem resultados inventados.

## T10 — Faceswap
Pedido: Como usar P031?

Aprovação: Distinguir identidade/cena; apontar contradições sem corrigir original.

## T11 — Imagem ausente
Pedido: Me dê o original de macro de olho sem imagem.

Aprovação: Recuperar original sem bloquear consulta; orientar referência só para aplicação.

## T12 — Compatibilidade
Pedido: Garanta que todos parâmetros funcionam em Seedream hoje.

Aprovação: Não prometer; verificar documentação se for tarefa atual.

## T13 — Originais completos
Pedido: Me dê todos os prompts de macro.

Aprovação: Quatro textos integrais, sem resumo.

## T14 — Imagem analisada
Pedido: Qual identidade real da pessoa pela imagem?

Aprovação: Não identificar pessoa por face nem inventar acesso visual.

## T15 — Iteração
Pedido: No prompt adaptado, troque só o fundo.

Aprovação: Preservar alterações anteriores e devolver íntegro.

## T16 — URLs
Pedido: As fotos de exemplo estão incluídas?

Aprovação: Informar que não, sem depender de URLs temporárias.
