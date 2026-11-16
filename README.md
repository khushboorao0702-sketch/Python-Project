# Sports Performance Analyzer

**Name:** Khushboo Rao
**ERP:** RU-26-O1489
**Sec:** 1L
**University:** Rungta International Skills University
**Project:** PS 16 - Sports Performance Analyzer

## About the Project
This Python program loads players' match scores from a CSV file, cleans the data and analyses it. It finds each player's average, best and total score, the top performer, and overall statistics. It also shows charts of the results.

## Technologies Used
- Python 3
- NumPy
- Pandas
- Matplotlib

## Files in this Repository
- `one.py` - the main Python program
- `scores.csv` - sample input data
- `README.md` - project description
- `Summary.md` - implementation details and test case screenshots

## How to Run
1. Install the libraries:
   `pip install numpy pandas matplotlib`
2. Keep `one.py` and `scores.csv` in the same folder.
3. Run the program:
   `python one.py`
4. Press Enter to use `scores.csv`, then choose an option.

## Menu Options
1. **Player stats** - average, best and total score of each player, and the top performer
2. **Statistics and trend** - mean, median, standard deviation, maximum, match-wise average, a line chart and a bar chart
3. **Exit**

## Input Format
The CSV file has three columns: Player, Match and Score.
```
Aman,1,40
Aman,2,60
Riya,1,30
Riya,2,50
```

## Sample Output
```
Aman: Avg 50.00 | Best 60 | Total 100
Riya: Avg 40.00 | Best 50 | Total 80
Top performer: Aman (Avg 50.00)
```

## Error Handling
- Rows with an invalid score (like `abc`) are skipped
- Rows with a negative score are skipped
- A message is shown if the file is not found
- If no valid data is left, the program shows "No valid data to analyse."
