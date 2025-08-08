#!/usr/bin/env python3
"""
SGCX YouTube Assets Capture Script
Captures YouTube profile picture and banner from HTML at exact sizes
"""

import os
import time
from pathlib import Path

def setup_output_directory():
    """Create output directory for YouTube assets"""
    output_dir = Path("youtube_assets")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir

def check_playwright():
    """Check if playwright is installed and install if needed"""
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        print("📦 Installing playwright...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        print("✅ Playwright installed!")
        from playwright.sync_api import sync_playwright
        return sync_playwright

def capture_youtube_assets():
    """Capture YouTube profile picture and banner"""
    
    output_dir = setup_output_directory()
    sync_playwright = check_playwright()
    
    # HTML file path - adjust this to your actual file location
    html_file = Path("youtube_assets_capture.html").absolute()
    
    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        print("Please save the YouTube HTML content as 'youtube_assets_capture.html' first")
        return
    
    print("🎨 SGCX YouTube Assets Capture Starting...")
    print("=" * 50)
    
    with sync_playwright() as p:
        # Launch browser with high DPI for quality
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--force-device-scale-factor=2',  # Higher DPI
                '--disable-web-security',         # Allow local file access
                '--disable-features=VizDisplayCompositor'  # Better rendering
            ]
        )
        
        # Large viewport to contain the banner
        page = browser.new_page(viewport={"width": 3000, "height": 2000})
        
        # Load the HTML file
        page.goto(f"file://{html_file}")
        
        # Wait for page to load and fonts to render
        time.sleep(3)
        
        # Force layout recalculation to ensure flexbox is properly rendered
        page.evaluate("""
            // Force a layout recalculation
            document.body.offsetHeight;
            
            // Ensure all elements are properly rendered
            const banner = document.getElementById('youtube-banner-capture');
            if (banner) {
                banner.style.display = 'flex';
                banner.style.alignItems = 'center';
                banner.style.justifyContent = 'center';
            }
            
            // Force another layout pass
            window.getComputedStyle(document.body).height;
        """)
        
        # Wait for layout to settle
        time.sleep(2)
        
        # Capture profile picture
        print(f"\n📸 Capturing YouTube Profile Picture...")
        try:
            profile_locator = page.locator("#youtube-profile-capture")
            profile_locator.wait_for(state="visible", timeout=10000)
            
            # Get bounding box
            profile_box = profile_locator.bounding_box()
            if profile_box:
                print(f"   Profile box: {profile_box['width']:.0f}x{profile_box['height']:.0f}")
                
                # Capture at exact size
                profile_path = output_dir / "sgcx_youtube_profile.png"
                page.screenshot(
                    path=str(profile_path),
                    clip={
                        "x": profile_box["x"],
                        "y": profile_box["y"],
                        "width": profile_box["width"],
                        "height": profile_box["height"]
                    },
                    type="png"
                )
                
                if profile_path.exists():
                    size = profile_path.stat().st_size
                    print(f"✅ Profile saved: {profile_path} ({size:,} bytes)")
                else:
                    print(f"❌ Failed to save profile picture")
                    
        except Exception as e:
            print(f"❌ Error capturing profile: {e}")
        
        # Capture banner
        print(f"\n📸 Capturing YouTube Banner...")
        try:
            banner_locator = page.locator("#youtube-banner-capture")
            banner_locator.wait_for(state="visible", timeout=10000)
            
            # Scroll the banner into view to ensure proper rendering
            banner_locator.scroll_into_view_if_needed()
            time.sleep(1)
            
            # Debug: Check the actual rendered layout
            banner_info = page.evaluate("""
                (function() {
                    const banner = document.getElementById('youtube-banner-capture');
                    const content = banner.querySelector('.banner-content');
                    const logo = banner.querySelector('.banner-logo');
                    const text = banner.querySelector('.banner-text');
                    
                    function getRectInfo(element) {
                        if (!element) return null;
                        const rect = element.getBoundingClientRect();
                        return {
                            x: rect.x,
                            y: rect.y,
                            width: rect.width,
                            height: rect.height
                        };
                    }
                    
                    return {
                        bannerRect: getRectInfo(banner),
                        contentRect: getRectInfo(content),
                        logoRect: getRectInfo(logo),
                        textRect: getRectInfo(text)
                    };
                })()
            """)
            
            print(f"   Banner rect: {banner_info['bannerRect']}")
            print(f"   Content rect: {banner_info['contentRect']}")
            print(f"   Logo rect: {banner_info['logoRect']}")
            print(f"   Text rect: {banner_info['textRect']}")
            
            # Get bounding box
            banner_box = banner_locator.bounding_box()
            if banner_box:
                print(f"   Playwright box: {banner_box['width']:.0f}x{banner_box['height']:.0f}")
                
                # Capture at full size
                banner_path = output_dir / "sgcx_youtube_banner.png"
                page.screenshot(
                    path=str(banner_path),
                    clip={
                        "x": banner_box["x"],
                        "y": banner_box["y"],
                        "width": banner_box["width"],
                        "height": banner_box["height"]
                    },
                    type="png",
                    full_page=False
                )
                
                if banner_path.exists():
                    size = banner_path.stat().st_size
                    print(f"✅ Banner saved: {banner_path} ({size:,} bytes)")
                else:
                    print(f"❌ Failed to save banner")
                    
        except Exception as e:
            print(f"❌ Error capturing banner: {e}")
        
        browser.close()
    
    print(f"\n🎉 YouTube assets capture complete!")
    print(f"📁 Files saved to: {output_dir}")
    
    # Check file sizes and provide upload guidance
    profile_path = output_dir / "sgcx_youtube_profile.png"
    banner_path = output_dir / "sgcx_youtube_banner.png"
    
    print(f"\n📋 Upload Guide:")
    
    if profile_path.exists():
        size_mb = profile_path.stat().st_size / (1024 * 1024)
        print(f"   Profile: {profile_path.name} ({size_mb:.1f}MB)")
        if size_mb > 4:
            print(f"   ⚠️  Profile too large! YouTube limit is 4MB")
        else:
            print(f"   ✅ Profile size OK for YouTube")
    
    if banner_path.exists():
        size_mb = banner_path.stat().st_size / (1024 * 1024)
        print(f"   Banner: {banner_path.name} ({size_mb:.1f}MB)")
        if size_mb > 6:
            print(f"   ⚠️  Banner too large! YouTube limit is 6MB")
        else:
            print(f"   ✅ Banner size OK for YouTube")

def debug_elements():
    """Debug function to check element visibility"""
    
    html_file = Path("youtube_assets_capture.html").absolute()
    if not html_file.exists():
        print(f"❌ HTML file not found: {html_file}")
        return
    
    sync_playwright = check_playwright()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible for debugging
        page = browser.new_page(viewport={"width": 3000, "height": 2000})
        page.goto(f"file://{html_file}")
        time.sleep(2)
        
        print("🔍 Debugging YouTube elements:")
        print("=" * 40)
        
        # Check profile element
        try:
            profile_locator = page.locator("#youtube-profile-capture")
            profile_count = profile_locator.count()
            print(f"\nProfile element (#youtube-profile-capture):")
            print(f"  Count: {profile_count}")
            
            if profile_count > 0:
                profile_box = profile_locator.bounding_box()
                if profile_box:
                    print(f"  Box: {profile_box['width']:.0f}x{profile_box['height']:.0f}")
                    print(f"  Position: ({profile_box['x']:.0f}, {profile_box['y']:.0f})")
                    print(f"  Visible: {profile_locator.is_visible()}")
        except Exception as e:
            print(f"  ERROR: {e}")
        
        # Check banner element
        try:
            banner_locator = page.locator("#youtube-banner-capture")
            banner_count = banner_locator.count()
            print(f"\nBanner element (#youtube-banner-capture):")
            print(f"  Count: {banner_count}")
            
            if banner_count > 0:
                banner_box = banner_locator.bounding_box()
                if banner_box:
                    print(f"  Box: {banner_box['width']:.0f}x{banner_box['height']:.0f}")
                    print(f"  Position: ({banner_box['x']:.0f}, {banner_box['y']:.0f})")
                    print(f"  Visible: {banner_locator.is_visible()}")
        except Exception as e:
            print(f"  ERROR: {e}")
        
        input("\nPress Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    import sys
    
    print("🎨 SGCX YouTube Assets Capture")
    print("=" * 35)
    
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        print("🔍 Running in debug mode...")
        debug_elements()
    else:
        print("🚀 Running capture...")
        capture_youtube_assets()
        
        print("\n🚀 Next steps:")
        print("1. Check the generated PNG files in youtube_assets/")
        print("2. Upload to YouTube:")
        print("   - Profile: sgcx_youtube_profile.png")
        print("   - Banner: sgcx_youtube_banner.png")
        print("3. Enjoy your professional YouTube channel!")
        print("\n💡 Tip: Run 'python script.py debug' to debug element detection")