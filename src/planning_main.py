"""Main script for transport planning project."""
import time

import pandas as pd
import matplotlib as mpl
from matplotlib import rcParams
from apscheduler.schedulers.background import BackgroundScheduler

import planning_functions as pf
import planning_config as cfg

rcParams["font.family"] = "Arial"
rcParams["figure.figsize"] = (16, 9)
rcParams["figure.dpi"] = 300
rcParams["axes.titlesize"] = 24
rcParams["axes.labelsize"] = 18
rcParams["font.size"] = 16
rcParams["xtick.labelsize"] = 16
rcParams["ytick.labelsize"] = 14
rcParams["legend.fontsize"] = 16
rcParams["legend.title_fontsize"] = 18

mpl.use("agg")

def calculate_time_taken():
    # Loop through public transport projects retrieving planning application
    # information from ABP and add to an accruing DataFrame.
    planning_apps_df = pd.DataFrame()
    for inf_type, projects in cfg.PROJECT_DETAILS.items():
        for project_name, planning_id in projects.items():
            planning_url = cfg.ABP_BASE_URL + f"{planning_id}"

            planning_app_df = pf.planning_request(planning_url)
            planning_app_df["infrastructure_type"] = inf_type
            planning_app_df["short_name"] = project_name
            planning_app_df["planning_id_code"] = planning_id

            planning_apps_df = pd.concat(
                [planning_apps_df, planning_app_df],
                ignore_index=True,
            )
            time.sleep(1)

    # Save retrieved data, clean and format data and then save cleaned data too
    planning_apps_df.to_csv(cfg.DATA_FOLDER + "planning_applications.csv")
    planning_apps_df = pf.clean_planning_columns(
        planning_apps_df, acronym_replacements=cfg.PROJECT_ACRONYMS
    )
    planning_apps_df.to_csv(
        cfg.DATA_FOLDER + "cleaned_planning_applications.csv"
    )

    # Create plot showing the time taken on all project applications so far by
    # ABP.
    _, _ = pf.plot_time_taken(
        planning_apps_df,
        save_dir=cfg.OUTPUTS_FOLDER,
        save_name="time_taken.png",
    )


def main():
    """Run this once a day."""

    schedule = BackgroundScheduler(
        {
            'apscheduler.timezone': 'UTC',
        }
    )

    schedule.add_job(calculate_time_taken, "interval", days=1)
    schedule.start()
    try:
        while True:
            time.sleep(120)
    except (KeyboardInterrupt, SystemExit):
        schedule.shutdown()


if __name__ == "__main__":
    main()
