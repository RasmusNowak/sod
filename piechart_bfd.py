import pandas as pd

def prepare_pie_chart_data():
    # Data for Tank and DPS
    data_tank_dps = [
        ["Rogue", "DPS", 71.67, 117.38, "2234"],
        ["Hunter", "Marksmanship", 69.98, 132.92, "4330"],
        ["Druid", "Feral", 64.92, 113.28, "2586"],
        ["Paladin", "DPS", 59.89, 107.72, "2320"],
        ["Warrior", "DPS", 57.45, 104.77, "2037"],
        ["Warlock", "DPS", 53.61, 90.93, "3061"],
        ["Mage", "Frost", 50.59, 75.66, "1833"],
        ["Shaman", "Enhancement", 47.23, 70.59, "385"],
        ["Mage", "Fire", 44.60, 57.44, "37"],
        ["Paladin", "Tank", 43.07, 64.21, "394"],
        ["Shaman", "Elemental", 41.67, 49.98, "131"],
        ["Warrior", "Tank", 39.26, 75.18, "1945"],
        ["Druid", "Tank", 39.16, 62.09, "640"],
        ["Druid", "Balance", 38.07, 53.36, "261"],
        ["Priest", "DPS", 31.22, 36.58, "81"]
    ]

    # Data for Healers
    data_healers = [
        ["Druid", "Healer", 13.02, 26.26, "856"],
        ["Paladin", "Healer", 5.62, 18.56, "607"],
        ["Priest", "Healer", 4.90, 21.37, "3684"],
        ["Shaman", "Healer", 2.67, 13.91, "424"]
    ]

    # Create DataFrame for Tank and DPS
    df_tank_dps = pd.DataFrame(data_tank_dps, columns=["Class", "Spec", "Score", "Max", "Parses"])

    # Create DataFrame for Healers
    df_healers = pd.DataFrame(data_healers, columns=["Class", "Spec", "Score", "Max", "Parses"])

    # Convert 'Parses' column to integers for df_tank_dps
    df_tank_dps['Parses'] = df_tank_dps['Parses'].astype(int)

    # Drop unnecessary columns in df_tank_dps
    df_tank_dps = df_tank_dps.drop(columns=["Spec", "Max", "Score"])

    # Group by 'Class' and sum 'Parses' in df_tank_dps
    df_tank_dps = df_tank_dps.groupby(["Class"]).sum().reset_index()

    # drop unnecessary columns in df_healers
    df_healers = df_healers.drop(columns=["Spec", "Max", "Score"])

    # convert 'Parses' column to integers for df_healers
    df_healers['Parses'] = df_healers['Parses'].astype(int)

    # combine df_tank_dps and df_healers
    df_combined = pd.concat([df_tank_dps, df_healers])

    # group class and parse by class
    df_combined = df_combined.groupby(["Class"]).sum().reset_index()

    classes_and_colors = [
        ["Druid", "#FF7D0A"],
        ["Hunter", "#ABD473"],
        ["Mage", "#69CCF0"],
        ["Paladin", "#F58CBA"],
        ["Priest", "#FFFFFF"],
        ["Rogue", "#FFF569"],
        ["Shaman", "#0070DE"],
        ["Warlock", "#9482C9"],
        ["Warrior", "#C79C6E"]
    ]

    class_colors = pd.DataFrame(classes_and_colors, columns=["Class", "Color"])

    # Merge df_combined and class_colors
    df_combined = pd.merge(df_combined, class_colors, on="Class")

    return df_combined
