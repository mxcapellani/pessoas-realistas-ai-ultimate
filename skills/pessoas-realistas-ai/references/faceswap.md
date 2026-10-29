# Faceswap

1. Gere a base neutra (pose frontal ou 3/4, rosto visível).
2. Escolha a imagem de referência do rosto (biblioteca ou foto com consentimento).
3. Ferramentas comuns: InstantID, IP-Adapter FaceID, PuLID, ReActor, Midjourney `--cref`/omni-reference, ou editores com referência de imagem.
4. Parâmetros: força de identidade média-alta (0.6-0.8); se a pele ficar lisa demais, reduza e aplique texturas naturais.
5. Pós-processo: restauração facial leve (não excessiva), igualar cor/iluminação do rosto ao corpo, conferir pescoço e linha do cabelo.

## Prompt de adaptação

```
Same person as reference face, keep identity, match skin tone to neck and body,
consistent lighting direction, natural skin texture
```

## Checklist

- Tom de pele do rosto igual ao pescoço
- Direção da luz coerente
- Sem bordas/halo na linha do cabelo
- Consentimento para o rosto usado
