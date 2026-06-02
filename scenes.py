"""
Cinematic Scene Components — rendered via st.components.v1.html()
Each scene is a self-contained HTML document with inline CSS + animations.
This bypasses Streamlit Cloud's markdown sanitizer completely.
"""

def _wrap(body_html: str, extra_css: str = "") -> str:
    """Wrap scene HTML in a full standalone document for iframe rendering."""
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:200px;overflow:hidden;background:transparent;font-family:'Inter',sans-serif}}
.scene{{position:relative;width:100%;height:200px;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,0.09)}}
.scene-text{{position:absolute;left:32px;top:50%;transform:translateY(-50%);z-index:20}}
.eyebrow{{display:flex;align-items:center;gap:7px;font-size:11px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:#38BDF8;margin-bottom:8px}}
.dot{{width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 10px #10B981;animation:dotPulse 2s ease infinite}}
@keyframes dotPulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.4;transform:scale(.8)}}}}
.scene-title{{font-size:28px;font-weight:800;color:white;letter-spacing:-.7px;line-height:1.1;text-shadow:0 4px 16px rgba(0,0,0,.6)}}
.scene-sub{{font-size:12px;color:rgba(255,255,255,.6);margin-top:7px}}
{extra_css}
</style>
</head>
<body>
{body_html}
</body>
</html>"""


# ══════════════════════════════════════════════════════════════════
#  SCENE 1 — OVERVIEW: Rocket through stars
# ══════════════════════════════════════════════════════════════════
SCENE_OVERVIEW_HTML = _wrap("""
<div class="scene" style="background:radial-gradient(ellipse at top right,#1a1f3a 0%,#080C14 60%,#020510 100%)">
  <!-- Stars -->
  <div class="stars-wrap">
    <span class="s" style="top:10%;left:5%;width:2px;height:2px;animation-delay:.0s"></span>
    <span class="s" style="top:25%;left:15%;width:1px;height:1px;animation-delay:.5s"></span>
    <span class="s" style="top:60%;left:8%;width:2px;height:2px;animation-delay:1.2s"></span>
    <span class="s" style="top:80%;left:20%;width:1px;height:1px;animation-delay:.8s"></span>
    <span class="s" style="top:15%;left:30%;width:2px;height:2px;animation-delay:1.8s"></span>
    <span class="s" style="top:45%;left:38%;width:1px;height:1px;animation-delay:.3s"></span>
    <span class="s" style="top:75%;left:45%;width:2px;height:2px;animation-delay:2.1s"></span>
    <span class="s" style="top:20%;left:55%;width:1px;height:1px;animation-delay:1.5s"></span>
    <span class="s" style="top:55%;left:65%;width:2px;height:2px;animation-delay:.6s"></span>
    <span class="s" style="top:85%;left:72%;width:1px;height:1px;animation-delay:1.9s"></span>
    <span class="s" style="top:30%;left:85%;width:2px;height:2px;animation-delay:.4s"></span>
    <span class="s" style="top:65%;left:92%;width:1px;height:1px;animation-delay:2.3s"></span>
    <span class="s big" style="top:20%;left:12%;animation-delay:.2s;background:#93DDFF;box-shadow:0 0 6px #93DDFF"></span>
    <span class="s big" style="top:50%;left:28%;animation-delay:1.4s;background:#FBBF24;box-shadow:0 0 6px #FBBF24"></span>
    <span class="s big" style="top:70%;left:82%;animation-delay:1.7s;background:#A855F7;box-shadow:0 0 6px #A855F7"></span>
  </div>
  <!-- Planets -->
  <div class="planet" style="width:44px;height:44px;top:18%;right:25%;background:radial-gradient(circle at 30% 30%,#A855F7,#3B1F8C);box-shadow:inset -6px -4px 14px rgba(0,0,0,.5),0 0 28px rgba(168,85,247,.4);animation:pSpin 20s linear infinite"></div>
  <div class="planet" style="width:22px;height:22px;bottom:20%;left:32%;background:radial-gradient(circle at 35% 30%,#FCD34D,#92400E);box-shadow:inset -4px -2px 8px rgba(0,0,0,.5),0 0 16px rgba(252,211,77,.4);animation:pSpin 35s linear infinite reverse"></div>
  <!-- Shooting star -->
  <div class="shoot"></div>
  <!-- Rocket -->
  <div class="rocket">
    <svg width="56" height="76" viewBox="0 0 60 80" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="30" cy="35" rx="11" ry="22" fill="#E2E8F0"/>
      <path d="M30 13 Q20 25 19 35 L41 35 Q40 25 30 13" fill="#F1F5FF"/>
      <circle cx="30" cy="32" r="5" fill="#0EA5E9" stroke="#0369A1" stroke-width="1.5"/>
      <circle cx="30" cy="32" r="2.5" fill="#7DD3FC"/>
      <path d="M19 50 L11 60 L19 60 Z" fill="#EF4444"/>
      <path d="M41 50 L49 60 L41 60 Z" fill="#EF4444"/>
      <path d="M25 55 L35 55 L33 62 L27 62 Z" fill="#1E3A8A"/>
      <g class="flame">
        <path d="M25 60 Q30 78 35 60 Q33 70 30 72 Q27 70 25 60" fill="#F59E0B"/>
        <path d="M27 60 Q30 74 33 60 Q31 68 30 69 Q29 68 27 60" fill="#FCD34D"/>
      </g>
    </svg>
  </div>
  <!-- Text -->
  <div class="scene-text">
    <div class="eyebrow"><span class="dot"></span>LIVE DASHBOARD</div>
    <div class="scene-title">Selamat Datang!</div>
    <div class="scene-sub">Real-time talent intelligence · Powered by AI</div>
  </div>
</div>
""", extra_css="""
.stars-wrap{position:absolute;inset:0}
.s{position:absolute;background:white;border-radius:50%;animation:twinkle 3s ease infinite}
.s.big{width:3px;height:3px}
@keyframes twinkle{0%,100%{opacity:.3;transform:scale(1)}50%{opacity:1;transform:scale(1.5)}}
.planet{position:absolute;border-radius:50%}
@keyframes pSpin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.shoot{position:absolute;top:20%;left:-10%;width:100px;height:1.5px;background:linear-gradient(90deg,transparent,white);animation:shoot 7s ease-in infinite;opacity:0}
@keyframes shoot{0%{left:-10%;top:15%;opacity:0}10%{opacity:1}30%{left:110%;top:55%;opacity:0}100%{opacity:0}}
.rocket{position:absolute;animation:rocketFly 12s ease-in-out infinite;z-index:10}
@keyframes rocketFly{
  0%{left:-70px;top:65%;transform:rotate(-15deg) scale(.7)}
  20%{top:32%;transform:rotate(15deg) scale(.95)}
  40%{left:45%;top:52%;transform:rotate(-8deg) scale(1.1)}
  60%{top:28%;transform:rotate(20deg) scale(1)}
  80%{left:82%;top:42%;transform:rotate(5deg) scale(.85)}
  100%{left:110%;top:33%;transform:rotate(10deg) scale(.6)}}
.flame{transform-origin:30px 60px;animation:flicker .1s ease infinite alternate}
@keyframes flicker{from{transform:scaleY(.8)}to{transform:scaleY(1.2)}}
""")


# ══════════════════════════════════════════════════════════════════
#  SCENE 2 — MASTER DATA: Plane through clouds
# ══════════════════════════════════════════════════════════════════
SCENE_MASTER_HTML = _wrap("""
<div class="scene" style="background:linear-gradient(to bottom,#0c1840 0%,#1a3a8a 40%,#2563EB 100%)">
  <!-- Sun -->
  <div class="sun"></div>
  <!-- Clouds -->
  <div class="cloud" style="top:28%;animation-duration:22s;animation-delay:0s">
    <div class="cpuff" style="width:52px;height:52px;left:20px;top:-26px"></div>
    <div class="cpuff" style="width:40px;height:40px;left:66px;top:-20px"></div>
  </div>
  <div class="cloud" style="top:58%;width:85px;height:24px;animation-duration:28s;animation-delay:5s;opacity:.75">
    <div class="cpuff" style="width:38px;height:38px;left:14px;top:-19px"></div>
    <div class="cpuff" style="width:30px;height:30px;left:44px;top:-14px"></div>
  </div>
  <div class="cloud" style="top:76%;width:100px;height:26px;animation-duration:18s;animation-delay:10s;opacity:.55">
    <div class="cpuff" style="width:44px;height:44px;left:18px;top:-22px"></div>
    <div class="cpuff" style="width:34px;height:34px;left:56px;top:-16px"></div>
  </div>
  <div class="cloud" style="top:14%;width:90px;height:22px;animation-duration:34s;animation-delay:14s;opacity:.45">
    <div class="cpuff" style="width:38px;height:38px;left:16px;top:-19px"></div>
    <div class="cpuff" style="width:28px;height:28px;left:50px;top:-13px"></div>
  </div>
  <!-- Plane -->
  <div class="plane">
    <svg width="80" height="40" viewBox="0 0 80 40" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="42" cy="20" rx="32" ry="6" fill="white"/>
      <path d="M10 20 L0 14 L0 26 Z" fill="#E2E8F0"/>
      <path d="M30 14 L20 4 L18 4 L24 16 Z" fill="#94A3B8"/>
      <path d="M30 26 L20 36 L18 36 L24 24 Z" fill="#94A3B8"/>
      <path d="M55 16 L60 8 L62 8 L60 18 Z" fill="#64748B"/>
      <path d="M55 24 L60 32 L62 32 L60 22 Z" fill="#64748B"/>
      <ellipse cx="62" cy="20" rx="6" ry="4" fill="#0EA5E9"/>
      <rect x="20" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="27" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="34" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="41" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="48" y="18" width="3" height="4" fill="#0EA5E9"/>
    </svg>
  </div>
  <!-- Text -->
  <div class="scene-text">
    <div class="eyebrow" style="color:white"><span class="dot"></span>DATABASE EXPLORER</div>
    <div class="scene-title">Master Data</div>
    <div class="scene-sub">Soar through your candidate records</div>
  </div>
</div>
""", extra_css="""
.sun{position:absolute;width:58px;height:58px;border-radius:50%;background:radial-gradient(circle,#FCD34D 0%,#F59E0B 60%,transparent 80%);top:12%;right:8%;animation:sunGlow 4s ease infinite}
@keyframes sunGlow{0%,100%{box-shadow:0 0 30px rgba(252,211,77,.5)}50%{box-shadow:0 0 65px rgba(252,211,77,.9)}}
.cloud{position:absolute;left:-130px;background:rgba(255,255,255,.2);border-radius:50px;width:120px;height:30px;animation:cloudFly linear infinite}
.cpuff{position:absolute;background:rgba(255,255,255,.22);border-radius:50%}
@keyframes cloudFly{from{left:-130px}to{left:110%}}
.plane{position:absolute;z-index:10;animation:planeFly 14s ease-in-out infinite}
@keyframes planeFly{
  0%{left:-80px;top:40%;transform:rotate(2deg) scale(.85)}
  25%{top:27%;transform:rotate(-3deg) scale(1)}
  50%{left:50%;top:35%;transform:rotate(2deg) scale(1.1)}
  75%{top:24%;transform:rotate(-2deg) scale(.95)}
  100%{left:110%;top:30%;transform:rotate(3deg) scale(.8)}}
""")


# ══════════════════════════════════════════════════════════════════
#  SCENE 3 — INPUT DATA: Floating documents + sparkles
# ══════════════════════════════════════════════════════════════════
SCENE_INPUT_HTML = _wrap("""
<div class="scene" style="background:linear-gradient(135deg,#1e1b4b 0%,#312e81 50%,#1e3a8a 100%)">
  <div class="paper" style="top:58%;left:8%;--r:-15deg;animation-delay:0s"></div>
  <div class="paper" style="top:26%;left:31%;--r:10deg;animation-delay:1.5s"></div>
  <div class="paper" style="top:53%;left:57%;--r:-8deg;animation-delay:3s"></div>
  <div class="paper" style="top:20%;left:74%;--r:20deg;animation-delay:5s"></div>
  <div class="paper" style="top:66%;left:84%;--r:-12deg;animation-delay:2s"></div>
  <span class="spark" style="top:22%;left:22%;animation-delay:0s"></span>
  <span class="spark" style="top:71%;left:47%;animation-delay:.7s"></span>
  <span class="spark" style="top:38%;left:64%;animation-delay:1.3s"></span>
  <span class="spark" style="top:78%;left:27%;animation-delay:1.9s"></span>
  <div class="scene-text">
    <div class="eyebrow"><span class="dot"></span>DATA ENTRY</div>
    <div class="scene-title">Input Data</div>
    <div class="scene-sub">Add new candidate records seamlessly</div>
  </div>
</div>
""", extra_css="""
.paper{position:absolute;width:48px;height:60px;background:white;border-radius:4px;
  box-shadow:0 8px 24px rgba(0,0,0,.4);transform:rotate(var(--r,0));
  animation:paperFloat 10s ease-in-out infinite}
.paper::before{content:'';position:absolute;top:8px;left:8px;right:8px;height:2px;background:#cbd5e1;border-radius:1px;
  box-shadow:0 6px 0 #cbd5e1,0 12px 0 #cbd5e1,0 18px 0 #e2e8f0,0 24px 0 #e2e8f0,0 30px 0 #e2e8f0}
@keyframes paperFloat{0%,100%{transform:translateY(0) rotate(var(--r,0))}50%{transform:translateY(-22px) rotate(var(--r,0))}}
.spark{position:absolute;width:7px;height:7px;border-radius:50%;background:#FCD34D;
  box-shadow:0 0 14px #FCD34D;animation:sparkPop 2.4s ease infinite}
@keyframes sparkPop{0%,100%{opacity:0;transform:scale(0)}50%{opacity:1;transform:scale(1.3)}}
""")


# ══════════════════════════════════════════════════════════════════
#  SCENE 4 — AI SCREENER: Pulsing neural network
# ══════════════════════════════════════════════════════════════════
SCENE_AI_HTML = _wrap("""
<div class="scene" style="background:radial-gradient(ellipse at center,#1e1b4b 0%,#0c0a3e 60%,#020510 100%)">
  <!-- Neural net lines -->
  <svg style="position:absolute;inset:0;width:100%;height:100%;opacity:.3" xmlns="http://www.w3.org/2000/svg">
    <line x1="15%" y1="30%" x2="45%" y2="20%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="15%" y1="30%" x2="45%" y2="50%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="15%" y1="65%" x2="45%" y2="50%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="15%" y1="65%" x2="45%" y2="80%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="45%" y1="20%" x2="78%" y2="35%" stroke="#A855F7" stroke-width="1"/>
    <line x1="45%" y1="50%" x2="78%" y2="35%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="45%" y1="50%" x2="78%" y2="65%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="45%" y1="80%" x2="78%" y2="65%" stroke="#38BDF8" stroke-width="1"/>
  </svg>
  <!-- Brain rings -->
  <div class="ring r1"></div>
  <div class="ring r2"></div>
  <div class="ring r3"></div>
  <!-- Nodes -->
  <span class="node" style="top:30%;left:15%;background:#38BDF8;box-shadow:0 0 18px #38BDF8;animation-delay:0s"></span>
  <span class="node" style="top:65%;left:15%;background:#22D3EE;box-shadow:0 0 18px #22D3EE;animation-delay:.3s"></span>
  <span class="node" style="top:20%;left:45%;background:#A855F7;box-shadow:0 0 18px #A855F7;animation-delay:.6s"></span>
  <span class="node" style="top:50%;left:45%;background:#22D3EE;box-shadow:0 0 18px #22D3EE;animation-delay:.9s"></span>
  <span class="node" style="top:80%;left:45%;background:#38BDF8;box-shadow:0 0 18px #38BDF8;animation-delay:1.2s"></span>
  <span class="node" style="top:35%;left:78%;background:#10B981;box-shadow:0 0 22px #10B981;animation-delay:1.5s"></span>
  <span class="node" style="top:65%;left:78%;background:#10B981;box-shadow:0 0 22px #10B981;animation-delay:1.8s"></span>
  <div class="scene-text">
    <div class="eyebrow"><span class="dot"></span>AI POWERED</div>
    <div class="scene-title">AI CV Screener</div>
    <div class="scene-sub">Claude analyzes every resume</div>
  </div>
</div>
""", extra_css="""
.ring{position:absolute;border-radius:50%;top:50%;left:50%;transform:translate(-50%,-50%)}
.r1{width:80px;height:80px;border:2px solid rgba(56,189,248,.5);box-shadow:0 0 20px rgba(56,189,248,.3);animation:spin 8s linear infinite}
.r2{width:104px;height:104px;border:1.5px solid rgba(112,0,255,.4);animation:spin 12s linear infinite reverse}
.r3{width:128px;height:128px;border:1px solid rgba(34,211,238,.3);animation:spin 16s linear infinite}
@keyframes spin{from{transform:translate(-50%,-50%) rotate(0)}to{transform:translate(-50%,-50%) rotate(360deg)}}
.node{position:absolute;width:14px;height:14px;border-radius:50%;animation:nodePulse 2s ease infinite}
@keyframes nodePulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.7);opacity:.6}}
""")


# ══════════════════════════════════════════════════════════════════
#  SCENE 5 — SYSTEM LOGS: Matrix code rain
# ══════════════════════════════════════════════════════════════════
SCENE_LOGS_HTML = _wrap("""
<div class="scene" style="background:linear-gradient(180deg,#020510 0%,#050810 100%)">
  <div class="col" style="left:6%;animation-duration:7s;animation-delay:0s">01011100<br>11001010<br>00110101<br>10011010<br>01110100<br>10101100</div>
  <div class="col" style="left:18%;animation-duration:5s;animation-delay:.8s">10110010<br>01010101<br>11100110<br>00101110<br>10011101<br>01010011</div>
  <div class="col" style="left:32%;animation-duration:9s;animation-delay:.4s">11000101<br>01101010<br>10010110<br>11110000<br>01010101<br>11001100</div>
  <div class="col" style="left:48%;animation-duration:6s;animation-delay:1.8s">01101001<br>10110011<br>01010111<br>10001010<br>11100110<br>00110011</div>
  <div class="col" style="left:63%;animation-duration:8s;animation-delay:.2s">10101010<br>01010101<br>11001100<br>00110011<br>10010110<br>01101100</div>
  <div class="col" style="left:78%;animation-duration:4.5s;animation-delay:1.2s">01010101<br>10101010<br>11110000<br>00001111<br>10110101<br>01001100</div>
  <div class="col" style="left:90%;animation-duration:6.5s;animation-delay:2.5s">11001010<br>00110101<br>10011010<br>01110100<br>10101100<br>01011100</div>
  <div class="scene-text">
    <div class="eyebrow"><span class="dot" style="background:#10B981;box-shadow:0 0 10px #10B981"></span>MONITOR</div>
    <div class="scene-title">System Logs</div>
    <div class="scene-sub">Real-time agent health stream</div>
  </div>
</div>
""", extra_css="""
.col{position:absolute;top:-130%;font-family:'JetBrains Mono','Courier New',monospace;
  font-size:11px;color:#10B981;text-shadow:0 0 8px #10B981;line-height:1.4;
  writing-mode:vertical-rl;letter-spacing:2px;opacity:.55;
  animation:matrixFall linear infinite}
@keyframes matrixFall{from{top:-130%}to{top:130%}}
""")


# ══════════════════════════════════════════════════════════════════
#  PUBLIC MAP
# ══════════════════════════════════════════════════════════════════
SCENES = {
    "overview": SCENE_OVERVIEW_HTML,
    "master":   SCENE_MASTER_HTML,
    "input":    SCENE_INPUT_HTML,
    "ai":       SCENE_AI_HTML,
    "logs":     SCENE_LOGS_HTML,
}
