# Implementação do problema _Image Matching_

Este repositório foi criado com o intuito de realizar uma nova implementação para resolver o problema do _Image Matching_, um problema NP-Completo. Abaixo é apresentado um breve resumo do que é o problema em si, para informações mais aprofundadas, verificar o [docs/RelatorioParcial.pdf](https://github.com/Levysantiago/image-matching-algorithm/tree/master/docs/RelatorioParcial.pdf).

## Sumário

- [Image Matching (IM)](#image-matching-im)
- [Getting Started](#getting-started)
  - [Versões](#versões)
  - [Organização](#organização)
  - [Dependências](#dependências)
    - [SIFT](#sift)
  - [Executando os algoritmos](#executando-os-algoritmos)
  - [Incluindo suas próprias imagens](#incluindo-suas-próprias-imagens)
- [Autores](#autores)
- [Conhecimentos](#conhecimentos)
  - [Livros](#livros)
  - [Artigos](#artigos)

## Image Matching (IM)

O problema do IM ou Correspondência de Imagem tem sido abordado por diversos autores, a fim de buscar melhores técnicas para uma solução mais rápida e precisa. O problema consiste em analisar duas imagens A e B, onde B é uma transformação geométrica de A. O resultado desta análise deve ser o encontro de características semelhantes entre elas, de forma que, no final, estas correspondências sejam realçadas e apresentadas para facilitar uma determinada investigação. O IM é um componente chave para diversos processos de análise de imagens e é muito importante para inúmeras aplicações, como navegação, orientação, vigilância automática, fotogrametria e visão robótica. Na medicina, por exemplo, é de grande importância para encontrar relações entre diferenças no posicionamento do paciente, modalidades e aquisição de imagens variadas.

## Getting Started

### Versões

- Python 3.6.12 (esta foi a versão utilizada, mas funciona para outras versões também)

### Organização

Os principais arquivos encontram-se na pasta _root_. O `main.py` abre as imagens para dar como entrada ao algoritmo `lr2Matching.py`, que irá tentar encontrar correspondências entre as imagens. `helpers.py` contém diversas funções implementadas para serem utilizadas pelo algoritmo, o algoritmo SIFT está implementado no arquivo `SIFT.py` e o `plotGraph.py` é uma biblioteca usada para plotar o gráfico de comparação dos tempos em que cada algoritmo tomaram para resolver o problema. Na pasta `assets`, são organizadas todas as imagens que podem ser utilizadas como entrada do algoritmo. A pasta `docs` contém os relatórios com uma explicação melhor do problema em si e da proposta deste trabalho. A pasta `graph` contém o gráfico comparativo gerado pelo algoritmo depois de rodar a `main.py`. A pasta `tests` irá conter todos os resultados das correlações em imagens gerados pelos algoritmos para cada caso de teste.

```text
assets/
    apple.jpg
    apple2.jpg
    ...
docs/
    RelatorioParcial.pdf
    RelatorioFinal.pdf
graph/
    comparison.png
tests/
    .gitkeep
    ...
main.py
lrMatching.py
SIFT.py
plotGraph.py
helpers.py
```

### Dependências

Se você não tiver a biblioteca **Pillow** instalada, para instalar você pode utilizar os seguintes comandos:

```bash
$ pip install Pillow --user
```

`Caso seu python3 não seja o padrão, pode ser que você precise usar pip3 ou pip3.6`

```bash
$ pip3 install Pillow --user
```

Mais informações aqui na [documentação da biblioteca](https://pillow.readthedocs.io/en/3.0.x/installation.html).

#### SIFT

Para rodar o SIFT foi necessário utilizar algumas exatas versões de alguns pacotes.

```bash
$ pip3.6 install opencv-python==3.4.2.16
```

```bash
$ pip3.6 install opencv-contrib-python==3.4.2.16
```

```bash
$ sudo apt-get install python3.6-tk
```

```bash
$ pip3.6 install matplotlib
```

O código do algoritmo SIFT foi obtido através do site: https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/, aqui o funcionamento do algoritmo é explicado brevemente.

### Executando os algoritmos

O arquivo principal é o `main.py` que, por sua vez, irá chamar o algoritmo `lr2Matching.py`. Para iniciar o primeiro teste, basta rodar o comando:

```bash
$ python main.py
```

ou

```bash
$ python3.6 main.py
```

Ao rodar o algoritmo, ele irá ridar as três implementações e gerar os resultados das correlações em imagens na pasta `tests`, também irá gerar um gráfico comparativo na pasta `graph/` em relação ao tempo de execução que cada algoritmo levou para resolver o problema.

### Incluindo suas próprias imagens

Para utilizar os algoritmos com outras imagens de teste, primeiramente você deve incluir as imagens na pasta `assets`. Depois é só abrir o arquivo `main.py` e incluir os nomes das imagens nas seguintes linhas:

```python
[...]
srcImages = [
    ('mundi.jpg', 'mundi2.jpg'),
    ('cube.jpg', 'cube2.jpg'),
    ('many.jpg', 'many2.jpg'),
    ('apple.jpg', 'apple2.jpg'),
    ('appleCima.jpg', 'appleCima2.jpg'),
    ('novaImagem.jpg', 'novaImagem2.jpg'), #Novas imagens incluídas
    ]
[...]
```

Lembrando que as imagens precisam ser de mesmo tamanho e que devem ser quadradas para que todos os algoritmos rodem bem. Também a segunda imagem deve ser uma transformação geométrica da primeira, isto é, o mesmo objeto em um ângulo diferente ou deslocado na imagem. Depois só rodar o algoritmo com `python3.6 main.py`.

## Autores

- [Levy Santiago](https://github.com/Levysantiago)
- [Marcos Pinheiro](https://github.com/Mrpsousa)
- Rita Barreto

## Conhecimentos

### Livros

- [Introduction to algorithms](https://books.google.com.br/books?hl=pt-BR&lr=&id=aefUBQAAQBAJ&oi=fnd&pg=PR5&dq=Introduction+to+algorithms&ots=dO2uTvYOeX&sig=YMyUQYOoXToTjjPUV99TIT58ohg#v=onepage&q=Introduction%20to%20algorithms&f=false)
- [Programming Computer Vision with Python: Tools and algorithms for analyzing images](https://books.google.com.br/books?hl=pt-BR&lr=&id=J9b_CH-NrycC&oi=fnd&pg=PP2&dq=Programming+Computer+Vision+with+Python:+Tools+and+algorithms+for+analyzing+images&ots=B-38UYbJqx&sig=WoLkUH6S22_Mm5S71cwjrsYTiDA#v=onepage&q=Programming%20Computer%20Vision%20with%20Python%3A%20Tools%20and%20algorithms%20for%20analyzing%20images&f=false)
- [Computer Vision with Python 3](https://books.google.com.br/books?hl=pt-BR&lr=&id=jpZGDwAAQBAJ&oi=fnd&pg=PP1&dq=Computer+Vision+with+python+3&ots=XMF3c6fGwh&sig=6H9AgtnYb7AneoYpzUJXukhJ9ns#v=onepage&q=Computer%20Vision%20with%20python%203&f=false)
- [Hands-On Image Processing with Python: Expert techniques for advanced image analysis and effective interpretation of image data](https://books.google.com.br/books?hl=pt-BR&lr=&id=gC59DwAAQBAJ&oi=fnd&pg=PP1&dq=Hands-On+Image+Processing+with+Python:+Expert+techniques+for+advanced+image+analysis+and+effective+interpretation+of+image+data&ots=AhZIih7R8C&sig=I5_pCu0rqBWm64t08qzMK2E8A10#v=onepage&q=Hands-On%20Image%20Processing%20with%20Python%3A%20Expert%20techniques%20for%20advanced%20image%20analysis%20and%20effective%20interpretation%20of%20image%20data&f=false)

### Artigos

- [Elastic image matching is NP-complete](https://www.sciencedirect.com/science/article/pii/S0167865502002684?casa_token=cCHDdprnZs0AAAAA:DXQhG5ygMFkNKBskKszKVCHyDZRDsQvq2va4WL1miM_EAcfNe_ECoXgUtaJTpT2PFlms5xA0HA)
- [A monotonic and continuous two-dimensional warping based on dynamic programming](https://ieeexplore.ieee.org/abstract/document/711195/?casa_token=LZq0AKFvXDoAAAAA:o5MgPyJFAbS2Z1fh-wd_JWls2h7RW1z07uKE4tNQVF0dd5xN7-mCeF1V5yW4PWYmIoyMq3pU3A)
- [Desenvolvimento de Algoritmos de Exploração e Mapeamento Visual para Robôs Móveis de Baixo Custo](https://www.maxwell.vrac.puc-rio.br/9142/9142_1.PDF)
- [Distinctive image features from scale-invariant keypoints](https://link.springer.com/article/10.1023/B:VISI.0000029664.99615.94)
- [Structural indexing of infra-red images using statistical histogram comparison](https://www.sciencedirect.com/science/article/pii/B9780444825872501439)
- [Digital image processing](https://www.pearson.com/us/higher-education/program/Gonzalez-Digital-Image-Processing-4th-Edition/PGM241219.html)
- [A novel approach to detecting duplicate images using multiple hash tables](https://link.springer.com/article/10.1007/s11042-014-1857-x)
- [Variational methods for multimodal image matching](https://link.springer.com/article/10.1023/A:1020830525823)
- [Adaptive least squares correlation: a powerful image matching technique](https://www.researchgate.net/profile/Armin_Gruen/publication/265292615_Adaptive_Least_Squares_Correlation_A_powerful_image_matching_technique/links/0deec52a08d9325463000000/Adaptive-Least-Squares-Correlation-A-powerful-image-matching-technique.pdf)
- [Medical image matching-a review with classification](https://ieeexplore.ieee.org/abstract/document/195938?casa_token=Z5wACQ0M-VUAAAAA:_1ZAYQF_WldvQ86uJAmL1lPLSkK4GZcUCmHSJM0xnyUea6uxybOaCOnZwqIPdl80up0fZsQHlg)
- [A nonlinear variational problem for image matching](https://epubs.siam.org/doi/abs/10.1137/0915014)
- [Variational problems on flows of diffeomorphisms for image matching](https://www.jstor.org/stable/43638248?casa_token=9ZTr5avo57EAAAAA%3A5RszoIxY-zHc_fV6UH9rxNsO5xr8kDO3_896qCiO2tveKlrDWKFbnt3KMoafas9mJsyi4gzeQ7CKBVMxXWOrdTzuu9mOkm3AsiUOJfnXiHgnIlj-Z_k&seq=1#metadata_info_tab_contents)
- [Image matching from handcrafted to deep features: A survey](https://link.springer.com/article/10.1007/s11263-020-01359-2)
- [Modification of blurred image matching method](http://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=co&paperid=807&option_lang=eng)
