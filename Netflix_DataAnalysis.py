#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[ ]:





# In[ ]:





# In[4]:


data = pd.read_csv("netflix_titles.csv")
data


# In[9]:


data.head()


# In[5]:


data.shape


# In[8]:


data['type'].unique()


# In[11]:


data['director'].unique()


# In[6]:


#SETTING THE STYLE FOR PLOTS

sns.set(style="darkgrid")


# In[7]:


print("Missing  values in dataset:")
data.isnull().sum()


# In[11]:


#CLEARNING OF DATA/DROPPING MISSING VALUES
netflix_clean_data = data.dropna()


# In[12]:


netflix_clean_data.shape


# In[13]:


#Dataset information after cleaning

print("Netflix dataset after cleaning:")
netflix_clean_data.isnull().sum()


# In[14]:


#Non - Graphical Anlysis
print("Value counts for 'type':")
netflix_clean_data['type'].value_counts()


# In[15]:


print("Unique values in each column:")
for column in netflix_clean_data.columns:
    print(f"{column}: {netflix_clean_data[column].nunique()} unique values")


# In[29]:


# Step 6: Visual Analysis
# Univariate Analysis
print("Distribution of Titles by Type:")
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=netflix_clean_data,color='lightblue')
plt.title('Distribution of Titles by Type')
plt.xlabel('Type')
plt.ylabel('Count')

plt.show()

print('Insight: Movies are more prevalent than TV shows on Netflix. This indicates that Netflix has historically focused more on acquiring or producing movies compared to TV shows.')


# In[32]:


print("Number of titles released each year:")
plt.figure(figsize=(10, 6))
sns.histplot(netflix_clean_data['release_year'], kde=False, bins=30, color='blue')
plt.title('Number of Titles Released Each Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

print("Insight: The number of movies released per year has seen a significant increase, especially in the last decade, indicating a growing trend in movie production and acquisition by Netflix.")


# In[34]:


# Bivariate Analysis
print("\nNumber of titles released each year by type:")
plt.figure(figsize=(10, 6))
sns.histplot(data=netflix_clean_data, x='release_year', hue='type', multiple='stack', bins=30, palette='viridis')
plt.title('Number of Titles Released Each Year by Type')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# In[16]:


# Analysis of Actors/Directors
# Let's focus on the top 10 actors and directors

from collections import Counter

# Function to get the top N elements from a column with list-like strings
def get_top_elements(column, n=10):
    all_elements = []
    netflix_clean_data[column].dropna().apply(lambda x: all_elements.extend(x.split(', ')))
    return Counter(all_elements).most_common(n)

top_actors = get_top_elements('cast', 10)
top_directors = get_top_elements('director', 10)


# In[17]:


print("Top 10 actors:")
print(top_actors)


# In[18]:


print("\nTop 10 directors:")
print(top_directors)


# In[42]:


# Plot top actors
import seaborn as sns
actors, counts = zip(*top_actors)
plt.figure(figsize=(10, 6))
sns.barplot(x=list(counts), y=list(actors))
plt.title('Top 10 Actors')
plt.xlabel('Count')
plt.ylabel('Actor')
plt.show()


# In[19]:


# Plot top directors
directors, counts = zip(*top_directors)
plt.figure(figsize=(10, 6))
sns.barplot(x=list(counts), y=list(directors), palette='viridis')
plt.title('Top 10 Directors')
plt.xlabel('Count')
plt.ylabel('Director')
plt.show()


# In[21]:


# Genre Analysis
print("\nTop 10 genres:")
top_genres = netflix_clean_data['listed_in'].value_counts().head(10)
print(top_genres)


# In[28]:


pd.options.mode.copy_on_write = True
plt.figure(figsize=(10, 6))
sns.barplot(y=top_genres.index, x=top_genres.values, palette='viridis')
plt.title('Top 10 Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()


# In[ ]:





# In[23]:


# Analysis 5: Duration Analysis (for Movies)
# Convert duration to numeric values for movies
netflix_movies = netflix_clean_data[netflix_clean_data['type'] == 'Movie']
netflix_movies['duration'] = netflix_movies['duration'].str.replace(' min', '').astype(int)

print("\nDistribution of movie durations:")
plt.figure(figsize=(10, 6))
sns.histplot(netflix_movies['duration'], bins=30, kde=True, color='blue')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.show()


# In[ ]:





# In[29]:


insights = {
    "Most titles on Netflix are movies.": "Netflix could explore increasing their series content to balance the distribution.",
    "The number of titles released each year has been increasing.": "Netflix should continue to invest in new content to maintain and grow its subscriber base.",
    "The USA is the leading country in terms of the number of titles.": "Netflix could focus on acquiring and producing more content from other countries to diversify its library.",
    "Drama, Comedy, and Documentaries are the most popular genres.": "Netflix should invest more in these genres, as they are highly popular among viewers.",
    "Most movies have a duration between 80 and 120 minutes.": "Netflix could consider producing more short films and mini-series to cater to viewers with less time.",
    "Certain actors and directors are frequently featured.": "Netflix should continue to collaborate with popular actors and directors to attract their fanbase.",
    "Most movies have a duration between 80 and 120 minutes.": "Netflix could consider producing more short films and mini-series to cater to viewers with less time."
}

print("\nInsights and Recommendations:")
for insight, recommendation in insights.items():
    print(f"- Insight: {insight}\n  Recommendation: {recommendation}\n")



```
# This is formatted as code
```

# Netflix Data Analysis Insights

## Non-Graphical Analysis Insights

- **Value Counts for 'type'**: There are more movies than TV shows.
- **Unique Values**: Highlights the variety in the dataset, e.g., unique genres, countries, etc.

## Visual Analysis Insights

- **Distribution of Titles by Type**: Most titles are movies, suggesting a focus on movie content.
- **Number of Titles Released Each Year**: Shows growth in content over the years.
- **Top Countries with Most Titles**: The USA leads, followed by other countries, indicating content production hubs.
- **Distribution of Ratings by Type**: Various ratings across movies and TV shows.
- **Distribution of Movie Durations**: Most movies are between 80-120 minutes long.

## Analysis of Actors/Directors

- **Top 10 Actors/Directors**: Identifies popular actors and directors frequently featured in Netflix content.

## Genre Analysis

- **Top 10 Genres**: Drama, Comedy, and Documentaries are the most common genres.

## Business Insights

- **Increase Series Content**: To balance the distribution of movies and series.
- **Invest in New Content**: To maintain and grow the subscriber base.
- **Diversify Content Library**: Focus on acquiring and producing content from countries other than the USA.
- **Invest in Popular Genres**: Drama, Comedy, and Documentaries are highly popular.
- **Produce Short Films and Mini-Series**: To cater to viewers with less time.
- **Collaborate with Popular Actors and Directors**: To attract their fanbase.

# In[32]:


# Focus on TV Shows vs. Movies in recent years
recent_years_data = netflix_clean_data[netflix_clean_data['release_year'] >= 2015]

plt.figure(figsize=(14, 7))
sns.histplot(data=recent_years_data, x='release_year', hue='type', multiple='stack', bins=10, palette='viridis')
plt.title('Focus on TV Shows vs. Movies in Recent Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

Insight: In recent years, there has been a noticeable increase in the number of TV shows compared to movies, suggesting that Netflix is shifting some of its focus towards producing or acquiring more TV show content.
# In[34]:


# Content available in different countries
top_countries_content = netflix_clean_data['country'].value_counts().head(10)

plt.figure(figsize=(14, 7))
sns.barplot(y=top_countries_content.index, x=top_countries_content.values, palette='viridis')
plt.title('Top 10 Countries with the Most Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

Insight: The USA leads in terms of content available on Netflix, followed by other countries. This can help in understanding the distribution of content and guide strategic decisions to expand and diversify the content library for other regions.## Summary and Recommendations
- Movie Releases Trend: The number of movies released each year has been increasing, especially in the last decade. Recommendation: Continue investing in movie content as it shows strong growth.

- TV Shows vs. Movies: Movies are more prevalent than TV shows. Recommendation: Balance the content library by increasing the production and acquisition of TV shows.

- Best Time to Launch TV Shows: Identifying peak months for TV show releases can help maximize viewership. Recommendation: Launch new TV shows during these peak periods.

- Actors/Directors Analysis: Popular actors and directors can attract more viewers. Recommendation: Collaborate with frequently featured actors and directors to draw their fanbase.

- Focus on TV Shows in Recent Years: There is a shift towards more TV shows. Recommendation: Maintain this focus and continue to diversify the content offerings with new TV shows.

- Content in Different Countries: The USA dominates in content availability. Recommendation: Diversify the content library by acquiring more titles from other countries to cater to a global audience.
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




