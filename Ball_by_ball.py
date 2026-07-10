import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_excel('Ball_by_ball_data.xlsx')
# print(df)

# print(df.dtypes)


# print(df.isna().sum())

# total_teams=df.groupby('Batter')['Innings'].sum().idxmax()
# print(total_teams) ?? Virat kohli 

# Player_Name=df.groupby('Batter')['Total_runs'].sum().idxmax()
# print("Player Name: ", total_runs) # Virat Kohli

# total_runs=df.groupby('Batter')['Total_runs'].sum().max()
# print(Player_Name,":",total_runs) 

# df["Batsman_type"] = df["Batsman_type"].str.replace("_", "")
print(df.dtypes)
# The_Bowling_Type=df.groupby("Bowler")["Bowler_type"]
# The_top_bowler=df.groupby('Bowler')['Innings'].sum().idxmax()
# print(The_top_bowler,":")
# The_top_bowler=df.groupby('Bowler')['Innings'].sum().idxmax()
# print(The_top_bowler) 

# Top_players = (
#     df.groupby("Batter")["Batter_runs"]
#       .sum()
#       .sort_values(ascending=False)
#       .head(10)
# )

# print(Top_players)

# The_highest_run_year=(df.groupby("Season_Id")["Total_runs"].sum().sort_values(ascending=False).head(10))
# print(The_highest_run_year)

# import seaborn as sns
# import matplotlib.pyplot as plt

# top_players = (
#     df.groupby("Batter")["Batter_runs"]
#       .sum()
#       .sort_values(ascending=False)
#       .head(10)
#       .reset_index()
# )

# sns.barplot(data=top_players, x="Batter_runs", y="Batter")

# plt.title("Top 10 Batsmen")
# plt.show()

# top_bowlers = (
#     df.groupby("Bowler")["Innings"] 
#         .sum()
#         .sort_values(ascending=False)
#         .head(10)
#         .reset_index()
      
# )
# # print(top_bowlers)
# sns.barplot(data=top_bowlers, x="Innings", y="Bowler")
# plt.title("Top 10 Bowlers")
# plt.show()


# top_seasons=(
#     df.groupby("Season_Id")["Total_runs"].size().sort_index().head(10)

# )

# # print(top_seasons)

# sns.lineplot(data=top_seasons,x="Total_runs",y="Season_Id")
# plt.title("Highest Run Season")
# plt.show()
