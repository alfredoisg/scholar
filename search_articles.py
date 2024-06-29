from scholarly import scholarly
import pandas as pd
import matplotlib.pyplot as plt
import argparse

import scienceplots

plt.style.use(['science','notebook', 'grid'])


def search_articles(keyword, start_year, end_year):
    search_query = scholarly.search_pubs(keyword)
    articles = []

    for pub in search_query:
        pub_year = pub.bib.get('pub_year')
        if pub_year and start_year <= int(pub_year) <= end_year:
            articles.append(pub_year)
    
    return articles

def plot_articles_per_year(articles):
    df = pd.DataFrame(articles, columns=['Year'])
    df['Count'] = 1
    df = df.groupby('Year').count().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Count'], marker='o')
    plt.title('Number of Articles Containing Keyword per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Search and plot the number of articles containing a keyword per year.')
    parser.add_argument('keyword', type=str, help='Keyword to search in article titles')
    parser.add_argument('start_year', type=int, help='Start year for the search')
    parser.add_argument('end_year', type=int, help='End year for the search')

    args = parser.parse_args()

    articles = search_articles(args.keyword, args.start_year, args.end_year)
    plot_articles_per_year(articles)

if __name__ == "__main__":
    main()

