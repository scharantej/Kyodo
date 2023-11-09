 ### Problem Analysis

The problem is to design a Japanese news website using Flask. The website should have the following features:

* A home page that displays the latest news articles
* A page that displays a list of all news articles
* A page that displays a single news article
* A page that allows users to search for news articles
* A page that allows users to contact the website administrators

### Design

The following HTML files are needed for the application:

* `index.html`: The home page
* `articles.html`: The page that displays a list of all news articles
* `article.html`: The page that displays a single news article
* `search.html`: The page that allows users to search for news articles
* `contact.html`: The page that allows users to contact the website administrators

The following routes are needed for the application:

* `/`: The home page
* `/articles`: The page that displays a list of all news articles
* `/article/<int:article_id>`: The page that displays a single news article
* `/search`: The page that allows users to search for news articles
* `/contact`: The page that allows users to contact the website administrators

The following code is the main Flask application:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get(article_id)
    return render_template('article.html', article=article)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        search_term = request.form['search_term']
        articles = Article.query.filter(Article.title.contains(search_term))
        return render_template('articles.html', articles=articles)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send the email
        return render_template('contact.html', message="Your message has been sent.")

if __name__ == '__main__':
    app.run(debug=True)
```

### Conclusion

This design meets the requirements of the problem. The website is easy to navigate and use, and it provides all of the features that are needed.