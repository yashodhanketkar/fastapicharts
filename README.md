<h1>API for Charts</h1>

API for charts using FastAPI

<h2>Tech Stack</h2>
<ul>
  <li>FastAPI</li>
  <li>MongoDB Atlas</li>
</ul>

<h2>Installation</h2>
<h3>Prerequisite</h3>
<ul>
  <li>Python 3</li>
  <li>Local MongoDB Server/Atlas</li>
</ul>

<h3>Steps</h3>

<h4>Install dependecies using</h4>

```py
# install requirements
pip install -r requirements.txt
```

<h4>Database configuration</h4>

Method 1: Store your MongoDB url inside os environment as <i>MONGO_URL</i>

Method 2: Replace value of <i>MONGO_URL</i> inside <code>app\server\database.py</code> with your MongoDB url

<h4>Run program using</h4>

```py
# for windows
py app\main.py

# for linux
python3 app/main.py

```
After starting server go to http://127.0.0.1:5555/docs for more info

<h2>Licence</h2>

MIT License

<h5>Copyright (c) 2023 Yashodhan Ketkar</h5>