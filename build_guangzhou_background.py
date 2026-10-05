from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

def build_guangzhou_school():
    W, H = 1920, 1080
    
    # Load authentic photo of the Vietnam Youth Political Training Class site
    img = Image.open('gz_2.jpg').convert('RGB')
    
    # Crop to 16:9 centered on the brick pillar and the historic signboards
    # Original size is 1280x853
    w, h = img.size
    target_h = int(w * H / W)
    if target_h > h:
        target_w = int(h * W / H)
        left = int((w - target_w) * 0.45)
        crop_box = (left, 0, left + target_w, h)
    else:
        top = int((h - target_h) * 0.5)
        crop_box = (0, top, w, top + target_h)
        
    canvas = img.crop(crop_box).resize((W, H), Image.Resampling.LANCZOS)
    
    # Vintage 1925 atmospheric treatment:
    # 1. Warm amber/ochre morning sunlight
    warm_tint = Image.new('RGB', (W, H), (245, 220, 185))
    canvas = Image.blend(canvas, warm_tint, 0.12)
    
    # 2. Rich cinematic contrast
    canvas = ImageEnhance.Contrast(canvas).enhance(1.18)
    canvas = ImageEnhance.Color(canvas).enhance(1.10)
    canvas = ImageEnhance.Brightness(canvas).enhance(0.96)
    
    # 3. Soft atmospheric lighting glow on the historic wooden plaque
    # The plaque is roughly in the center: x=800-1100, y=200-900
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([700, 150, 1200, 950], fill=(255, 230, 160, 45))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    canvas = Image.alpha_composite(canvas.convert('RGBA'), glow).convert('RGB')
    
    # 4. Flawless smooth radial vignette (pure Gaussian blur, zero banding)
    vignette = Image.new('L', (W, H), 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse([-120, -120, W + 120, H + 120], fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(130))
    
    dark_base = Image.new('RGB', (W, H), (16, 12, 10))
    canvas = Image.composite(canvas, dark_base, vignette)
    
    canvas.save('act5_2_guangzhou_school.jpg', quality=95)
    print("act5_2_guangzhou_school.jpg generated successfully!")

if __name__ == '__main__':
    build_guangzhou_school()
