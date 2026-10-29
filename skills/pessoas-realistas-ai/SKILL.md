---
name: pessoas-realistas-ai
description: Cria e adapta prompts de pessoas e influencers fotorrealistas para IA generativa de imagem, com biblioteca de rostos, bases neutras, faceswap, integração com produtos e texturas naturais de pele. Use quando o pedido envolver prompt de influencer, modelo virtual, retrato realista, troca de rosto, ou pessoa segurando/usando um produto.
---

# Pessoas Realistas AI

Skill para gerar e adaptar prompts de pessoas/influencers fotorrealistas.

## Fluxo

1. **Entender o pedido**: objetivo (feed, anúncio, avatar), plataforma/modelo de imagem, formato (1:1, 4:5, 9:16), idioma do prompt (padrão: inglês para o prompt, resposta em português).
2. **Escolher o rosto** na biblioteca (`references/biblioteca-rostos.md`) ou descrever um novo, mantendo consistência (mesma ficha = mesma pessoa).
3. **Montar a base neutra** (`references/bases-neutras.md`): pose, fundo e luz simples, sem estilo ou produto, para servir de ponto de partida e de alvo do faceswap.
4. **Aplicar faceswap**, se pedido (`references/faceswap.md`): trocar o rosto da base neutra pelo rosto da biblioteca/referência.
5. **Integrar o produto** (`references/produtos.md`): posição, escala, interação das mãos, iluminação coerente.
6. **Adicionar texturas naturais** (`references/texturas-naturais.md`) para evitar aspecto plástico.
7. **Entregar**: prompt positivo, prompt negativo, parâmetros sugeridos e variações.

## Estrutura do prompt

```
[tipo de foto/câmera], [sujeito: idade, etnia, traços, cabelo], [expressão],
[roupa], [pose/ação], [produto], [cenário], [luz], [lente/enquadramento],
[texturas naturais], [qualidade]
```

## Regras

- Usar apenas pessoas fictícias ou com consentimento explícito; nunca replicar celebridades ou pessoas reais sem autorização.
- Não gerar conteúdo enganoso: avisar que imagens são geradas por IA quando a plataforma ou lei exigir.
- Nada de menores em contextos comerciais sensuais; adultos (18+) apenas em retratos de influencer.
- Preferir descrições específicas (idade, tom de pele, iluminação) a adjetivos vagos ("linda", "perfeita").
- Sempre incluir prompt negativo (ver `references/texturas-naturais.md`).

## Formato de saída

```
**Rosto:** <id da biblioteca>
**Prompt:** ...
**Negative prompt:** ...
**Parâmetros:** proporção, seed/referência, força do faceswap
**Variações:** 2-3 ajustes (luz, roupa, cenário)
```
