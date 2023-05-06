

# SusaPad Software

> [[English](./README.md)] | [[Español](./README.es.md)]

![gpl-3.0](./susapad/media/gplv3-with-text-136x68.png)

*SusaPad Software* is the software used to configure *SusaPad*/[*MiniPad*][minipad].

> **Note**: *SusaPad Software* refere-se a esse projeto em si,
> mas não é o mesmo que o *SusaPad*, o qual é um *keypad* (hardware).

[minipad]: https://github.com/minipadKB

## Guia do Usuário

### Instalação

> **Warning**: Em produção...

### Propostas

Você poderá adicionar propostas:
bugs, dúvidas, perguntas, requisições de recursos,
via Issues.

Por favor, leia atentamente [nossa proposta fixada][issue-1]
e tenha certeza de estar ciente das
[Diretrizes da Comunidade do GitHub][gh-rules].

[issue-1]: https://github.com/susapad/software/issues/1
[gh-rules]: https://docs.github.com/pt/site-policy/github-terms/github-community-guidelines#maintaining-a-strong-community

---


## Licenses

> Parte dessa secção será mantida em inglês.

### SusaPad Software

*SusaPad Software* é coberto por *GPL-3.0*, e segue os seguintes
quatro degraus de liberdade:

- Liberdade de rodar o programa para quaisquer propósito.
- Liberdade de estudar como o programa funciona e adaptá-lo para necessidades específicas.
- Liberdade de de redistribuir cópias assim podendo ajudar seu próximo.
- Liberdade de aprimorar o programa e lançar suas melhorias para o público,
    assim toda a comunidade se beneficia.

Para mais detalhes sobre nossa licença: [LICENSE](./LICENSE).

### GNU Logo

Official GPL, AGPL and LGPL logos
These images are in the public domain.

For more details about GNU's logo, [GNU License Logos][gnu-logos].

### Nuitka

The Apache License, Version 2.0,
© 2023, Kay Hayen and Nuitka Contributors. All rights reserved.

This product is compiled by software developed
by Kay Hayen and Nuitka Contributors.
https://nuitka.net/index.html

For more details about their license, [read Nuitka's License][nuitka-license].

### pySerial

BSD license,
© 2001-2020 Chris Liechti <cliechti@gmx.net>

This product includes libraries developed
by Chris Liechti and pySerial's Contributors.
https://github.com/pyserial

For more details about their license, [read pySerial's License][pyserial-license].

### PySide6

The Lesser General Public License (LGPL),
© Copyright 2023 The Qt Company Ltd. All rights reserved.

This product includes libraries developed by The Qt Company Ltd.
for use in GUI.
https://www.qt.io/

For more details about their license, [read Qt's License][qt-license].

[gnu-logos]: https://www.gnu.org/graphics/license-logos.html
[nuitka-license]: https://www.apache.org/licenses/LICENSE-2.0
[pyserial-license]: https://github.com/pyserial/pyserial/blob/master/LICENSE.txt
[qt-license]: https://www.qt.io/licensing/


## FAQ

### Isto é compatível com *Minipad*?

Sim, isto é compatível com a [versão atual do *minipad-firmware*
(*2023.410.1*)][minipad-release],
o qual *SusaPad* utilizará.


### Por que minha aplicação é tão lenta?

Isso não é a aplicação em si,
mas a forma como nos comunicamos com o arduino.

Infelizmente, os comandos só podem ser enviado com
um segundo de intervalo entre eles.
Como resultado, algumas configurações
podem levar até seis segundos para serem completadas.


### Esse software é traduzido?

Não, mas planejamos traduzí-lo em breve.
Por enquanto, o *SusaPad Software* se apresenta
disponível apenas em português,
a linguagem nativa desse projeto.


### Esse projeto tem algum relacionamento com outros?

Não, ele não tem. Esse projeto é independete
e não tem quaisquer relações com outros projetos
como *Minipad Project*, *Nuitka*, *pySerial* ou *QT Company*,
apenas com o *SusaPad* em si.

[minipad-release]: https://github.com/minipadKB/minipad-firmware/releases/tag/2023.410.1


## Contribuidores

- Mantenedor: [sousaone1][sousa]
- Desenvolvedor: [rickbarretto][rick]
- Designer da Logo: [Axiey][logo]
- Applicação legado por: [Luiz Fernando][batatinho]

É bom mencionar Luiz Fernando o qual foi responsável por criar
a primeira versão funcional do *SusaPad* em *Kivy*.


[sousa]: https://github.com/sousaone1
[rick]: https://github.com/RickBarretto
[logo]: https://osu.ppy.sh/users/11711340
[batatinho]: https://github.com/batatinhoProGamer
