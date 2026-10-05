from PIL import Image, ImageEnhance, ImageDraw, ImageFilter

def build_flawless_paris_room():
    W, H = 1920, 1080
    caillebotte = Image.open('caillebotte_paris_snow.jpg').convert('RGB')
    
    # 1. 16:9 crop centered on Paris mansard roofs, dormers and chimneys
    w, h = caillebotte.size
    target_h = int(w * H / W)
    top = int((h - target_h) * 0.42)
    canvas = caillebotte.crop((0, top, w, top + target_h)).resize((W, H), Image.Resampling.LANCZOS)
    
    # 2. Rich winter twilight grade: Deep charcoal-blue shadows, warm ochre highlights
    canvas = ImageEnhance.Brightness(canvas).enhance(0.92)
    canvas = ImageEnhance.Contrast(canvas).enhance(1.12)
    canvas = ImageEnhance.Color(canvas).enhance(1.08)
    
    # 3. Soft golden lamplight emanating from the garret windows (organic radial Gaussian glow)
    lamp_glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(lamp_glow)
    
    # Garret dormer window lights
    # Dormer window 1 (lower right mansard)
    gdraw.ellipse([1180, 720, 1320, 860], fill=(255, 190, 80, 120))
    # Dormer window 2 (right roof)
    gdraw.ellipse([1320, 780, 1440, 900], fill=(255, 180, 70, 110))
    # Distant left garret window
    gdraw.ellipse([380, 440, 480, 540], fill=(255, 200, 90, 90))
    # Distant center building window
    gdraw.ellipse([880, 260, 960, 340], fill=(255, 210, 100, 80))
    
    # Heavy Gaussian blur to create atmospheric light diffusion through winter air
    lamp_glow = lamp_glow.filter(ImageFilter.GaussianBlur(45))
    canvas = Image.alpha_composite(canvas.convert('RGBA'), lamp_glow).convert('RGB')
    
    # 4. Flawless smooth radial vignette (ZERO banding, pure Gaussian blur)
    vignette = Image.new('L', (W, H), 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse([-150, -150, W + 150, H + 150], fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(140))
    
    # Dark border base
    dark_base = Image.new('RGB', (W, H), (12, 14, 18))
    canvas = Image.composite(canvas, dark_base, vignette)
    
    canvas.save('act4_2_paris_room.jpg', quality=95)
    print("Flawless act4_2_paris_room.jpg saved successfully!")

if __name__ == '__main__':
    build_flawless_paris_room()
