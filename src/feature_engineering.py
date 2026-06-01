def create_features(df):

    df["loan_to_income_ratio"] = (df["loan_amnt"] / (df["annual_inc"] + 1))

    df["fico_avg"] = (df["fico_range_low"] + df["fico_range_high"]) / 2

    df["monthly_income"] = (df["annual_inc"] / 12)
    df["installment_income_ratio"] = (df["installment"] / (df["monthly_income"] + 1))

    df["credit_utilization"] = (df["revol_util"]    )

    return df