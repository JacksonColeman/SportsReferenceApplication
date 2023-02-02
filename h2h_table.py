import json
import pandas


def create_h2h_table(data):
    # Load JSON data
    with open(data, "r") as f:
        records = json.load(f)

    # Get list of teams and create nested dictionary
    teams = list(records.keys())
    record_dict = {team: {opp: records[team][opp]["W"] if team !=
                          opp else "--" for opp in teams} for team in teams}

    # Convert dictionary to pandas dataframe
    table = pandas.DataFrame.from_dict(record_dict, orient="index")
    return table


# call function using sample data and print result
table = create_h2h_table("sample-data.json")
print(table)
