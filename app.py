import math
import re
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Pro Scientific Calculator", page_icon="🧮", layout="centered"
)

# Sidebar Settings for Theme and History
with st.sidebar:
  st.header("⚙️ Settings & Features")
  theme = st.radio("Theme Selector", ["Dark Mode", "Light Mode"])
  mode = st.radio("Calculator Mode", ["Standard", "Scientific"])
  st.markdown("---")
  st.header("📜 Calculation History")

  if "history_log" not in st.session_state:
    st.session_state.history_log = []

  if st.session_state.history_log:
    for hist in reversed(st.session_state.history_log[-10:]):
      st.text(hist)
    if st.button("Clear History"):
      st.session_state.history_log = []
      st.rerun()
  else:
    st.info("No history yet.")

# Dynamic Theme Colors
if theme == "Dark Mode":
  bg_style = "linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)"
  screen_bg = "linear-gradient(145deg, #090d16, #111827)"
  screen_border = "#334155"
  text_color = "#f8fafc"
  btn_bg = "linear-gradient(145deg, #1e293b, #0f172a)"
  btn_color = "#e2e8f0"
  btn_hover_border = "#38bdf8"
else:
  bg_style = "linear-gradient(135deg, #f1f5f9 0%, #cbd5e1 100%)"
  screen_bg = "linear-gradient(145deg, #ffffff, #f8fafc)"
  screen_border = "#94a3b8"
  text_color = "#0f172a"
  btn_bg = "linear-gradient(145deg, #ffffff, #f1f5f9)"
  btn_color = "#1e293b"
  btn_hover_border = "#0284c7"

# Compact Screen CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {bg_style};
        color: {text_color};
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .app-header {{
        text-align: center;
        font-weight: 700;
        letter-spacing: 1.5px;
        color: #38bdf8;
        font-size: 22px;
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }}

    .calc-screen {{
        background: {screen_bg};
        border: 2px solid {screen_border};
        border-radius: 12px;
        padding: 10px 18px;
        text-align: right;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1), 0 6px 15px -3px rgba(0, 0, 0, 0.2);
    }}
    .history-text {{
        color: #64748b;
        font-size: 13px;
        font-family: monospace;
        min-height: 18px;
        margin-bottom: 2px;
    }}
    .main-result {{
        color: #38bdf8;
        font-size: 30px;
        font-weight: 700;
        font-family: monospace;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }}

    .stButton>button {{
        width: 100%;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: {btn_bg};
        color: {btn_color};
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
        transition: all 0.2s ease-in-out;
    }}
    .stButton>button:hover {{
        border-color: {btn_hover_border};
        color: #38bdf8;
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(56, 189, 248, 0.2);
    }}
    .stButton>button:active {{
        transform: translateY(1px);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State
if "expression" not in st.session_state:
  st.session_state.expression = ""
if "last_expr" not in st.session_state:
  st.session_state.last_expr = ""
if "result" not in st.session_state:
  st.session_state.result = "0"
if "history_log" not in st.session_state:
  st.session_state.history_log = []


def evaluate_calc():
  try:
    allowed_names = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "factorial": math.factorial,
        "pi": math.pi,
        "e": math.e,
    }

    raw_expr = st.session_state.expression

    if not raw_expr.strip():
      return

    processed_expr = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", raw_expr)

    eval_str = (
        processed_expr.replace("^", "**")
        .replace("×", "*")
        .replace("÷", "/")
        .replace("%", "/100")
    )

    open_brackets = eval_str.count("(")
    close_brackets = eval_str.count(")")
    if open_brackets > close_brackets:
      eval_str += ")" * (open_brackets - close_brackets)

    res = eval(eval_str, {"__builtins__": {}}, allowed_names)

    if isinstance(res, float):
      res = round(res, 10)

    full_expr = raw_expr + " = " + str(res)
    st.session_state.last_expr = raw_expr + " ="
    st.session_state.result = str(res)
    st.session_state.history_log.append(full_expr)
    st.session_state.expression = str(res)
  except ZeroDivisionError:
    st.session_state.last_expr = st.session_state.expression + " ="
    st.session_state.result = "Math Error"
    st.session_state.expression = ""
  except ValueError:
    st.session_state.last_expr = st.session_state.expression + " ="
    st.session_state.result = "Math Error"
    st.session_state.expression = ""
  except Exception:
    st.session_state.last_expr = st.session_state.expression + " ="
    st.session_state.result = "Syntax Error"
    st.session_state.expression = ""


def handle_click(val):
  if val == "C":
    st.session_state.expression = ""
    st.session_state.last_expr = ""
    st.session_state.result = "0"
  elif val == "⌫":
    st.session_state.expression = st.session_state.expression[:-1]
  elif val == "=":
    evaluate_calc()
  elif val == "±":
    if st.session_state.expression.startswith("-"):
      st.session_state.expression = st.session_state.expression[1:]
    else:
      st.session_state.expression = "-" + st.session_state.expression
  else:
    if st.session_state.result in ["Math Error", "Syntax Error"]:
      st.session_state.expression = ""
      st.session_state.result = "0"
    st.session_state.expression += str(val)


# --- UI Layout ---
st.markdown(
    '<div class="app-header">✨ PRO SCIENTIFIC CALCULATOR</div>',
    unsafe_allow_html=True,
)

# Screen Display
history_display = (
    st.session_state.last_expr if st.session_state.last_expr else ""
)
main_display = (
    st.session_state.result
    if st.session_state.expression == ""
    else st.session_state.expression
)

st.markdown(
    f"""
    <div class="calc-screen">
        <div class="history-text">{history_display}</div>
        <div class="main-result">{main_display}</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Scientific Mode Panel
if mode == "Scientific":
  sc1, sc2, sc3, sc4 = st.columns(4)
  with sc1:
    if st.button("sin("):
      handle_click("sin(")
      st.rerun()
  with sc2:
    if st.button("cos("):
      handle_click("cos(")
      st.rerun()
  with sc3:
    if st.button("tan("):
      handle_click("tan(")
      st.rerun()
  with sc4:
    if st.button("sqrt("):
      handle_click("sqrt(")
      st.rerun()

  sc5, sc6, sc7, sc8 = st.columns(4)
  with sc5:
    if st.button("log("):
      handle_click("log(")
      st.rerun()
  with sc6:
    if st.button("ln("):
      handle_click("ln(")
      st.rerun()
  with sc7:
    if st.button("^"):
      handle_click("^")
      st.rerun()
  with sc8:
    if st.button("n!"):
      handle_click("factorial(")
      st.rerun()

  sc9, sc10, sc11, sc12 = st.columns(4)
  with sc9:
    if st.button("π"):
      handle_click("pi")
      st.rerun()
  with sc10:
    if st.button("e"):
      handle_click("e")
      st.rerun()
  with sc11:
    if st.button("("):
      handle_click("(")
      st.rerun()
  with sc12:
    if st.button(")"):
      handle_click(")")
      st.rerun()

# Main Calculator Button Grid
col1, col2, col3, col4 = st.columns(4)

# Row 1
with col1:
  if st.button("C"):
    handle_click("C")
    st.rerun()
with col2:
  if st.button("⌫"):
    handle_click("⌫")
    st.rerun()
with col3:
  if st.button("%"):
    handle_click("%")
    st.rerun()
with col4:
  if st.button("÷"):
    handle_click("÷")
    st.rerun()

# Row 2
with col1:
  if st.button("7"):
    handle_click("7")
    st.rerun()
with col2:
  if st.button("8"):
    handle_click("8")
    st.rerun()
with col3:
  if st.button("9"):
    handle_click("9")
    st.rerun()
with col4:
  if st.button("×"):
    handle_click("×")
    st.rerun()

# Row 3
with col1:
  if st.button("4"):
    handle_click("4")
    st.rerun()
with col2:
  if st.button("5"):
    handle_click("5")
    st.rerun()
with col3:
  if st.button("6"):
    handle_click("6")
    st.rerun()
with col4:
  if st.button("-"):
    handle_click("-")
    st.rerun()

# Row 4
with col1:
  if st.button("1"):
    handle_click("1")
    st.rerun()
with col2:
  if st.button("2"):
    handle_click("2")
    st.rerun()
with col3:
  if st.button("3"):
    handle_click("3")
    st.rerun()
with col4:
  if st.button("+"):
    handle_click("+")
    st.rerun()

# Row 5
with col1:
  if st.button("±"):
    handle_click("±")
    st.rerun()
with col2:
  if st.button("0"):
    handle_click("0")
    st.rerun()
with col3:
  if st.button("."):
    handle_click(".")
    st.rerun()
with col4:
  if st.button("="):
    evaluate_calc()
    st.rerun()