# -*- coding: utf-8 -*-
"""
Build high fidelity museum masterpiece plates for:
- Act 5 Scene 1: act5_1_moscow_1923.jpg (Aivazovsky Moscow in Winter)
- Act 5 Scene 3: act5_3_hongkong_unification.jpg (Hong Kong / Kowloon 1930)
- Act 6 Scene 1: act5_1_pacbo_return.jpg (Authentic Pác Bó Coc Bo border landscape)
- Act 6 Scene 2: act5_2_pacbo_lamp.jpg (Hang Cốc Bó with warm revolutionary lamplight)
- Act 6 Scene 3: act5_3_sunrise_independence.jpg (Karst sunrise over Vietnamese homeland)
"""

import os, math
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw

W, H = 1920, 1080

def apply_cinematic_vignette(img, dark_overlay=(15, 12, 10), vignette_strength=0.35):
    vignette = Image.new('L', (W, H), 0)
    v_draw = ImageDraw.Draw(vignette)
    cx, cy = W / 2, H / 2
    max_d = math.hypot(cx, cy)
    for r in range(0, int(max_d), 20):
        alpha = int(255 * (1 - (r / max_d) ** 1.9))
        v_draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=max(0, min(255, alpha)), width=22)
    vignette = vignette.filter(ImageFilter.GaussianBlur(60))
    overlay = Image.new('RGB', (W, H), dark_overlay)
    composite = Image.composite(img, overlay, vignette)
    return Image.blend(img, composite, vignette_strength)

def build_moscow_plate():
    """Aivazovsky's Moscow in Winter from Sparrow Hills"""
    src = 'aivazovsky_moscow.jpg'
    raw = Image.open(src).convert('RGB')
    orig_w, orig_h = raw.size
    
    # Crop to 16:9
    crop_h = int(orig_w / (16 / 9))
    y_start = (orig_h - crop_h) // 2
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Color grade: Russian winter cool twilight with soft warm highlights
    enh_c = ImageEnhance.Contrast(resized)
    graded = enh_c.enhance(1.08)
    enh_col = ImageEnhance.Color(graded)
    graded = enh_col.enhance(1.05)
    
    final = apply_cinematic_vignette(graded, dark_overlay=(16, 20, 26), vignette_strength=0.35)
    final.save('act5_1_moscow_1923.jpg', quality=95)
    print("Successfully built act5_1_moscow_1923.jpg (1920x1080)")

def build_hongkong_plate():
    """Hong Kong / Kowloon 1930 historic archive photo with warm revolutionary sepia"""
    src = 'hongkong_1930_archive.jpg'
    raw = Image.open(src).convert('RGB')
    orig_w, orig_h = raw.size
    
    # Crop to 16:9: Take the bustling street and colonial rooftops of Kowloon
    crop_h = int(orig_w / (16 / 9))
    y_start = int((orig_h - crop_h) * 0.45)
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Sepia & rich contrast
    gray = resized.convert('L')
    sepia = ImageOps.colorize(gray, black=(22, 16, 12), white=(242, 222, 192), mid=(146, 114, 82))
    
    enh_c = ImageEnhance.Contrast(sepia)
    graded = enh_c.enhance(1.15)
    
    # Warm amber glow in center (secret room lantern warmth)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([W*0.35, H*0.35, W*0.65, H*0.75], fill=(245, 158, 11, 40))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    graded.paste(glow, (0, 0), glow)
    
    final = apply_cinematic_vignette(graded, dark_overlay=(18, 14, 10), vignette_strength=0.45)
    final.save('act5_3_hongkong_unification.jpg', quality=95)
    print("Successfully built act5_3_hongkong_unification.jpg (1920x1080)")

def build_pacbo_return():
    """Authentic Pác Bó stream and mountain border landscape (No blur!)"""
    src = 'reference_pac_bo_coc_bo.jpg'
    raw = Image.open(src).convert('RGB')
    orig_w, orig_h = raw.size
    
    crop_h = int(orig_w / (16 / 9))
    y_start = (orig_h - crop_h) // 2
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Natural film grade: crisp limestone details, deep emerald moss, morning dawn light
    enh_c = ImageEnhance.Contrast(resized)
    graded = enh_c.enhance(1.12)
    enh_col = ImageEnhance.Color(graded)
    graded = enh_col.enhance(1.10)
    
    # Slight historical sepia-gold tint to honor 1941 return
    sepia_overlay = ImageOps.colorize(graded.convert('L'), black=(15, 18, 12), white=(240, 230, 205), mid=(125, 120, 95))
    blended = Image.blend(graded, sepia_overlay, 0.28)
    
    final = apply_cinematic_vignette(blended, dark_overlay=(12, 16, 12), vignette_strength=0.35)
    final.save('act5_1_pacbo_return.jpg', quality=95)
    print("Successfully built act5_1_pacbo_return.jpg (1920x1080)")

def build_pacbo_lamp():
    """Hang Cốc Bó interior with warm kerosene lamplight glowing on the stone table"""
    src = 'reference_pac_bo_coc_bo.jpg'
    raw = Image.open(src).convert('RGB')
    orig_w, orig_h = raw.size
    
    # Crop focusing on cave interior and stone formations
    crop_h = int(orig_w / (16 / 9))
    y_start = int((orig_h - crop_h) * 0.6)
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Deepen cave shadows
    enh_c = ImageEnhance.Contrast(resized)
    graded = enh_c.enhance(1.18)
    
    # Warm amber lantern glow radiating from the revolutionary stone workspace
    lamp_x, lamp_y = int(W * 0.42), int(H * 0.58)
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([lamp_x - 360, lamp_y - 280, lamp_x + 360, lamp_y + 280], fill=(245, 158, 11, 75))
    g_draw.ellipse([lamp_x - 180, lamp_y - 140, lamp_x + 180, lamp_y + 140], fill=(253, 224, 71, 130))
    g_draw.ellipse([lamp_x - 60, lamp_y - 50, lamp_x + 60, lamp_y + 50], fill=(255, 255, 220, 210))
    glow = glow.filter(ImageFilter.GaussianBlur(55))
    
    blended = Image.alpha_composite(graded.convert('RGBA'), glow).convert('RGB')
    final = apply_cinematic_vignette(blended, dark_overlay=(10, 8, 6), vignette_strength=0.55)
    final.save('act5_2_pacbo_lamp.jpg', quality=95)
    print("Successfully built act5_2_pacbo_lamp.jpg (1920x1080)")

def build_sunrise_plate():
    """Glorious karst sunrise over Vietnamese homeland"""
    src = 'karst_sunrise.jpg'
    raw = Image.open(src).convert('RGB')
    orig_w, orig_h = raw.size
    
    # Crop to 16:9: Capturing the dramatic limestone karst peaks, sea of mist, and glowing red/golden dawn
    crop_h = int(orig_w / (16 / 9))
    y_start = int((orig_h - crop_h) * 0.35)
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Enhance the heroic golden-crimson sunrise
    enh_c = ImageEnhance.Contrast(resized)
    graded = enh_c.enhance(1.14)
    enh_col = ImageEnhance.Color(graded)
    graded = enh_col.enhance(1.18)
    
    final = apply_cinematic_vignette(graded, dark_overlay=(18, 10, 8), vignette_strength=0.30)
    final.save('act5_3_sunrise_independence.jpg', quality=95)
    print("Successfully built act5_3_sunrise_independence.jpg (1920x1080)")

if __name__ == '__main__':
    build_moscow_plate()
    build_hongkong_plate()
    build_pacbo_return()
    build_pacbo_lamp()
    build_sunrise_plate()
