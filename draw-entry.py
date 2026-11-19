#!/usr/bin/env python3
"""Draw the 19 November 2026 front page: one 1024x1024 image that sums up
the day's world news. Deterministic: fixed seed, fixed fonts, fixed text.
Run:  python3 draw-entry.py   -> writes entry.png beside this file.
Only the Python standard library plus Pillow are used, at build time.
The entry program itself (main.ts) only copies the finished entry.png.
"""
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap, returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def gradient(draw, box, top, bottom):
    x0, y0, x1, y1 = box
    for yy in range(y0, y1):
        t = (yy - y0) / max(1, y1 - y0)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        draw.line([(x0, yy), (x1, yy)], fill=c)


def skyline(draw, x0, y_base, x1, color, seed=7):
    rnd = random.Random(seed)
    x = x0
    while x < x1:
        w = rnd.randint(28, 58)
        h = rnd.randint(28, 92)
        draw.rectangle([x, y_base - h, min(x + w, x1), y_base], fill=color)
        for wy in range(y_base - h + 8, y_base - 6, 14):
            for wx in range(x + 6, min(x + w - 4, x1 - 4), 12):
                if rnd.random() < 0.35:
                    draw.rectangle([wx, wy, wx + 4, wy + 5],
                                   fill=(255, 214, 120))
        x += w + 4


def main():
    img = Image.new("RGB", (W, H), (248, 244, 232))
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 118], fill=(14, 30, 58))
    d.text((512, 14), "THE WORLD TODAY", font=font(SERIF_B, 62),
           fill=(255, 255, 255), anchor="ma")
    d.text((512, 82), "THURSDAY  19  NOVEMBER  2026    •    ONE DAY, ONE IMAGE",
           font=font(SANS_B, 19), fill=(232, 196, 106), anchor="ma")
    d.rectangle([0, 118, W, 122], fill=(232, 196, 106))

    # ---- hero: GTA VI / Vice City --------------------------------------
    hx0, hy0, hx1, hy1 = 24, 134, 1000, 470
    gradient(d, (hx0, hy0, hx1, hy1), (255, 94, 138), (64, 24, 110))
    d.ellipse([452, 168, 572, 288], fill=(255, 214, 120))
    d.ellipse([472, 188, 552, 268], fill=(255, 236, 170))
    skyline(d, hx0, hy1 - 78, hx1, (38, 10, 68), seed=11)
    d.rectangle([hx0, hy1 - 78, hx1, hy1], fill=(16, 8, 40))
    d.rectangle([hx0, hy1 - 78, hx1, hy1 - 74], fill=(255, 94, 138))
    d.rectangle([hx0, hy1 - 182, hx1, hy1 - 78], fill=(16, 8, 40))
    d.text((hx0 + 28, hy1 - 168), "CULTURE  •  THE BIGGEST LAUNCH IN YEARS",
           font=font(SANS_B, 20), fill=(255, 214, 120))
    d.text((hx0 + 26, hy1 - 142), "VICE CITY IS OPEN",
           font=font(SANS_B, 58), fill=(255, 255, 255),
           stroke_width=2, stroke_fill=(16, 8, 40))
    para(d, hx0 + 28, hy1 - 72,
         "GTA VI launches today after a 13-year wait — Lucia & Jason return "
         "to Leonida on PS5 & Xbox, at midnight local time.",
         font(SANS, 21), (255, 255, 255), hx1 - hx0 - 56, 27)

    # ---- middle row ----------------------------------------------------
    my0, my1 = 482, 742
    # Gulf panel (left)
    gx0, gx1 = 24, 500
    d.rectangle([gx0, my0, gx1, my1], fill=(58, 13, 13))
    d.rectangle([gx0, my0, gx1, my0 + 6], fill=(217, 119, 6))
    for r in (56, 40, 24):
        d.ellipse([gx0 + 410 - r, my0 + 62 - r, gx0 + 410 + r, my0 + 62 + r],
                  outline=(217, 119, 6), width=3)
    d.ellipse([gx0 + 404, my0 + 56, gx0 + 416, my0 + 68],
              fill=(255, 214, 120))
    d.text((gx0 + 24, my0 + 18), "WAR  •  THE GULF",
           font=font(SANS_B, 19), fill=(255, 170, 80))
    d.text((gx0 + 24, my0 + 48), "GULF WAR\nWIDENS",
           font=font(SANS_B, 40), fill=(255, 255, 255))
    para(d, gx0 + 24, my0 + 148,
         "Iran fires on US sites in Kuwait overnight, after the US struck "
         "Qeshm Island. Bahrain intercepts attacks for a third time in a week.",
         font(SANS, 20), (245, 235, 220), gx1 - gx0 - 48, 27)

    # Jeffries panel (right)
    jx0, jx1 = 524, 1000
    d.rectangle([jx0, my0, jx1, my1], fill=(18, 50, 94))
    d.rectangle([jx0, my0, jx1, my0 + 6], fill=(232, 196, 106))
    # Capitol dome, white silhouette, top-right beside the headline
    d.rectangle([jx0 + 356, my0 + 62, jx0 + 404, my0 + 118], fill=(255, 255, 255))
    d.pieslice([jx0 + 352, my0 + 28, jx0 + 408, my0 + 84], 180, 360,
               fill=(255, 255, 255))
    d.rectangle([jx0 + 376, my0 + 14, jx0 + 384, my0 + 34], fill=(255, 255, 255))
    d.rectangle([jx0 + 344, my0 + 118, jx0 + 416, my0 + 126],
                fill=(255, 255, 255))
    d.text((jx0 + 24, my0 + 18), "USA  •  A FIRST IN WAITING",
           font=font(SANS_B, 19), fill=(232, 196, 106))
    d.text((jx0 + 24, my0 + 48), "JEFFRIES\nNOMINATED",
           font=font(SANS_B, 40), fill=(255, 255, 255))
    para(d, jx0 + 24, my0 + 148,
         "House Democrats pick Hakeem Jeffries 251–11. If elected on "
         "3 January, he becomes the first Black Speaker.",
         font(SANS, 20), (235, 242, 255), jx1 - jx0 - 48, 27)

    # ---- lower row -----------------------------------------------------
    ly0, ly1 = 754, 934
    # Pew panel (left)
    px0, px1 = 24, 500
    d.rectangle([px0, ly0, px1, ly1], fill=(15, 94, 91))
    d.text((px0 + 24, ly0 + 14), "FAITH IN 2035  •  PEW RESEARCH",
           font=font(SANS_B, 18), fill=(150, 230, 220))
    d.text((px0 + 24, ly0 + 42), "ISLAM TO PASS",
           font=font(SANS_B, 30), fill=(255, 255, 255))
    d.text((px0 + 24, ly0 + 76), "CHRISTIANITY",
           font=font(SANS_B, 30), fill=(255, 255, 255))
    d.rectangle([px0 + 24, ly0 + 122, px0 + 330, ly0 + 140],
                fill=(255, 214, 120))
    d.text((px0 + 32, ly0 + 123), "Islam", font=font(SANS_B, 15),
           fill=(15, 94, 91))
    d.text((px0 + 340, ly0 + 120), "2.57bn", font=font(SANS_B, 20),
           fill=(255, 255, 255))
    d.rectangle([px0 + 24, ly0 + 148, px0 + 322, ly0 + 166],
                fill=(180, 220, 215))
    d.text((px0 + 32, ly0 + 149), "Christians", font=font(SANS_B, 15),
           fill=(15, 94, 91))
    d.text((px0 + 332, ly0 + 146), "2.52bn", font=font(SANS_B, 20),
           fill=(255, 255, 255))

    # EU panel (right)
    ex0, ex1 = 524, 1000
    d.rectangle([ex0, ly0, ex1, ly1], fill=(29, 78, 158))
    for i in range(12):
        import math
        a = math.radians(i * 30 - 90)
        sx = ex0 + 410 + int(34 * math.cos(a))
        sy = ly0 + 62 + int(34 * math.sin(a))
        d.text((sx, sy), "*", font=font(SANS_B, 22), fill=(255, 214, 0),
               anchor="mm")
    d.text((ex0 + 24, ly0 + 14), "EUROPE  •  UKRAINE",
           font=font(SANS_B, 18), fill=(255, 214, 0))
    d.text((ex0 + 24, ly0 + 42), "€45BN FOR",
           font=font(SANS_B, 30), fill=(255, 255, 255))
    d.text((ex0 + 24, ly0 + 76), "UKRAINE",
           font=font(SANS_B, 30), fill=(255, 255, 255))
    para(d, ex0 + 24, ly0 + 122,
         "EU proposes a 2027 loan, to be repaid from future Russian "
         "reparations.",
         font(SANS, 19), (235, 242, 255), ex1 - ex0 - 48, 25)

    # ---- footer strip: Voyager + ticker --------------------------------
    d.rectangle([0, 946, W, H], fill=(8, 12, 24))
    rnd = random.Random(99)
    for _ in range(90):
        sx = rnd.randint(0, W - 1)
        sy = rnd.randint(946, H - 1)
        d.point((sx, sy), fill=(200, 210, 235))
    d.text((24, 956),
           "VOYAGER 1  •  ONE LIGHT-DAY AWAY — 25.9bn km, the farthest "
           "human-made object",
           font=font(SANS_B, 18), fill=(255, 255, 255))
    d.text((24, 982),
           "Also: Cyclone Akvan nears India's east coast  •  Nvidia chief "
           "Jensen Huang out",
           font=font(SANS, 17), fill=(180, 195, 220))

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}: {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
