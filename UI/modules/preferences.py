
import streamlit as st

def render_preferences():
  with st.container(border=True):
      st.markdown(
          """
          <div class="preferences-card">
              <div class="sidebar-title">
                  Analyze Investments
              </div>
          </div>
          """,
          unsafe_allow_html=True
      )

      amount_column, sector_column, risk_column = st.columns(3)

      with amount_column:
          investment = st.number_input(
              "Investment Amount ($)",
              value=1_000_000
          )

      with sector_column:
          sector = st.selectbox(
              "Investment Sector",
              [
                  "All",
                  "Technology",
                  "Healthcare",
                  "Energy",
                  "Finance",
                  "Consumer",
                  "Industrials",
                  "Communication",
                  "Utilities",
                  "Real Estate"
              ]
          )

      with risk_column:
          risk = st.selectbox(
              "Risk Tolerance",
              [
                  "Low",
                  "Moderate",
                  "High"
              ]
          )

      goal_column, button_column = st.columns([1, 1])

      with goal_column:
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

      with button_column:
        analyze = st.button("Analyze Investments", use_container_width=True)

      if analyze:
          st.session_state.analyzed = True

          st.session_state.analysis_settings = {
              "investment": investment,
              "sector": sector,
              "risk": risk,
              "goal": goal
          }

          st.rerun()
