from typing import cast
from coldtype import (
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


@animation((1920, 1080), timeline=tl, audio='30-intro.wav', bg=0)
def anim(f: Frame):
    f.a = cast(animation, f.a)

    bumbo = tl.ki(36)
    tom_1 = tl.ki(43)
    tan = tl.ki(64)
    dan = tl.ki(65)

    style = Style(
        font, 250,
        wght=bumbo.adsr([0, 100], rng=(1, 0)),
    )

    texto = Glyphwise('30\nDias de\nPYTHON!', lambda g: style)
    
    (texto
     .align(f.a.r, ty=1)
     .f(hsl(.3, 1, .5))
     .rotate(
         tom_1.adsr(
             [0, 15], rng=(0, 10)
         )
     )
    )

    layers = (
        lambda p: p.castshadow(-45, 50).f(0),
        lambda p: p.fssw(1, hsl(0.9), 5)
    )

    match bumbo.adsr([0, 100], find=1):
        case _, 0:
            texto.visible(True).layer(
                *layers
            ).removeOverlap()
        case _, 1:
            texto[0].visible(True)
            texto[0].scale(2)
            texto[0].align(f.a.r)
            texto[0].layer(
                *layers
            ).removeOverlap()
            texto[1].visible(False)
            texto[2].visible(False)
        case _, 2:
            texto[1].visible(True)
            texto[1].scale(2)
            texto[1].align(f.a.r)
            texto[1].layer(
                *layers
            ).removeOverlap()
            texto[0].visible(False)
            texto[2].visible(False)
        case _, 3:
            texto[2].visible(True)
            texto[2].scale(1.7)
            texto[2].layer(
                *layers
            ).removeOverlap()
            texto[2].align(f.a.r)
            texto[0].visible(False)
            texto[1].visible(False)

    match tan.adsr([0, 100], find=1):
        case 1, 0:
            texto.layer(
                lambda ps: ps.mapv(
                    lambda p: p.s(
                        hsl(random())).sw(4)
                )
            )

    match (a:= dan.adsr([0, 100], find=1)):
        case _, 0 if a[0] > 0:
            texto.layer(
                lambda ps: ps.mapv(
                    lambda p: p
                    .s(hsl(random())).sw(4)
                )
            )

    path = P().rect(
            f.a.r.inset(
                f.e(
                    'seio',
                    rng=(1_000, -100_000),
                    loop=1
                )
            )
        )

    return (
        path,
        texto
    )

anim.export('libx265', loops=1)
