import pandas as pd
from ydata_profiling import ProfileReport

# First we check which of the columns have NANs.
df = pd.read_csv("movie_dataset.csv",index_col=0)
df.columns = df.columns.str.replace(' ', '_') # Fix column names.

#Placing the columns with nans in a list
nan_columns = df.columns[df.isna().any()].tolist()

def clean_df(column_name, nan_columns=nan_columns,df=df):
    # Check if the column is in the list of columns with NaN values
    if column_name in nan_columns:
        # Drop rows with NaNs in the specified column
        df_cleaned = df.dropna(subset=[column_name])
    else:
        df_cleaned = df

    return df_cleaned

# Question 1
def highest_rated_film(column_name="Rating"):

    df_cleaned = clean_df(column_name)

    max_rating = df_cleaned['Rating'].max()

    film_title = df_cleaned[df_cleaned['Rating'] == max_rating]['Title'].iloc[0]

    return film_title

print(highest_rated_film())

# Question 2

def average_revenue(column_name="Revenue_(Millions)"):
    df_cleaned = clean_df(column_name)
    return df_cleaned["Revenue_(Millions)"].mean()

print(average_revenue())

# Question 3

def average_revenue_2015_2017(column_name="Revenue_(Millions)"):
    df_cleaned = clean_df(column_name)
    df_cleaned = df_cleaned[df_cleaned["Year"]>=2015]
    df_cleaned = df_cleaned[df_cleaned["Year"]<=2017]
    return df_cleaned["Revenue_(Millions)"].mean()

print(average_revenue_2015_2017())

# Question 4

def num_films_in_2016(column_name="Year"):
    df_cleaned = clean_df(column_name)
    df_cleaned = df_cleaned[df_cleaned["Year"]==2016]
    return df_cleaned.shape[0]

print(num_films_in_2016())

# Question 5

def nolan_films(column_name="Director"):
    df_cleaned = clean_df(column_name)
    df_cleaned = df_cleaned[df_cleaned["Director"]=="Christopher Nolan"]
    return df_cleaned.shape[0]

print(nolan_films())

# Question 6

def rated_8_or_higher(column_name="Rating"):
    df_cleaned = clean_df(column_name)
    df_cleaned = df_cleaned[df_cleaned["Rating"]>=8.0]
    return df_cleaned.shape[0]

print(rated_8_or_higher())

# Question 7
def median_nolan_films(column_name="Rating"):
    df_cleaned = clean_df(column_name)
    df_cleaned = df_cleaned[df_cleaned["Director"]=="Christopher Nolan"]
    return df_cleaned["Rating"].median()

print(median_nolan_films())

# Question 8
def year_highest_average_rating(column_name="Rating"):
    df_cleaned = clean_df(column_name)
    years=df['Year'].unique().tolist()
    max_rating = 0 
    max_year = 0
    for year in years:
        df_year=df_cleaned[df_cleaned["Year"]==year]
        if max_rating<df_year["Rating"].mean():
            max_rating=df_year["Rating"].mean()
            max_year=year
    return max_year

print(year_highest_average_rating())

# Question 9

def percentage_increase_2006_2016(column_name="Year"):
    df_cleaned = clean_df(column_name)
    df_2006 = df_cleaned[df_cleaned["Year"]==2006]
    df_2016 = df_cleaned[df_cleaned["Year"]==2016]

    return ((df_2016.shape[0]-df_2006.shape[0])/df_2006.shape[0])*100

print(percentage_increase_2006_2016())

#Question 10

def common_actor(column_name="Actors"):
    df_cleaned = clean_df(column_name)
    actors_series = df_cleaned['Actors'].str.split(',').explode()

    # Trim whitespace and count occurrences of each actor
    actor_counts = actors_series.str.strip().value_counts()

    # Find the most common actor
    most_common_actor = actor_counts.idxmax()
    return most_common_actor

print(common_actor())

# Question 11

def unique_genres(column_name="Genre"):
    df_cleaned = clean_df(column_name)

    genres=df_cleaned['Genre'].str.split(',').explode()

    print(len(genres.unique()))

unique_genres()

# Question 12

# Drop rows with any NaN values
df_cleaned = df.dropna()
profile = ProfileReport(df_cleaned,title="Film_report")
profile.to_file("your_report.html")