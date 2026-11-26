# Roteirista IA — Escrita Cinematográfica e Direção para Vídeo com IA

Uma Skill modular para desenvolver histórias originais, escrever roteiros audiovisuais e converter cenas em planos e prompts de produção para ferramentas de vídeo com inteligência artificial.

A proposta não é imitar um roteirista famoso nem aplicar uma fórmula a toda história. É combinar fundamentos dramáticos, análise crítica de cinema, clareza de execução e planejamento visual para que cada projeto encontre a forma que melhor serve à sua ideia.

## O que esta Skill faz

- Desenvolve ideias, premissas, loglines, sinopses e tratamentos.
- Constrói personagens com objetivos, contradições, decisões e vozes próprias.
- Escolhe uma arquitetura narrativa adequada ao gênero e ao motor dramático.
- Escreve roteiros para curtas, longas, séries, anúncios, vídeos narrativos, Shorts, Reels e TikTok.
- Revisa cenas, diálogos, ritmo, continuidade, causalidade e impacto emocional.
- Transforma roteiros aprovados em sequências, shot lists, storyboards textuais e prompts para geradores de imagem e vídeo.
- Mantém consistência de personagem, cenário, figurino, objetos, luz, paleta, tempo e ação entre tomadas.
- Pesquisa fatos quando o projeto é histórico, documental, biográfico ou depende de informação atual.

## Estrutura

```text
.
├── SKILL.md
├── README.md
├── SOURCES.md
└── references/
    ├── fundamentos-de-roteiro.md
    ├── atlas-de-cinema-e-roteiristas.md
    ├── pipeline-de-video-com-ia.md
    ├── modelos-e-checklists.md
    └── roteiro-de-comentario-e-react.md
ferramentas/
    ├── vtt_texto.py
    └── edicao_metricas.py
aprendizados.md
```

## Como usar

Mantenha o arquivo `SKILL.md` junto da pasta `references/`. A Skill aponta para esses guias quando precisa de técnicas, estudos de caso, modelos ou procedimentos de produção.

Exemplos de pedidos:

- “Tenho uma ideia para um suspense psicológico. Desenvolva a premissa e me mostre três caminhos narrativos.”
- “Escreva um curta de 5 minutos, com poucos personagens e final memorável.”
- “Analise este roteiro com critérios profissionais e proponha uma revisão.”
- “Transforme esta cena em 6 tomadas de vídeo com continuidade do personagem.”
- “Crie um roteiro de 40 segundos para TikTok, com gancho visual e payoff.”
- “Faça um roteiro cinematográfico e depois gere prompts separados para cada plano.”

## Método de trabalho

1. Entender a intenção, o público, o formato e as restrições.
2. Encontrar o motor dramático e a promessa emocional.
3. Definir personagens, forças de oposição, mundo e tema.
4. Escolher a arquitetura narrativa sem tratar modelos como leis.
5. Planejar sequências e cenas antes de escrever páginas extensas.
6. Redigir com ação filmável, diálogos específicos e subtexto.
7. Revisar estrutura, causalidade, personagem, ritmo, voz e significado.
8. Só então converter as cenas em planos e prompts técnicos para IA.

## Princípios editoriais

- Originalidade acima de fórmula.
- Personagens revelados por escolhas e ações, não apenas por biografias.
- Conflito com causa, consequência e escalada.
- Imagens e ações antes de explicações desnecessárias.
- Diálogo com intenção, voz e subtexto.
- Estrutura a serviço da história.
- Prompts específicos, coerentes e verificáveis.
- Separação entre roteiro literário, decupagem e prompt de geração.

## Pesquisa e referências

A base inclui listas históricas da Writers Guild of America, o poll Sight and Sound do BFI, critérios públicos do Academy Nicholl, orientações de formatação da Academy e entrevistas da BAFTA com roteiristas e cineastas. A bibliografia e as limitações de cada fonte estão em [SOURCES.md](SOURCES.md).

As listas de “melhores” são tratadas como recortes de votação e curadoria — não como um ranking universal e definitivo. O estudo de filmes busca extrair mecanismos narrativos, não copiar cenas, diálogos ou a assinatura de autores.

## Estado

Versão 1.1 (26/11/2026): módulo de roteiro de comentário/react (estudo de 48 roteiros e 12 edições do canal Jun Lie), ferramentas de estudo de canal e arquivo de aprendizados. Versão 1.0: pesquisa e operação inicial. O material é deliberadamente modular para receber estudos de caso, modelos e adaptações futuras para ferramentas específicas.
