# Pessoas Realistas AI Ultimate
Biblioteca assistida de **39 prompts integrais** para pessoas/influencers fotorrealistas. Busca por nome, ID ou características; devolve o original completo e orienta como utilizar. Adaptações, traduções e correções somente quando solicitadas, sempre identificadas.

## Coleções
| Coleção | Cadastros |
|---|---:|
| Rostos realistas | 20 |
| Fundos neutros | 9 |
| Faceswap | 2 |
| Produto + influencer | 4 |
| Macro e texturas | 4 |

Todos os textos ficam nas referências da [Skill](.agents/skills/pessoas-realistas-ai-ultimate/SKILL.md) e no [catálogo JSON](.agents/skills/pessoas-realistas-ai-ultimate/assets/prompt-catalog.json). IDs P001–P039. Não depender apenas do arquivo principal para recuperar textos: manter a pasta inteira.

## Como usar
- “Me dê o prompt Rosto Realista Ruiva.” → original completo.
- “Quais versões de mulher morena existem?” → lista títulos/IDs, sem escolher aleatoriamente.
- “Somente o prompt P001.” → texto literal sem metadados.
- “Adapte P001, trocando só a cor dos olhos.” → texto completo identificado como adaptação.
- “Explique como usar produto + influencer.” → etapas e imagens necessárias, sem fingir geração.

Formato padrão: nome, ID, coleção, ferramenta indicada no cadastro, bloco original e orientação curta se necessária. Idioma original preservado; traduções não são impostas. Sem imagem ainda é possível consultar o catálogo.

## Instalação e ferramentas
Copiar `.agents/skills/pessoas-realistas-ai-ultimate` completa para a mesma estrutura do projeto. Host precisa reconhecer Skills ou carregar SKILL.md explicitamente. Modelo de linguagem basta para consulta; visão para analisar imagens, gerador externo para executá-las. Nenhuma chave, conta ou API é configurada por este pacote. [Instalação](docs/INSTALLATION.md).

Busca opcional por Python padrão, sem dependências:
```bash
python .agents/skills/pessoas-realistas-ai-ultimate/scripts/search_catalog.py 'homem idoso'
python .agents/skills/pessoas-realistas-ai-ultimate/scripts/search_catalog.py P001 --original
```
Busca lexical limitada; consultar o índice para sinônimos não reconhecidos. Ferramentas e “gratuito” são metadados da fonte, sem garantia atual de compatibilidade/preço.

## Integridade e testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_catalog.py
python -m unittest discover -s tests -p 'test_*.py'
```
Verificações de contagem, metadados, conteúdo literal, hashes, links, busca e ambiguidades. [Cobertura](docs/CONTENT_COVERAGE.md), [aceitação](tests/acceptance-tests.md), [resultados](tests/RESULTS.md). Testes estruturais e busca não comprovam qualidade de geração ou comportamento do host.

## Limitações e origem
P035 contém campo pendente; P032/P034 têm texto repetido e são preservados como passos diferentes. Prompts podem ter contradições e sintaxe de fornecedor não verificada. Não prometer identidade, 8K ou assertividade absoluta. Imagens não incluídas; links assinados temporários omitidos sem alterar prompts.
MIT para contribuições originais; prompts da coleção Influencer A.I mantêm direitos de origem. [NOTICE](NOTICE.md), [fonte textual com links temporários omitidos](docs/SOURCE_CATALOG.md), [auditoria](docs/FUNCTIONAL_AUDIT.md), [CHANGELOG](CHANGELOG.md).
