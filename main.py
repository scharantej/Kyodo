 
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


 수정된 코드 


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
