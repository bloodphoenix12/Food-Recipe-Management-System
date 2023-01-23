import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Product


def combined_features(row):
    return row['name'] + "" + row['Ingredients'] + "" + row['Instructions']


def get_id_from_index(df, index):
    return df[df.index == index]["id"].values[0]


def get_index_from_id(df, id):
    return df[df.id == id].index.values[0]


def get_recommendation_recipes(movie_id):
    df = pd.DataFrame(list(Product.objects.all().values()))
    features = ['name', 'Ingredients', 'Instructions']
    for feature in features:
        df[feature] = df[feature].fillna('')

    df["combined_features"] = df.apply(combined_features, axis=1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    id = get_index_from_id(df, movie_id)

    similar_recipes = list(enumerate(cosine_sim[id]))

    sorted_similar_recipes = sorted(
        similar_recipes, key=lambda x: x[1], reverse=True
    )

    i = 1
    recipe_ids = []
    for recipe in sorted_similar_recipes:
        i = i + 1
        recipe_ids.append(get_id_from_index(df, recipe[0]))

        if i > 39:
            break

    return recipe_ids
