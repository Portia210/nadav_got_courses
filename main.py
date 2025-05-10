import os
import re
from ai_article_analysis import analyze_article

def read_file_and_split_to_lessons(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # check if the spliter is open the line with the number
        articles = re.split(r'(\n?\d+[\)])', content)
        articles = [article.strip() for article in articles if article.strip()]
        # create a new dict that take the odd values in articles as the index of the even values
        articles = {re.sub(r'\D+', '', articles[i]): articles[i+1] for i in range(0, len(articles), 2)}
    if not articles:
        return None
    
    for key, article in articles.items():
        # split the article to name and body
        article_name = article.split('\n')[0]
        # remove all the Illegal Filename Characters
        article_name = re.sub(r'[\/:*?"<>|]', '', article_name)
        article_body = '\n'.join(article.split('\n')[1:])
        articles[key] = (article_name, article_body)
    return articles if articles else None



def create_folder_and_save_articles(dir_name, articles):
    os.makedirs(dir_name, exist_ok=True)
    for key, (article_name, article_body) in articles.items():
        file_path = os.path.join(dir_name, f"{key}) {article_name}.md")
        if os.path.exists(file_path):
            continue
        print(f"starting to analyze {article_name}")
        article_analysis = analyze_article(f"article name: {article_name}\narticle body: {article_body}", f"the content discussesed in the article is the topic that you should expand on, if there are linux commands in the article, *ALSO* add more information about the commands, popular usage and options")
        if not article_analysis:
            continue
        with open(f"{dir_name}/{key}) {article_name}.md", 'w', encoding='utf-8') as file:
            file.write(article_analysis)


def main():
    input_file_path = "טכנולוגיות ענן.txt"
    output_file_path = "cloud_basic/lessons_summaries"
    articles = read_file_and_split_to_lessons(input_file_path)
    if not articles:
        print("Error: Failed to parse the file")
        return
    create_folder_and_save_articles(output_file_path, articles)

if __name__ == "__main__":
    main()



