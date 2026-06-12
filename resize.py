import os
import glob
from PIL import Image

def optimize_images(directory, max_size_kb=500, max_width=1920):
    # Find all images
    extensions = ('*.jpg', '*.jpeg', '*.png')
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(directory, '**', ext), recursive=True))
    
    total_saved = 0
    
    for f in files:
        try:
            size_kb = os.path.getsize(f) / 1024
            if size_kb > max_size_kb:
                print(f"Processing: {f} ({size_kb:.1f} KB)")
                img = Image.open(f)
                
                # Resize if wider than max_width
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                    print(f"  Resized to {max_width}x{new_height}")
                
                # Overwrite the original file with optimized settings
                if f.lower().endswith('.png'):
                    img.save(f, optimize=True)
                else:
                    img.save(f, quality=80, optimize=True)
                
                new_size_kb = os.path.getsize(f) / 1024
                saved = size_kb - new_size_kb
                total_saved += saved
                print(f"  New size: {new_size_kb:.1f} KB (Saved {saved:.1f} KB)")
        except Exception as e:
            print(f"Error processing {f}: {e}")
            
    print(f"Done. Total space saved: {total_saved / 1024:.2f} MB")

if __name__ == '__main__':
    optimize_images('assets/images')
