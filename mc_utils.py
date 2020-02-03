'''
Med Cabinet app functionality 
'''
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def combine_features(row):
    '''Combine features into block of text.
    '''
    return row['Strain'] + " " + row['Type'] + " " + row['Rating'] + " " + row['Effects'] + " " + row['Flavor'] + " " + row['Description']


def fill_nans(df):
    '''Features are the column names for the features you want to include
       This function fills nans with an empt string.
    '''
    features = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']
    for feature in features:
        df[feature] = df[feature].fillna('')
    return df


def get_index_from_strain(strain):
    '''Get an index from your strains.
    '''
    strain_index = df[df['Strain'] == strain_user_likes].index[0]
    return strain_index


def get_strain_from_index(index):
    '''Get strains from your index.
    '''
    strain_name = df.iloc[index][0]
    return strain_name


def column_contains(df, column, query):
    '''Returns rows based on condition.
    '''
    return df[df[column].str.contains(query)]


def drop_duplicates(df):
    '''Drops duplicate rows in dataframe
    '''
    df = df.drop_duplicates(keep='first')
    return df


# create a count matrix from new combined column

# instantiate an object of CountVectorizer class
cv = CountVectorizer()

# apply fit transform onto our combined column
count_matrix = cv.fit_transform(df['combined_features'])

# calculate cosine-similarity between items
cosine_sim = cosine_similarity(count_matrix)

strain_user_likes='Skywalker'

strain_index = get_index_from_strain(strain_user_likes)

## find similar strains
## enumerate assigns an index 
## list casts our result as list
similar_strains = list(enumerate(cosine_sim[strain_index]))

## sort similar strains so most close are at the top
sorted_similar_strains = sorted(similar_strains, key= lambda x:x[1], reverse=True)

## print 10 closest strain names
i = 0
result = for strain in sorted_similar_strains:
            print(get_strain_from_index(strain[0]))
            i = i + 1
            if i > 11:
                break