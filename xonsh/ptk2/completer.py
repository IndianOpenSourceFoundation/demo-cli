# -*- coding: utf-8 -*-
"""Completer implementation to use with prompt_toolkit."""

from prompt_toolkit.completion import Completer

from dynamic.completer import CompleterDynamic


class PromptToolkitCompleter(Completer):
    """Simple prompt_toolkit Completer object.

    It just redirects requests to normal Xonsh completer.
    """

    def __init__(self, completer, ctx, shell):
        """Takes instance of xonsh.completer.Completer, the xonsh execution
        context, and the shell instance itself.
        """
        self.completer = completer
        self.ctx = ctx
        self.shell = shell
        self.completer_Dynamic = CompleterDynamic()

    def get_completions(self, document, complete_event):
        """Returns a generator for list of completions."""
        line = document.current_line.lstrip()
        endidx = document.cursor_position_col
        space_pos = document.find_backwards(' ')
        if space_pos is None:
            begidx = 0
        else:
            begidx = space_pos + endidx + 1
        prefix = line[begidx:endidx]
        completions, dummy = self.completer.complete(prefix,
                                                     line,
                                                     begidx,
                                                     endidx,
                                                     self.ctx)
        completions_Dynamic = \
            self.completer_Dynamic.get_completions(document,
                                                   complete_event)
        completions_with_meta = \
            self.completer_Dynamic.build_completions_with_meta(line,
                                                               prefix,
                                                               completions)
        completions_Dynamic.extend(completions_with_meta)
        for comp in completions_Dynamic:
            yield comp