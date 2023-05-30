import pandas as pd

batting = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\Batting.csv")
fielding = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\Fielding.csv")
# battingPost = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\BattingPost.csv")
pitching = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\Pitching.csv")
# pitchingPost = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\PitchingPost.csv")
awards = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\contrib\AwardsPlayers.csv")
hof = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\contrib\HallOfFame.csv")
players = pd.read_csv("C:\\Users\Owner\Downloads\\baseballdatabank-2022.2\\baseballdatabank-2022.2\core\People.csv")


# modifiedBatting = batting.fillna("null")
# modifiedBattingPost = battingPost.fillna("null")
# modifiedPitching = pitching.fillna("null")
# modifiedPitchingPost = pitchingPost.fillna("null")
# modifiedPitchingPost = modifiedPitchingPost.replace("inf", "null")
# modifiedAwards = awards.fillna("null")
modifiedPlayers = players.fillna("null")
modifiedFielding = fielding.fillna("null")
modifiedHOF = hof.fillna("null")




# modifiedBatting.to_csv("C:\\Users\Owner\Desktop\Batting.csv")
# modifiedBattingPost.to_csv("C:\\Users\Owner\Desktop\BattingPost.csv")
# modifiedPitching.to_csv("C:\\Users\Owner\Desktop\Pitching.csv")
# modifiedPitchingPost.to_csv("C:\\Users\Owner\Desktop\PitchingPost.csv")
# modifiedPlayers.to_csv("C:\\Users\Owner\Desktop\People.csv")
# modifiedFielding.to_csv("C:\\Users\Owner\Desktop\Fielding.csv")
modifiedHOF.to_csv("C:\\Users\Owner\Desktop\HallOfFame.csv")
# modifiedAwards.to_csv("C:\\Users\Owner\Desktop\AwardsPlayers.csv")
