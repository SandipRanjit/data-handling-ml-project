
import streamlit as st

from modules import styles
from modules import preferences
from modules import chat
from modules import dashboard
from modules import analysis

st.set_page_config(
    page_title="InvestIQ",
    layout="wide",
    initial_sidebar_state="expanded"
)

chat.initialize_chat()
styles.apply_styles()

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

if "analysis_settings" not in st.session_state:
    st.session_state.analysis_settings = None

if "top_5" not in st.session_state:
    st.session_state.top_5 = None

if "best_company" not in st.session_state:
    st.session_state.best_company = None

with st.sidebar:
  st.markdown(
      """
      <div class="workspace-subtitle">
          Ask questions about companies, financial information,
          risk, and investments.
      </div>
      """,
      unsafe_allow_html=True
  )

  chat.render_chat()

# preferences.render_preferences()

if st.session_state.analyzed:
    preferences.render_preferences()
    dashboard.render_dashboard()
    analysis.render_analysis()

else:
    dashboard.render_home()
    preferences.render_preferences()
