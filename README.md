# calibre

<img align="left" src="https://raw.githubusercontent.com/kovidgoyal/calibre/master/resources/images/lt.png" height="200" width="200"/>

calibre is an e-book manager. It can view, convert, edit and catalog e-books 
in all of the major e-book formats. It can also talk to e-book reader 
devices. It can go out to the internet and fetch metadata for your books. 
It can download newspapers and convert them into e-books for convenient 
reading. It is cross platform, running on Linux, Windows and macOS.

For more information, see the [calibre About page](https://calibre-ebook.com/about).

[![Build Status](https://github.com/kovidgoyal/calibre/workflows/CI/badge.svg)](https://github.com/kovidgoyal/calibre/actions?query=workflow%3ACI)

## Screenshots  

[Screenshots page](https://calibre-ebook.com/demo)

## Usage

See the [User Manual](https://manual.calibre-ebook.com).

## Development

[Setting up a development environment for calibre](https://manual.calibre-ebook.com/develop.html).

A [tarball of the source code](https://calibre-ebook.com/dist/src) for the 
current calibre release.

## Bugs

Bug reports and feature requests should be made in the calibre bug tracker at [Launchpad](https://bugs.launchpad.net/calibre).
GitHub is only used for code hosting and pull requests.

## Support calibre

calibre is a result of the efforts of many volunteers from all over the world.
If you find it useful, please consider contributing to support its development.
[Donate to support calibre development](https://calibre-ebook.com/donate).

## Building calibre binaries

See [Build instructions](bypy/README.rst) for instructions on how to build the
calibre binaries and installers for all the platforms calibre supports.

## calibre package versions in various repositories

[![Packaging Status](https://repology.org/badge/vertical-allrepos/calibre.svg)](https://repology.org/project/calibre/versions)

# 1
Do on cmd, will not work on powershell
set CALIBRE_DEVELOP_FROM=C:\Projects\calibre\src   (must add src-different from doc)
echo %CALIBRE_DEVELOP_FROM% 

# 2 
https://manual.calibre-ebook.com/develop.html#debugging-tips

This is Kovid’s favorite way to debug. Simply insert print statements at points of interest and run your program in the terminal. For example, you can start the GUI from the terminal as:

calibre-debug -g
Similarly, you can start the E-book viewer as:

calibre-debug -w /path/to/file/to/be/viewed
The e-book-editor can be started as:

calibre-debug -t /path/to/be/edited

# 3

python calibre\gui2\tts\develop.py
> ModuleNotFoundError: No module named 'qt'

import sys
print(sys.path)
> No path in the path list

sys.path.append('C:\\Projects\\calibre\\src')
> ImportError: cannot import name 'QDialogButtonBox' from 'qt.core' (C:\Projects\calibre\src\qt\core.py)

pip install PyQt6

>File "C:\Projects\calibre\src\calibre\constants.py", line 173, in <module>
    plugins_loc = sys.extensions_location
AttributeError: module 'sys' has no attribute 'extensions_location'

You cant really use calibre code in external python interpreters, except on linux, if you install calibre system-wide. On windows, if you want to use calibre use calibre-debug as the python interpreter.

calibre-debug file.py

https://manual.calibre-ebook.com/dev...on-environment


# 4 Change Jap encoder 

New 'from calibre.ebooks.unihandecode.pykakasi.kakasi import Kakasi'

"src\calibre\ebooks\unihandecode"
src\calibre\ebooks\unihandecode\__init__.py
src\calibre\ebooks\unihandecode\jadecoder.py

