import streamlit as st
import pandas as pd
import html
from datetime import date, datetime

# ============================================================
# VEHICLE FINANCE PRO ULTRA
# Cars • Three Wheelers • Bikes
# Customer-ready leasing + loan calculator
# ============================================================

st.set_page_config(
    page_title="Vehicle Finance Pro",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# THEME / PREMIUM RESPONSIVE UI
# -----------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root{
    --navy:#07111f; --navy2:#102b45; --green:#10b981; --green2:#087748;
    --blue:#2563eb; --ink:#101828; --muted:#667085; --line:#e4e7ec;
    --bg:#f4f7fa; --white:#fff; --orange:#f79009; --red:#d92d20;
}

html, body, [class*="css"]{font-family:Inter,system-ui,sans-serif;}
.stApp{
    background:
      radial-gradient(850px 450px at -5% -5%,rgba(16,185,129,.13),transparent 60%),
      radial-gradient(750px 430px at 105% 0%,rgba(37,99,235,.10),transparent 62%),
      #f4f7fa;
}
.block-container{max-width:1220px;padding:1.1rem 1rem 3rem;}

.hero{
    position:relative;overflow:hidden;color:#fff;padding:30px;border-radius:30px;
    background:linear-gradient(135deg,#050d18,#0c243a 55%,#0d4937);
    box-shadow:0 24px 60px rgba(7,17,31,.18);margin-bottom:16px;
}
.hero:after{
    content:"";position:absolute;width:420px;height:420px;border-radius:50%;
    right:-220px;top:-250px;background:radial-gradient(circle,#25e59a40,transparent 68%);
}
.hero-content{position:relative;z-index:2;}
.brand{display:flex;align-items:center;gap:15px;}
.logo{
    width:64px;height:64px;border-radius:20px;display:grid;place-items:center;
    font-size:31px;background:linear-gradient(145deg,#24df91,#087b4b);
    border:1px solid #ffffff2b;box-shadow:0 12px 28px #0006;
}
.hero h1{margin:0;font-size:31px;font-weight:900;letter-spacing:-1px;}
.hero p{margin:5px 0 0;color:#c9d8e4;font-size:12px;}
.badges{display:flex;flex-wrap:wrap;gap:7px;margin-top:17px;}
.badge{
    padding:7px 10px;border-radius:999px;background:#ffffff12;border:1px solid #ffffff20;
    font-size:9px;font-weight:800;color:#f6fbff;
}

.card{
    background:rgba(255,255,255,.94);border:1px solid #e8edf2;border-radius:22px;
    padding:20px;box-shadow:0 14px 38px rgba(7,17,31,.07);margin-bottom:14px;
}
.section-title{font-size:18px;font-weight:900;color:var(--ink);margin:0;}
.section-sub{font-size:10px;color:var(--muted);margin:4px 0 15px;}
.pill{
    display:inline-flex;padding:7px 10px;border-radius:999px;background:var(--navy);
    color:#fff;font-size:8px;font-weight:900;letter-spacing:.4px;
}

.vehicle-grid{
    display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:4px;
}
.vehicle-card{
    border:1px solid #dfe5eb;border-radius:17px;padding:15px;background:#fff;
    cursor:pointer;transition:.18s;
}
.vehicle-card:hover{transform:translateY(-2px);box-shadow:0 10px 24px #07111f12;}
.vehicle-icon{font-size:26px;}
.vehicle-name{font-weight:900;font-size:13px;margin-top:6px;color:#101828;}
.vehicle-desc{font-size:9px;color:#667085;margin-top:3px;}

.metric{
    padding:16px;border:1px solid var(--line);border-radius:17px;background:#fafbfc;
}
.metric-label{font-size:8px;font-weight:900;color:#667085;letter-spacing:.4px;}
.metric-value{font-size:18px;font-weight:900;color:#101828;margin-top:5px;}
.metric-help{font-size:8px;color:#98a2b3;margin-top:3px;}

.finance{
    padding:21px;border-radius:22px;border:1px solid #dfe5eb;background:#fff;
    height:100%;box-shadow:0 10px 28px rgba(7,17,31,.05);
}
.finance.lease{background:linear-gradient(145deg,#effcf6,#fff 70%);border-color:#bce9d2;}
.finance.loan{background:linear-gradient(145deg,#f1f5ff,#fff 70%);border-color:#d3dfff;}
.finance-title{font-size:18px;font-weight:900;color:#101828;}
.emi{font-size:31px;font-weight:950;letter-spacing:-.8px;color:#101828;margin:7px 0 2px;}
.finance-sub{font-size:9px;color:#667085;font-weight:700;}
.row{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-bottom:1px solid #0000000c;font-size:10px;}
.row:last-child{border:0}.row span{color:#667085}.row b{color:#101828;text-align:right;}

.total{
    padding:25px;border-radius:24px;text-align:center;color:#fff;
    background:linear-gradient(135deg,#050d18,#173752 60%,#104633);
    box-shadow:0 18px 42px rgba(7,17,31,.15);margin:14px 0;
}
.total small{font-size:9px;color:#c5d3df;font-weight:900;letter-spacing:.5px;}
.total strong{display:block;font-size:38px;line-height:1.15;margin:5px 0;word-break:break-word;}
.total div{font-size:10px;color:#cbd7e0;}

.offer{
    padding:22px;border-radius:22px;color:#fff;
    background:linear-gradient(135deg,#06101e,#0d2a42 58%,#104633);
    box-shadow:0 18px 42px rgba(7,17,31,.13);
}
.offer h2{margin:0;font-size:23px;font-weight:950;}
.offer p{margin:4px 0 14px;color:#c6d5df;font-size:10px;}
.offer-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;}
.offer-item{padding:11px;border-radius:14px;background:#ffffff0b;border:1px solid #ffffff14;}
.offer-item small{display:block;color:#b8c6d2;font-size:7px;font-weight:900;}
.offer-item b{display:block;margin-top:4px;font-size:13px;word-break:break-word;}

.warning{padding:12px 14px;border-radius:14px;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;font-size:10px;font-weight:700;}
.success{padding:12px 14px;border-radius:14px;background:#ecfdf3;border:1px solid #b7ebcf;color:#087748;font-size:10px;font-weight:800;}

.quote{
    padding:23px;border-radius:23px;color:#fff;background:linear-gradient(135deg,#06101e,#12354f);
}
.quote h2{margin:0;font-size:21px;font-weight:950;}
.quote .muted{color:#bfd0dc;font-size:9px;margin-top:4px;}
.quote-line{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #ffffff12;font-size:10px;}
.quote-total{margin-top:13px;padding:15px;border-radius:16px;background:#ffffff0b;text-align:center;}
.quote-total small{color:#c0ced9;font-size:8px;font-weight:900}.quote-total b{display:block;font-size:25px;margin-top:4px;}

.table-wrap{width:100%;overflow-x:auto;border:1px solid #e1e6eb;border-radius:17px;background:#fff;}
table{width:100%;border-collapse:collapse;min-width:650px;}
th{background:#07111f;color:#fff;padding:10px;font-size:9px;text-align:right;white-space:nowrap;}
th:first-child{text-align:center}
td{padding:9px;font-size:9px;text-align:right;border-bottom:1px solid #e8ebef;white-space:nowrap;}
td:first-child{text-align:center;font-weight:800;background:#f8fafc;}

.stApp label,.stApp [data-testid="stWidgetLabel"] *{color:#344054!important;}
.stApp input,.stApp textarea,.stApp [data-baseweb="select"]>div,.stApp [data-testid="stNumberInput"]>div{
    background:#fff!important;color:#101828!important;-webkit-text-fill-color:#101828!important;
    border-color:#d0d5dd!important;
}
.stApp input::placeholder{color:#98a2b3!important;}
.stButton button,.stDownloadButton button{border-radius:13px!important;min-height:45px;}
.stButton button[kind="primary"],.stDownloadButton button{
    background:#07111f!important;color:#fff!important;-webkit-text-fill-color:#fff!important;
}
.stTabs [data-baseweb="tab"]{font-size:10px;font-weight:800;}

@media(max-width:800px){
    .block-container{padding:8px 10px 25px;}
    .hero{padding:20px;border-radius:22px;}
    .hero h1{font-size:24px}.logo{width:53px;height:53px;font-size:26px}
    .vehicle-grid{grid-template-columns:1fr 1fr;}
    .offer-grid{grid-template-columns:1fr 1fr;}
    .finance{margin-bottom:10px}.emi{font-size:28px}
    .total strong{font-size:29px}
    .stButton,.stDownloadButton{width:100%!important;margin:3px 0;}
    .stButton button,.stDownloadButton button{width:100%!important;}
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# HELPERS
# -----------------------------
def money(v):
    return "රු. " + format(float(v or 0), ",.2f")

def pct(v):
    return f"{float(v):.2f}%"

def emi(principal, annual_rate, years):
    principal = float(principal or 0)
    months = int(round(float(years or 0) * 12))
    if principal <= 0 or months <= 0:
        return 0.0
    r = float(annual_rate) / 100 / 12
    if r == 0:
        return principal / months
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)

def amortization(principal, annual_rate, years):
    principal = float(principal or 0)
    months = int(round(float(years or 0) * 12))
    payment = emi(principal, annual_rate, years)
    r = float(annual_rate) / 100 / 12
    rows, balance = [], principal
    for m in range(1, months + 1):
        opening = balance
        interest = opening * r
        principal_paid = max(0.0, payment - interest)
        if m == months:
            principal_paid = opening
            actual_payment = opening + interest
            closing = 0.0
        else:
            actual_payment = payment
            closing = max(0.0, opening - principal_paid)
        rows.append({
            "Month": m, "Opening Balance": opening,
            "Monthly Payment": actual_payment, "Principal": principal_paid,
            "Interest": interest, "Closing Balance": closing
        })
        balance = closing
    return pd.DataFrame(rows)

def calculate(price, down, insurance, years, lease_rate, loan_rate,
              max_finance_pct, lease_split_pct, doc_charge, commission_pct):
    price, down = float(price), float(down)
    base_finance = max(0.0, price - down)
    max_finance = price * max_finance_pct / 100
    lease_base = min(base_finance, price * lease_split_pct / 100)
    loan_base = max(0.0, base_finance - lease_base)
    commission = price * commission_pct / 100
    lease_amount = lease_base + doc_charge + commission + insurance
    loan_years = max(1, int(years) - 1)
    lease_emi = emi(lease_amount, lease_rate, years)
    loan_emi = emi(loan_base, loan_rate, loan_years)
    return {
        "price": price, "down": down, "insurance": insurance, "years": int(years),
        "base_finance": base_finance, "max_finance": max_finance,
        "finance_percent": (base_finance / price * 100) if price else 0,
        "lease_base": lease_base, "loan_base": loan_base,
        "doc_charge": doc_charge, "commission": commission,
        "lease_amount": lease_amount, "loan_years": loan_years,
        "lease_rate": lease_rate, "loan_rate": loan_rate,
        "lease_emi": lease_emi, "loan_emi": loan_emi,
        "total_emi": lease_emi + loan_emi,
        "lease_schedule": amortization(lease_amount, lease_rate, years),
        "loan_schedule": amortization(loan_base, loan_rate, loan_years),
    }

def display_table(df):
    x = df.copy()
    for c in x.columns:
        if c != "Month":
            x[c] = x[c].map(money)
    heads = "".join(f"<th>{html.escape(str(c))}</th>" for c in x.columns)
    body = ""
    for _, row in x.iterrows():
        body += "<tr>" + "".join(f"<td>{html.escape(str(v))}</td>" for v in row.tolist()) + "</tr>"
    st.markdown(f'<div class="table-wrap"><table><thead><tr>{heads}</tr></thead><tbody>{body}</tbody></table></div>', unsafe_allow_html=True)

def quote_id():
    return "VFP-" + datetime.now().strftime("%y%m%d-%H%M%S")

# -----------------------------
# SESSION STATE
# -----------------------------
defaults = {
    "result": None, "quote_id": quote_id(),
    "customer_name": "", "phone": "", "vehicle_model": "", "reference": ""
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="hero">
  <div class="hero-content">
    <div class="brand">
      <div class="logo">🚘</div>
      <div>
        <h1>Vehicle Finance Pro</h1>
        <p>Professional leasing & loan calculator for Cars, Three Wheelers & Bikes</p>
      </div>
    </div>
    <div class="badges">
      <span class="badge">🚘 CARS</span>
      <span class="badge">🛺 THREE WHEELERS</span>
      <span class="badge">🏍️ BIKES</span>
      <span class="badge">⚙️ CUSTOM RATES</span>
      <span class="badge">📊 REDUCING BALANCE</span>
      <span class="badge">📱 MOBILE READY</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# VEHICLE TYPE
# -----------------------------
st.markdown("""
<div class="card">
  <h2 class="section-title">🚗 Select Vehicle Category</h2>
  <p class="section-sub">Choose the vehicle type first. You can then enter your own finance rates and limits.</p>
  <div class="vehicle-grid">
    <div class="vehicle-card"><div class="vehicle-icon">🚘</div><div class="vehicle-name">Car</div><div class="vehicle-desc">Cars / SUVs / vans</div></div>
    <div class="vehicle-card"><div class="vehicle-icon">🛺</div><div class="vehicle-name">Three Wheeler</div><div class="vehicle-desc">Passenger / commercial</div></div>
    <div class="vehicle-card"><div class="vehicle-icon">🏍️</div><div class="vehicle-name">Motorcycle</div><div class="vehicle-desc">Bikes / scooters</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

vehicle = st.selectbox(
    "VEHICLE CATEGORY",
    ["🚘 Car", "🛺 Three Wheeler", "🏍️ Motorcycle"],
    label_visibility="collapsed"
)

vehicle_defaults = {
    "🚘 Car": {"max": 70.0, "lease": 50.0, "lease_rate": 24.0, "loan_rate": 26.0, "years": 5, "doc": 9500.0, "commission": 3.0},
    "🛺 Three Wheeler": {"max": 70.0, "lease": 50.0, "lease_rate": 25.0, "loan_rate": 27.0, "years": 5, "doc": 9500.0, "commission": 3.0},
    "🏍️ Motorcycle": {"max": 60.0, "lease": 40.0, "lease_rate": 26.0, "loan_rate": 28.0, "years": 4, "doc": 9500.0, "commission": 3.0},
}
cfg = vehicle_defaults[vehicle]

# -----------------------------
# CUSTOMER
# -----------------------------
with st.expander("👤 Customer & Quotation Details", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.session_state.customer_name = st.text_input("CUSTOMER NAME", st.session_state.customer_name, placeholder="Customer name")
    with c2:
        st.session_state.phone = st.text_input("CONTACT NUMBER", st.session_state.phone, placeholder="07XXXXXXXX")
    with c3:
        st.session_state.vehicle_model = st.text_input("VEHICLE / MODEL", st.session_state.vehicle_model, placeholder="e.g. Toyota Aqua / Bajaj RE")
    with c4:
        st.session_state.reference = st.text_input("REFERENCE", st.session_state.reference, placeholder="Optional")
    st.caption(f"Quotation ID: {st.session_state.quote_id}  •  Date: {date.today().strftime('%d/%m/%Y')}")

# -----------------------------
# MAIN INPUTS
# -----------------------------
st.markdown("""
<div class="card">
  <h2 class="section-title">💰 Finance Inputs</h2>
  <p class="section-sub">Enter the agreed vehicle price, down payment, insurance and period.</p>
</div>
""", unsafe_allow_html=True)

a, b, c = st.columns(3)
with a:
    price = st.number_input("VEHICLE VALUE (රු.)", min_value=0.0, value=2_000_000.0 if "Car" in vehicle else 1_000_000.0, step=10_000.0, format="%.2f")
    down = st.number_input("DOWN PAYMENT (රු.)", min_value=0.0, value=800_000.0 if "Car" in vehicle else 400_000.0, step=10_000.0, format="%.2f")
with b:
    insurance = st.number_input("INSURANCE (රු.)", min_value=0.0, value=0.0, step=1_000.0, format="%.2f")
    years = st.selectbox("FINANCE PERIOD", [2, 3, 4, 5, 6, 7], index=[2,3,4,5,6,7].index(cfg["years"]) if cfg["years"] in [2,3,4,5,6,7] else 3, format_func=lambda x: f"{x} YEARS")
with c:
    st.markdown('<div class="metric"><div class="metric-label">SELECTED VEHICLE</div><div class="metric-value">' + html.escape(vehicle) + '</div><div class="metric-help">Finance settings can be customized below.</div></div>', unsafe_allow_html=True)
    if price > 0:
        st.markdown(f'<div class="success">Suggested minimum down payment at {100-cfg["max"]:.0f}%: <b>{money(price*(1-cfg["max"]/100))}</b></div>', unsafe_allow_html=True)

# -----------------------------
# CUSTOM RATE / POLICY CONTROL
# -----------------------------
with st.expander("⚙️ Advanced Finance Settings — Enter ANY Rate You Need", expanded=True):
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        lease_rate = st.number_input("LEASE RATE (% p.a.)", min_value=0.0, max_value=100.0, value=float(cfg["lease_rate"]), step=0.25, format="%.2f")
        loan_rate = st.number_input("LOAN RATE (% p.a.)", min_value=0.0, max_value=100.0, value=float(cfg["loan_rate"]), step=0.25, format="%.2f")
    with r2:
        max_finance_pct = st.number_input("MAX FINANCE (%)", min_value=1.0, max_value=100.0, value=float(cfg["max"]), step=1.0, format="%.1f")
        lease_split_pct = st.number_input("LEASE PORTION (%)", min_value=0.0, max_value=100.0, value=float(cfg["lease"]), step=1.0, format="%.1f")
    with r3:
        doc_charge = st.number_input("DOCUMENT CHARGE (රු.)", min_value=0.0, value=float(cfg["doc"]), step=500.0, format="%.2f")
        commission_pct = st.number_input("COMMISSION (%)", min_value=0.0, max_value=30.0, value=float(cfg["commission"]), step=0.25, format="%.2f")
    with r4:
        rate_type = st.selectbox("INTEREST METHOD", ["Reducing Balance", "Flat Rate"])
        st.info("Current EMI engine uses reducing-balance monthly EMI. Flat-rate is shown as a selection for future policy expansion.")

st.markdown(f"""
<div class="card">
  <div class="metric-label">ACTIVE FINANCE SETTINGS</div>
  <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;">
    <span class="pill">LEASE {lease_rate:.2f}%</span>
    <span class="pill">LOAN {loan_rate:.2f}%</span>
    <span class="pill">MAX {max_finance_pct:.0f}%</span>
    <span class="pill">LEASE PORTION {lease_split_pct:.0f}%</span>
    <span class="pill">COMMISSION {commission_pct:.2f}%</span>
    <span class="pill">METHOD {html.escape(rate_type.upper())}</span>
  </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# ACTIONS
# -----------------------------
x, y = st.columns([4, 1])
with x:
    calculate_clicked = st.button("🧮 CALCULATE COMPLETE FINANCE PLAN", type="primary", use_container_width=True)
with y:
    reset_clicked = st.button("↻ RESET", use_container_width=True)

if reset_clicked:
    for k in ["result"]:
        st.session_state[k] = None
    st.session_state.quote_id = quote_id()
    st.rerun()

if calculate_clicked:
    error = None
    if price <= 0:
        error = "Vehicle value එක 0 ට වඩා වැඩි විය යුතුයි."
    elif down < 0 or down >= price:
        error = "Down payment එක vehicle value එකට වඩා අඩු විය යුතුයි."
    elif lease_split_pct > max_finance_pct:
        error = "Lease portion (%) එක maximum finance (%) එකට වඩා වැඩි කරන්න බැහැ."
    if error:
        st.error(error)
    else:
        result = calculate(
            price, down, insurance, years, lease_rate, loan_rate,
            max_finance_pct, lease_split_pct, doc_charge, commission_pct
        )
        if result["base_finance"] > result["max_finance"] + 0.01:
            st.error(
                f"Maximum base finance is {max_finance_pct:.1f}% of vehicle value. "
                f"Required minimum down payment: {money(price-result['max_finance'])}"
            )
        else:
            st.session_state.result = result
            st.session_state.quote_id = quote_id()
            st.success("Finance plan calculated successfully.")

# -----------------------------
# RESULTS
# -----------------------------
d = st.session_state.result

if d:
    st.markdown('<div class="card"><h2 class="section-title">📊 Finance Summary</h2><p class="section-sub">Professional calculation overview for internal use and customer presentation.</p></div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    for col, label, value, helptext in [
        (m1, "VEHICLE VALUE", money(d["price"]), "Agreed value"),
        (m2, "DOWN PAYMENT", money(d["down"]), f"Finance {d['finance_percent']:.1f}%"),
        (m3, "TOTAL MONTHLY", money(d["total_emi"]), "Lease + loan"),
        (m4, "PERIOD", f"{d['years']} Years", f"Loan: {d['loan_years']} years"),
    ]:
        with col:
            st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-help">{helptext}</div></div>', unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        st.markdown(f"""
        <div class="finance lease">
          <div class="finance-title">🟢 Lease Component</div>
          <div class="emi">{money(d["lease_emi"])}</div>
          <div class="finance-sub">MONTHLY LEASE EMI • {d["lease_rate"]:.2f}% p.a. • REDUCING BALANCE</div>
          <div class="row"><span>Lease Base</span><b>{money(d["lease_base"])}</b></div>
          <div class="row"><span>Document Charge</span><b>{money(d["doc_charge"])}</b></div>
          <div class="row"><span>Commission</span><b>{money(d["commission"])}</b></div>
          <div class="row"><span>Insurance</span><b>{money(d["insurance"])}</b></div>
          <div class="row"><span>Total Lease Amount</span><b>{money(d["lease_amount"])}</b></div>
          <div class="row"><span>Period</span><b>{d["years"]*12} months</b></div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown(f"""
        <div class="finance loan">
          <div class="finance-title">🔵 Loan Component</div>
          <div class="emi">{money(d["loan_emi"])}</div>
          <div class="finance-sub">MONTHLY LOAN EMI • {d["loan_rate"]:.2f}% p.a. • REDUCING BALANCE</div>
          <div class="row"><span>Loan Principal</span><b>{money(d["loan_base"])}</b></div>
          <div class="row"><span>Interest Rate</span><b>{d["loan_rate"]:.2f}% p.a.</b></div>
          <div class="row"><span>Period</span><b>{d["loan_years"]*12} months</b></div>
          <div class="row"><span>Payment Method</span><b>Reducing Balance</b></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="total">
      <small>CUSTOMER TOTAL MONTHLY PAYMENT</small>
      <strong>{money(d["total_emi"])}</strong>
      <div>Lease {money(d["lease_emi"])} + Loan {money(d["loan_emi"])} / month</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="offer">
      <h2>✨ Customer Finance Offer</h2>
      <p>{html.escape(vehicle)} • {html.escape(st.session_state.vehicle_model or "Selected Vehicle")} • Personalized monthly plan</p>
      <div class="offer-grid">
        <div class="offer-item"><small>VEHICLE VALUE</small><b>{money(d["price"])}</b></div>
        <div class="offer-item"><small>DOWN PAYMENT</small><b>{money(d["down"])}</b></div>
        <div class="offer-item"><small>MONTHLY PAYMENT</small><b>{money(d["total_emi"])}</b></div>
        <div class="offer-item"><small>TERM</small><b>{d["years"]} Years</b></div>
        <div class="offer-item"><small>FINANCE</small><b>{d["finance_percent"]:.1f}%</b></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # PAYMENT SCHEDULES
    # -------------------------
    st.write("")
    lt, lo, co = st.tabs(["📄 LEASE PLAN", "💰 LOAN PLAN", "📊 COMBINED PLAN"])

    with lt:
        st.dataframe(d["lease_schedule"].style.format({
            "Opening Balance":"{:,.2f}", "Monthly Payment":"{:,.2f}",
            "Principal":"{:,.2f}", "Interest":"{:,.2f}", "Closing Balance":"{:,.2f}"
        }), use_container_width=True, hide_index=True)
        st.download_button("⬇️ Download Lease CSV", d["lease_schedule"].to_csv(index=False).encode("utf-8-sig"),
                           file_name=f"{st.session_state.quote_id}_lease.csv", mime="text/csv", use_container_width=True)

    with lo:
        st.dataframe(d["loan_schedule"].style.format({
            "Opening Balance":"{:,.2f}", "Monthly Payment":"{:,.2f}",
            "Principal":"{:,.2f}", "Interest":"{:,.2f}", "Closing Balance":"{:,.2f}"
        }), use_container_width=True, hide_index=True)
        st.download_button("⬇️ Download Loan CSV", d["loan_schedule"].to_csv(index=False).encode("utf-8-sig"),
                           file_name=f"{st.session_state.quote_id}_loan.csv", mime="text/csv", use_container_width=True)

    with co:
        n = max(len(d["lease_schedule"]), len(d["loan_schedule"]))
        combined = []
        for i in range(n):
            lp = float(d["lease_schedule"].iloc[i]["Monthly Payment"]) if i < len(d["lease_schedule"]) else 0
            op = float(d["loan_schedule"].iloc[i]["Monthly Payment"]) if i < len(d["loan_schedule"]) else 0
            combined.append({"Month":i+1, "Lease Payment":lp, "Loan Payment":op, "Total Monthly Payment":lp+op})
        combined_df = pd.DataFrame(combined)
        display_table(combined_df)
        st.download_button("⬇️ Download Combined CSV", combined_df.to_csv(index=False).encode("utf-8-sig"),
                           file_name=f"{st.session_state.quote_id}_combined.csv", mime="text/csv", use_container_width=True)

    # -------------------------
    # CUSTOMER QUOTE
    # -------------------------
    st.write("")
    st.markdown(f"""
    <div class="quote">
      <h2>👤 Customer Quotation</h2>
      <div class="muted">{html.escape(st.session_state.customer_name or "Valued Customer")} • {html.escape(st.session_state.vehicle_model or vehicle)} • {st.session_state.quote_id}</div>
      <div style="margin-top:14px">
        <div class="quote-line"><span>Vehicle Category</span><b>{html.escape(vehicle)}</b></div>
        <div class="quote-line"><span>Vehicle Value</span><b>{money(d["price"])}</b></div>
        <div class="quote-line"><span>Down Payment</span><b>{money(d["down"])}</b></div>
        <div class="quote-line"><span>Lease Rate</span><b>{d["lease_rate"]:.2f}% p.a.</b></div>
        <div class="quote-line"><span>Loan Rate</span><b>{d["loan_rate"]:.2f}% p.a.</b></div>
        <div class="quote-line"><span>Finance Period</span><b>{d["years"]} years</b></div>
      </div>
      <div class="quote-total"><small>ESTIMATED TOTAL MONTHLY PAYMENT</small><b>{money(d["total_emi"])}</b></div>
    </div>
    """, unsafe_allow_html=True)

    quote_text = (
        "VEHICLE FINANCE QUOTATION\n"
        f"Quotation ID: {st.session_state.quote_id}\n"
        f"Customer: {st.session_state.customer_name or 'Valued Customer'}\n"
        f"Vehicle: {vehicle} / {st.session_state.vehicle_model or 'Selected Vehicle'}\n"
        f"Vehicle Value: {money(d['price'])}\n"
        f"Down Payment: {money(d['down'])}\n"
        f"Lease Rate: {d['lease_rate']:.2f}% p.a.\n"
        f"Loan Rate: {d['loan_rate']:.2f}% p.a.\n"
        f"Total Monthly Payment: {money(d['total_emi'])}\n"
        f"Finance Period: {d['years']} years\n"
        "Note: Estimated quotation. Final approval and official charges are subject to company policy.\n"
    )
    st.download_button("📄 Download Customer Quotation", quote_text.encode("utf-8-sig"),
                       file_name=f"{st.session_state.quote_id}_quotation.txt", mime="text/plain", use_container_width=True)

    st.markdown("""
    <div class="warning">
      <b>Important:</b> This calculator is an estimate. Final approval, rates, charges,
      insurance conditions and company terms must be confirmed before issuing a binding quotation.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="text-align:center;color:#7b8794;font-size:9px;padding:20px 0 4px;">Vehicle Finance Pro Ultra • Cars • Three Wheelers • Motorcycles • Custom Rates • Responsive Customer Finance Tool</div>', unsafe_allow_html=True)
