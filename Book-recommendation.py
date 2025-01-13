import pandas as pd
from google.colab import files
import io

# Step 1: Upload the CSV file
uploaded = files.upload()

# Step 2: Load the CSV file into a pandas DataFrame
df = pd.read_csv(io.BytesIO(uploaded['books.csv']))

# Step 3: Display the first few rows of the dataset to ensure it's loaded correctly
df.head()

# Step 4: Function to search and filter books based on user input
def filter_books():
    # Step 1: Ask the user for the primary criterion
    print("You can search by one of the following criteria:")
    print("1. Title")
    print("2. Genre")
    print("3. Height")
    print("4. Author")

    primary_criteria = input("Enter the number corresponding to the criterion you want to search by: ").strip()

    # Step 2: Handle the user input based on the chosen criterion
    if primary_criteria == '1':
        title_input = input("Enter the title of the book you're looking for: ").strip()
        filtered_books = df[df['Title'].str.contains(title_input, case=False, na=False)]
    elif primary_criteria == '2':
        genre_input = input("Enter the genre you're interested in: ").strip()
        filtered_books = df[df['Genre'].str.contains(genre_input, case=False, na=False)]
    elif primary_criteria == '3':
        height_input = float(input("Enter the height (or size) of the book you prefer (in cm): "))
        filtered_books = df[df['Height'] <= height_input]
    elif primary_criteria == '4':
        author_input = input("Enter the author you're looking for: ").strip()
        filtered_books = df[df['Author'].str.contains(author_input, case=False, na=False)]
    else:
        print("Invalid option.")
        return

    # Step 3: Check if the filtered books are empty
    if not filtered_books.empty:
        # Step 4: Ask for an additional criteria, if needed
        more_criteria = input("Would you like to filter further by another criterion? (yes/no): ").strip().lower()

        if more_criteria == 'yes':
            print("You can filter by:")
            print("1. Genre")
            print("2. Height")
            print("3. Author")

            additional_criteria = input("Enter the number corresponding to the additional criterion you want to filter by: ").strip()

            if additional_criteria == '1' and primary_criteria != '2':
                additional_genre_input = input("Enter the genre: ").strip()
                filtered_books = filtered_books[filtered_books['Genre'].str.contains(additional_genre_input, case=False, na=False)]
            elif additional_criteria == '2' and primary_criteria != '3':
                additional_height_input = float(input("Enter the height: "))
                filtered_books = filtered_books[filtered_books['Height'] <= additional_height_input]
            elif additional_criteria == '3' and primary_criteria != '4':
                additional_author_input = input("Enter the author: ").strip()
                filtered_books = filtered_books[filtered_books['Author'].str.contains(additional_author_input, case=False, na=False)]
            else:
                print("You already provided this criterion, no further filtering needed.")

        # Step 5: Show the filtered results
        if not filtered_books.empty:
            print("\nRecommended books based on your preferences:")
            for index, row in filtered_books.iterrows():
                print(f"- {row['Title']} by {row['Author']} (Genre: {row['Genre']}, Height: {row['Height']} cm)")
        else:
            print("\nNo books found based on your combined criteria.")
    else:
        print("\nNo books found based on your criteria.")

# Run the function
filter_books()
