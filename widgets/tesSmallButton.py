from widgets import tesButtonclass tesSmallButton(tesButton):    def __init__(self,                 container,                 text: str | None = None,                 width: int = 40,                 height: int = 40,                 radius: int = 5,                 backgroundidx: int = 2,                 icon: str | bool = './icons/tk_smal.png',                 shadow: int | bool = 0,                 style='simple',                 **kw):        tesButton.__init__(self,                           container=container,                           text=text,                           width=width,                           height=height,                           radius=radius,                           backgroundidx=backgroundidx,                           icon=icon,                           shadow=shadow,                           style=style,                           **kw)    def _record_style(self) -> None:        self.draw_diode(size=5)