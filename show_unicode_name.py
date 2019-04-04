# -*- coding: utf-8 -*-
import sublime_plugin
import unicodedata

class NedShowUnicode(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        self.show_unicode(view)

    def on_activated(self, view):
        self.show_unicode(view)

    def show_unicode(self, view):
        selected = view.substr(view.sel()[0].a)
        view.set_status('a-ned-unicode', "U+{0:0>4X} #{0} {1}".format(ord(selected), unicodedata.name(selected, selected.encode('unicode_escape').decode('utf-8')).title()))
