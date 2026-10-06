import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Strip ALL Emojis (The biggest cause of a 'childish' look)
emojis = ['🤝', '🐢', '🙏', '☕', '🌸', '🎙️', '🛑', '💡', '🎶', '🚂', '🎓', '✅', '🔴', '⚠️', '✨', '👴', '🛡️', '👨‍⚕️', '👵', '📻', '🎧']
for e in emojis:
    html = html.replace(e, '')

# 2. Sharpen all borders to strict enterprise standard (rounded-md / rounded-lg)
html = html.replace('rounded-2xl', 'rounded-lg')
html = html.replace('rounded-xl', 'rounded-lg')
html = html.replace('rounded-3xl', 'rounded-lg')
html = html.replace('rounded-full', 'rounded-md') # For pills/tags

# Restore rounded-full specifically for avatars/status dots if needed, but square avatars are fine for enterprise.
html = html.replace('w-3 h-3 rounded-md', 'w-3 h-3 rounded-full')
html = html.replace('w-2 h-2 rounded-md', 'w-2 h-2 rounded-full')
html = html.replace('w-12 h-12 rounded-md', 'w-12 h-12 rounded-full')

# 3. Simplify shadows
html = html.replace('shadow-2xl', 'shadow-md')
html = html.replace('shadow-xl', 'shadow-md')
html = html.replace('shadow-lg', 'shadow-sm')

# 4. Remove ANY remaining gradients
html = html.replace('bg-gradient-to-br', '')
html = html.replace('bg-gradient-to-r', '')
html = html.replace('from-slate-900 to-slate-950', 'bg-white')
html = html.replace('from-blue-600 to-blue-800', 'bg-blue-700')

# 5. Clean up overly colorful semi-transparent buttons in the call controls
# Change them to professional outlined buttons
html = html.replace('bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40', 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50')
html = html.replace('bg-amber-400/20 hover:bg-amber-400/30 text-amber-300 border border-amber-400/40', 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50')
html = html.replace('bg-orange-500/20 hover:bg-orange-500/30 text-orange-300 border border-orange-500/40', 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50')
html = html.replace('bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/40', 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50')

# Fix text colors inside the call modal that were yellow/pink to standard dark gray
html = html.replace('text-amber-400', 'text-blue-600')
html = html.replace('text-amber-300', 'text-gray-600')

# 6. Change all 'slate' to 'gray' for a true neutral enterprise look (removing the blue tint of slate)
html = html.replace('slate-', 'gray-')

# 7. Make the app background very clean
html = html.replace('bg-gray-50', 'bg-white')
html = html.replace('bg-white/40', 'bg-white')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Executed extreme Enterprise UI overhaul.')
