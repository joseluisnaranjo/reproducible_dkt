# Description: This module contains the function that reads a CSV file and gives back a instance of a dataset.
import pandas as pd


# Function that reads a CSV file and gives back a instance of a dataset
def read_csv_file(file_path):
    """
    Read a CSV file and return a Pandas DataFrame after executing some preprocessing steps.
        1. Drop rows with missing values in the 'skill_id' column.
        2. Extract only the desired columns.
        3. Print the number of unique skills.         
    
    Parameters
    ----------
    file_path : str
        The path to the CSV file to be read.
        
    Returns
    -------
    pandas.DataFrame
        The dataset read from the CSV file.
            
    """
    try:
        # Read CSV file into a Pandas DataFrame with a specified encoding
        df = pd.read_csv(file_path, encoding='latin1') 

    except FileNotFoundError:
        print("The file '{}' could not be found.".format(file_path))
        return None
    
    try:
        # Drop rows with missing values in the 'skill_id' column
        df.dropna(subset=[ 'skill_id'], inplace=True)

        # Extract only the desired columns
        selected_columns = df[['user_id', 'correct', 'skill_id']]

        # Extract only the skill_id in a set  to get the number of unique skills and print the numebr of unique skills
        print("Number of different skills:", len(set(df['skill_id'].astype(str))))

        # Extract only the users_id in a set  to get the number of unique users and print the numebr of unique skills
        print("Number of different users:", len(set(df['user_id'].astype(str))))
        
        # Extract the 'user_id' column
        user_ids = df['user_id'].unique()

        # Create a lookup table that maps each unique 'user_id' to a unique integer starting from 0
        user_id_lookup = {user_id: idx for idx, user_id in enumerate(user_ids)}

        # Apply the lookup table to transform the 'user_id' column in the DataFrame
        selected_columns['user_id'] = selected_columns['user_id'].map(user_id_lookup)

        return selected_columns  
         
    except Exception as e:
        print("An unexpected error occurred: {}".format(str(e)))
        return None
    
