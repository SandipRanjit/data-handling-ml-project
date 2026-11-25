
import streamlit as st
import pandas as pd

from modules import utils
from modules import investment_score
from modules import styles
from modules import classical_ml

# Display the InvestIQ landing page before an analysis is performed
def render_home():
  brain_svg = utils.load_svg("brain-circuit.svg")
  chart_svg = utils.load_svg("chart-column.svg")
  shield_svg = utils.load_svg("shield-check.svg")
  sparkles_svg = utils.load_svg("sparkles.svg")
  chat_svg = utils.load_svg("message-square.svg")
  brain_img = utils.load_svg_as_image("brain-circuit.svg")

  st.html(
    f"""
      <div class="home-page">
        <div class="home-logo">
          <div class="home-logo-icon">
            <img src="{brain_img}" alt="brian">
          </div>
            <div class="home-logo-text">
              <div class="home-title">
                InvestIQ — AI Investment Research
              </div>
              <div class="home-subtitle">
                AI Investment Research Assistant
              </div>
            </div>
          </div>

          <div class="description-title">
              Analyze investments with an
            <span class="ai-gradient">AI analyst</span>
          </div>

          <div class="description">
            Describe your investment preferences in plain language.
            InvestIQ analyzes companies, identifies the strongest matches,
            and explains the reasoning behind each result.
          </div>
        </div>
    """
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
            <span class="feature-icon">{shield_svg}</span>
              Transparent Scoring
          </div>
        """,
        unsafe_allow_html=True
       )

  with f4:
    st.markdown(
        f"""
          <div class="feature">
            <span class="feature-icon">{sparkles_svg}</span>
              Visual Analytics
          </div>
        """,
        unsafe_allow_html=True
        )

  st.markdown("""<div class="preferences-separator"></div>""", unsafe_allow_html=True)

def render_navigation(best_company, companies_scanned):
  nav1, nav2, nav3, nav4 = st.columns([5, 6, 4, 5])

  with nav1:
    st.markdown(
        f"""
          <div class="status-badge">
            <span class="status-dot"></span>
              Top Ranked: {best_company["Ticker"]}
          </div>
        """,
        unsafe_allow_html=True
       )

  with nav3:
    risk_level = investment_score.get_risk_level(best_company["Historical Volatility"])

    st.markdown(
      f"""
        <div class="status-badge">
          <span class="status-dot"></span>
            {best_company["Ticker"]} Risk:
            &nbsp; {risk_level}
        </div>
      """,
      unsafe_allow_html=True
      )

  with nav4:
    st.markdown(
      f"""
        <div class="live-badge">
            ● &nbsp; {companies_scanned} companies screened
        </div>
      """,
      unsafe_allow_html=True
      )

# Display key performance indicators for the selected Top 5 companies
def render_kpis(top_5, best_company):
  """
    Identifies the company with the highest revenue growth, highest
    profit margin, lowest risk, highest historical return, and the
    top-ranked company.
    """
  highest_growth = top_5.loc[top_5["Revenue Growth"].idxmax()]

  highest_profit = top_5.loc[top_5["Net Profit Margin"].idxmax()]

  lowest_risk = top_5.loc[top_5["Historical Volatility"].idxmin()]

  highest_return = top_5.loc[top_5["Historical Return"].idxmax()]

  c1, c2, c3, c4, c5 = st.columns(5)

  with c1:
    st.markdown(
      f"""
        <div class="kpi-card">
          <div class="kpi-label">
                Highest Revenue Growth
          </div>
          <div class="kpi-value" style="color:#00D6FF;">
              {highest_growth["Revenue Growth"] * 100:.1f}%
          </div>
          <div class="kpi-description">
              {highest_growth["Company_Name"]}
          </div>
        </div>
      """,
      unsafe_allow_html=True
      )

  with c2:
    st.markdown(
      f"""
        <div class="kpi-card">
          <div class="kpi-label">
              Highest Profit Margin
          </div>
          <div class="kpi-value" style="color:#00FF88;">
              {highest_profit["Net Profit Margin"] * 100:.1f}%
          </div>
          <div class="kpi-description">
              {highest_profit["Company_Name"]}
          </div>
        </div>
      """,
      unsafe_allow_html=True
      )

  with c3:
    st.markdown(
      f"""
        <div class="kpi-card">
          <div class="kpi-label">
              Lowest Risk
          </div>
          <div class="kpi-value" style="color:#C96BFF;">
              {investment_score.get_risk_level(lowest_risk["Historical Volatility"])}
          </div>
          <div
              class="kpi-description"
              style="color:#A05ACB;"
          >
              {lowest_risk["Company_Name"]}
          </div>
        </div>
      """,
      unsafe_allow_html=True
      )

  with c4:
    st.markdown(
      f"""
        <div class="kpi-card">
          <div class="kpi-label">
              Highest Historical Return
          </div>
          <div class="kpi-value" style="color:#00FF88;">
              {highest_return["Historical Return"] * 100:.1f}%
          </div>
          <div class="kpi-description">
              {highest_return["Company_Name"]}
          </div>
        </div>
      """,
      unsafe_allow_html=True
      )

  with c5:
    st.markdown(
      f"""
        <div class="kpi-card">
          <div class="kpi-label">
              Top Ranked Company
          </div>
          <div class="kpi-value" style="color:#00FF88;">
              {best_company["Company_Name"]}
          </div>
          <div class="kpi-description">
              {best_company["Investment Score"]:.0f}/100
          </div>
        </div>
      """,
      unsafe_allow_html=True
      )

# Display the Top 5 companies and their main financial and ML metrics
def render_company_table(top_5):
  """
    Includes growth, profit margin, risk level, Investment Score, and
    the estimated probability of a positive 1-year return.
  """
  companies = top_5[
      [
          "Rank",
          "Company_Name",
          "Ticker",
          "Sector",
          "Revenue Growth",
          "Net Profit Margin",
          "Historical Volatility",
          "Investment Score",
          "Positive Return Probability"
      ]
  ].copy()

  companies = companies.rename(
      columns={
          "Company_Name":"Company",
          "Net Profit Margin":"Profit Margin",
          "Investment Score":"Score",
          "Positive Return Probability": "Positive 1-Year Return Probability"
      }
  )

  companies["Risk"] = companies["Historical Volatility"].apply(investment_score.get_risk_level)

  companies["Revenue Growth"] = (companies["Revenue Growth"]*100).round(1)

  companies["Profit Margin"] = (companies["Profit Margin"]*100).round(1)

  companies["Positive 1-Year Return Probability"] = (companies["Positive 1-Year Return Probability"] * 100).round(1)

  companies["Score"] = (companies["Score"].round().astype(int))

  companies = companies[
      [
          "Rank",
          "Company",
          "Ticker",
          "Sector",
          "Revenue Growth",
          "Profit Margin",
          "Risk",
          "Score",
          "Positive 1-Year Return Probability"
      ]
  ]

  styled_companies = (companies.style
      .map(styles.style_company, subset=["Company"])
      .map(styles.style_ticker, subset=["Ticker"])
      .map(styles.style_percentage, subset=["Revenue Growth", "Profit Margin", "Positive 1-Year Return Probability"])
      .map(styles.style_risk, subset=["Risk"])
      .map(styles.style_score, subset=["Score"])
      .format({"Revenue Growth": "{:.1f}%", "Profit Margin": "{:.1f}%", "Score": "{:.0f}", "Positive 1-Year Return Probability": "{:.1f}%"})
      )

  with st.container(border=True):
    st.subheader("Top Companies")

    st.caption(
      "Estimated probability of a positive 1-year return. "
      "This is a model estimate, not a guarantee of future performance."
    )

    st.dataframe(
      styled_companies,
      use_container_width=True,
      hide_index=True
    )

# Run the dashboard analysis using the user's selected preferences
def render_dashboard():
  """
    Calculates the Top 5 companies, obtains the classical ML probability
    for each company, stores the results in session state, and renders
    the dashboard components.
  """
  settings = st.session_state.analysis_settings

  top_5, companies_scanned = investment_score.get_top_5(
      sector=settings["sector"],
      risk=settings["risk"],
      goal=settings["goal"]
  )

  # Add classical ML prediction to the selected Top 5
  for index in top_5.index:
    company_row = top_5.loc[[index]]

    probability = classical_ml.predict_positive_return_probability(company_row)

    top_5.loc[index, "Positive Return Probability"] = probability

  best_company = top_5.iloc[0]

  st.session_state.top_5 = top_5
  st.session_state.best_company = best_company

  render_navigation(best_company, companies_scanned)

  render_kpis(top_5, best_company)

  render_company_table(top_5)
