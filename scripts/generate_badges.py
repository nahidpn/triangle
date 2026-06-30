"""
Generate badges for README
"""
from PIL import Image, ImageDraw, ImageFont
import os

class BadgeGenerator:
    def __init__(self):
        self.font_size = 14
        self.padding = 10
        
    def create_badge(self, label, value, color, output_path):
        """Create a badge image"""
        # Create image
        width = 200
        height = 30
        img = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(img)
        
        # Draw label background
        draw.rectangle([0, 0, width//2, height], fill=color)
        
        # Draw value background
        draw.rectangle([width//2, 0, width, height], fill=(50, 50, 50))
        
        # Add text
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        except:
            font = ImageFont.load_default()
        
        draw.text((self.padding, height//2 - 5), label, fill='white', font=font)
        draw.text((width//2 + self.padding, height//2 - 5), value, fill='white', font=font)
        
        img.save(output_path)
        return output_path

def generate_all_badges():
    """Generate all project badges"""
    gen = BadgeGenerator()
    
    badges = [
        ('Accuracy', '92%', (46, 204, 113)),
        ('Speed', '<500ms', (52, 152, 219)),
        ('Python', '3.10+', (3, 102, 214)),
        ('PyTorch', '2.0+', (238, 75, 43)),
        ('FastAPI', '0.104+', (0, 170, 0)),
        ('Docker', 'Ready', (2, 150, 219)),
        ('License', 'MIT', (96, 0, 0)),
        ('Status', 'Active', (46, 204, 113)),
    ]
    
    os.makedirs('assets/badges', exist_ok=True)
    
    for label, value, color in badges:
        filename = f"assets/badges/{label.lower()}.png"
        gen.create_badge(label, value, color, filename)
        print(f"✓ Created: {filename}")

if __name__ == "__main__":
    generate_all_badges()
