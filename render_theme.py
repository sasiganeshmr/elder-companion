import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Global background to pure white
html = html.replace('body class="bg-white text-gray-800', 'body class="bg-white text-gray-900')
html = html.replace('bg-gray-50', 'bg-white')

# 2. Remove all shadows, replace with crisp 1px borders
html = html.replace('shadow-md', 'shadow-none border border-gray-200')
html = html.replace('shadow-sm', 'shadow-none border border-gray-200')
html = html.replace('shadow-lg', 'shadow-none border border-gray-200')

# 3. Change all rounded corners to extremely sharp (rounded-sm)
html = html.replace('rounded-lg', 'rounded-sm')
html = html.replace('rounded-xl', 'rounded-sm')
html = html.replace('rounded-2xl', 'rounded-sm')

# 4. Make all Primary buttons solid black (Render style)
html = html.replace('bg-blue-600', 'bg-black')
html = html.replace('bg-blue-700', 'bg-black')
html = html.replace('hover:bg-blue-700', 'hover:bg-gray-800')
html = html.replace('hover:bg-blue-800', 'hover:bg-gray-800')
html = html.replace('text-blue-700', 'text-black')
html = html.replace('text-blue-600', 'text-black')

# 5. Make the login hero section ultra-minimalist (White instead of Dark)
html = html.replace('bg-gray-900 text-white', 'bg-white text-gray-900 border-r border-gray-200')
html = html.replace('text-indigo-200', 'text-gray-500')
html = html.replace('text-gray-300', 'text-gray-500')
html = html.replace('text-white', 'text-gray-900') # Flip white text on dark backgrounds to black

# Fix a specific dark mode background from the earlier theme
html = html.replace('bg-slate-900', 'bg-gray-50')
html = html.replace('bg-gray-900', 'bg-white')

# 6. Change heading to match Render's massive, tight font
html = html.replace('text-3xl font-extrabold', 'text-5xl font-medium tracking-tight text-black mb-4')
html = html.replace('font-bold', 'font-medium')

# 7. Button outlines (Render uses black/white contrast)
html = html.replace('bg-gray-100', 'bg-white border border-gray-200')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Executed Render-style UI overhaul.')
