from typing import cast
from coldtype import (
    Rect,
    random,
    StSt,
    animation,
    Frame,
    P,
    Style,
    Font,
    Glyphwise,
    hsl,
    MidiTimeline,
    renderable
)
import coldtype.fx.shapes as shapes
from coldtype.fx.skia import phototype

font_path = '~/.fonts/RobotoFlex-VariableFont_GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght.ttf'

font = Font.Cacheable(font_path)

tl = MidiTimeline(
    'drum.mid',
    bpm=80,
    fps=60,
)


@renderable((1920, 1080))
def anim(r: Rect):

    style = Style(
        font, 250,
        wght=1
    )

    texto = Glyphwise('30\nDias de\nPYTHON!', lambda g: style)
    
    (texto
     .align(r)
     .f(hsl(.3, 1, .5))
     .layer(
        lambda p: p.castshadow(-45, 50).f(0),
        lambda p: p.fssw(1, hsl(0.9), 5)
    ).removeOverlap()

    )

    return texto
