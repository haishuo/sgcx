#!/usr/bin/env python3
"""
SGCX Logo Asset Generator - SVG Paths Instead of Text
Using proper SVG paths for the X, which should be much more reliable
"""

import os
from pathlib import Path

def create_logo_assets():
    """Generate SGCX logo SVG files using SVG paths for the X"""
    
    # Use 'images' directory
    base_dir = Path("landing/static/images")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Main logo SVG - Using SVG paths for reliable X shape
    main_logo_svg = '''<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
  <!-- Large outlined X behind using SVG paths (stretched horizontally) -->
  <g transform="translate(100, 40) scale(2.5, 1.4)" opacity="0.25">
    <path d="M -20 -15 L 20 15 M 20 -15 L -20 15" 
          stroke="#333" 
          stroke-width="3" 
          stroke-linecap="round" 
          fill="none"/>
  </g>
  
  <!-- SGC letters in front -->
  <text x="100" y="40" 
        font-family="Georgia, serif" 
        font-size="32" 
        font-weight="bold"
        text-anchor="middle" 
        dominant-baseline="middle"
        fill="#333"
        letter-spacing="3px">SGC</text>
</svg>'''
    
    # Navigation logo SVG
    nav_logo_svg = '''<svg width="120" height="48" viewBox="0 0 120 48" xmlns="http://www.w3.org/2000/svg">
  <!-- Large outlined X behind using SVG paths -->
  <g transform="translate(60, 24) scale(1.5, 0.8)" opacity="0.25">
    <path d="M -20 -15 L 20 15 M 20 -15 L -20 15" 
          stroke="#333" 
          stroke-width="3" 
          stroke-linecap="round" 
          fill="none"/>
  </g>
  
  <!-- SGC letters in front -->
  <text x="60" y="24" 
        font-family="Georgia, serif" 
        font-size="20" 
        font-weight="bold"
        text-anchor="middle" 
        dominant-baseline="middle"
        fill="#333"
        letter-spacing="2px">SGC</text>
</svg>'''
    
    # Small logo SVG
    small_logo_svg = '''<svg width="64" height="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <!-- Large outlined X behind using SVG paths -->
  <g transform="translate(32, 32) scale(1.2, 0.8)" opacity="0.3">
    <path d="M -15 -10 L 15 10 M 15 -10 L -15 10" 
          stroke="#333" 
          stroke-width="2.5" 
          stroke-linecap="round" 
          fill="none"/>
  </g>
  
  <!-- SGC letters in front -->
  <text x="32" y="32" 
        font-family="Georgia, serif" 
        font-size="16" 
        font-weight="bold"
        text-anchor="middle" 
        dominant-baseline="middle"
        fill="#333"
        letter-spacing="1px">SGC</text>
</svg>'''

    # White version for dark backgrounds
    white_logo_svg = '''<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
  <!-- Large outlined X behind using SVG paths -->
  <g transform="translate(100, 40) scale(2.5, 1.4)" opacity="0.4">
    <path d="M -20 -15 L 20 15 M 20 -15 L -20 15" 
          stroke="white" 
          stroke-width="3" 
          stroke-linecap="round" 
          fill="none"/>
  </g>
  
  <!-- SGC letters in front -->
  <text x="100" y="40" 
        font-family="Georgia, serif" 
        font-size="32" 
        font-weight="bold"
        text-anchor="middle" 
        dominant-baseline="middle"
        fill="white"
        letter-spacing="3px">SGC</text>
</svg>'''
    
    # White nav version
    white_nav_logo_svg = '''<svg width="120" height="48" viewBox="0 0 120 48" xmlns="http://www.w3.org/2000/svg">
  <!-- Large outlined X behind using SVG paths -->
  <g transform="translate(60, 24) scale(1.5, 0.8)" opacity="0.4">
    <path d="M -20 -15 L 20 15 M 20 -15 L -20 15" 
          stroke="white" 
          stroke-width="3" 
          stroke-linecap="round" 
          fill="none"/>
  </g>
  
  <!-- SGC letters in front -->
  <text x="60" y="24" 
        font-family="Georgia, serif" 
        font-size="20" 
        font-weight="bold"
        text-anchor="middle" 
        dominant-baseline="middle"
        fill="white"
        letter-spacing="2px">SGC</text>
</svg>'''
    
    # Write all the files
    files_to_create = {
        'sgcx-logo-main.svg': main_logo_svg,
        'sgcx-logo-nav.svg': nav_logo_svg,
        'sgcx-logo-small.svg': small_logo_svg,
        'sgcx-logo-white.svg': white_logo_svg,
        'sgcx-logo-nav-white.svg': white_nav_logo_svg,
    }
    
    for filename, content in files_to_create.items():
        file_path = base_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {file_path}")
    
    print(f"\n✅ All logo assets created in {base_dir}/")
    print("\nFiles created:")
    for filename in files_to_create.keys():
        print(f"  - {filename}")
    
    print(f"\n🎯 KEY IMPROVEMENT:")
    print(f"   - Using SVG <path> elements instead of <text> for the X")
    print(f"   - Paths are drawn as two lines: one diagonal, then the other")
    print(f"   - Much more reliable than text transforms!")
    print(f"   - stroke-linecap='round' gives clean line endings")

def create_test_html():
    """Create a test HTML file to verify the logos work"""
    
    test_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SGCX Logo Test</title>
    <style>
        body { font-family: Georgia, serif; margin: 20px; background: #f5f5f5; }
        .test-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .test-card { background: white; padding: 20px; border-radius: 10px; text-align: center; }
        .blue-bg { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        h1 { text-align: center; }
        h3 { margin-bottom: 15px; }
    </style>
</head>
<body>
    <h1>SGCX Logo Test - SVG Paths</h1>
    
    <div class="test-grid">
        <div class="test-card">
            <h3>Main Logo (Dark)</h3>
            <img src="landing/static/images/sgcx-logo-main.svg" alt="SGCX Main" style="height: 80px;">
        </div>
        
        <div class="test-card">
            <h3>Nav Logo (Dark)</h3>
            <img src="landing/static/images/sgcx-logo-nav.svg" alt="SGCX Nav" style="height: 48px;">
        </div>
        
        <div class="test-card blue-bg">
            <h3>White Version</h3>
            <img src="landing/static/images/sgcx-logo-nav-white.svg" alt="SGCX White" style="height: 48px;">
        </div>
        
        <div class="test-card">
            <h3>Small/Favicon</h3>
            <img src="landing/static/images/sgcx-logo-small.svg" alt="SGCX Small" style="height: 32px;">
        </div>
    </div>
    
    <p style="text-align: center; margin-top: 30px;">
        <strong>If you can see clear X shapes behind SGC, the path approach worked!</strong>
    </p>
</body>
</html>'''
    
    test_file = Path("logo_test.html")
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_html)
    print(f"\n📁 Created {test_file} - open this in your browser to test the logos!")

if __name__ == "__main__":
    print("🎨 SGCX Logo Asset Generator - SVG Paths Approach")
    print("=" * 55)
    
    create_logo_assets()
    create_test_html()
    
    print("\n🚀 Next steps:")
    print("1. Open logo_test.html in your browser to verify the X is visible")
    print("2. If it looks good, test with: python manage.py runserver")
    print("3. The X should be much more reliable now!")