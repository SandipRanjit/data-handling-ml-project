import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

.horizon-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: -5px;
    margin-bottom: 18px;
    color: #64748B;
    font-size: 13px;
}

.horizon-row strong {
    color: #FFFF00;
    font-size: 18px;
    font-weight: 500;
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
    box-shadow:
        0 0 3px #FFFFFF,
        0 0 8px #D96EFF,
        0 0 15px #D96EFF,
        0 0 30px #A05ACB,
        0 0 50px rgba(160, 90, 203, 0.6);

    transform: translateY(-1px);
}

.sidebar-mini-cards {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 0;
    margin-bottom: 35px;
}

.mini-card {
    width: 90px;
    height: 66px;

    border-radius: 7px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;

    font-size: 11px;
    font-weight: 600;
}

.mini-card strong {
    font-size: 17px;
    margin-top: 4px;
}

.cyan-card {
    color: #00D6FF;
    background: #062A2D;
    border: 1px solid #00D6FF;
}

.purple-card {
    color: #A05ACB;
    background: #241633;
    border: 1px solid #A05ACB;
}

.chat-title {
    color: #64748B;
    font-size: 14px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 12px;
}

.chat-user {
    background: #442080;
    border-radius: 9px;
    padding: 16px 14px 10px 14px;
    margin-bottom: 14px;
    color: #D9B8FF;
}

.chat-ai {
    background: #07383A;
    border: 1px solid #00D6FF;
    border-radius: 9px;
    padding: 16px 14px 10px 14px;
    margin-bottom: 14px;
    color: #00D6FF;
}

.chat-message {
    font-size: 14px;
    line-height: 1.4;
}

.chat-time {
    text-align: right;
    font-size: 11px;
    margin-top: 8px;
    opacity: 0.75;
}

.chat-user .chat-time {
    color: #C56BFF;
}

.chat-ai .chat-time {
    color: #00D6FF;
}

[data-testid="stChatInput"] button {
    background: linear-gradient(
        to bottom,
        #A05ACB,
        #D96EFF
    ) !important;
    border-radius: 7px !important;
}

.top-nav {
    display: flex;
    align-items: center;
    gap: 40px;
    height: 55px;
    border-bottom: 1px solid #202938;
    margin-bottom: 30px;
}

.nav-active {
    color: #00D6FF;
    font-size: 15px;
    font-weight: 600;
    padding: 18px 25px 14px 25px;
    border-bottom: 3px solid #00D6FF;
    white-space: nowrap;
    text-align: center;
}

.nav-item {
    color: #64748B;
    font-size: 15px;
    padding: 18px 0;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    padding: 7px 15px;
    border: 1px solid #00D6FF;
    border-radius: 8px;
    color: #00D6FF;
    font-size: 14px;
    font-weight: 600;
    background: #06242A;
}

.status-dot {
    width: 10px;
    height: 10px;
    background: #00E5A0;
    border-radius: 50%;
}

.live-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 15px;
    border: 1px solid #4B607C;
    border-radius: 8px;
    color: #64748B;
    font-size: 14px;
    background: #111D2A;
}

.stButton > button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 15px;
    color: white;
    background: linear-gradient(
        to bottom,
        #A05ACB,
        #D96EFF
    );

    border: none;
    border-radius: 8px;
}

.stButton > button:hover {
    box-shadow:
        0 0 5px #A05ACB,
        0 0 15px #00D6FF,
        0 0 30px rgba(0, 214, 255, 0.5);

    transform: translateY(-1px);
}

.kpi-card {
    background: #11151D;
    width: 100%;
    min-height: 105px;
    padding: 16px;
    box-sizing: border-box;
    border: 1px solid #293241;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 20px;
    margin-bottom: 20px;
}

.kpi-label {
    color: #64748B;
    font-size: 12px;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 22px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 5px;
    overflow-wrap: break-word;
}

.kpi-description {
    color: #64748B;
    font-size: 11px;
    line-height: 1.3;
    overflow-wrap: break-word;
}

.score-title {
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 18px;
}

.score-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}

.company-name {
    color: #00D6FF;
    font-size: 30px;
    font-weight: 700;
}

.score-number {
    color: #FFFFFF;
    font-size: 30px;
    font-weight: 700;
}

.score-number small {
    color: #526784;
    font-size: 24px;
    font-weight: 700;
}

.score-row {
    margin-bottom: 13px;
}

.score-label-row {
    display: flex;
    justify-content: space-between;
    align-items: center;

    color: #64748B;
    font-size: 14px;
    font-weight: 500;

    margin-bottom: 6px;
}

.progress-background {
    width: 100%;
    height: 5px;

    background: #202938;

    border-radius: 10px;

    overflow: hidden;
}

.progress-fill {
    height: 5px;
    border-radius: 10px;
}

.recommendation-card {
    min-height: 418px;
}

.recommendation-title {
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 18px;
}

.recommendation-company {
    color: #D9B8FF;
    font-size: 30px;
    font-weight: 700;
    line-height: 1;
}

.recommendation-sector {
    color: #64748B;
    font-size: 14px;
    margin-top: 3px;
}

.recommendation-score {
    color: #00D6FF;
    font-size: 14px;
    font-weight: 600;
    margin-top: 5px;
}

.why-title {
    color: #A0A8B9;
    font-size: 14px;
    font-weight: 700;
    margin-top: 17px;
    margin-bottom: 17px;
}

.recommendation-text {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
    line-height: 1.45;
}

.strengths-card {
    min-height: 125px;
}

.strengths-title {
    color: #6FCF97;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 12px;
}

.strength-item {
    color: #D1D5DB;
    font-size: 14px;
    margin-bottom: 8px;
}

.risks-card {
    min-height: 125px;
}

.risks-title {
    color: #FFFF00;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 12px;
}

.risk-item {
    color: #D1D5DB;
    font-size: 14px;
    margin-bottom: 8px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 8px;
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
        5,
        label_visibility="collapsed"
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

    # small kpi cards
    st.html(
        """
        <div class="sidebar-mini-cards">

            <div class="mini-card cyan-card">
                <div>IRR EST.</div>
                <strong>18.4%</strong>
            </div>

            <div class="mini-card purple-card">
                <div>RISK<br>SCORE</div>
                <strong>B+</strong>
            </div>

            <div class="mini-card cyan-card">
                <div>MARKETS</div>
                <strong>12</strong>
            </div>

        </div>
        """
    )

    # Ai Assistant
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "user",
                "message": "Which EU countries offer the best tax subsidies for green energy projects over 5 years?",
                "time": "14:32"
            },
            {
                "role": "assistant",
                "message": "Based on your €10M capital and 5-year horizon targeting EU Green Energy, France and Ireland rank highest. Ireland offers a 12.5% corporate rate + 25% R&D credits; France provides €20M+ solar relief under the Green Deal framework.",
                "time": "14:32"
            }
        ]


    st.markdown(
        """
        <div class="chat-title">
            AI ADVISOR CHAT
        </div>
        """,
        unsafe_allow_html=True
    )

    for chat in st.session_state.chat_messages:

        if chat["role"] == "user":

            st.html(
                f"""
                <div class="chat-user">
                    <div class="chat-message">
                        {chat["message"]}
                    </div>

                    <div class="chat-time">
                        You · {chat["time"]}
                    </div>
                </div>
                """
        )

        else:
            st.html(
                f"""
                <div class="chat-ai">
                    <div class="chat-message">
                        {chat["message"]}
                    </div>

                    <div class="chat-time">
                        FDI Advisor · {chat["time"]}
                    </div>
                </div>
                """
            )

    prompt = st.chat_input(
        "Can you break down Ireland's tax incentives further?"
    )


    if prompt:
        st.session_state.chat_messages.append(
            {
                "role": "user",
                "message": prompt,
                "time": "14:35"
            }
        )

    # Temporary response

        response = (
            "I can provide a detailed breakdown of Ireland's "
            "tax incentives, including corporate tax, R&D credits "
            "and renewable energy incentives."
        )

        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "message": response,
                "time": "14:35"
            }
        )

        st.rerun()

# Top navigation
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Analysis"

nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(
    [2, 2, 2, 2, 4, 2]
)

with nav1:
    st.markdown(
        '<div class="nav-active">Analysis</div>',
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        '<div class="nav-item">Document Sources (RAG)</div>',
        unsafe_allow_html=True
    )

with nav3:
    st.markdown(
        '<div class="nav-item">Yield Models (NN)</div>',
        unsafe_allow_html=True
    )

with nav5:
    st.markdown(
        """
        <div class="status-badge">
            <span class="status-dot"></span>
            Sovereign Risk: &nbsp; Low Risk (84/100)
        </div>
        """,
        unsafe_allow_html=True
    )

with nav6:
    st.markdown(
        """
        <div class="live-badge">
            ● &nbsp; Live · 12 sources
        </div>
        """,
        unsafe_allow_html=True
    )

# kpi cards
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Highest Revenue Growth</div>
        <div class="kpi-value" style="color:#00D6FF;">34.7%</div>
        <div class="kpi-description">Ireland baseline</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Highest Profit Margin</div>
        <div class="kpi-value" style="color:#00FF88;">24.1%</div>
        <div class="kpi-description">Across EU portfolio</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Lowest Risk</div>
        <div class="kpi-value" style="color:#C96BFF;">LOW</div>
        <div class="kpi-description" style="color:#A05ACB;">Company B</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Highest 5-Year Return</div>
        <div class="kpi-value" style="color:#00FF88;">32.7%</div>
        <div class="kpi-description">Ireland baseline</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Best Overall</div>
        <div class="kpi-value" style="color:#00FF88;">Company A</div>
        <div class="kpi-description">84/100</div>
    </div>
    """, unsafe_allow_html=True)

    # top companies table
    companies = pd.DataFrame({

    "Rank":[1,2,3,4,5],

    "Company":[
        "Company A",
        "Company B",
        "Company C",
        "Company D",
        "Company E"
    ],

    "Sector":[
        "Technology",
        "Energy",
        "Finance",
        "Healthcare",
        "Technology"
    ],

    "Revenue Growth":[34.7,22.8,20.5,18.1,17.9],

    "Profit Margin":[24.1,18.3,16.7,14.9,14.4],

    "Score":[84,79,74,71,68]

})
with st.container(border=True):
    st.subheader("Top Companies")

    st.dataframe(
        companies,
        use_container_width=True,
        hide_index=True
    )

# revenue growth
GREEN = "#6FCF97"
PURPLE = "#A05ACB"
BLUE = "#00D6FF"
YELLOW = "#f7ce46"
BLUE_PURPLE = "#7B7EDB"

years=["Year 1","Year 2","Year 3","Year 4","Year 5"]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=years,
        y=[70,82,95,88,94],
        mode="lines+markers",
        name="Company A",
        line=dict(color=BLUE),
        marker=dict(color=BLUE),
    )
)

fig.add_trace(
    go.Scatter(
        x=years,
        y=[48,57,63,65,68],
        mode="lines+markers",
        name="Company B",
        line=dict(color=BLUE_PURPLE),
        marker=dict(color=BLUE_PURPLE),
    )
)

fig.add_trace(
    go.Scatter(
        x=years,
        y=[60,56,60,65,72],
        mode="lines+markers",
        name="Company C",
        line=dict(color=PURPLE),
        marker=dict(color=PURPLE),
    )
)

fig.add_trace(
    go.Scatter(
        x=years,
        y=[40,23,50,47,40],
        mode="lines+markers",
        name="Company D",
        line=dict(color=GREEN),
        marker=dict(color=GREEN),
    )
)

fig.add_trace(
    go.Scatter(
        x=years,
        y=[50,52,60,61,65],
        mode="lines+markers",
        name="Company E",
        line=dict(color=YELLOW),
        marker=dict(color=YELLOW),
    )
)

fig.update_layout(
    template="plotly_dark",
    title=dict(
        text=(
            "<b>5-Year Revenue Growth</b>"
            "<br>"
            "<span style='font-size:12px; color:#64748B;'>"
            "Projected returns by target market · $10M capital deployed"
            "</span>"
        ),
        x=0.025,
        xanchor="left",
        y=0.95,
        yanchor="top",
        font=dict(
            size=14,
            color="#A0A8B9"
        )
    ),
    height=380,
    margin=dict(
        l=55,
        r=20,
        t=75,
        b=80
    ),
    yaxis=dict(
        range=[0, 120],
        tickvals=[0, 30, 60, 90, 120],
        gridcolor="#293241",
        zeroline=False,
        showline=False,
        tickfont=dict(
            color="#64748B",
            size=11
        )
    ),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        tickfont=dict(
            color="#64748B",
            size=12
        )
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="left",
        x=0,
        font=dict(
            size=12
        ),
        bgcolor="rgba(0,0,0,0)"
    ),
    hovermode="x unified"
)

with st.container(border=True):
    st.plotly_chart(fig, use_container_width=True)

# investment score
left,right = st.columns([1,1])

bars = [
  ("Profitability", 25, 25, GREEN),
  ("Historical Growth", 20, 14, BLUE),
  ("Financial Stability", 20, 16, BLUE_PURPLE),
  ("Future Growth", 20, 19, PURPLE),
  ("Historical Return", 15, 12, YELLOW),
]

with left:
    with st.container(border=True):
        st.markdown(
            "<p style='color:#FFFFFF; font-size:14px; font-weight:700;'>"
            "INVESTMENT SCORE"
            "</p>",
            unsafe_allow_html=True
        )

        st.html(
            f"""
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                margin-bottom:25px;
            ">

                <div style="
                    color:{BLUE};
                    font-size:30px;
                    font-weight:700;
                ">
                    COMPANY A
                </div>

                <div style="
                    color:#FFFFFF;
                    font-size:30px;
                    font-weight:700;
                ">
                    84<span style="
                        color:#526784;
                        font-size:24px;
                    ">/100</span>
                </div>

            </div>
            """
        )

        for title, maximum, value, color in bars:

            percentage = (value / maximum) * 100

            st.html(
                f"""
                <div style="margin-bottom:12px;">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        color:#64748B;
                        font-size:14px;
                        margin-bottom:6px;
                    ">
                        <span>{title}</span>
                        <span>{value}/{maximum}</span>
                    </div>

                    <div style="
                        width:100%;
                        height:5px;
                        background:#202938;
                        border-radius:10px;
                    ">
                        <div style="
                            width:{percentage}%;
                            height:5px;
                            background:{color};
                            border-radius:10px;
                        "></div>
                    </div>

                </div>
                """
            )

# Recommendation
with right:
  with st.container(border=True):
    st.html(
            """
            <div class="recommendation-card">

                <div class="recommendation-title">
                    AI RECOMMENDATION
                </div>

                <div class="recommendation-company">
                    COMPANY A
                </div>

                <div class="recommendation-sector">
                    Technology · USA
                </div>

                <div class="recommendation-score">
                    Investment score: 84/100
                </div>

                <div class="why-title">
                    Why was it selected?
                </div>

                <div class="recommendation-text">
                    Company A ranks highest because it combines strong
                    profitability, consistent historical growth, a healthy
                    financial position and competitive projected growth.
                    Although another company may show a higher historical
                    return, Company A offers a stronger overall balance
                    between return and risk for your selected profile.
                </div>

            </div>
            """
        )

# strengths risks
c1,c2 = st.columns(2)


with c1:
    with st.container(border=True):
        st.html(
            f"""
            <div class="strengths-card">

                <div class="strengths-title">
                    STRENGTHS
                </div>

                <div class="strength-item">
                    Strong revenue growth
                </div>

                <div class="strength-item">
                    High profit margin
                </div>

                <div class="strength-item">
                    Consistent historical performance
                </div>

            </div>
            """
        )

with c2:
    with st.container(border=True):
        st.html(
            f"""
            <div class="risks-card">

                <div class="risks-title">
                    RISKS
                </div>

                <div class="risk-item">
                    Market volatility
                </div>

                <div class="risk-item">
                    Industry competition
                </div>

                <div class="risk-item">
                    Future growth uncertainty
                </div>

            </div>
            """
        )

# projection
projection = pd.DataFrame({

    "Year":[
        "Year 1",
        "Year 2",
        "Year 3",
        "Year 4",
        "Year 5"
    ],

    "Value":[
        1.0,
        1.15,
        1.38,
        1.62,
        1.82
    ]

})

with st.container(border=True):

    st.markdown(
        """
        <div style="
            color: #A0A8B9;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 14px;
        ">
            Investment Recovery Projection
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    card_style = """
    <div style="
        border: 1px solid #293241;
        border-radius: 6px;
        padding: 10px 12px;
        min-height: 60px;
        background-color: #11151D;
        box-sizing: border-box;
    ">
        <div style="
            color: #64748B;
            font-size: 11px;
            font-weight: 500;
            margin-bottom: 5px;
            line-height: 1.2;
        ">
            {title}
        </div>

        <div style="
            color: #FFFFFF;
            font-size: 17px;
            font-weight: 600;
            line-height: 1.2;
        ">
            {value}
        </div>
    </div>
    """

    with col1:
        st.html(
            card_style.format(
                title="INITIAL INVESTMENT",
                value="$1.00M"
            )
        )

    with col2:
        st.html(
            card_style.format(
                title="ESTIMATED ANNUAL RETURN",
                value="12.5%"
            )
        )

    with col3:
        st.html(
            card_style.format(
                title="ESTIMATED RECOVERY PERIOD",
                value="5.9 years"
            )
        )

    with col4:
        st.html(
            card_style.format(
                title="VALUE AT HORIZON",
                value="$1.80M"
            )
        )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    fig = go.Figure()

    colors = [
        BLUE,
        BLUE_PURPLE,
        PURPLE,
        GREEN,
        YELLOW
    ]

    for i, row in projection.iterrows():

        fig.add_trace(
            go.Bar(
                x=[row["Year"]],
                y=[row["Value"]],
                name=row["Year"],
                marker=dict(
                    color=colors[i],
                    line=dict(width=0)
                ),
                text=[f"{row['Value']:.2f}M"],
                textposition="outside"
            )
        )


    fig.update_layout(
        height=300,
        margin=dict(
            l=55,
            r=20,
            t=20,
            b=60
        ),
        bargap=0.45,
        yaxis=dict(
            range=[0, 2.0],
            tickvals=[
                0,
                0.5,
                1.0,
                1.5,
                2.0
            ],
            ticktext=[
                "0.0M",
                "0.5M",
                "1.0M",
                "1.5M",
                "2.0M"
            ],
            gridcolor="#293241",
            gridwidth=1,
            zeroline=False,
            showline=False,
            tickfont=dict(
                color="#64748B",
                size=11
            )
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                color="#64748B",
                size=12
            )
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.32,
            xanchor="left",
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(
                size=12
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )