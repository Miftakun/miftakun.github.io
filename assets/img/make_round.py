import sys
from PIL import Image, ImageDraw

def make_circle(img_path, out_path):
    try:
        img = Image.open(img_path).convert("RGBA")
        
        # Crop to square first
        min_dim = min(img.size)
        left = (img.size[0] - min_dim) / 2
        top = (img.size[1] - min_dim) / 2
        right = (img.size[0] + min_dim) / 2
        bottom = (img.size[1] + min_dim) / 2
        
        img = img.crop((left, top, right, bottom))
        
        # Create a blank mask image
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
        
        # Apply mask
        result = img.copy()
        result.putalpha(mask)
        
        # Save output
        result.save(out_path)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

make_circle('passport-new.png', 'passport-round.png')
