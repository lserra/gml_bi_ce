# GML BI Community Edition

This is a Data Analytics Platform to help you to get more leads, increase your sales and
revenue.

You can use those data with our other integration tools to improve your customer
relationship, reputation tracking or get more feedback. This tool is free (Community
Edition).

## How does it work?

First all, you need to [download](https://www.getmoreleads.com.br/download/) the
database. This database contains 6M Companies (CNPJ) and the size is roughly 500MB.

Those data have been cleaned up and enriched, and they are available to be used through
**Dashboard** or **EDA** tools. Both are Web Analysis Tool (WAT) where you run locally.

- **Dashboard**: it's the tool started initially when using with Docker.
- **EDA**: this tool has many features for an exploratory data analysis, and
  it's not started initially when using with Docker. To use this tool is necessary
  to execute a command in the terminal.

The **Dashboard**, it's the tool started initially when using with Docker, being
user-friendly and very easy to get insights and generate leads. Just filter by UF,
Municipio, and Company Size. And all values in the dashboard are refreshed
automatically.

Also, you are able to export/download this data to a CSV file format and save it
in your own computer.

<_insert a sample of the dashboard image_>

But there are a few _limitations_:

- The data available with this Data Analytics Platform is partial.
- The complete database contains more than 30M Companies (CNPJ).
- To use this complete database you can choose
  a [Plan](https://www.getmoreleads.com.br/plans/) and use our Cloud Solution.
- Or you can [contact us](mailto:service@getmoreleads.com.br) to make specific lists
  more fit with your needs.

**NOTES**:

- This app version was not created or tested to run on Windows just Linux and Mac.
- To run on Windows we recommend you to use Docker.

## How to install?

You need to have `git` installed in your machine. Type the commands below to clone the
repository from GitLab:

````shell
$ git@gitlab.com:l_serra/transcribe.git
````

## How to use?

1-Download your favorite podcast and save it into the local path app: `/tpodcli/data`

2-The audio file should be in the **MP3** format.

3-Using the terminal window execute the commands described below:

```shell script
$ cd tpodcli
$ bash install.sh
```

The command above will check all folders structure and files necessary to run the
application.

After that, if no errors has been found, you are ready to use the `tpod` app to start
your transcription and/or translation.

Automatically, a prompt appears to you, asking you to inform the name of the audio
file (podcast).

4-Type the name of the audio file (podcast).

**NOTES**:

- The podcast is a _**short**_ audio file if the duration is smaller than 60" (seconds).

- The podcast is a _**long**_ audio file if the duration is bigger than 60" (seconds).

This is necessary because for long audio files the `tpod` app works with audio
optimization.

5-After you've typed the name of the audio file (podcast), a new prompt appears asking
you about the translation to Portuguese (Y/N).

You should type `Y` for Yes - if you want to translate to Portuguese, or

You should type `N` for No - if you don't want to translate to Portuguese.

6-The output files are: `audio_transcript.csv` and `audio_transcript_pt.csv`.

You can find these files into the local path app: `/tpodcli/output`.

For this version, the main capabilities are: transcription and translation from audio
file (podcast) in EN-PT (English/Portuguese).

But, if you prefer you can use our [API](http://www.tpod.app.br/blog/api.html).
Thus, you can transcribe and translate your favorite podcast from other languages:

- EN/FR ou FR/EN (English/French or French/English)
- EN/ES ou ES/EN (English/Spanish or Spanish/English)

Or, if you're interested you can try out our other products/services:

- tpod Web
- tpod API
- storage and search podcasts
- transcribe and translate video's file

New updates are coming soon.

Please, visit our [site](http://www.tpod.app.br/)

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

Copyright (c) 2021 Laercio Serra

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
