# -*- coding: utf-8 -*-
"""
Build high fidelity museum masterpiece plates for Act 4:
- act4_1_versailles_1919.jpg: Sir William Orpen's The Signing of Peace in the Hall of Mirrors (1919)
- act4_3_tours_congress.jpg: Congrès de Tours 1920 grand hall (Salle du Manège)
"""

import os, math
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

W, H = 1920, 1080

def apply_cinematic_vignette(img, vignette_strength=0.35):
    """Adds subtle museum depth vignette without muddying the painting."""
    vignette = Image.new('L', (W, H), 0)
    import ImageDraw
    draw = ImageDraw.Draw(vignette)
    cx, cy = W / 2, H / 2
    max_d = math.hypot(cx, cy)
    for r in range(0, int(max_d), 20):
        alpha = int(255 * (1 - (r / max_d) ** 1.8))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=max(0, min(255, alpha)), width=22)
    vignette = vignette.filter(ImageFilter.GaussianBlur(50))
    dark_overlay = Image.new('RGB', (W, H), (14, 11, 8))
    # Blend gently
    return Image.blend(img, Image.composite(img, dark_overlay, vignette), vignette_strength)

def build_versailles():
    src_path = 'versailles_orpen.jpg'
    if not os.path.exists(src_path):
        print(f"Error: {src_path} not found")
        return
    
    raw = Image.open(src_path).convert('RGB')
    orig_w, orig_h = raw.size
    
    # In Orpen's masterpiece, include the towering golden chandeliers, gilded arches and delegates
    crop_h = int(orig_w / (16 / 9))
    y_start = int((orig_h - crop_h) * 0.40)
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Lift shadows & enhance golden palace warmth
    enh_bright = ImageEnhance.Brightness(resized)
    graded = enh_bright.enhance(1.15)
    enh_color = ImageEnhance.Color(graded)
    graded = enh_color.enhance(1.18)
    enh_contrast = ImageEnhance.Contrast(graded)
    graded = enh_contrast.enhance(1.05)
    
    # Subtle soft vignette only at the very extreme corners
    from PIL import ImageDraw
    vignette = Image.new('L', (W, H), 0)
    v_draw = ImageDraw.Draw(vignette)
    cx, cy = W / 2, H / 2
    max_d = math.hypot(cx, cy)
    for r in range(0, int(max_d), 20):
        alpha = int(255 * (1 - (r / max_d) ** 2.5))
        v_draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=max(0, min(255, alpha)), width=25)
    vignette = vignette.filter(ImageFilter.GaussianBlur(80))
    dark_overlay = Image.new('RGB', (W, H), (20, 16, 12))
    final = Image.composite(graded, dark_overlay, vignette)
    final = Image.blend(graded, final, 0.25)
    
    final.save('act4_1_versailles_1919.jpg', quality=95)
    print("Successfully built act4_1_versailles_1919.jpg (1920x1080)")

def build_tours_congress():
    src_path = 'tours_salle.jpg'
    if not os.path.exists(src_path):
        print(f"Error: {src_path} not found")
        return
        
    raw = Image.open(src_path)
    orig_w, orig_h = raw.size
    
    # Crop to 16:9
    crop_h = int(orig_w / (16 / 9))
    y_start = (orig_h - crop_h) // 2
    cropped = raw.crop((0, y_start, orig_w, y_start + crop_h))
    resized = cropped.resize((W, H), Image.Resampling.LANCZOS)
    
    # Convert grayscale to rich historical warm sepia tint
    gray = resized.convert('L')
    sepia = ImageOps.colorize(gray, black=(20, 16, 12), white=(245, 226, 198), mid=(148, 118, 86))
    
    enh_contrast = ImageEnhance.Contrast(sepia)
    graded = enh_contrast.enhance(1.12)
    
    # Soft vignette
    from PIL import ImageDraw
    vignette = Image.new('L', (W, H), 0)
    v_draw = ImageDraw.Draw(vignette)
    cx, cy = W / 2, H / 2
    max_d = math.hypot(cx, cy)
    for r in range(0, int(max_d), 20):
        alpha = int(255 * (1 - (r / max_d) ** 2.0))
        v_draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=max(0, min(255, alpha)), width=22)
    vignette = vignette.filter(ImageFilter.GaussianBlur(60))
    dark_overlay = Image.new('RGB', (W, H), (16, 12, 10))
    final = Image.composite(graded, dark_overlay, vignette)
    final = Image.blend(graded, final, 0.45)
    
    final.save('act4_3_tours_congress.jpg', quality=95)
    print("Successfully built act4_3_tours_congress.jpg (1920x1080)")

if __name__ == '__main__':
    build_versailles()
    build_tours_congress()
