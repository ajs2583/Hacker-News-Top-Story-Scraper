from bs4 import BeautifulSoup
import requests


def get_top_rated_story():
    response = requests.get("https://news.ycombinator.com/news")
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")

    # Grab all span elements with the class "titleline" which contain the article titles
    article_span = soup.find_all(name="span", class_="titleline")
    article_texts = []
    article_links = []

    # Iterate through each span element found
    for tag in article_span:
        # Find the anchor tag within the span element
        article_tag = tag.find(name="a")

        # Get the text inside the anchor tag (article title)
        texts = article_tag.get_text()
        article_texts.append(texts)

        # Get the href attribute of the anchor tag (article link)
        link = article_tag.get("href")
        article_links.append(link)

        # Find the span element with the class "score" to get the article score
        article_scores = [
            int(score.get_text().split()[0])
            for score in soup.find_all(name="span", class_="score")
        ]

        max_upvote_index = article_scores.index(max(article_scores))

    # Retrieve corresponding elements
    print(f"Title: {article_texts[max_upvote_index]}")
    print(f"Link: {article_links[max_upvote_index]}")
    print(f"Score: {article_scores[max_upvote_index]}")


if __name__ == "__main__":
    get_top_rated_story()
    