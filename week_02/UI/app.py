import streamlit as st

st.set_page_config(
    page_title="Global Investment Dashboard",
    layout="wide"
)

#CSS
st.markdown("""
<style>

.stApp {
    background: #030616;
    color: #A0A8B9;
}

.block-container {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    padding-top: 4rem;
    max-width: 100%;
}

[data-testid="stSidebar"] {
    background: #030616;
}

.sidebar-brand {
    color: #00D6FF;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 4px;
}

.sidebar-title {
    color: #FFFFFF;
    font-size: 24px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 32px;
}

.sidebar-section-title {
    color: #64748B;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 14px;
}

.sidebar-value {
    color: #00D6FF;
    font-size: 14px;
    font-weight: 700;
    margin-top: -8px;
    margin-bottom: 22px;
}

.purple-label {
    color: #A05ACB;
    font-size: 14px;
    margin-bottom: -5px;
}

[data-testid="stSidebar"] .stButton > button {
    height: 54px;

    background: linear-gradient(
        to bottom,
        #A05ACB,
        #D96EFF
    );

    color: #FFFFFF;
    border: none;
    border-radius: 8px;

    font-size: 16px;
    font-weight: 700;

    transition: all 0.25s ease;

    margin-top: 5px;
    margin-bottom: 20px;
}

[data-testid="stSidebar"] .stButton > button:hover {
    border-color: #D96EFF;
    box-shadow:
        0 0 8px #A05ACB,
        0 0 20px #D96EFF;

    transform: translateY(-2px);
}

.home-page {
    padding: 20px;
    padding-top: 50px;
}

.home-logo {
    display: flex;
    align-items: center;
    gap: 22px;
    margin-bottom: 48px;
}

.home-logo-icon {
    width: 96px;
    height: 96px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 24px;

    background: linear-gradient(
        135deg,
        #28B9D6,
        #7B4BE8
    );

    color: white;
    font-size: 52px;
}

.home-logo-icon svg {
    width: 55px;
    height: 55px;
}

.home-logo-text {
    display: flex;
    flex-direction: column;
}

.home-title {
    color: #F1F5F9;
    font-size: 40px;
    font-weight: 700;
    line-height: 1;
}

.home-subtitle {
    color: #94A3B8;
    font-size: 20px;
    margin-top: 10px;
}

.description-title {
    max-width: 900px;

    color: #F1F5F9;

    font-size: 50px;
    font-weight: 750;

    line-height: 1.25;

    margin-bottom: 25px;
}

.description-title::after {
    content: "";
}

.ai-gradient {
    background: linear-gradient(
        90deg,
        #00D6FF,
        #A05ACB
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.description {
    max-width: 850px;

    color: #94A3B8;

    font-size: 27px;
    line-height: 1.6;

    margin-bottom: 45px;
}

.feature {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 100%;
    box-sizing: border-box;

    padding: 12px 22px;

    border: 2px solid #202938;
    border-radius: 35px;

    background: rgba(8, 17, 35, 0.65);

    color: #CBD5E1;

    font-size: 21px;
    font-weight: 600;

    white-space: nowrap;

    transition: all 0.2s ease;
}

.feature:hover {
    border-color: #00D6FF;

    box-shadow:
        0 0 8px rgba(0, 214, 255, 0.4),
        0 0 20px rgba(0, 214, 255, 0.15);

    transform: translateY(-2px);
}

.feature-icon {
    color: #00D6FF;
    font-size: 25px;
    margin-right: 10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            AI FDI ADVISOR
        </div>

        <div class="sidebar-title">
            Global Investment Dashboard
        </div>

        <div class="sidebar-section-title">
            INVESTMENT PREFERENCES
        </div>
        """,
        unsafe_allow_html=True
    )

    investment = st.number_input(
        "Investment Amount ($)",
        value=1_000_000
    )

    st.markdown(
        f"""
        <div class="sidebar-value">
            ${investment / 1_000_000:.1f}M
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="purple-label">Investment Horizon</div>',
        unsafe_allow_html=True
    )

    horizon = st.slider(
        "Investment Horizon",
        1,
        10,
        5
    )

    sector = st.selectbox(
        "Investment Sector",
        [
            "All",
            "Technology",
            "Healthcare",
            "Energy",
            "Finance"
        ]
    )

    risk = st.selectbox(
        "Risk Tolerance",
        [
            "Low",
            "Moderate",
            "High"
        ]
    )

    goal = st.selectbox(
        "Investment Goal",
        [
            "Balanced Return and Risk",
            "Long Term Stability",
            "Maximum Growth",
            "Fast Investment Recovery",
            "High Profitability"
        ]
    )

    st.button("Analyze Investments", use_container_width=True)

#Home screen

with open("assets/brain-circuit.svg", "r") as f:
    brain_svg = f.read()
with open("assets/chart-column.svg", "r") as f:
    chart_svg = f.read()
with open("assets/shield-check.svg", "r") as f:
    sheild_svg = f.read()
with open("assets/sparkles.svg", "r") as f:
    sparkes_svg = f.read()
with open("assets/message-square.svg", "r") as f:
    chat_svg = f.read()

st.markdown(
    f"""
    <div class="home-page">
        <div class="home-logo">
            <div class="home-logo-icon">
                {brain_svg}
            </div>
            <div class="home-logo-text">
                <div class="home-title">
                    Global Investment Dashboard
                </div>
                <div class="home-subtitle">
                    AI Investment Analyst
                </div>
            </div>
        </div>
        <div class="description-title">
            Analyze investments with an
            <span class="ai-gradient">AI analyst</span>
        </div>
        <div class="description">
            Describe your investment preferences in plain language.
            InvestIQ scores the available companies, ranks the top
            candidates, and explains the reasoning — all on one screen.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown(
        f"""
        <div class="feature">
            <span class="feature-icon">{chat_svg}</span>
            Conversational AI
        </div>
        """,
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        f"""
        <div class="feature">
            <span class="feature-icon">{chart_svg}</span>
            Smart Ranking
        </div>
        """,
        unsafe_allow_html=True
    )

with f3:
    st.markdown(
        f"""
        <div class="feature">
            <span class="feature-icon">{sheild_svg}</span>
            Transparent Scoring
        </div>
        """,
        unsafe_allow_html=True
    )

with f4:
    st.markdown(
        f"""
        <div class="feature">
            <span class="feature-icon">{sparkes_svg}</span>
            Visual Analytics
        </div>
        """,
        unsafe_allow_html=True
    )
