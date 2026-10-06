import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Premium Font (Plus Jakarta Sans)
if 'Plus+Jakarta+Sans' not in html:
    font_link = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    /* Premium Animations & Shadows */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.08);
    }
    .premium-gradient {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    }
'''
    html = html.replace('<style>', font_link)

# 2. Main Background (Soft elegant off-white)
html = html.replace('body class="bg-white text-gray-900', 'body class="bg-slate-50 text-slate-800')

# 3. Main Login Card
html = html.replace('bg-white rounded-sm shadow-none border border-gray-200 overflow-hidden border border-gray-100', 'glass-card rounded-[2rem] overflow-hidden')

# 4. Login Left Banner
html = html.replace('bg-white text-gray-900 border-r border-gray-200 p-8 sm:p-10 flex flex-col justify-between relative overflow-hidden', 'premium-gradient text-white p-10 flex flex-col justify-between relative overflow-hidden')

# 5. Fix text colors inside the new dark premium gradient
html = html.replace('text-blue-200 font-semibold', 'text-blue-100 font-semibold')
html = html.replace('text-gray-500 text-xs mt-3', 'text-blue-100 text-sm mt-3 opacity-90')
html = html.replace('bg-blue-900/30 text-blue-200', 'bg-white/20 text-white backdrop-blur-md')
html = html.replace('border-blue-700/50 mb-6', 'border-white/30 mb-6')
html = html.replace('text-5xl font-medium tracking-tight text-black mb-4 tracking-tight', 'text-5xl font-bold tracking-tight text-white mb-2')

# 6. Global Buttons (Creative & Neat)
html = html.replace('bg-black', 'bg-blue-600')
html = html.replace('hover:bg-gray-800', 'hover:bg-blue-700')
html = html.replace('rounded-sm', 'rounded-xl') # Elegant soft corners
html = html.replace('shadow-none border border-gray-200', 'shadow-sm border border-slate-200')

# 7. Other UI Containers
html = html.replace('bg-gray-50', 'bg-white shadow-sm border border-slate-100')
html = html.replace('bg-gray-100 text-gray-900', 'bg-slate-50 text-slate-800 border border-slate-200')

# Fix the duplicate text-white if any
html = html.replace('text-white text-white', 'text-white')

# Ensure the app sections are beautifully spaced
html = html.replace('min-h-screen flex items-center justify-center p-4', 'min-h-screen flex items-center justify-center p-6 sm:p-12')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Executed Premium Creative UI overhaul.')
