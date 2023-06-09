

# SusaPad Software

> [[Português](./README.pt-br.md)] | [[Español](./README.es.md)]

![gpl-3.0](./susapad/media/gplv3-with-text-136x68.png)

*SusaPad Software* is the software used to configure [*SusaPad*][susapad]/[*MiniPad*][minipad].

> **Note**: *SusaPad Software* refers to this project itself,
> but it's not the same as *SusaPad*, which is just a *keypad* (hardware).

[susapad]: https://github.com/susapad/susapad
[minipad]: https://github.com/minipadKB

## User Guide

### Installation

*SusaPad Software* is a portable application, so no installation required.

You can download it from [*Github's release*][releases].
Be careful and select the right one for your system.

![releases](./susapad/media/releases.png)

Then unzip the package in some folder that you won't delete or change,
and pin to your start-up page.

![pin susapad](./susapad/media/pin-susapad-software.png)


[releases]: https://github.com/susapad/software/releases

### Uninstallation

As said before, *SusaPad Software* is portable,
so to uninstall you just need to erase *SusaPad Software*'s folder.

### Issues

You can add issues: bugs, doubts, questions, feature requests,
via Issues.

Please, carefully read [our pinned Issue][issue-1]
and make sure that you know about
[Github's Community Guideline][gh-rules].

[issue-1]: https://github.com/susapad/software/issues/1
[gh-rules]: https://docs.github.com/en/site-policy/github-terms/github-community-guidelines#maintaining-a-strong-community

---


## Licenses

### SusaPad Software

*SusaPad Software* is under *GPL-3.0*, and it follows the following
four degrees of freedom:

- Freedom to run the program for any purpose.
- Freedom to study how the program works & adapt it to specific needs.
- Freedom to redistribute copies so you can help your neighbor.
- Freedom to improve the program & release your improvements to the public,
    so that the whole community benefits.

For more details about our licence: [LICENSE](./LICENSE).

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

### Is it compatible with *Minipad*?

Yes, it's compatible with the [current *minipad-firmware*'s
version (*2023.410.1*)][minipad-release],
which *SusaPad* will use.


### Why my application is so slow?

It's not the application itself,
but the way it comunicate with arduino.

Unfortunately, the commands can only be sent with
one second of interval between.
As a result, some configurations
may take up to six seconds to complete.


### Is this software translated?

No, it isn't. But we plan to translate it soon.
For now *SusaPad Software* is just available to Portuguese,
the native language of this project.


### Does this project have any relationship with others?

No, it isn't. This project is independent
and has no relationship with other projects
such as *Minipad Project*, *Nuitka*, *pySerial* or *QT Company*,
but it has relationship with *SusaPad* itself.


[minipad-release]: https://github.com/minipadKB/minipad-firmware/releases/tag/2023.410.1


## Contributors

- Maintainer: [sousaone1][sousa]
- Developer: [rickbarretto][rick]
- Logo Designer: [Axiey][logo]
- Legacy application by: [Luiz Fernando][batatinho]

It's good to mention Luiz Fernando who was responsible for creating
the first functional version of *SusaPad* in *Kivy*.


[sousa]: https://github.com/sousaone1
[rick]: https://github.com/RickBarretto
[logo]: https://osu.ppy.sh/users/11711340
[batatinho]: https://github.com/batatinhoProGamer
