import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scientific Calculator", layout="wide")

# --- SIDEBAR ME OPTIONS ---
st.sidebar.title("⚙️ Settings")

THEMES = {
    "Original Blue": {"body": "#a8bdff", "ear": "#8aa8ff", "border": "#6d8cff", "bg_light": "#e6ecff", "bg_dark": "#1a1d2e", "light": "#d6e6ff"},
    "Barbie Pink": {"body": "#ffb6d9", "ear": "#ff8fab", "border": "#ff4d8f", "bg_light": "#ffe5ec", "bg_dark": "#2e1a24", "light": "#ffc8dd"},
    "Lavender": {"body": "#cbb6ff", "ear": "#a48bff", "border": "#8a5cff", "bg_light": "#ede7ff", "bg_dark": "#211a2e", "light": "#e5d3ff"},
    "Mint Green": {"body": "#b9f6ca", "ear": "#81e6a0", "border": "#4caf7a", "bg_light": "#e8f5e9", "bg_dark": "#1a2e20", "light": "#dcedc8"},
}

color_choice = st.sidebar.selectbox("🎨 Color Theme:", list(THEMES.keys()))
mode_choice = st.sidebar.radio("🌓 Mode:", ["Light Mode ☀️", "Dark Mode 🌙"])

t = THEMES[color_choice]
is_dark = "Dark" in mode_choice

bg_color = t['bg_dark'] if is_dark else t['bg_light']
text_color = "white" if is_dark else "#1e2a5a"

st.markdown(f"""
<div style='text-align:center; margin-top:15px; margin-bottom:20px;'>
    <h1 style='font-family: "Poppins", Sans-serif; font-weight: 900; font-size: 50px; color: {text_color}; margin:0; text-shadow: 2px 2px 0px white;'>
        🧮 Scientific Calculator 
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<style>.stApp{{background:{bg_color} !important}} header,footer{{visibility:hidden}}</style>", unsafe_allow_html=True)

# --- CALCULATOR HTML ---
html_code = f"""
<html><head><style>
body{{margin:0;display:flex;justify-content:center;background:transparent;font-family:'Segoe UI',sans-serif}}
.wrap{{position:relative;padding-top:35px}}
.ears::before,.ears::after{{content:'';position:absolute;top:0;width:68px;height:60px;background:{t['ear']};border-radius:70% 70% 20% 20%;z-index:0;border:4px solid white}}
.ears::before{{left:22px;transform:rotate(-12deg)}}.ears::after{{right:22px;transform:rotate(12deg)}}
.calculator{{width:378px;background:{t['body']};border-radius:42px 42px 65px 65px;padding:20px 18px 24px 18px;position:relative;z-index:1;border:5px solid white;box-shadow:0 22px 45px rgba(0,0,0,.30)}}
.display{{background:white;border:3.5px solid {t['border']};border-radius:20px;padding:14px 16px;min-height:75px;text-align:right;}}
#history{{font-size:13px;color:#8a9cc5;min-height:18px;word-break:break-all}}#result{{font-size:42px;font-weight:800;color:#1e2a5a;line-height:1.1;word-break:break-all}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:11px;margin-top:15px}}
button{{border:none;border-radius:18px;padding:14px 3px;font-size:13px;font-weight:800;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.15);color:#3b4a8a}}
button:active{{transform:translateY(4px);box-shadow:0 1px 0 rgba(0,0,0,.15)}}
.mem{{background:#c9f0d8}}.func-y{{background:#fde9a0}}.func-b{{background:{t['light']}}}.light{{background:#e3f2fd}}.num{{background:#fff}}.op{{background:{t['border']};color:white}}.pink{{background:#ff8a9d;color:white}}.ac{{background:#ff7a8e;color:white}}.equals{{background:{t['border']};color:white}}
.sep{{border-top:3px dotted white;margin:8px 0;grid-column:1 / -1}}
</style></head><body>
<div class="wrap"><div class="ears"></div><div class="calculator">
<div class="display"><small style="float:left;background:{t['light']};padding:3px 10px;border-radius:12px;font-size:11px;font-weight:bold">DEG</small><div id="history"></div><div id="result">0</div></div>
<div class="grid">
<button class="mem" onclick="mem('MC')">MC</button><button class="mem" onclick="mem('MR')">MR</button><button class="mem" onclick="mem('M+')">M+</button><button class="mem" onclick="mem('M-')">M-</button><button class="mem" onclick="mem('MS')">MS</button>
<button class="func-y" onclick="toggleDeg()">DEG</button><button class="func-y" onclick="toggleHyp()">hyp</button><button class="func-y">SHIFT</button><button class="func-b" onclick="insert('*10**')">EXP</button><button class="func-b" onclick="doRandom()">Ran#</button>
<button class="func-b" onclick="handleSci('sin')">sin</button><button class="func-b" onclick="handleSci('cos')">cos</button><button class="func-b" onclick="handleSci('tan')">tan</button><button class="func-b" onclick="insert('π')">π</button><button class="func-b" onclick="insert('E')">e</button>
<button class="func-b" onclick="handleSci('ln')">ln</button><button class="func-b" onclick="handleSci('log')">log</button><button class="func-b" onclick="handleSci('sqrt')">√</button><button class="func-b" onclick="insert('^')">xʸ</button><button class="func-b" onclick="handleSci('fact')">n!</button>
<button class="func-b" onclick="handleSci('cube')">x³</button><button class="func-b" onclick="handleSci('inv')">1/x</button><button class="func-b" onclick="handleSci('abs')">|x|</button><button class="func-b" onclick="insert('P')">nPr</button><button class="func-b" onclick="insert('C')">nCr</button>
<button class="light" onclick="insert('(')">(</button><button class="light" onclick="insert(')')">)</button><button class="light" onclick="insert('%')">%</button><button class="light" onclick="insert('mod')">mod</button><button class="light" onclick="insert('°')">°</button>
<div class="sep"></div>
<button class="num" onclick="insert('7')">7</button><button class="num" onclick="insert('8')">8</button><button class="num" onclick="insert('9')">9</button><button class="op" onclick="insert('÷')">÷</button><button class="pink" onclick="back()">⌫</button>
<button class="num" onclick="insert('4')">4</button><button class="num" onclick="insert('5')">5</button><button class="num" onclick="insert('6')">6</button><button class="op" onclick="insert('×')">×</button><button class="ac" onclick="clearAll()">AC</button>
<button class="num" onclick="insert('1')">1</button><button class="num" onclick="insert('2')">2</button><button class="num" onclick="insert('3')">3</button><button class="op" onclick="insert('−')">−</button><button class="light" onclick="useAns()">Ans</button>
<button class="num" onclick="insert('0')">0</button><button class="num" onclick="insert('.')">.</button><button class="num" onclick="neg()">±</button><button class="op" onclick="insert('+')">+</button><button class="equals" onclick="calculate()">=</button>
</div></div></div>
<script>
let expr='', ans=0, memory=0, isDeg=true, isHyp=false;
function update(){{document.getElementById('history').innerText=expr;document.getElementById('result').innerText=expr||'0';}}
function insert(v){{expr+=v;update();}}function doRandom(){{expr+=Math.random().toFixed(5);update();}}
function clearAll(){{expr='';document.getElementById('result').innerText='0';document.getElementById('history').innerText='';}}
function back(){{expr=expr.slice(0,-1);update();}}function useAns(){{expr+=ans;update();}}
function neg(){{if(expr.startsWith('-'))expr=expr.slice(1);else expr='-'+expr;update();}}
function toggleDeg(){{isDeg=!isDeg}}function toggleHyp(){{isHyp=!isHyp}}
function mem(k){{if(k==='MC')memory=0;if(k==='MS'){{let v=safeEval(expr);if(v!=null)memory=v;}}if(k==='MR'){{expr+=memory;update();}}if(k==='M+'){{let v=safeEval(expr);if(v!=null)memory+=v;}}if(k==='M-'){{let v=safeEval(expr);if(v!=null)memory-=v;}}}}
function toRad(x){{return isDeg?x*Math.PI/180:x;}}function factorial(n){{n=Math.floor(Number(n));if(n<0||isNaN(n))return NaN;if(n===0)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r;}}
function nPr(n,r){{return factorial(n)/factorial(n-r);}}function nCr(n,r){{return factorial(n)/(factorial(r)*factorial(n-r));}}
function safeEval(s){{try{{if(!s||s.trim()==='')return null;let t=s.replace(/π/g,'Math.PI').replace(/E/g,'Math.E').replace(/÷/g,'/').replace(/×/g,'*').replace(/−/g,'-').replace(/\\^/g,'**').replace(/mod/g,'%');t=t.replace(/(\\d+(\\.\\d+)?)P(\\d+)/g,'nPr($1,$3)');t=t.replace(/(\\d+(\\.\\d+)?)C(\\d+)/g,'nCr($1,$3)');t=t.replace(/(\\d+(\\.\\d+)?)%/g,'($1/100)');t=t.replace(/sqrt\\(/g,'Math.sqrt(');t=t.replace(/ln\\(/g,'Math.log(');t=t.replace(/log\\(/g,'Math.log10(');t=t.replace(/sin\\(/g,'__sin(');t=t.replace(/cos\\(/g,'__cos(');t=t.replace(/tan\\(/g,'__tan(');function __sin(x){{return isHyp?Math.sinh(toRad(x)):Math.sin(toRad(x));}}function __cos(x){{return isHyp?Math.cosh(toRad(x)):Math.cos(toRad(x));}}function __tan(x){{return isHyp?Math.tanh(toRad(x)):Math.tan(toRad(x));}}return Function('nPr','nCr','factorial','Math','__sin','__cos','__tan','return '+t)(nPr,nCr,factorial,Math,__sin,__cos,__tan);}}catch(e){{return null;}}}}
function handleSci(f){{let curr=expr.trim();let val=safeEval(curr);if(val!=null&&curr!==''&&!isNaN(val)&&!/[+\\-×÷^%()P C]$/.test(curr)){{let res=val;if(f==='sin')res=isHyp?Math.sinh(toRad(val)):Math.sin(toRad(val));if(f==='cos')res=isHyp?Math.cosh(toRad(val)):Math.cos(toRad(val));if(f==='tan')res=isHyp?Math.tanh(toRad(val)):Math.tan(toRad(val));if(f==='ln')res=Math.log(val);if(f==='log')res=Math.log10(val);if(f==='sqrt')res=Math.sqrt(val);if(f==='cube')res=Math.pow(val,3);if(f==='inv')res=1/val;if(f==='fact')res=factorial(val);res=Number(Number(res).toFixed(10));document.getElementById('history').innerText=curr+' '+f+' =';expr=String(res);ans=res;document.getElementById('result').innerText=res;return;}}if(f==='sin'||f==='cos'||f==='tan'||f==='ln'||f==='log'||f==='sqrt'){{expr+=f+'(';update();}}else if(f==='cube'){{expr+='^3';update();}}else if(f==='inv'){{expr='1/('+curr+')';update();}}else if(f==='fact'){{let r=factorial(val||0);expr=String(r);update();}}}}
function calculate(){{let r=safeEval(expr);if(r!=null&&!isNaN(r)){{ans=r;r=Number(Number(r).toFixed(10));expr=String(r);document.getElementById('result').innerText=r;document.getElementById('history').innerText='';}}else{{document.getElementById('result').innerText='Error';}}}}

// === DIRECT KEYBOARD SUPPORT - NO BAR ===
document.addEventListener('keydown', function(e) {{
    if (e.key >= '0' && e.key <= '9') {{ insert(e.key); }}
    if (e.key === '.') {{ insert('.'); }}
    if (e.key === '+') {{ insert('+'); }}
    if (e.key === '(' || e.key === ')') {{ insert(e.key); }}
    if (e.key === '%') {{ insert('%'); }}
    if (e.key === '/') {{ e.preventDefault(); insert('÷'); }}
    if (e.key === '*') {{ e.preventDefault(); insert('×'); }}
    if (e.key === '-') {{ insert('−'); }}
    if (e.key === 'Enter' || e.key === '=') {{ e.preventDefault(); calculate(); }}
    if (e.key === 'Backspace') {{ e.preventDefault(); back(); }}
    if (e.key === 'Escape' || e.key.toLowerCase() === 'c') {{ clearAll(); }}
}});

</script></body></html>
"""

col1, col2, col3 = st.columns([1,2,1])
with col2:
    components.html(html_code, height=1100, scrolling=False)
