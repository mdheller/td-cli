from .base import Render


class RenderOutput(Render):
    def __init__(self, string_to_format):
        self.string_to_format = string_to_format

    def render(self, **kwargs):
        print(self._format(f"{self.string_to_format}%s" % "{reset}", **kwargs))
