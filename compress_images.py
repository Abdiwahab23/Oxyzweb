import os
import glob
from PIL import Image

def optimize_image(img_path):
    try:
        size_mb = os.path.getsize(img_path) / 1024 / 1024
        if size_mb < 1.0: # Skip if less than 1MB
            return None
        
        # Don't try to process ARW or weird files
        if not img_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            return None

        with Image.open(img_path) as img:
            # Convert to RGB if it's RGBA and we want to save as JPEG/WebP safely, 
            # but WebP supports alpha. Let's just keep as is for WebP.
            if img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGBA')

            # Resize if too large
            max_dim = 1600
            if img.width > max_dim or img.height > max_dim:
                img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
            
            # Save as webp
            new_path = os.path.splitext(img_path)[0] + '.webp'
            img.save(new_path, 'WEBP', quality=80, method=4)
            
            new_size_mb = os.path.getsize(new_path) / 1024 / 1024
            print(f"Compressed {img_path}: {size_mb:.2f}MB -> {new_size_mb:.2f}MB")
            
            # Delete original
            os.remove(img_path)
            
            return new_path
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return None

# Find large images
all_images = glob.glob('Training/*.*') + glob.glob('StemCell/*.*') + glob.glob('Products/*.*')
replacements = {}

for img_path in all_images:
    new_path = optimize_image(img_path)
    if new_path:
        old_name = os.path.basename(img_path)
        new_name = os.path.basename(new_path)
        
        # We need to replace spaces with %20 for HTML matching too
        old_name_url = old_name.replace(' ', '%20')
        new_name_url = new_name.replace(' ', '%20')
        
        replacements[old_name] = new_name
        replacements[old_name_url] = new_name_url

# Update HTML files
html_files = glob.glob('*.html') + ['js/script.js']
for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated references in {f}")
    except Exception as e:
        print(f"Error updating {f}: {e}")

print("Done optimizing images!")
