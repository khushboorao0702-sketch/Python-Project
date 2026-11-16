import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------Step 1:Read the CSV file----------
file_name = input("Enter CSV file name :")
if file_name == "":
    file_name = "score.csv"

try:
    data = pd.read_csv(file_name,header=None,
                       names=["Player", "Match", "Score"],dtype=str)
except FileNotFoundError:
    print("File not found!")
    exit()

# If the file has a header row (Player,Match,Score),remove it
if data.iloc[0]["Player"] == "Player":
    data = data.iloc[1:]

#----------Step 2: Clean the data----------
players = []
matches = []
score= []

row_no = 1
for p, m, s in zip(data["Player"], data["Match"], data["Score"]):
    try:
        s = float(s)        # try to convert score to number
        m = int(m)           # try to convert match to number
        if s < 0:
            print(f"Row {row_no} skipped: Score cannot be negative.")
        else:
            players.append(p)
            matches.append(m)
            score.append(s)
    except (ValueError, TypeError):
        print(f"Row {row_no} skipped: invalid Score {str(s)}.")
    row_no += 1

# Make a clean table with only valid rows
df = pd.DataFrame({"Player": players,"Match":matches,"Score":score})

if len(df) == 0:
    print("No valid data to analyse.")
    exit()

#----------Step 3:Menu----------
while True:
    print()
    print("1.Player stats")
    print("2.Statistics and trend")
    print("3.Exit")
    choice = input("Enter your choice:")

    if choice =="1":
        # groupby:find average, best and total score of each player
        stats = df.groupby("Player")["Score"].agg(["mean","max","sum"])
        top_player = stats["mean"].idxmax()

        if len(df) == 1:
            # only one row of data
            std_dev = np.std(df["Score"])
            print(f"{top_player} Avg {stats.loc[top_player,"mean"]:.2f} | Best {stats.loc[top_player,"max"]:.2f} | Std Dev {std_dev:.2f}")
            print(f"Top performer {top_player}")
        else:
            for name in stats.index:
                print(f"{name} Avg {stats.loc[name,"mean"]:.2f} | Best {stats.loc[name,"max"]:.2f} | Total {stats.loc[name,"sum"]:.2f}")
                print(f"Top performer {top_player} Avg {stats.loc[top_player,"mean"]:.2f}")

    elif choice == "2":
        #NumPy calculations on all scores
        arr = np.array(df["Score"])
        mean = np.mean(arr)
        median = np.median(arr)
        std_dev = np.std(arr)           # population standard deviation
        highest = np.max(arr)
        lowest = np.min(arr)

        #Find who got the highest score and in which match
        best_row = df["Score"].idxmax()
        best_player = df["Player"][best_row]
        best_match = df["Match"][best_row]

        print(f"Mean: {mean} | Median: {median} | Std Dev: {std_dev} | Max: {highest} ({best_player} Match {str(best_match)}")

        # groupby:average score of each match
        match_avg = df.groupby("Match")["Score"].mean()
        text =""
        for match_no in match_avg.index:
            text = f"{text} Match {str(match_no)} : {match_avg[match_no]:.2f} |"
        print(f"Match-wise average: {text.rstrip("|")}")

        #Line chart: average score of each match
        plt.figure()
        plt.plot(match_avg.index,match_avg.values,marker="o")
        plt.title("Score Trend")
        plt.xlabel("Match")
        plt.ylabel("Average Score")
        plt.xticks(match_avg.index)
        print("Line chart 'Score Trend' displayed")

        #Bar chart: average score of each player
        player_avg = df.groupby("Player")["Score"].mean()
        plt.figure()
        plt.bar(player_avg.index,player_avg.values,color="skyblue")
        plt.title("Player Average Score")
        plt.xlabel("Player")
        plt.ylabel("Average Score")

        plt.show()
        
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter 1,2 or 3.")