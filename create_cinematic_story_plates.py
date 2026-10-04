import os, random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance

W, H = 1920, 1080

def create_vintage_base(bg_tone=(38, 28, 20), warmth=(215, 185, 140)):
    img = Image.new('RGB', (W, H), bg_tone)
    draw = ImageDraw.Draw(img)
    random.seed(1911)
    for _ in range(50):
        cx = random.randint(0, W)
        cy = random.randint(0, H)
        rx = random.randint(150, 600)
        ry = random.randint(100, 400)
        c = (
            min(255, warmth[0] + random.randint(-25, 25)),
            min(255, warmth[1] + random.randint(-25, 25)),
            min(255, warmth[2] + random.randint(-25, 25))
        )
        draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=c)
    img = img.filter(ImageFilter.GaussianBlur(radius=80))
    return img

def apply_ink_vignette_and_grain(img, intensity=0.65):
    vignette = Image.new('L', (W, H), 0)
    v_draw = ImageDraw.Draw(vignette)
    v_draw.ellipse([-int(W * 0.2), -int(H * 0.2), int(W * 1.2), int(H * 1.2)], fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=160))
    vignette_rgb = Image.new('RGB', (W, H), (15, 10, 8))
    result = Image.composite(img, vignette_rgb, vignette)
    return result

def make_dock_ship():
    base = create_vintage_base((45, 35, 25), (225, 195, 150))
    if os.path.exists('ship_1911.jpg'):
        ship_raw = Image.open('ship_1911.jpg').convert('RGB')
        ship_w, ship_h = ship_raw.size
        target_ratio = W / H
        if ship_w / ship_h > target_ratio:
            new_w = int(ship_h * target_ratio)
            left = (ship_w - new_w) // 2
            ship_cropped = ship_raw.crop((left, 0, left + new_w, ship_h))
        else:
            new_h = int(ship_w / target_ratio)
            top = (ship_h - new_h) // 2
            ship_cropped = ship_raw.crop((0, top, ship_w, top + new_h))
        
        ship_resized = ship_cropped.resize((W, H), Image.Resampling.LANCZOS)
        gray = ImageOps.grayscale(ship_resized)
        sepia_ship = ImageOps.colorize(gray, black=(25, 18, 12), white=(245, 215, 168), mid=(160, 125, 85))
        final = Image.blend(base, sepia_ship, 0.78)
    else:
        final = base

    draw = ImageDraw.Draw(final)
    for _ in range(35):
        sx = random.randint(int(W * 0.45), int(W * 0.85))
        sy = random.randint(int(H * 0.05), int(H * 0.35))
        sr = random.randint(40, 160)
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(22, 18, 16))
    final = final.filter(ImageFilter.GaussianBlur(radius=15))
    final = apply_ink_vignette_and_grain(final)
    final.save('dock_1_ship.jpg', quality=92)
    print('Generated dock_1_ship.jpg')

def make_dock_register():
    base = create_vintage_base((32, 22, 15), (230, 205, 160))
    draw = ImageDraw.Draw(base)
    book_x1, book_y1 = int(W * 0.12), int(H * 0.12)
    book_x2, book_y2 = int(W * 0.88), int(H * 0.88)
    
    draw.rectangle([book_x1 - 25, book_y1 - 25, book_x2 + 25, book_y2 + 25], fill=(55, 38, 25), outline=(90, 65, 40), width=4)
    draw.rectangle([book_x1, book_y1, book_x2, book_y2], fill=(240, 222, 185), outline=(120, 95, 65), width=3)
    mid_x = (book_x1 + book_x2) // 2
    draw.rectangle([mid_x - 12, book_y1, mid_x + 12, book_y2], fill=(185, 160, 125))
    
    for y in range(book_y1 + 180, book_y2 - 60, 48):
        draw.line([book_x1 + 40, y, mid_x - 40, y], fill=(200, 180, 145), width=1)
        draw.line([mid_x + 40, y, book_x2 - 40, y], fill=(200, 180, 145), width=1)
        
    seal_cx, seal_cy = book_x2 - 140, book_y1 + 140
    draw.ellipse([seal_cx - 55, seal_cy - 55, seal_cx + 55, seal_cy + 55], fill=(165, 40, 30), outline=(120, 25, 20), width=3)
    
    final = apply_ink_vignette_and_grain(base)
    final.save('dock_2_register.jpg', quality=92)
    print('Generated dock_2_register.jpg')

def make_dock_gangway():
    base = create_vintage_base((40, 30, 22), (230, 195, 145))
    if os.path.exists('ship_1911.jpg'):
        ship_raw = Image.open('ship_1911.jpg').convert('RGB').resize((W, H))
        gray = ImageOps.grayscale(ship_raw)
        sepia = ImageOps.colorize(gray, black=(20, 15, 10), white=(245, 220, 175), mid=(150, 115, 75))
        final = Image.blend(base, sepia, 0.70)
    else:
        final = base
    final = apply_ink_vignette_and_grain(final)
    final.save('dock_3_gangway.jpg', quality=92)
    print('Generated dock_3_gangway.jpg')

def make_ship_boiler():
    base = Image.new('RGB', (W, H), (20, 14, 10))
    draw = ImageDraw.Draw(base)
    for r in range(450, 50, -30):
        intensity = int(255 * (1 - r / 450))
        glow_color = (intensity, int(intensity * 0.45), int(intensity * 0.08))
        draw.ellipse([W//2 - r, int(H - r*1.2), W//2 + r, int(H + r*0.4)], fill=glow_color)
    base = base.filter(ImageFilter.GaussianBlur(radius=60))
    final = apply_ink_vignette_and_grain(base)
    final.save('ship_1_boiler.jpg', quality=92)
    print('Generated ship_1_boiler.jpg')

def make_ship_study():
    base = Image.new('RGB', (W, H), (14, 18, 25))
    draw = ImageDraw.Draw(base)
    lx, ly = int(W * 0.32), int(H * 0.58)
    for r in range(380, 40, -25):
        alpha = int(240 * (1 - r / 380))
        color = (alpha, int(alpha * 0.72), int(alpha * 0.28))
        draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=color)
    base = base.filter(ImageFilter.GaussianBlur(radius=55))
    final = apply_ink_vignette_and_grain(base)
    final.save('ship_2_study.jpg', quality=92)
    print('Generated ship_2_study.jpg')

def make_paris_lenin():
    base = create_vintage_base((30, 25, 20), (225, 200, 160))
    draw = ImageDraw.Draw(base)
    lx, ly = int(W * 0.48), int(H * 0.48)
    for r in range(420, 40, -30):
        intensity = int(255 * (1 - r / 420))
        color = (intensity, int(intensity * 0.78), int(intensity * 0.35))
        draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=color)
    base = base.filter(ImageFilter.GaussianBlur(radius=65))
    final = apply_ink_vignette_and_grain(base)
    final.save('act4_1_paris_lenin.jpg', quality=92)
    print('Generated act4_1_paris_lenin.jpg')

def make_guangzhou_school():
    base = create_vintage_base((38, 28, 18), (230, 195, 145))
    final = apply_ink_vignette_and_grain(base)
    final.save('act4_2_guangzhou_school.jpg', quality=92)
    print('Generated act4_2_guangzhou_school.jpg')

def make_party_founded():
    base = create_vintage_base((35, 22, 16), (225, 180, 130))
    draw = ImageDraw.Draw(base)
    for r in range(360, 50, -30):
        intensity = int(220 * (1 - r / 360))
        draw.ellipse([W//2 - r, H//2 - r, W//2 + r, H//2 + r], fill=(intensity, int(intensity * 0.25), int(intensity * 0.15)))
    base = base.filter(ImageFilter.GaussianBlur(radius=75))
    final = apply_ink_vignette_and_grain(base)
    final.save('act4_3_party_founded.jpg', quality=92)
    print('Generated act4_3_party_founded.jpg')

def make_pacbo_return():
    base = create_vintage_base((35, 30, 24), (210, 195, 160))
    if os.path.exists('reference_pac_bo_coc_bo.jpg'):
        pacbo_raw = Image.open('reference_pac_bo_coc_bo.jpg').convert('RGB').resize((W, H))
        gray = ImageOps.grayscale(pacbo_raw)
        sepia = ImageOps.colorize(gray, black=(20, 18, 14), white=(235, 215, 175), mid=(135, 120, 95))
        final = Image.blend(base, sepia, 0.72)
    else:
        final = base
    final = apply_ink_vignette_and_grain(final)
    final.save('act5_1_pacbo_return.jpg', quality=92)
    print('Generated act5_1_pacbo_return.jpg')

def make_pacbo_lamp():
    base = create_vintage_base((30, 26, 20), (220, 190, 140))
    if os.path.exists('reference_pac_bo_coc_bo.jpg'):
        pacbo_raw = Image.open('reference_pac_bo_coc_bo.jpg').convert('RGB').resize((W, H))
        gray = ImageOps.grayscale(pacbo_raw)
        sepia = ImageOps.colorize(gray, black=(18, 15, 12), white=(240, 210, 160), mid=(140, 115, 80))
        final = Image.blend(base, sepia, 0.65)
    else:
        final = base
    draw = ImageDraw.Draw(final)
    lx, ly = int(W * 0.35), int(H * 0.62)
    for r in range(320, 30, -25):
        intensity = int(245 * (1 - r / 320))
        draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=(intensity, int(intensity * 0.75), int(intensity * 0.32)))
    final = final.filter(ImageFilter.GaussianBlur(radius=40))
    final = apply_ink_vignette_and_grain(final)
    final.save('act5_2_pacbo_lamp.jpg', quality=92)
    print('Generated act5_2_pacbo_lamp.jpg')

def make_sunrise_independence():
    base = Image.new('RGB', (W, H), (45, 18, 12))
    draw = ImageDraw.Draw(base)
    sx, sy = W // 2, int(H * 0.62)
    for r in range(850, 40, -45):
        progress = 1 - r / 850
        r_col = 255
        g_col = int(220 * progress)
        b_col = int(90 * progress)
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(r_col, g_col, b_col))
    base = base.filter(ImageFilter.GaussianBlur(radius=80))
    final = apply_ink_vignette_and_grain(base, intensity=0.4)
    final.save('act5_3_sunrise_independence.jpg', quality=94)
    print('Generated act5_3_sunrise_independence.jpg')

if __name__ == '__main__':
    make_dock_ship()
    make_dock_register()
    make_dock_gangway()
    make_ship_boiler()
    make_ship_study()
    make_paris_lenin()
    make_guangzhou_school()
    make_party_founded()
    make_pacbo_return()
    make_pacbo_lamp()
    make_sunrise_independence()
    print('All historical art plates generated successfully!')
