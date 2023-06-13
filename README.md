# GML BI Community Edition

Esta é uma ferramenta de análise de dados que pode ajudá-lo a obter mais leads, aumentar
suas vendas e receita.

É possível integrar os dados com nossas outras ferramentas, para melhorar o
relacionamento com o cliente (CRM), ou melhorar a sua reputação ou ainda obter feedback.

Esta ferramenta é de uso gratuito.

## Como funciona?

Primeiramente, você precisa [baixar](https://www.getmoreleads.com.br/download/) a
base de dados. Este banco de dados contém 6M Empresas (CNPJ) e o tamanho é de
aproximadamente 500MB.

Esses dados foram limpos e enriquecidos e estão disponíveis para serem usados por meio
de um **Dashboard** ou **EDA**. Ambos são ferramentas analíticas, conhecidas como Web
Analysis Tool (WAT), onde você pode executar no seu próprio computador sem a necessidade
de adquirir licenças.

- **Dashboard**: ferramenta de análise primária, iniciada automaticamente quando usado
  com o Docker.
- **EDA**: ferramenta de análise secundária, possui diversos recursos para fazer uma
  análise exploratória de dados, e não é iniciada automaticamente quando usado com o
  Docker. Para utilizar esta ferramenta, é necessário executar um comando no terminal.

O **Dashboard**, é uma ferramenta muito simples e fácil de usar, excelente para obter
informações rápidas e gerar leads. Basta filtrar por UF, Município e Tamanho da
Empresa. E todos os valores são atualizados automaticamente.

Além disso, você pode exportar/baixar os dados para um formato de arquivo CSV e
salvá-los em seu próprio computador.

<_insira uma amostra da imagem do painel_>

Mas há algumas _limitações_:

- Os dados disponibilizados é uma parte do banco de dados completo.
- O banco de dados completo contém mais de 30 milhões de empresas (CNPJ).
- Para usar este banco de dados completo, você pode escolher
  um [Plano](https://www.getmoreleads.com.br/plans/) e utilizar a nossa Solução Cloud.
- Ou você pode [fazer contato](mailto:service@getmoreleads.com.br), para saber mais
  sobre listas segmentadas que estejam mais adequado às suas necessidades.

**NOTAS**:

- Esta versão do aplicativo não foi criada ou testada para rodar no Windows apenas em
  Linux e Mac.
- Para rodar no Windows recomendamos o uso do Docker.

## Como instalar?

Você precisa ter o `git` instalado em sua máquina. Digite o comando abaixo para clonar o
repositório do GitHub:

````shell
$ git@github.com:lserra/gml_bi_ce.git
````

## Como usar?

1-Após clonar o repositório e baixar o banco de dados, você precisa mover a base de
dados para o seguinte caminho: `../gml_bi_ce/data/output`

2-Usando a janela do terminal, execute os comandos abaixo, para criar um _docker image_:

```shell
$ cd gml_bi_ce
$ bash build_local_image.sh
```

**NOTA**: certifique-se de que o Docker está instalado no seu computador e que ele está
ativo. Se você observar o retorno da mensagem de erro abaixo, provavelmente você não
possui o Docker instalado, ou não ele está ativo.

```text
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker
daemon running?
```

3-Em seguida, usando a janela do terminal, execute o comando abaixo, para ativar o
_docker container_:

```shell
$ bash start_local_container.sh
```

## Usage CLI command

You should type the commands below:

```shell script
$ cd tpodcli
$ bash tpod.sh
```

Output on your screen:

```text
------------------------------------------------------------
|||||||||||||||||| |||||[   tpod   ]||||| ||||||||||||||||||
------------------------------------------------------------
Podcast Audio File (MP3): Episode-142.mp3
Translating to Portuguese [N]: N
```

About the questions:

- For the first question you should type the full name of the audio file (podcast)¹.
- For the second question you should type Y (Yes) or N (No) to translate from English to
  Portuguese.

¹ *Note on library usage*:

- The audio file (podcast) is considered _**short**_, when the duration is smaller than
  60" (seconds).
- The audio file (podcast) is considered _**long**_, when the duration is longer than
  60" (seconds).

**Important**:

If the message below pops up on your screen during the app execution, DON'T WORRY!

``` text
RuntimeWarning: Couldn't find ffmpeg or avconv
```

It's not a bug and it's just WARNING! ⚠️

So, to use this app successfully is necessary to have installed on your machine the
following library ``ffmpeg``.
To know more about this library, please click [here](https://ffmpeg.org/about.html).

To download and install this library in your machine, please follow these
instructions [here](https://ffmpeg.org/download.html).

## Usage Docker

If you have Docker daemon installed in your machine you can use this app on Windows,
Linux or Mac.
You should execute the command below into the location of the directory containing the
Dockerfile.

```shell script
$ cd tpodcli
$ docker build t tpod/cli .
```

## Partnership or Sponsorship

If you found any issue or bug, please send us an [e-mail](mailto:tpodapp@gmail.com).

Or, if you have an idea or suggestion to improve it, or you are interested to contribute
with this project, please send us an [e-mail](mailto:tpodapp@gmail.com).

Or, if you prefer, you can . . .

<a href="https://buymeacoffee.com/cYXalAb" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
</a>

## Comments

This app is licensed under MIT copyright and is open-source.

```text
The MIT License (MIT)

Copyright (c) 2023 Laercio Serra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
