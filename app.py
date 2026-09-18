from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

posts = [
    {"username": "vishnu_coder", "caption": "Coding in progress! 🚀", "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c"},
    {"username": "cyber_guy", "caption": "Exploring Linux & Termux terminal...", "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5"}
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini Instagram</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #fafafa; margin: 0; padding: 0; color: #262626; }
        header { background: white; border-bottom: 1px solid #dbdbdb; padding: 15px; text-align: center; font-size: 24px; font-weight: bold; font-family: cursive; }
        .container { max-width: 500px; margin: 20px auto; padding: 0 10px; }
        .card { background: white; border: 1px solid #dbdbdb; margin-bottom: 20px; border-radius: 3px; }
        .card-header { padding: 10px; font-weight: bold; border-bottom: 1px solid #efefef; }
        .card img { width: 100%; height: auto; }
        .card-body { padding: 10px; }
        .upload-box { background: white; border: 1px solid #dbdbdb; padding: 15px; margin-bottom: 20px; border-radius: 3px; }
        input[type="text"], input[type="url"] { width: 100%; padding: 8px; margin: 5px 0 10px 0; border: 1px solid #dbdbdb; border-radius: 3px; box-sizing: border-box; }
        button { background: #0095f6; color: white; border: none; padding: 8px 15px; border-radius: 3px; cursor: pointer; font-weight: bold; width: 100%; }
    </style>
</head>
<body>
    <header>MiniInstagram</header>
    <div class="container">
        <div class="upload-box">
            <h3>Nayi Post Banayein</h3>
            <form action="/post" method="POST">
                <label>Username:</label>
                <input type="text" name="username" placeholder="Aapka naam" required>
                <label>Image URL:</label>
                <input type="url" name="image" placeholder="Photo ka direct link dalein" required>
                <label>Caption:</label>
                <input type="text" name="caption" placeholder="Kuch likhiye..." required>
                <button type="submit">Post Karein</button>
            </form>
        </div>

        {% for post in posts %}
        <div class="card">
            <div class="card-header">@{{ post.username }}</div>
            <img src="{{ post.image }}" alt="Post Image">
            <div class="card-body">
                <p><b>@{{ post.username }}</b> {{ post.caption }}</p>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, posts=posts)

@app.route('/post', methods=['POST'])
def add_post():
    username = request.form.get('username')
    image = request.form.get('image')
    caption = request.form.get('caption')
    if username and image and caption:
        posts.insert(0, {"username": username, "image": image, "caption": caption})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
<div class="nav-bar"> <a href="#">Reel</a> <a href="#">Like</a> <a href="#">Profile</a> </div>.
