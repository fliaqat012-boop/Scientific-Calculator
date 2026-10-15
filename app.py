import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="FATIMA LIAQAT Calculator", layout="centered")

THEMES = {
    "Original Blue": {"body": "#a8bdff", "ear": "#8aa8ff", "border": "#6d8cff", "bg_light": "#e6ecff", "bg_dark": "#1a1d2e", "light": "#d6e6ff"},
    "Barbie Pink": {"body": "#ffb6d9", "ear": "#ff8fab", "border": "#ff4d8f", "bg_light": "#ffe5ec", "bg_dark": "#2e1a24", "light": "#ffc8dd"},
    "Lavender": {"body": "#cbb6ff", "ear": "#a48bff", "border": "#8a5cff", "bg_light": "#ede7ff", "bg_dark": "#211a2e", "light": "#e5d3ff"},
    "Mint Green": {"body": "#b9f6ca", "ear": "#81e6a0", "border": "#4caf7a", "bg_light": "#e8f5e9", "bg_dark": "#1a2e20", "light": "#dcedc8"},
}

if 'theme_selector' not in st.session_state:
    st.session_state['theme_selector'] = 'Original Blue'
if 'mode_selector' not in st.session_state:
    st.session_state['mode_selector'] = 'Light Mode ☀️'

t = THEMES[st.session_state['theme_selector']]
is_dark = "Dark" in st.session_state['mode_selector']
bg_color = t['bg_dark'] if is_dark else t['bg_light']
text_color = "white" if is_dark else "black"

st.markdown(f"<h1 style='text-align:center; font-weight:900; color:{text_color} !important; -webkit-text-fill-color:{text_color} !important;'> FATIMA LIAQAT</h1>", unsafe_allow_html=True)

st.markdown(f"""
<style>
.stApp{{background:{bg_color} !important;}}
header,footer{{visibility:hidden}}
* {{ scroll-behavior: auto !important; }}
html, body, [data-testid="stVerticalBlock"] {{ overflow-anchor: none !important; }}
h1, label, p {{ color:{text_color} !important; -webkit-text-fill-color:{text_color} !important; }}
div[data-testid='stWidgetLabel'] label {{ color:{text_color} !important; font-weight:800 !important; }}
[data-testid="stVerticalBlockBorderWrapper"]{{background: rgba(255,255,255,0.95) !important; border: 2px solid {t['border']} !important; border-radius: 15px !important;}}
</style>
""", unsafe_allow_html=True)

_, mid_col, _ = st.columns([0.5, 3, 0.5])
with mid_col:
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.selectbox("🎨 Theme", list(THEMES.keys()), key='theme_selector')
        with c2:
            st.radio("🌓 Mode", ["Light Mode ☀️", "Dark Mode 🌙"], key='mode_selector')

HTML_TEMPLATE = """
<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{margin:0;display:flex;justify-content:center;background:transparent;font-family:'Segoe UI',sans-serif; outline:none;}
.wrap{position:relative;padding-top:35px; width:100%; max-width:400px; display:flex; justify-content:center; margin:0 auto;}
.ears::before,.ears::after{content:'';position:absolute;top:0;width:68px;height:60px;background:__EAR__;border-radius:70% 70% 20% 20%;z-index:0;border:4px solid white}
.ears::before{left:22px;transform:rotate(-12deg)}.ears::after{right:22px;transform:rotate(12deg)}
.calculator{width:95%; max-width:378px; background:__BODY__;border-radius:42px 42px 65px 65px;padding:20px 18px 24px 18px;position:relative;z-index:1;border:5px solid white;box-shadow:0 22px 45px rgba(0,0,0,.30); margin:0 auto;} 
.display{background:white;border:3.5px solid __BORDER__;border-radius:20px;padding:14px 16px;min-height:75px;text-align:right;}
#history{font-size:13px;color:#8a9cc5;min-height:18px;word-break:break-all}#result{font-size:36px;font-weight:800;color:#1e2a5a;line-height:1.1;word-break:break-all}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:11px;margin-top:15px}
button{border:none;border-radius:18px;padding:14px 3px;font-size:13px;font-weight:800;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.15);color:#3b4a8a;}
.mem{background:#c9f0d8}.func-y{background:#fde9a0}.func-b{background:__LIGHT__}.light{background:#e3f2fd}.num{background:#fff}.op{background:__BORDER__;color:white}.pink{background:#ff8a9d;color:white}.ac{background:#ff7a8e;color:white}.equals{background:__BORDER__;color:white}
.sep{border-top:3px dotted white;margin:8px 0;grid-column:1 / -1}
</style></head><body tabindex="0">
<div class="wrap"><div class="ears"></div><div class="calculator">
<div class="display"><small id="degLabel" style="float:left;background:__LIGHT__;padding:3px 10px;border-radius:12px;font-size:11px;font-weight:bold">DEG</small><div id="history"></div><div id="result">0</div></div>
<div class="grid">
<button class="mem" onclick="mem('MC')">MC</button><button class="mem" onclick="mem('MR')">MR</button><button class="mem" onclick="mem('M+')">M+</button><button class="mem" onclick="mem('M-')">M-</button><button class="mem" onclick="mem('MS')">MS</button>
<button class="func-y" onclick="toggleDeg()">DEG</button><button class="func-y" onclick="toggleHyp()">hyp</button><button class="func-y" id="shiftBtn" onclick="toggleShift()">SHIFT</button><button class="func-b" onclick="insert('*10**')">EXP</button><button class="func-b" onclick="doRandom()">Ran#</button>
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
let expr='', ans=0, memory=0, isDeg=true, isHyp=false, isShift=false;
function update(){document.getElementById('history').innerText=expr;document.getElementById('result').innerText=expr||'0';}
function insert(v){expr+=v;update();}
function doRandom(){expr+=Math.random().toFixed(5);update();}
function clearAll(){expr='';document.getElementById('result').innerText='0';document.getElementById('history').innerText='';}
function back(){expr=expr.slice(0,-1);update();}
function useAns(){expr+=ans;update();}
function neg(){if(expr.startsWith('-'))expr=expr.slice(1);else expr='-'+expr;update();}
function toggleDeg(){isDeg=!isDeg; document.getElementById('degLabel').innerText = isDeg?'DEG':'RAD';}
function toggleHyp(){isHyp=!isHyp;}
function toggleShift(){isShift=!isShift; let btn=document.getElementById('shiftBtn'); if(isShift){ btn.style.background='#ff8a9d'; btn.style.color='white'; } else{ btn.style.background='#fde9a0'; btn.style.color='#3b4a8a'; }}
function toRad(x){return isDeg?x*Math.PI/180:x;}
function factorial(n){n=Math.floor(Number(n));if(n<0||isNaN(n))return NaN;if(n===0)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r;}
function nPr(n,r){return factorial(n)/factorial(n-r);}
function nCr(n,r){return factorial(n)/(factorial(r)*factorial(n-r));}
function balanceBrackets(s){let o=(s.match(/\\(/g)||[]).length; let c=(s.match(/\\)/g)||[]).length; if(o>c) s+=')'.repeat(o-c); return s;}
function safeEval(s){
  try{
    if(!s||s.trim()==='')return null;
    s=s.replace(/(sin|cos|tan|ln|log|sqrt|asin|acos|atan)(\\d+(\\.\\d+)?)/g,'$1($2)');
    s=balanceBrackets(s);
    s=s.replace(/(\\d|\\))(\\()/g,'$1*$2');
    s=s.replace(/(\\))(\\d)/g,'$1*$2');
    let t=s.replace(/π/g,'Math.PI').replace(/E/g,'Math.E').replace(/÷/g,'/').replace(/×/g,'*').replace(/−/g,'-').replace(/\\^/g,'**').replace(/mod/g,'%');
    t=t.replace(/°/g,'*Math.PI/180');
    t=t.replace(/(\\d+(\\.\\d+)?|\\))%/g,'($1/100)');
    t=t.replace(/(\\d+(\\.\\d+)?|\\))!/g,'factorial($1)');
    t=t.replace(/(\\d+(\\.\\d+)?|\\))P(\\d+(\\.\\d+)?)/g,'nPr($1,$3)');
    t=t.replace(/(\\d+(\\.\\d+)?|\\))C(\\d+(\\.\\d+)?)/g,'nCr($1,$3)');
    t=t.replace(/\\|([^|]+)\\|/g,'Math.abs($1)');
    t=t.replace(/asin\\(/g,'__ASIN__('); t=t.replace(/acos\\(/g,'__ACOS__('); t=t.replace(/atan\\(/g,'__ATAN__(');
    t=t.replace(/sqrt\\(/g,'Math.sqrt('); t=t.replace(/log\\(/g,'Math.log10('); t=t.replace(/ln\\(/g,'Math.log('); t=t.replace(/exp\\(/g,'Math.exp(');
    t=t.replace(/sin\\(/g,'__SIN__('); t=t.replace(/cos\\(/g,'__COS__('); t=t.replace(/tan\\(/g,'__TAN__(');
    function __SIN__(x){return isHyp?Math.sinh(x):Math.sin(toRad(x));}
    function __COS__(x){return isHyp?Math.cosh(x):Math.cos(toRad(x));}
    function __TAN__(x){return isHyp?Math.tanh(x):Math.tan(toRad(x));}
    function __ASIN__(x){let r=Math.asin(x); return isDeg?r*180/Math.PI:r;}
    function __ACOS__(x){let r=Math.acos(x); return isDeg?r*180/Math.PI:r;}
    function __ATAN__(x){let r=Math.atan(x); return isDeg?r*180/Math.PI:r;}
    return Function('nPr','nCr','factorial','Math','__SIN__','__COS__','__TAN__','__ASIN__','__ACOS__','__ATAN__','return '+t)(nPr,nCr,factorial,Math,__SIN__,__COS__,__TAN__,__ASIN__,__ACOS__,__ATAN__);
  }catch(e){return null;}
}
function handleSci(f){
  let curr=expr.trim();
  if(isShift){
    if(f==='sin') f='asin'; else if(f==='cos') f='acos'; else if(f==='tan') f='atan';
    else if(f==='ln') f='exp'; else if(f==='log') f='tenpow'; else if(f==='sqrt') f='square';
    isShift=false; document.getElementById('shiftBtn').style.background='#fde9a0'; document.getElementById('shiftBtn').style.color='#3b4a8a';
  }
  let val=safeEval(curr);
  if(val!=null&&curr!==''&&!isNaN(val)&&!/[+\\-×÷^%\\(PC|]/.test(curr.slice(-1))){
    let res=val;
    if(f==='sin') res=isHyp?Math.sinh(val):Math.sin(toRad(val));
    else if(f==='cos') res=isHyp?Math.cosh(val):Math.cos(toRad(val));
    else if(f==='tan') res=isHyp?Math.tanh(val):Math.tan(toRad(val));
    else if(f==='asin') res=isDeg?Math.asin(val)*180/Math.PI:Math.asin(val);
    else if(f==='acos') res=isDeg?Math.acos(val)*180/Math.PI:Math.acos(val);
    else if(f==='atan') res=isDeg?Math.atan(val)*180/Math.PI:Math.atan(val);
    else if(f==='ln') res=Math.log(val); else if(f==='log') res=Math.log10(val);
    else if(f==='sqrt') res=Math.sqrt(val); else if(f==='cube') res=Math.pow(val,3);
    else if(f==='square') res=Math.pow(val,2); else if(f==='exp') res=Math.exp(val);
    else if(f==='tenpow') res=Math.pow(10,val); else if(f==='inv') res=1/val;
    else if(f==='fact') res=factorial(val); else if(f==='abs') res=Math.abs(val); else return;
    res=Number(Number(res).toFixed(10));
    document.getElementById('history').innerText=curr+' '+f+' ='; expr=String(res); ans=res;
    document.getElementById('result').innerText=res; return;
  }
  if(['sin','cos','tan','asin','acos','atan','ln','log','sqrt','exp'].includes(f)){expr+=f+'(';update();}
  else if(f==='cube'){expr+='^3';update();} else if(f==='square'){expr+='^2';update();}
  else if(f==='tenpow'){expr+='10^';update();} else if(f==='fact'){expr+='!';update();}
  else if(f==='inv'){expr='1/('+curr+')';update();} else if(f==='abs'){if(curr) expr='|'+curr+'|'; else expr+='|'; update();}
}
function calculate(){
  if(!expr || expr.trim() === "") return;
  let r=safeEval(balanceBrackets(expr));
  if(r!=null&&!isNaN(r)){ans=r; r=Number(Number(r).toFixed(10)); document.getElementById('history').innerText=expr + ' ='; expr=String(r); document.getElementById('result').innerText=r;}
  else{document.getElementById('result').innerText='Error';}
}
function mem(k){
  if(k==='MC')memory=0;
  else if(k==='MR'){expr+=memory; update();}
  else if(k==='M+'){let v=safeEval(expr); if(v!=null) memory+=v;}
  else if(k==='M-'){let v=safeEval(expr); if(v!=null) memory-=v;}
  else if(k==='MS'){let v=safeEval(expr); if(v!=null) memory=v;}
}
document.addEventListener('keydown', function(e) {
    if (e.key >= '0' && e.key <= '9') { insert(e.key); return; }
    if (e.key === '.') { insert('.'); return; }
    if (e.key === '+') { insert('+'); return; }
    if (e.key === '(' || e.key === ')') { insert(e.key); return; }
    if (e.key === '%') { insert('%'); return; }
    if (e.key === '/') { e.preventDefault(); insert('÷'); return; }
    if (e.key === '*') { e.preventDefault(); insert('×'); return; }
    if (e.key === '-') { insert('−'); return; }
    if (e.key === '^') { insert('^'); return; }
    if (e.key === 'Enter' || e.key === '=') { e.preventDefault(); calculate(); return; }
    if (e.key === 'Backspace') { e.preventDefault(); back(); return; }
    if (e.key === 'Escape' || e.key.toLowerCase() === 'c') { clearAll(); return; }
});
</script></body></html>
"""

html_code = HTML_TEMPLATE.replace("__BODY__", t['body']).replace("__EAR__", t['ear']).replace("__BORDER__", t['border']).replace("__LIGHT__", t['light'])
components.html(html_code, height=850, scrolling=False)
