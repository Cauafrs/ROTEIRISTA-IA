# Pipeline de pré-produção e prompts para vídeo com IA

## Objetivo

Converter uma cena aprovada em uma sequência de planos geráveis, mantendo intenção dramática, legibilidade visual, identidade de personagem e continuidade. O pipeline não substitui o roteiro: é uma camada posterior de interpretação e produção.

## 1. Não misture três documentos

### Roteiro literário
Descreve o que acontece na história, ações, ambientes, falas e sons significativos. Precisa ser lido como narrativa.

### Decupagem / shot list
Define como uma cena será dividida em tomadas e quais informações cada tomada precisa transmitir. Pode incluir escala de plano, ângulo, movimento e duração estimada.

### Prompt de geração
Instrui um modelo específico a criar uma imagem ou clipe. Precisa especificar sujeito, ação, espaço, aparência, composição, tempo, luz, movimento e restrições relevantes.

Não coloque todas as escolhas de câmera no roteiro literário por padrão. A direção é uma etapa própria.

## 2. Pipeline recomendado

1. Congelar ou identificar a versão do roteiro de referência.
2. Dividir a história em sequências e cenas com IDs estáveis.
3. Criar bíblia de continuidade.
4. Definir a função dramática de cada cena.
5. Quebrar cada cena em tomadas com uma ação dominante por tomada.
6. Criar prompts globais de personagem e ambiente.
7. Criar prompts específicos para cada tomada.
8. Planejar imagens de referência e quadros-chave quando a ferramenta permitir.
9. Gerar, revisar e registrar desvios.
10. Corrigir a continuidade na geração ou na montagem.
11. Finalizar som, diálogos, legendas e ritmo em pós-produção.

## 3. Bíblica visual e de continuidade

Crie uma ficha estável para cada elemento recorrente.

### Personagem
- ID e nome;
- faixa etária narrativa e aparência adulta/juvenil somente quando relevante;
- formato de rosto e traços visíveis;
- cabelo, cor, corte e textura;
- tom de pele descrito com neutralidade e consistência;
- altura/proporções gerais;
- figurino por cena e estado do figurino;
- acessórios e objetos carregados;
- postura e maneirismos;
- voz, idioma e ritmo;
- estado emocional no começo da cena;
- mudanças físicas acumuladas: sujeira, suor, ferimento, chuva, cansaço.

Não invente atributos sensíveis sem necessidade. Não use uma descrição diferente do rosto em cada plano. Use uma descrição-base idêntica e altere apenas o estado que a história realmente modifica.

### Local
- ID e nome;
- arquitetura e layout;
- materiais e texturas;
- objetos fixos;
- entradas, saídas, janelas e eixos espaciais;
- clima e horário;
- fontes de luz;
- elementos que podem ou não mudar entre planos.

### Figurino e objetos
Registre estado inicial e mudanças:
- roupa, cor, material, caimento;
- acessórios;
- objetos em cada mão;
- posição antes e depois da ação;
- dano, sujeira ou desaparecimento;
- lado do corpo e continuidade espacial.

### Fotografia e direção de arte
- proporção de tela;
- paleta;
- contraste;
- qualidade da luz;
- textura visual;
- nível de realismo ou estilização;
- lente ou distância aparente, somente quando fizer diferença;
- referências abstratas de composição, sem pedir cópia de um artista específico.

## 4. Construção de uma shot list

Uma tomada deve ter função narrativa. Exemplos:
- apresentar espaço e relação de poder;
- mostrar reação;
- revelar informação;
- esconder informação;
- marcar mudança emocional;
- criar suspense;
- permitir orientação espacial;
- entregar um detalhe que terá payoff.

Para cada tomada, documente:

| Campo | Descrição |
|---|---|
| ID | Identificador estável, como S03-C02-P05 |
| Cena | Cena de origem |
| Batida | O que muda nesta tomada |
| Duração | Estimativa, ajustada ao modelo e à edição |
| Escala | Geral, conjunto, médio, close, detalhe etc. |
| Ângulo | Altura e relação com o sujeito |
| Composição | Onde sujeitos e objetos aparecem |
| Movimento | Câmera e/ou movimento do sujeito |
| Ação | Uma ação dominante claramente descrita |
| Performance | Comportamento visível, não emoção abstrata |
| Luz e cor | Continuidade e intenção |
| Som | Diálogo, ambiente, efeito, música ou silêncio |
| Continuidade | Elementos que precisam permanecer idênticos |
| Transição | Corte, match cut, elipse, som contínuo etc. |

Não é obrigatório usar todos os campos em todo clipe. Use apenas o que ajuda o modelo e a produção.

## 5. Anatomia de um prompt de vídeo

Organize o prompt nesta ordem, ajustando a ferramenta:

1. **Tipo de entrega:** vídeo cinematográfico, animação, plano de detalhe etc.
2. **Sujeito:** personagem/objeto consistente.
3. **Ação:** o que acontece, em que ordem, com início e fim claros.
4. **Ambiente:** local, espaço, hora, clima e objetos importantes.
5. **Composição:** escala do plano, posição e profundidade.
6. **Câmera:** ângulo, movimento e estabilidade, quando suportados.
7. **Luz e aparência:** fonte, direção, contraste, cor e textura.
8. **Performance:** gesto, olhar, ritmo e deslocamento.
9. **Som:** fala, idioma, som ambiente ou instrução para silêncio, se a ferramenta aceitar áudio.
10. **Continuidade:** identidade, roupa, acessórios, orientação, objetos e cenário.
11. **Restrições:** o que não deve surgir ou mudar.
12. **Parâmetros:** proporção, duração, resolução e controles disponíveis na ferramenta.

Escreva de forma visual e concreta. “Ela está triste” é menos acionável que “ela mantém os olhos no copo intacto, tenta falar, inspira, mas deixa a frase morrer”. Emoções podem ser especificadas, porém devem ser traduzidas em comportamento observável.

## 6. Ação e tempo

- Prefira uma ação dominante por clipe.
- Quando houver várias ações, divida em planos ou descreva a sequência com ordem inequívoca.
- Evite pedir que o modelo mude de locação, figurino, idade, personagem e iluminação num único clipe, salvo quando a transformação é intencional.
- Ajuste duração à complexidade da ação e às capacidades atuais do gerador.
- Não force uma duração universal. Verifique limites e controles da plataforma escolhida.
- Use pausas, olhares e microações quando forem importantes, mas não peça movimento excessivo em todo plano.

## 7. Consistência entre tomadas

Use:
- IDs estáveis;
- descrições-base repetidas sem variação gratuita;
- imagem de referência quando suportada;
- quadro inicial/final de referência, se disponível;
- notas de figurino e objeto;
- eixo de ação e direção do olhar;
- mesma hora e condições de luz em planos contíguos;
- prompt de continuidade que descreva o estado exato no início de cada tomada.

### Verificação de continuidade

Antes de aprovar a sequência, confira:
- rosto, cabelo, idade aparente e proporções;
- figurino e acessórios;
- lado em que personagem e objetos aparecem;
- posição de objetos e mãos;
- ferimentos, sujeira e desgaste;
- horário, clima e direção da luz;
- geografia do local;
- direção do movimento e do olhar;
- estado emocional e consequência da cena.

Se houver um salto, torne-o intencional por montagem ou corrija a geração.

## 8. Som e montagem

O áudio também conta a história:
- diálogo inteligível e coerente com a boca, quando houver sincronização;
- idioma e sotaque consistentes;
- som ambiente para situar espaço;
- silêncio para mudança de atenção;
- efeito sonoro com função;
- música sem mascarar a fala;
- transições sonoras que conectam planos ou cenas.

Não dependa exclusivamente do áudio gerado pelo vídeo. Planeje dublagem, gravação, Foley, trilha e mixagem como etapas independentes quando necessário.

## 9. Adaptação a ferramentas

Quando o usuário indicar um gerador:
1. pesquise a documentação oficial atual;
2. confirme controles reais de proporção, duração, imagem de referência, movimento, áudio e seed;
3. escreva prompts dentro dos limites documentados;
4. deixe claro quais parâmetros são texto livre e quais são opções da interface;
5. não invente sintaxe, parâmetros, resolução ou garantias.

Se a ferramenta não for especificada, entregue um prompt agnóstico e sinalize o que deverá ser adaptado.

## 10. Exemplo neutro de decomposição

**Batida de roteiro:** Uma mulher percebe que a carta deixada sobre a mesa foi aberta.

**Plano A — estabelecer**
- Plano médio do ambiente.
- Ela entra e deixa a bolsa na cadeira.
- A carta está visível, mas fora do centro do quadro.
- Função: apresentar espaço e rotina.

**Plano B — descoberta**
- Close da mão interrompendo o movimento ao notar o envelope aberto.
- Função: fazer o público descobrir junto com ela.

**Plano C — reação**
- Close do rosto; olhar sai do envelope e vai para a porta entreaberta.
- Não mostrar a emoção como uma careta exagerada.
- Função: converter descoberta em suspeita.

**Plano D — consequência**
- Plano sobre o ombro, mostrando a carta e a porta no mesmo eixo.
- Ela não toca na carta.
- Função: encerrar com decisão suspensa.

Cada plano deve receber um prompt independente, mas compartilhar a bíblia visual da personagem, do local e do figurino.

## 11. Falhas comuns a evitar

- Um único prompt tentando contar a cena inteira.
- Descrição de personagem que varia entre tomadas.
- Muitos movimentos de câmera contraditórios.
- Emoção abstrata sem ação visível.
- Excesso de adjetivos sem relação com o enquadramento.
- Prompts que repetem a mesma ação com palavras diferentes.
- Alterações acidentais de clima, cor, horário, roupa ou objeto.
- Texto pequeno ou legível em cena quando o modelo não controla tipografia.
- Exigir continuidade perfeita sem referência visual ou revisão.
- Gerar prompts antes de compreender a função dramática da cena.

## 12. Entrega de produção

Um pacote robusto pode incluir:
- versão do roteiro;
- bíblia de personagens;
- bíblia de ambientes;
- paleta e regras visuais;
- shot list;
- prompt global por personagem;
- prompt global por local;
- prompt individual por tomada;
- som e diálogo;
- instruções de continuidade;
- lista de riscos e soluções de pós-produção.

A qualidade final depende tanto da clareza dramática quanto de geração, seleção de takes, montagem, som e revisão humana.
