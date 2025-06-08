import pandas as pd
import os

def load_movie(data_path):
    return pd.read_csv(os.path.join(data_path, 'movie.csv'))

def load_rating(data_path):
    return pd.read_csv(os.path.join(data_path, 'rating.csv'))

def load_tag(data_path):
    return pd.read_csv(os.path.join(data_path, 'tag.csv'))

def load_link(data_path):
    return pd.read_csv(os.path.join(data_path, 'link.csv'))

def load_genome_scores(data_path):
    return pd.read_csv(os.path.join(data_path, 'genome_scores.csv'))

def load_genome_tags(data_path):
    return pd.read_csv(os.path.join(data_path, 'genome_tags.csv'))
