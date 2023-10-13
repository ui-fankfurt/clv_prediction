import matplotlib.pyplot as plt


#Edited the original code in the lifetimes package to save the graph image
def plot_calibration_purchases_vs_holdout_purchases(model, calibration_holdout_matrix, kind="frequency_cal", n=7, **kwargs):

    x_labels = {
        "frequency_cal": "Purchases in calibration period",
        "recency_cal": "Age of customer at last purchase",
        "T_cal": "Age of customer at the end of calibration period",
        "time_since_last_purchase": "Time since user made last purchase",
    }
    summary = calibration_holdout_matrix.copy()
    duration_holdout = summary.iloc[0]["duration_holdout"]

    summary["model_predictions"] = model.conditional_expected_number_of_purchases_up_to_time(
            duration_holdout, summary["frequency_cal"], summary["recency_cal"], summary["T_cal"])

    if kind == "time_since_last_purchase":
        summary["time_since_last_purchase"] = summary["T_cal"] - summary["recency_cal"]
        ax = (
            summary.groupby(["time_since_last_purchase"])[["frequency_holdout", "model_predictions"]]
            .mean()
            .iloc[:n]
            .plot(**kwargs)
        )
    else:
        ax = summary.groupby(kind)[["frequency_holdout", "model_predictions"]].mean().iloc[:n].plot(**kwargs)

    plt.title("Actual Purchases in Holdout Period vs Predicted Purchases")
    plt.xlabel(x_labels[kind])
    plt.ylabel("Average of Purchases in Holdout Period")
    plt.legend()
    #saves the graph
    plt.savefig('static/model_validation.png')

    return ax