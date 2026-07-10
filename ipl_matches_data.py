import pandas as pd

df=pd.read_excel("ipl_matches_data.xlsx")


print(df.dtypes)

# total_teams=df["Team1"].unique()
# print(total_teams)

# Top_winner_team=(
#     df.groupby('Team1')['Match_winner'].count().sort_values(ascending=False).head(10)
# )
# print(Top_winner_team)


# Top_winner_team = (
#     df.groupby(['Season_id', 'Match_winner'])
#       .size()
#       .reset_index(name='Wins')
#       .sort_values(by='Wins', ascending=False)
#       .head(10)
# )

# print(Top_winner_team)