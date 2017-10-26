# colorshift.py
Automatically apply colorscheme to one or all urxvt instances

# Dependencies
* urxvt
* [urxvt-config-reload](https://github.com/regnarg/urxvt-config-reload)
* Xresources colorschemes (I use [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes))

# Setup
`colorshift.py` will overwrite the first line of `.Xresources` with a line of the form `#include "<path_to_colorscheme>"`. You must verify that this won't break your `.Xresources` before running the script. If no `.Xresources` file is specified, `~/.Xresources` will be used by default.

# Usage
```
usage: colorshift.py [-h] [-a] [-x XRESOURCES] colorscheme

positional arguments:
  colorscheme           the .Xresources colorscheme to use

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             change colors on all urvxt instances
  -x XRESOURCES, --xresources XRESOURCES
                        path to the .Xresources file
```
