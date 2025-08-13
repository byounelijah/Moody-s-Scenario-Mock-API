import sys
import s2api
import datetime
import pandas as pd

# enter your keys here
# obtain them from: https://economy.com/myeconomy/api-key-info
access_key = "your key here"
encryption_key = "your key here"

# instantiate api
api = s2api.ScenarioStudioAPI(access_key, encryption_key)

# get information on your Scenario Studio projects
projects = api.get_project_list()

# get info on the first project in that list
project_id = projects[0]['id']
project_info = api.get_project_info(project_id)

# get info on the first scenario in the project
scenarios = api.get_project_scenarios(project_id)
scenario_id = scenarios[0]['id']
scenario_alias = scenarios[0]['alias']
scenario_info = api.get_scenario_info(project_id,scenario_id)

# get variable listing for this scenario
series_list = api.search_series(project_id,scenario_ids=[scenario_id])

# download data
download_list = []
for n in range(0,4):
    download_list.append(scenario_alias+"."+series_list[n]['variableId'])
data = api.get_series_data(project_id,download_list)

# import matplotlib.pyplot as plt

# Moody's long-term rating scale
ratings = [
    "Aaa", "Aa1", "Aa2", "Aa3",
    "A1", "A2", "A3",
    "Baa1", "Baa2", "Baa3",
    "Ba1", "Ba2", "Ba3",
    "B1", "B2", "B3",
    "Caa1", "Caa2", "Caa3",
    "Ca", "C"
]
rating_positions = list(range(len(ratings), 0, -1))  # Highest rating at top

# Example: Map GDP and Unemployment mock values to rating positions
# (You can later replace these with actual API values)
rating_mapping = {
    "GDP_US": [1, 3, 5, 7, 10, 15],      # GDP rating positions over time
    "UNRATE_US": [20, 18, 15, 12, 9, 5]  # Unemployment rating positions
}

dates = pd.date_range("2025-01", periods=len(rating_mapping["GDP_US"]), freq="M")

plt.figure(figsize=(10, 6))
for series_id, positions in rating_mapping.items():
    plt.plot(dates, positions, marker='o', label=series_id)

plt.yticks(rating_positions, ratings)
plt.gca().invert_yaxis()  # Aaa at top
plt.xlabel("Date")
plt.ylabel("Credit Rating")
plt.title(f"Scenario: {scenario_alias} — Moody's Style Ratings")
plt.legend()
plt.tight_layout()
plt.show()