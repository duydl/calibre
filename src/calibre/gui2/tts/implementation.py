#!/usr/bin/env python
# License: GPL v3 Copyright: 2020, Kovid Goyal <kovid at kovidgoyal.net>

from calibre.constants import iswindows, ismacos
from calibre.gui2.viewer.web_view import is_Audio_Ebook

print("is_Audio_Ebook", is_Audio_Ebook)
if is_Audio_Ebook:
    from .audio_player import Client
    print("Start to audioplayer!!!!!!!!")
elif iswindows:
    from calibre.utils.config_base import tweaks
    if tweaks.get('prefer_winsapi'):
        print("Winapi")
        from .windows_sapi import Client
    else:
        from .windows import Client
        print("Win")
elif ismacos:
    from .macos import Client
else:
    from .linux import Client
Client
