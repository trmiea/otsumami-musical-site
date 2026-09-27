import re
import os

NAV_CSS = """
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(10, 10, 10, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        nav .nav-container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 90px;
        }
        nav .logo {
            display: flex;
            align-items: center;
            font-weight: 700;
            color: #c29a5b;
            font-size: 1.4rem;
            letter-spacing: 0.05em;
            text-decoration: none;
        }
        nav .logo img {
            height: 55px;
            margin-right: 18px;
            filter: drop-shadow(0 0 5px rgba(194, 154, 91, 0.4));
        }
        nav .nav-links {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
        }
        nav .nav-links li {
            margin-left: 25px;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
            display: flex;
            align-items: center;
        }
        nav .nav-links li a {
            color: #ccc;
            transition: color 0.3s;
            text-decoration: none;
        }
        nav .nav-links li a:hover {
            color: #fff;
        }
        
        /* Hamburger Button */
        .hamburger {
            display: none;
            flex-direction: column;
            justify-content: space-between;
            width: 24px;
            height: 18px;
            cursor: pointer;
            z-index: 1001;
        }
        .hamburger span {
            display: block;
            height: 2px;
            width: 100%;
            background-color: #fff;
            border-radius: 2px;
            transition: all 0.3s ease;
        }
        
        /* Mobile Menu */
        .mobile-menu {
            display: none;
            background: #0a0a0a;
            border-top: 1px solid rgba(255,255,255,0.05);
            position: absolute;
            top: 90px;
            left: 0;
            width: 100%;
        }
        .mobile-menu.active {
            display: block;
        }
        .mobile-menu ul {
            list-style: none;
            margin: 0;
            padding: 10px 0;
        }
        .mobile-menu li {
            padding: 15px 20px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .mobile-menu li:last-child {
            border-bottom: none;
        }
        .mobile-menu li a {
            color: #ccc;
            text-decoration: none;
            font-size: 1rem;
            display: block;
        }
        
        @media (max-width: 768px) {
            nav .nav-links {
                display: none;
            }
            .hamburger {
                display: flex;
            }
        }
"""

NAV_HTML = """    <nav>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="res/input/logo.png" alt="Otsumami Logo">
                <span>Otsumami Musical</span>
            </a>
            
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="vol8.html">Next</a></li>
                <li><a href="archive.html">Archive</a></li>
                <li><a href="vol9.html" style="color: #c29a5b; font-weight: bold;">🔒 Practice</a></li>
            </ul>

            <div class="hamburger" id="hamburger-btn" onclick="document.getElementById('mobile-menu').classList.toggle('active')">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div id="mobile-menu" class="mobile-menu">
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="vol8.html">Next</a></li>
                <li><a href="archive.html">Archive</a></li>
                <li><a href="vol9.html" style="color: #c29a5b; font-weight: bold;">🔒 Practice</a></li>
            </ul>
        </div>
    </nav>"""

for file in ["index.html", "archive.html", "vol8.html"]:
    with open(file, "r") as f:
        content = f.read()
    
    # Replace nav CSS
    # For index.html, archive.html, vol8.html, they all have a nav {} block.
    # We will replace from "nav {" up to "header {" (or similar).
    content = re.sub(r'nav\s*\{.*?(?=header\s*\{|\.hero|@media)', NAV_CSS, content, flags=re.DOTALL)
    
    # Replace nav HTML
    content = re.sub(r'<nav>.*?</nav>', NAV_HTML, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(content)
        
print("Patched basic files.")
