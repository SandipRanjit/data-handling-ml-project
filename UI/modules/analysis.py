
import streamlit as st
import plotly.graph_objects as go

from modules import utils

# Display the selected company's Investment Score
def render_investment_score(best_company):
  """
    The score is divided into four components:
    profitability, historical growth, financial stability, and historical return.
  """
  left, right = st.columns([1, 1])

  bars = [
      ("Profitability", 30, round(best_company["Profitability Score"]), utils.GREEN),
      ("Historical Growth", 25, round(best_company["Historical Growth Score"]), utils.BLUE),
      ("Financial Stability", 25, round(best_company["Financial Stability Score"]), utils.BLUE_PURPLE),
      ("Historical Return", 20, round(best_company["Historical Return Score"]), utils.YELLOW)
  ]

  with left:
    with st.container(border=True):
      st.markdown(
        """
          <p style="color:#FFFFFF; font-size:14px; font-weight:700;">
              INVESTMENT SCORE
          </p>
        """,
        unsafe_allow_html=True
    )

      st.html(
        f"""
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:25px;">
            <div style="color:{utils.BLUE}; font-size:30px; font-weight:700;">
                {best_company["Company_Name"]}
            </div>

            <div style="color:#FFFFFF; font-size:30px; font-weight:700;">
                {best_company["Investment Score"]:.0f}
                  <span style="color:#526784; font-size:24px;">
                    /100
                  </span>
            </div>
          </div>
        """
      )

      for title, maximum, value, color in bars:
        percentage = (value / maximum) * 100

        st.html(
          f"""
            <div style="margin-bottom:12px;">
                <div style="display:flex; justify-content:space-between; color:#64748B; font-size:14px; margin-bottom:6px;">
                    <span>{title}</span>
                    <span>{value}/{maximum}</span>
                </div>

                <div style="width:100%; height:5px; background:#202938; border-radius:10px;">
                    <div style="width:{percentage}%; height:5px; background:{color}; border-radius:10px;"></div>
                </div>
            </div>
          """
        )

  with right:
    with st.container(border=True):
        st.html(
          f"""
            <div class="recommendation-card">
               <div class="recommendation-title">
                  TOP RANKED
                </div>

                <div class="recommendation-company">
                    {best_company["Company_Name"]}
                </div>

                <div class="recommendation-sector">
                    {best_company["Sector"]} · {best_company["Ticker"]}
                </div>

                <div class="recommendation-score">
                    Investment  Score: {best_company["Investment Score"]:.0f}/100
                </div>

                <div class="why-title">
                    Ranking Summary
                </div>

                <div class="recommendation-text">
                    This company has the highest ranking score among
                    the companies screened for your selected investment
                    preferences. Its Investment Score is
                    {best_company["Investment Score"]:.0f}/100,
                    while its Preference Score reflects the selected
                    investment goal and risk tolerance.
                </div>
            </div>
          """
        )

# Show an illustrative investment scenario using historical returns
def render_historical_return_illustration(investment, top_5_companies):
  """
    The calculation applies each company's historical return to the
    selected investment amount. It is an illustration based on past
    performance, not a forecast or guarantee of future returns.
  """
  illustration = top_5_companies.copy()

  illustration["Illustrative Investment Value"] = (investment * (1 + illustration["Historical Return"]))

  illustration["Illustrative Gain"] = (illustration["Illustrative Investment Value"] - investment)

  with st.container(border=True):
    st.markdown(
      """
        <div style="color:#A0A8B9; font-size:14px; font-weight:600; margin-bottom:14px;">
            HISTORICAL RETURN ILLUSTRATION
        </div>
      """,
      unsafe_allow_html=True
    )

    highest_company = illustration.loc[illustration["Illustrative Investment Value"].idxmax()]

    col1, col2, col3, col4 = st.columns(4)

    card_style = """
      <div style="
          border:1px solid #293241;
          border-radius:6px;
          padding:10px 12px;
          min-height:60px;
          background-color:#11151D;
          box-sizing:border-box;
      ">

          <div style="
              color:#64748B;
              font-size:11px;
              font-weight:500;
              margin-bottom:5px;
              line-height:1.2;
          ">
              {title}
          </div>

          <div style="color:#FFFFFF; font-size:17px; font-weight:600; line-height:1.2;">
              {value}
          </div>
        </div>
      """

    initial_investment = investment / 1_000_000

    illustrative_value = (highest_company["Illustrative Investment Value"]/ 1_000_000)

    illustrative_gain = (highest_company["Illustrative Gain"]/ 1_000_000)

    historical_return = (highest_company["Historical Return"] * 100)

    with col1:
        st.html(card_style.format(title="INITIAL INVESTMENT", value=f"${initial_investment:.2f}M"))

    with col2:
        st.html(card_style.format(title="HIGHEST HISTORICAL RETURN", value=highest_company["Company_Name"]))

    with col3:
        st.html(card_style.format(title="ILLUSTRATIVE VALUE AFTER 1 YEAR", value=f"${illustrative_value:.2f}M"))

    with col4:
        st.html(card_style.format(title="ILLUSTRATIVE GAIN", value=f"${illustrative_gain:.2f}M"))

    st.caption(
      f"""
        Illustration based on the selected companies' historical returns.
        For {highest_company["Company_Name"]}, the historical return used
        in this calculation was {historical_return:.1f}%. This is not a
        forecast or guarantee of future performance.
      """
    )

    st.markdown(
        "<div style='height:20px;'></div>",
        unsafe_allow_html=True
    )

    fig = go.Figure()

    colors = [
        utils.BLUE,
        utils.BLUE_PURPLE,
        utils.PURPLE,
        utils.GREEN,
        utils.YELLOW
    ]

    max_value = (illustration["Illustrative Investment Value"].max() / 1_000_000) * 1.15

    for i, row in illustration.iterrows():
        color = colors[i % len(colors)]

        illustrative_value_m = (row["Illustrative Investment Value"] / 1_000_000)

        fig.add_trace(
            go.Bar(
                x=[row["Company_Name"]],
                y=[illustrative_value_m],
                name=row["Company_Name"],

                marker=dict(color=color, line=dict(width=0)),

                text=[f"${illustrative_value_m:.2f}M"],

                textposition="outside"
            )
        )

    fig.update_layout(
        height=300,
        margin=dict(l=55, r=20, t=20, b=60),
        bargap=0.45,
        yaxis=dict(
          range=[0, max_value],
          gridcolor="#293241",
          gridwidth=1,
          zeroline=False,
          showline=False,

          tickformat=",.0f",
          ticksuffix="M",

          tickfont=dict(
              color="#64748B",
              size=11
          )
        ),

        xaxis=dict(
          showgrid=False,
          zeroline=False,

          tickfont=dict(color="#64748B", size=12)
        ),

        legend=dict(
          orientation="h",
          yanchor="bottom",
          y=-0.32,
          xanchor="left",
          x=0,
          bgcolor="rgba(0,0,0,0)",

          font=dict(size=12)
        ),

        showlegend=False
      )

    st.plotly_chart(
      fig,
      use_container_width=True,
      config={"displayModeBar": False}
     )

# Render the complete analysis section
def render_analysis():
    """
      Displays the Investment Score, the factual ranking explanation,
      and the historical-return investment illustration.
    """

    settings = st.session_state.analysis_settings
    top_5 = (st.session_state.top_5)
    best_company = (st.session_state.best_company)
    investment = settings["investment"]

    render_investment_score(best_company)

    render_historical_return_illustration(investment, top_5)
