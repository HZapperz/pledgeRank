import pandas as pd

def rank_pledges(file_path, weights):
    """
    Rank pledges based on weighted scores and output only names and rankings.

    :param file_path: Path to the Excel file containing the pledge data.
    :param weights: Dictionary of weights for each category.
    :return: DataFrame with the names and ranks of the pledges.
    """
    # Load the data
    pledge_data = pd.read_excel(file_path)

    # Calculate the total score for each pledge
    pledge_data['Total Score'] = sum(pledge_data[col] * weight for col, weight in weights.items())

    # Sorting the data based on the total score in descending order
    ranked_pledges = pledge_data.sort_values(by='Total Score', ascending=False)

    # Adding a rank column
    ranked_pledges['Rank'] = range(1, len(ranked_pledges) + 1)

    # Select only the names and ranks
    names_and_ranks = ranked_pledges[['Names', 'Rank']]

    return names_and_ranks

# Example usage of the function
file_path = r'C:\Users\hamza\OneDrive\Documents\ZN2\PLEDGES\Final_Updated_Pledge_Grading_System.xlsx'  # Replace with your file path
weights = {
    "Quiz Scores": 0.25,
    "Homework Scores": 0.15,
    "Attendance": 0.35,
    "Group Participation": 0.25
}

# Rank the pledges and output names and rankings
names_and_rankings = rank_pledges(file_path, weights)

# Print the names and rankings
print(names_and_rankings)
