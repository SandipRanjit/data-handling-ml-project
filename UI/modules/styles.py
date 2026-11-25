
import streamlit as st

def apply_styles():
    st.markdown("""
    <style>

    /* global */

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


    /* sidebar */

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
        color: #9bb7de;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .sidebar-value {
        color: #00D6FF;
        font-size: 14px;
        font-weight: 700;
        margin-top: -8px;
        margin-bottom: 22px;
    }

    .stNumberInput input:focus {
        border-color: #00D6FF !important;
        box-shadow: 0 0 0 1px #00D6FF !important;
    }

    [data-baseweb="select"]:focus-within {
        border-color: #00D6FF !important;
        box-shadow: 0 0 0 1px #00D6FF !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        height: 54px;
        background: linear-gradient(
            to bottom,
            #A05ACB,
            #D96EFF
        );

        color: #081c38;
        border: none;
        border-radius: 8px;
        font-size: 20px;
        font-weight: 900;
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

    /* chat section */

    .chat-card {
        background: #ffffff;
        border: 1px solid #434445;
        border-radius: 22px;
        padding: 28px;
        margin-bottom: 30px;
    }

    .chat-title {
        color: #F1F5F9;
        font-size: 20px;
        font-weight: 800;
    }

    .chat-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .chat-badge {
        color: #B86CFF;
        border: 1px solid #66358A;
        background: rgba(168, 85, 247, 0.08);
        border-radius: 20px;
        padding: 7px 13px;
        display: flex;
        gap: 8px;
        font-size: 13px;
        font-weight: 600;
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

    .chat-messages {
        height: 230px;
        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 8px;
        margin-bottom: 15px;
    }

    .chat-message {
        display: flex;
        gap: 12px;
        margin-bottom: 15px;
        overflow: hidden;
    }

    .chat-icon {
        min-width: 34px;
        height: 34px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        color: #B86CFF;
        border: 1px solid #66358A;
        background: rgba(168, 85, 247, 0.08);
    }

    .chat-bubble {
        background: #090F19;
        border: 1px solid #243148;
        border-radius: 14px;

        padding: 14px 17px;

        color: #E2E8F0;
        font-size: 15px;
        line-height: 1.65;

        max-width: 90%;
        overflow-wrap: anywhere;
        word-break: break-word;
        white-space: normal;
        box-sizing: border-box;
    }

    .user-message {
        display: flex;
        justify-content: flex-end;
        gap: 12px;
        margin-bottom: 15px;
    }

    .user-icon {
        min-width: 34px;
        height: 34px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        color: #7B7EDB;
        border: 1px solid #7B7EDB;
        background: rgba(168, 85, 247, 0.08);
    }

    .user-bubble {
        background: #16263A;
        border: 1px solid #24425C;

        border-radius: 14px;

        padding: 14px 17px;

        color: #E2E8F0;

       max-width: 75%;
    }

    .chat-user .chat-time {
        color: #C56BFF;
    }

    .chat-ai .chat-time {
        color: #00D6FF;
    }

    .chat-icon img {
        width: 20px;
        height: 20px;
        display: block;
    }

    .user-icon svg {
        width: 18px;
        height: 18px;
    }

    [data-testid="stChatInput"] button {
        background: linear-gradient(
            to bottom,
            #A05ACB,
            #D96EFF
        ) !important;

        border-radius: 7px !important;
    }

    /* home page */

    .home-page {
        padding: 10px;
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

    .home-logo-icon img {
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
        margin: 5px;
    }

    .description-title {
        max-width: 900px;
        color: #F1F5F9;
        font-size: 50px;
        font-weight: 750;
        line-height: 1.25;
        margin-bottom: 15px;
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
        font-size: 20px;
        line-height: 1.5;
        margin-bottom: 16px;
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
        font-size: 16px;
        font-weight: 500;
        white-space: nowrap;
        transition: all 0.2s ease;
        margin-bottom: 4px;
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

    .preferences-separator {
        width: 100%;
        height: 1px;
        background: #87818a;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .preferences-card-title {
      color: #9bb1de;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      margin-bottom: 18px;
    }

    /* Preference labels */
    .preferences-card ~ div label {
        color: #64748B !important;
        font-size: 11px !important;
        font-weight: 600 !important;
    }

    /* Preference controls */
    .preferences-card ~ div [data-baseweb="select"] {
        margin-top: 3px;
    }

    /* Number input */
    .preferences-card ~ div input {
        font-size: 13px !important;
    }

    /* Analyze button */
    .preferences-card ~ div .stButton {
        display: flex;
        justify-content: flex-end;
    }

    .preferences-card ~ div .stButton > button {
        width: auto;
        min-width: 180px;
        padding: 8px 18px;
        margin: 6px;
    }

    .analyze-button-wrapper .stButton > button {
        color: #081c38;
        font-size: 18px;
        font-weight: 900;
    }

    /* analytics page */

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
        margin-top: 25px;

        border: 2px solid #00D6FF;
        border-radius: 8px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #00D6FF;
        box-shadow: 0 0 10px #00D6FF;
        transform: translateY(-1px);
    }

    .stButton > button p {
        font-size: 16px !important;
        font-weight: 800 !important;
        color: #EAFBFF !important;
    }

    .kpi-card {
        background: #11151D;
        width: 100%;
        min-height: 88px;
        padding: 12px;
        box-sizing: border-box;
        border: 1px solid #293241;
        border-radius: 8px;
        overflow: hidden;
        margin-top: 12px;
        margin-bottom: 12px;
    }

    .kpi-label {
        color: #64748B;
        font-size: 11px;
        font-weight: 600;
        line-height: 1.2;
        margin-bottom: 6px;
    }

    .kpi-value {
        font-size: 20px;
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 4px;
        overflow-wrap: break-word;
    }

    .kpi-description {
        color: #64748B;
        font-size: 10px;
        line-height: 1.2;
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
        min-height: 358px;
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

    [data-testid="stBaseButton-secondaryFormSubmit"] {
        flex-shrink: 0 !important;
    }


    /* Laptop sidebar responsiveness */

    @media (max-height: 850px), (max-width: 1400px) {

        .chat-messages {
            height: 150px;
        }

        [data-testid="stBaseButton-secondaryFormSubmit"] {
            min-width: 42px !important;
            width: 42px !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)

def style_company(value):
    return """
        font-weight: 700;
    """


def style_ticker(value):
    return """
        color: #00D6FF;
        font-weight: 600;
    """


def style_percentage(value):

    if value >= 20:
        return """
            color: #6FCF97;
            font-weight: 600;
        """

    elif value >= 10:
        return """
            color: #F7CE46;
            font-weight: 600;
        """

    else:
        return """
            color: #FF6B6B;
            font-weight: 600;
        """


def style_score(value):

    if value >= 75:
        return """
            color: #6FCF97;
            font-weight: 700;
        """

    elif value >= 60:
        return """
            color: #F7CE46;
            font-weight: 700;
        """

    else:
        return """
            color: #FF6B6B;
            font-weight: 700;
        """


def style_risk(value):

    if value == "Low":
        return """
            color: #6FCF97;
            font-weight: 600;
        """

    elif value == "Medium":
        return """
            color: #F7CE46;
            font-weight: 600;
        """

    else:
        return """
            color: #FF6B6B;
            font-weight: 600;
        """
