

# SusaPad Software

> [[English](./README.md)] | [[Português](./README.pt-br.md)]

![gpl-3.0](./susapad/media/gplv3-with-text-136x68.png)

*SusaPad Software* es el software usado para configurar *SusaPad*/[*MiniPad*][minipad].

> **Note**: *SusaPad Software* hace referencia al proyecto en si mismo,
> el no es el mismo que *SusaPad*, cuyo es un *keypad* (hardware).

[minipad]: https://github.com/minipadKB

## Guía del usuario

### Instalación

> **Warning**: En produción...

### Issues

Puedes añadir propuestas: bugs, dudas, preguntas,
solicitud de nuevas funcionalidades via Issues.

Por favor, leas cuidadosamiente [nosa Issue fijada][issue-1]
y asegúrase de saber sobre las
[Pautas de la Comunidad de GitHub][gh-rules].

[issue-1]: https://github.com/susapad/software/issues/1
[gh-rules]: https://docs.github.com/es/site-policy/github-terms/github-community-guidelines#maintaining-a-strong-community

---


## Licencias

> Parte de esa secção será mantida en inglés.

### SusaPad Software

*SusaPad Software* está cubierto por la *GPL-3.0*, y sigue los siguientes
cuatro grados de liberdad:

- Liberdad de ejecutar el programa para cualquier propósito.
- Liberdad de estudiar como el programa funciona y adaptarlo a certas necesidades.
- Liberdad de redistribuir copias, de modo que pueda ayudar tu próximo.
- Liberdad de mejorar el programa y lanzar tus mejoramientos para el público,
    así de que toda la comunidad se beneficiará.

Para mas detalles nuestra licensa: [LICENSE](./LICENSE).

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

### ¿Es este software compatíble con el *Minipad*?

Si, esse software es compatible con la [versión actual del *minipad-firmware*
 (*2023.410.1*)][minipad-release], que el *SusaPad* irá usar.

### ¿Por qué mi aplicación es tan lenta?

Esto no es la aplicación en si,
mas la forma con que comunicamonos con el arduino.

Infelismente, los comando somente pueden ser enviados con
uno segundo de intervalo entre los mismos.
Como resultado, algunas configuraciones pueden
levar hasta seis segundos para completarse.

### Ese software es traducido?

No, pero planejamos traducirlo próximamente.
Por ahora, el *SusaPad Software* apresentase
disponible sólo en el portugués,
la lenguaje nativa del proyeto.


### ¿Este proyecto tiene alguna relación con otros?

No. Este proyecto es independiente
y no tiene alguna relación con otros proyectos
como *Minipad Project*, *Nuitka*, *pySerial* o *QT Company*,
solamente con *SusaPad* en si.


[minipad-release]: https://github.com/minipadKB/minipad-firmware/releases/tag/2023.410.1


## Contributors

- Mantenedor: [sousaone1][sousa]
- Desarollador: [rickbarretto][rick]
- Designer de Logo: [Axiey][logo]
- Aplicación legado por: [Luiz Fernando][batatinho]

Es bueno mencionar Luiz Fernando o cuál fue responsable por crear
la primera versión funcional de el *SusaPad* en *Kivy*.


[sousa]: https://github.com/sousaone1
[rick]: https://github.com/RickBarretto
[logo]: https://osu.ppy.sh/users/11711340
[batatinho]: https://github.com/batatinhoProGamer
