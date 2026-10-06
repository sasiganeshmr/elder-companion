import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="loginView"')
print(html[start-30:start+1500])
