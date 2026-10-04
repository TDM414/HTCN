# -*- coding: utf-8 -*-
"""
Generate the extended historical story plates for the 30-Year Epic Odyssey (1911-1941)
Strictly adhering to ink-wash watercolor sepia aesthetic on aged parchment.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def make_sepia_parchment(width=1920, height=1080, base_color=(24, 20, 16)):
    """Create aged vintage paper canvas with natural warmth and vignette."""
    im = Image.new('RGB', (width, height), base_color)
    draw = ImageDraw.Draw(im)
    
    # Warm sepia gradients
    for y in range(0, height, 4):
        t = y / height
        r = int(24 + 18 * math.sin(t * math.pi))
        g = int(20 + 14 * math.sin(t * math.pi))
        b = int(16 + 10 * math.sin(t * math.pi))
        draw.line([(0, y), (width, y)], fill=(r, g, b), width=4)
        
    return im

def apply_ink_vignette_and_grain(im):
    """Apply historical ink wash vignette, texture, and subtle film grain."""
    w, h = im.size
    
    # Radial vignette mask
    vignette = Image.new('L', (w, h), 0)
    v_draw = ImageDraw.Draw(vignette)
    cx, cy = w / 2, h / 2
    max_dist = math.hypot(cx, cy)
    
    for r in range(0, int(max_dist), 15):
        alpha = int(255 * (1 - (r / max_dist) ** 1.8))
        alpha = max(0, min(255, alpha))
        bbox = [cx - r, cy - r, cx + r, cy + r]
        v_draw.ellipse(bbox, outline=alpha, width=16)
        
    vignette = vignette.filter(ImageFilter.GaussianBlur(35))
    
    # Blend vignette to darken edges
    dark_bg = Image.new('RGB', (w, h), (10, 8, 6))
    result = Image.composite(im, dark_bg, vignette)
    
    # Sepia color grade
    enhancer = ImageEnhance.Color(result)
    result = enhancer.enhance(0.75)
    
    return result

def generate_boston_london_plate():
    """Hồi 3: Lao động bến cảng Châu Phi, Boston & Mùa đông tuyết trắng London (1912-1917)"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (18, 16, 14))
    draw = ImageDraw.Draw(canvas)
    
    # Distant Victorian London & Boston skyline in fog
    for x in range(0, w, 60):
        b_h = 320 + int(80 * math.sin(x * 0.02)) + int(40 * math.cos(x * 0.05))
        draw.rectangle([x, h - b_h - 220, x + 50, h - 220], fill=(28, 24, 20))
        # Spire or chimneys
        if x % 180 == 0:
            draw.polygon([(x + 25, h - b_h - 320), (x + 10, h - b_h - 220), (x + 40, h - b_h - 220)], fill=(22, 18, 16))
            
    # Snow ground
    draw.polygon([(0, h - 260), (w, h - 240), (w, h), (0, h)], fill=(42, 38, 34))
    
    # Vintage London gas lamppost with glowing warm lantern
    post_x = 420
    draw.line([(post_x, h - 240), (post_x, h - 680)], fill=(15, 12, 10), width=10)
    draw.line([(post_x - 35, h - 680), (post_x + 35, h - 680)], fill=(20, 16, 12), width=6)
    draw.polygon([(post_x - 25, h - 680), (post_x + 25, h - 680), (post_x + 15, h - 740), (post_x - 15, h - 740)], fill=(30, 24, 18))
    
    # Warm amber glow from streetlamp
    glow_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_img)
    g_draw.ellipse([post_x - 120, h - 770, post_x + 120, h - 630], fill=(245, 158, 11, 80))
    g_draw.ellipse([post_x - 60, h - 740, post_x + 60, h - 660], fill=(253, 224, 71, 150))
    canvas.paste(Image.alpha_composite(canvas.convert('RGBA'), glow_img).convert('RGB'))
    
    # Blend authentic portrait of young Bác in wool coat looking into the distance
    if os.path.exists('reference_nguyen_tat_thanh_1920.jpg'):
        ref = Image.open('reference_nguyen_tat_thanh_1920.jpg').convert('RGBA')
        ref = ref.resize((560, 680), Image.Resampling.LANCZOS)
        # Soft mask
        mask = Image.new('L', ref.size, 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse([40, 20, 520, 660], fill=230)
        mask = mask.filter(ImageFilter.GaussianBlur(25))
        canvas.paste(ref, (1080, 260), mask)
        
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('world_1_boston_london.jpg', quality=95)
    print("Created world_1_boston_london.jpg")

def generate_versailles_plate():
    """Hồi 4: Hội nghị Versailles 1919 - Bản Yêu sách 8 điểm ký tên Nguyễn Ái Quốc"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (22, 18, 15))
    draw = ImageDraw.Draw(canvas)
    
    # Grand classical arches of Palace of Versailles in ink lines
    for arc_x in [300, 750, 1200, 1650]:
        draw.arc([arc_x - 180, 120, arc_x + 180, 480], start=180, end=360, fill=(35, 28, 22), width=5)
        draw.line([(arc_x - 180, 300), (arc_x - 180, 850)], fill=(32, 26, 20), width=6)
        draw.line([(arc_x + 180, 300), (arc_x + 180, 850)], fill=(32, 26, 20), width=6)
        
    # Large vintage parchment manifesto document in the foreground
    doc_x, doc_y = 580, 240
    doc_w, doc_h = 760, 640
    draw.rectangle([doc_x, doc_y, doc_x + doc_w, doc_y + doc_h], fill=(210, 190, 155), outline=(100, 75, 45), width=4)
    
    # Header of the historic document
    d_draw = ImageDraw.Draw(canvas)
    d_draw.rectangle([doc_x + 30, doc_y + 30, doc_x + doc_w - 30, doc_y + 80], fill=(185, 165, 130))
    d_draw.line([(doc_x + 40, doc_y + 110), (doc_x + doc_w - 40, doc_y + 110)], fill=(80, 60, 35), width=2)
    
    # Simulated text lines
    for i in range(12):
        ly = doc_y + 140 + i * 32
        d_draw.line([(doc_x + 50, ly), (doc_x + doc_w - 50, ly)], fill=(75, 55, 35), width=3)
        
    # Red wax seal and signature "NGUYỄN ÁI QUỐC"
    seal_cx, seal_cy = doc_x + doc_w - 150, doc_y + doc_h - 100
    d_draw.ellipse([seal_cx - 50, seal_cy - 50, seal_cx + 50, seal_cy + 50], fill=(160, 30, 25), outline=(110, 20, 15), width=3)
    d_draw.ellipse([seal_cx - 40, seal_cy - 40, seal_cx + 40, seal_cy + 40], outline=(200, 70, 60), width=2)
    
    # Blend authentic portrait of Nguyễn Ái Quốc 1921
    if os.path.exists('reference_nguyen_ai_quoc_1921.jpg'):
        ref = Image.open('reference_nguyen_ai_quoc_1921.jpg').convert('RGBA')
        ref = ref.resize((520, 650), Image.Resampling.LANCZOS)
        mask = Image.new('L', ref.size, 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse([40, 20, 480, 630], fill=220)
        mask = mask.filter(ImageFilter.GaussianBlur(30))
        canvas.paste(ref, (120, 280), mask)
        
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('act4_1_versailles_1919.jpg', quality=95)
    print("Created act4_1_versailles_1919.jpg")

def generate_paris_room_plate():
    """Hồi 4: Căn gác trọ ngõ Compoint mùa đông Paris 1920 - Viên gạch hồng sưởi ấm & báo L'Humanité"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (18, 14, 12))
    draw = ImageDraw.Draw(canvas)
    
    # Attic sloping wooden roof beam
    draw.polygon([(0, 0), (w, 180), (w, 0)], fill=(12, 10, 8))
    draw.polygon([(0, 180), (w, 240), (w, 180), (0, 120)], fill=(28, 22, 18))
    
    # Small frosty window looking out into cold Paris night
    win_x, win_y = 1250, 140
    win_w, win_h = 380, 440
    draw.rectangle([win_x, win_y, win_x + win_w, win_y + win_h], fill=(15, 24, 38), outline=(50, 40, 30), width=8)
    draw.line([(win_x + win_w / 2, win_y), (win_x + win_w / 2, win_y + win_h)], fill=(50, 40, 30), width=6)
    draw.line([(win_x, win_y + win_h / 2), (win_x + win_w, win_y + win_h / 2)], fill=(50, 40, 30), width=6)
    
    # Heavy wooden writing desk across the midground
    table_y = 520
    draw.polygon([(0, table_y + 120), (w, table_y + 60), (w, h), (0, h)], fill=(32, 24, 18))
    draw.line([(0, table_y + 120), (w, table_y + 60)], fill=(70, 52, 38), width=5)
    
    # Newspaper L'Humanité spread open on the desk
    np_x, np_y = 650, 580
    np_w, np_h = 620, 380
    draw.polygon([(np_x, np_y), (np_x + np_w, np_y - 20), (np_x + np_w + 40, np_y + np_h), (np_x - 30, np_y + np_h + 30)], fill=(205, 185, 150), outline=(80, 60, 40), width=3)
    
    # Glowing heated brick wrapped in newspapers (viên gạch hồng sưởi ấm)
    brick_x, brick_y = 380, 660
    draw.rectangle([brick_x, brick_y, brick_x + 180, brick_y + 90], fill=(160, 50, 30), outline=(100, 30, 20), width=3)
    
    # Warm amber glow around brick
    b_glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(b_glow)
    bg_draw.ellipse([brick_x - 60, brick_y - 40, brick_x + 240, brick_y + 130], fill=(220, 38, 38, 65))
    canvas.paste(Image.alpha_composite(canvas.convert('RGBA'), b_glow).convert('RGB'))
    
    # Kerosene desk lamp on the corner of the table
    lamp_x, lamp_y = 1420, 560
    draw.rectangle([lamp_x - 25, lamp_y + 80, lamp_x + 25, lamp_y + 160], fill=(60, 45, 30), outline=(90, 70, 45), width=3)
    draw.ellipse([lamp_x - 35, lamp_y - 40, lamp_x + 35, lamp_y + 80], fill=(245, 158, 11, 70), outline=(180, 130, 60), width=3)
    
    # Lamp flame
    l_glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    lg_draw = ImageDraw.Draw(l_glow)
    lg_draw.ellipse([lamp_x - 140, lamp_y - 120, lamp_x + 140, lamp_y + 160], fill=(245, 158, 11, 75))
    lg_draw.ellipse([lamp_x - 60, lamp_y - 50, lamp_x + 60, lamp_y + 70], fill=(253, 224, 71, 140))
    canvas.paste(Image.alpha_composite(canvas.convert('RGBA'), l_glow).convert('RGB'))
    
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('act4_2_paris_room.jpg', quality=95)
    print("Created act4_2_paris_room.jpg")

def generate_tours_congress_plate():
    """Hồi 4: Đại hội Tours 12/1920 & Báo Le Paria (Người Cùng Khổ) 1922"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (20, 16, 14))
    draw = ImageDraw.Draw(canvas)
    
    # Grand hall with banner: 18e CONGRÈS NATIONAL - TOURS 1920
    draw.rectangle([350, 100, 1570, 200], fill=(140, 30, 25), outline=(90, 20, 15), width=4)
    draw.rectangle([360, 110, 1560, 190], outline=(220, 180, 100), width=2)
    
    # Crowd silhouettes with hands raised voting
    for x in range(100, w - 100, 80):
        c_h = 350 + int(60 * math.sin(x * 0.04))
        draw.ellipse([x - 20, h - c_h - 40, x + 20, h - c_h], fill=(22, 18, 16))
        draw.polygon([(x - 35, h - c_h + 10), (x + 35, h - c_h + 10), (x + 45, h), (x - 45, h)], fill=(18, 14, 12))
        if x % 160 == 0:
            # Raised voting arm
            draw.line([(x, h - c_h + 20), (x + 30, h - c_h - 90)], fill=(22, 18, 16), width=10)
            
    # Front page of Le Paria newspaper on right
    p_x, p_y = 1150, 420
    draw.rectangle([p_x, p_y, p_x + 520, p_y + 540], fill=(215, 195, 160), outline=(90, 70, 45), width=4)
    draw.rectangle([p_x + 20, p_y + 20, p_x + 500, p_y + 80], fill=(180, 40, 30))
    
    # Blend authentic portrait of Nguyễn Ái Quốc 1921 at rostrum
    if os.path.exists('reference_nguyen_ai_quoc_1921.jpg'):
        ref = Image.open('reference_nguyen_ai_quoc_1921.jpg').convert('RGBA')
        ref = ref.resize((540, 680), Image.Resampling.LANCZOS)
        mask = Image.new('L', ref.size, 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse([30, 20, 510, 660], fill=230)
        mask = mask.filter(ImageFilter.GaussianBlur(30))
        canvas.paste(ref, (220, 260), mask)
        
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('act4_3_tours_congress.jpg', quality=95)
    print("Created act4_3_tours_congress.jpg")

def generate_moscow_plate():
    """Hồi 5: Mát-xcơ-va tuyết trắng 1923 - 1924, Đại học Phương Đông (KUTV)"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (20, 22, 24))
    draw = ImageDraw.Draw(canvas)
    
    # Kremlin onion domes and Red Square architecture in winter mist
    domes = [(450, 380, 70), (700, 320, 90), (950, 360, 75), (1200, 400, 65), (1450, 340, 85)]
    for dx, dy, dr in domes:
        # Tower
        draw.rectangle([dx - dr * 0.7, dy, dx + dr * 0.7, h - 250], fill=(35, 32, 30))
        # Onion dome curve
        draw.ellipse([dx - dr, dy - dr, dx + dr, dy + dr * 0.8], fill=(45, 38, 32), outline=(75, 60, 45), width=3)
        draw.polygon([(dx, dy - dr * 1.5), (dx - dr * 0.4, dy - dr * 0.6), (dx + dr * 0.4, dy - dr * 0.6)], fill=(50, 42, 34))
        # Spire cross
        draw.line([(dx, dy - dr * 1.8), (dx, dy - dr * 1.3)], fill=(85, 70, 50), width=4)
        
    # Snowdrifts ground
    draw.polygon([(0, h - 280), (w, h - 250), (w, h), (0, h)], fill=(48, 46, 44))
    
    # Falling winter snowflakes
    snow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(snow)
    for x in range(0, w, 35):
        for y in range(0, h, 45):
            if (x * 7 + y * 13) % 23 == 0:
                s_draw.ellipse([x, y, x + 4, y + 4], fill=(240, 245, 255, 140))
    canvas.paste(Image.alpha_composite(canvas.convert('RGBA'), snow).convert('RGB'))
    
    # Blend authentic portrait of young Bác
    if os.path.exists('reference_nguyen_ai_quoc_1921.jpg'):
        ref = Image.open('reference_nguyen_ai_quoc_1921.jpg').convert('RGBA')
        ref = ref.resize((500, 630), Image.Resampling.LANCZOS)
        mask = Image.new('L', ref.size, 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse([30, 20, 470, 610], fill=220)
        mask = mask.filter(ImageFilter.GaussianBlur(30))
        canvas.paste(ref, (1120, 280), mask)
        
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('act5_1_moscow_1923.jpg', quality=95)
    print("Created act5_1_moscow_1923.jpg")

def generate_hongkong_table_plate():
    """Hồi 5: Bàn hội nghị bí mật Hương Cảng 03.02.1930 - Hợp nhất thành lập Đảng"""
    w, h = 1920, 1080
    canvas = make_sepia_parchment(w, h, (18, 14, 12))
    draw = ImageDraw.Draw(canvas)
    
    # Modest room wall with wooden shutters
    draw.rectangle([100, 80, 550, 420], fill=(22, 17, 13), outline=(45, 35, 25), width=6)
    for sy in range(120, 400, 30):
        draw.line([(120, sy), (530, sy)], fill=(35, 28, 20), width=3)
        
    # Large polished mahogany conference table in the center
    table_y = 520
    draw.polygon([(150, table_y + 80), (w - 150, table_y + 80), (w - 50, h), (50, h)], fill=(38, 26, 18), outline=(65, 45, 30), width=4)
    
    # Center document: Chánh cương vắn tắt, Sách lược vắn tắt (1930)
    doc_cx, doc_cy = w / 2, table_y + 190
    draw.polygon([(doc_cx - 280, doc_cy - 120), (doc_cx + 280, doc_cy - 120), (doc_cx + 310, doc_cy + 190), (doc_cx - 310, doc_cy + 190)], fill=(215, 195, 160), outline=(90, 70, 45), width=3)
    
    # Kerosene lantern on the table corner
    lamp_x, lamp_y = 380, table_y + 110
    draw.rectangle([lamp_x - 20, lamp_y + 50, lamp_x + 20, lamp_y + 110], fill=(55, 40, 25), outline=(85, 65, 40), width=2)
    draw.ellipse([lamp_x - 30, lamp_y - 30, lamp_x + 30, lamp_y + 50], fill=(245, 158, 11, 75), outline=(160, 120, 50), width=2)
    
    # Warm amber glow
    l_glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    lg_draw = ImageDraw.Draw(l_glow)
    lg_draw.ellipse([lamp_x - 150, lamp_y - 120, lamp_x + 150, lamp_y + 180], fill=(245, 158, 11, 70))
    canvas.paste(Image.alpha_composite(canvas.convert('RGBA'), l_glow).convert('RGB'))
    
    canvas = apply_ink_vignette_and_grain(canvas)
    canvas.save('act5_3_hongkong_unification.jpg', quality=95)
    print("Created act5_3_hongkong_unification.jpg")

if __name__ == '__main__':
    print("Generating extended historical plates for 30-year epic...")
    generate_boston_london_plate()
    generate_versailles_plate()
    generate_paris_room_plate()
    generate_tours_congress_plate()
    generate_moscow_plate()
    generate_hongkong_table_plate()
    print("ALL EXTENDED PLATES SUCCESSFULLY CREATED!")
