
import pandas as pd
import numpy as np

dataset = "/content/drive/MyDrive/data_handling_and_machine_learning/datasets/merged_dataset/merged_dataset.csv"
company_info_file = "/content/drive/MyDrive/data_handling_and_machine_learning/week_03/outputs/olga_companies_info.csv"

# missing values give a neutral score
def normalize_score(series):
    scores = series.rank(pct=True, method="average") * 100

    return scores.fillna(50)

def calculate_profitability(df):

    net_margin = normalize_score(df["Net Profit Margin"])
    operating_margin = normalize_score(df["Operating Profit Margin"])
    fcf_margin = normalize_score(df["FCF Margin"])
    raw_score = (
        net_margin * 0.40
        + operating_margin * 0.30
        + fcf_margin * 0.30
    )
    df["Profitability Score"] = (raw_score * 0.30)

    return df

def calculate_historical_growth(df):

    revenue_growth = normalize_score(df["Revenue Growth"])
    net_income_growth = normalize_score(df["Net Income Growth"])
    operating_income_growth = normalize_score(df["Operating Income Growth"])
    asset_growth = normalize_score(df["Asset Growth"])
    raw_score = (
        revenue_growth * 0.40
        + net_income_growth * 0.30
        + operating_income_growth * 0.20
        + asset_growth * 0.10
    )
    df["Historical Growth Score"] = (raw_score * 0.25)

    return df

def calculate_financial_stability(df):

    current_ratio = normalize_score(df["Current Ratio"])
    debt = 100 - normalize_score(df["Debt-to-Equity"])
    free_cash_flow = normalize_score(df["Free Cash Flow"])
    equity = normalize_score(df["Total Equity"])
    raw_score = (
        current_ratio * 0.25
        + debt * 0.30
        + free_cash_flow * 0.25
        + equity * 0.20
    )
    df["Financial Stability Score"] = (
        raw_score * 0.25
    )

    return df

def calculate_historical_return(df):

    historical_return = normalize_score(df["Historical Return"])
    low_volatility = (100 - normalize_score(df["Historical Volatility"]))
    raw_score = (historical_return * 0.70 + low_volatility * 0.30)
    df["Historical Return Score"] = (raw_score * 0.20)

    return df

def calculate_investment_score(df):

    df = df.copy()
    df = calculate_profitability(df)
    df = calculate_historical_growth(df)
    df = calculate_financial_stability(df)
    df = calculate_historical_return(df)

    df["Investment Score"] = (
        df["Profitability Score"]
        + df["Historical Growth Score"]
        + df["Financial Stability Score"]
        + df["Historical Return Score"]
    )

    return df

def get_risk_level(volatility):

    if pd.isna(volatility):
        return "Medium"
    if volatility <= 0.20:
        return "Low"
    elif volatility <= 0.35:
        return "Medium"
    else:
        return "High"

def load_company_data():

    financials = pd.read_csv(dataset)
    company_info = pd.read_csv(company_info_file)

    df = financials.merge(
        company_info[
            [
                "Ticker",
                "SimFinId",
                "Company_Name",
                "Sector",
                "Industry",
                "Currency"
            ]
        ],
        on="Ticker",
        how="left"
    )

    return df

def get_latest_companies(df):

    df = df.sort_values(
        "Fiscal Year"
    )

    latest = (
        df
        .groupby(
            "Ticker",
            as_index=False
        )
        .tail(1)
        .copy()
    )

    return latest

def apply_preferences(
    df,
    sector,
    risk,
    goal
):
    filtered = df.copy()

#sector
    if sector != "All":
        filtered = filtered[
            filtered["Sector"] == sector
        ].copy()

# risk
    volatility_percentile = normalize_score(
        filtered["Historical Volatility"]
    )

    if risk == "Low":
        risk_match = 100 - volatility_percentile

    elif risk in ["Moderate", "Medium"]:
        percentile = (
            filtered["Historical Volatility"]
            .rank(pct=True)
        )

        risk_match = (
            1 - abs(percentile - 0.5) * 2
        ) * 100

    elif risk == "High":
        risk_match = volatility_percentile

    else:
        risk_match = pd.Series(
            50,
            index=filtered.index
        )

#goal
    if goal == "High Profitability":
        goal_match = (
            normalize_score(
                filtered["Net Profit Margin"]
            ) * 0.40
            +
            normalize_score(
                filtered["Operating Profit Margin"]
            ) * 0.30
            +
            normalize_score(
                filtered["FCF Margin"]
            ) * 0.30
        )

    elif goal == "Maximum Growth":
        goal_match = (
            normalize_score(
                filtered["Revenue Growth"]
            ) * 0.40
            +
            normalize_score(
                filtered["Net Income Growth"]
            ) * 0.30
            +
            normalize_score(
                filtered["Operating Income Growth"]
            ) * 0.20
            +
            normalize_score(
                filtered["Asset Growth"]
            ) * 0.10
        )

    elif goal == "Long Term Stability":
        goal_match = (
            filtered["Financial Stability Score"]
            / 25
            * 100
        )

    elif goal == "Fast Investment Recovery":
        goal_match = normalize_score(
            filtered["Historical Return"]
        )

    elif goal == "Balanced Return and Risk":
        return_match = normalize_score(
            filtered["Historical Return"]
        )

        low_volatility_match = (
            100
            - normalize_score(
                filtered["Historical Volatility"]
            )
        )

        goal_match = (
            return_match * 0.50
            + low_volatility_match * 0.50
        )

    else:
        goal_match = pd.Series(
            50,
            index=filtered.index
        )

    filtered["Goal Match"] = goal_match
    filtered["Risk Match"] = risk_match

    filtered["Preference Score"] = (
        filtered["Goal Match"] * 0.70
        + filtered["Risk Match"] * 0.30
    )

    filtered["Ranking Score"] = (
        filtered["Investment Score"]
        + filtered["Preference Score"] * 0.25
    )

    return filtered

def get_top_5(
    sector,
    risk,
    goal
):

    df = load_company_data()
    latest = get_latest_companies(df)
    latest = calculate_investment_score(latest)

    filtered = apply_preferences(
        latest,
        sector,
        risk,
        goal
    )

    companies_scanned = filtered["Ticker"].nunique()

    top_5 = (
        filtered
        .sort_values(
            "Ranking Score",
            ascending=False
        )
        .head(5)
        .reset_index(drop=True)
    )

    top_5["Rank"] = (
        top_5.index + 1
    )

    return top_5, companies_scanned
