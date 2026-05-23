import pandas as pd

# Load the dataset
df = pd.read_csv("results.csv")

#Show first rows
print (df.head())

#Show all column names
print (df.columns)

#Basic info 
print (df.info())


#Who where the highest goal scoreing team in the 
print ("\n Highest Scoring Teams")
top_teams = df.groupby("home_team")["home_goals"].sum()
print(top_teams.sort_values(ascending=False).head(10))


#Which season had the highest amount of goals 
print("\n Season With Highest number of goals scored ")
df["total_goals"] = df["home_goals"] + df ["away_goals"]
goals_by_season = df.groupby ("season")["total_goals"].sum()
print(goals_by_season.sort_values(ascending=False).head(5))

#Team with most Home Wins between Chelsea and Man_City
print ("\n Team With Highest amount of Home Games btw Chelsea and Manchester City")
man_city = df[(df["home_team"] == "Manchester City") & (df["result"] == "H" )]
Chelsea = df[(df["home_team"] == "Chelsea") & (df["result"] == "H" )]
print (f"Man City home wins: {len(man_city)}") 
print (f"Chelsea home wins: {len(Chelsea)}") 