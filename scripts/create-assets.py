from pathlib import Path
from urllib.request import Request,urlopen
import re,html
p=Path('public/images');p.mkdir(exist_ok=True)
for family,name in [('Space Grotesk','space-grotesk'),('Inter','inter'),('JetBrains Mono','jetbrains-mono')]:
 url='https://fonts.googleapis.com/css2?family='+family.replace(' ','+')+':wght@400..700&display=swap'
 css=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})).read().decode()
 links=re.findall(r'url\((https://[^)]+)\)',css)
 data=urlopen(links[-1]).read();Path('public/fonts/'+name+'.woff2').write_bytes(data)
 print(name,len(data))

def text(x,y,t,size=18,color='#f5f5f7',weight=400):return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(t)}</text>'
def rect(x,y,w,h,fill,rx=12,stroke='none'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
cases=[('paykaro','PayKaro','#7c5cff','#3f23a2','fintech'),('greencart','GreenCart','#30b77d','#0b6149','commerce'),('mednest','MedNest','#22b8cd','#075b78','health'),('yatra-lite','Yatra Lite','#f2aa53','#90501e','travel')]
for slug,title,a,b,kind in cases:
 for v in range(3):
  s=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'+rect(0,0,1200,800,'url(#g)',0)+f'<circle cx="1000" cy="80" r="400" fill="#ffffff0b"/><circle cx="190" cy="780" r="380" fill="#ffffff08"/>'
  if kind in ['fintech','travel']:
   for n in range(2):
    x=270+n*330;y=72+n*65
    s+=rect(x,y,280,600,'#101318',38,'#ffffff50')+rect(x+10,y+10,260,580,'#f7f8fb',30)+rect(x+100,y+18,80,15,'#101318',10)
    s+=text(x+30,y+65,title,21,'#1d2434',700)+text(x+30,y+91,['Make everyday simpler.','Less searching. More going.'][kind=='travel'],11,'#627085')
    if kind=='fintech':
     s+=rect(x+25,y+120,230,125,a,18)+text(x+43,y+151,'YOUR BALANCE',10)+text(x+43,y+195,'₹ 24,850',33,'#fff',700)+text(x+43,y+222,'Ready when you are',11)
     s+=text(x+27,y+283,['Quick payments','Choose your bank'][n],15,'#1d2434',700)
     for i,label in enumerate(['Scan & pay','To a friend','Bank transfer']):
      s+=rect(x+25,y+305+i*66,230,52,'#fff',12,'#e6e8ef')+rect(x+37,y+315+i*66,32,32,a,9)+text(x+48,y+338+i*66,['↗','◎','+'][i],17)+text(x+82,y+337+i*66,label,12,'#344154')
     s+=rect(x+25,y+524,230,42,a,12)+text(x+105,y+550,'Continue',12,'#fff',700)
    else:
     s+=rect(x+25,y+120,230,175,'#c9dbc4',18)+f'<path d="M{x+25} {y+280}L{x+110} {y+155}L{x+185} {y+240}L{x+235} {y+180}L{x+255} {y+295}H{x+25}Z" fill="#4f7562"/>'
     s+=text(x+40,y+327,['A little closer to nature','Your next great escape'][n],13,'#1d2434',700)+text(x+40,y+352,'Coorg, Karnataka',11,'#697483')
     for i,label in enumerate(['Choose your dates','2 travellers · 1 room','Save for later']):s+=rect(x+25,y+374+i*49,230,39,'#fff',10,'#e4e7e9')+text(x+40,y+399+i*49,label,12,'#445164')
     s+=rect(x+25,y+535,230,37,'#754217',9)+text(x+99,y+559,'Explore stays',11,'#fff',700)
  else:
   x=120;y=135
   s+=rect(x,y,960,550,'#f6f8fb',16)+rect(x,y,960,42,'#fff',16)+rect(x,y+30,960,15,'#fff',0)
   for i in range(3):s+=f'<circle cx="{x+24+i*18}" cy="{y+22}" r="5" fill="{a if i==0 else "#d9dce4"}"/>'
   s+=rect(x,y+44,185,506,'#172c30' if kind=='commerce' else '#11313e',0)+text(x+25,y+87,title,22,'#fff',700)
   for i,l in enumerate(['Overview','Appointments' if kind=='health' else 'Discover','People' if kind=='health' else 'My basket','Reports','Settings']):s+=rect(x+14,y+120+i*57,157,40,a if i==0 else 'transparent',8)+text(x+30,y+145+i*57,l,12,'#fff')
   s+=text(x+215,y+90,'Good morning, '+('Dr. Asha' if kind=='health' else 'Ananya')+' 👋',23,'#263640',700)+text(x+215,y+117,'Everything you need, in one place.',13,'#657786')
   for i,l in enumerate(['Today’s appointments','Waiting','Completed'] if kind=='health' else ['Fresh picks','In your basket','Next delivery']):
    s+=rect(x+215+i*235,y+145,218,90,'#fff',12,'#e1e6ec')+text(x+233+i*235,y+170,l,11,'#637781')+text(x+233+i*235,y+211,['24','03','18'][i] if kind=='health' else ['12','06','Today'][i],29,'#1b3945',700)
   s+=rect(x+215,y+260,690,245,'#fff',12,'#e1e6ec')+text(x+238,y+294,'Upcoming appointments' if kind=='health' else 'Good things, picked for you',17,'#17333f',700)
   for i in range(3):
    if kind=='health':
     s+=rect(x+235,y+315+i*55,645,43,'#f5f8fa',8)+f'<circle cx="{x+258}" cy="{y+336+i*55}" r="13" fill="{a}33"/>'+text(x+282,y+341+i*55,['Aarav Sharma','Priya Nair','Sahil Khan'][i],12,'#304652')+text(x+520,y+341+i*55,['10:30 AM','11:00 AM','11:30 AM'][i],11,'#657985')+rect(x+748,y+325+i*55,112,24,a+'25',7)+text(x+767,y+341+i*55,'Confirmed',10,'#12636d')
    else:
     s+=rect(x+236+i*220,y+319,200,160,'#eef6e8',10)+f'<circle cx="{x+336+i*220}" cy="{y+369}" r="30" fill="{["#eaa45a","#7cac58","#d56b50"][i]}"/>'+text(x+250+i*220,y+431,['Farm-fresh oranges','Everyday greens','Seasonal tomatoes'][i],11,'#324a39',700)+text(x+250+i*220,y+456,['₹ 120 / kg','₹ 45 / bunch','₹ 35 / kg'][i],11,'#5d7062')
  s+=text(34,755,f'{title.upper()}   /   '+['PRODUCT CONCEPT','INTERACTION STUDY','DESIGN EXPLORATION'][v],13,'#fff',600)+text(900,755,'FICTIONAL DEMO UI',12,'#fff')+'</svg>'
  if v: s=s.replace('viewBox="0 0 1200 800"','viewBox="0 0 1200 800"').replace(f'fill="{a}"',f'fill="{[a,b][v%2]}"')
  (p/f'{slug}-{v}.svg').write_text(s)
Path('public/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="43" fill="white" font-family="Arial" font-size="29" font-weight="700" text-anchor="middle">km</text></svg>')
(p/'avatar.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="#7c5cff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs><rect width="500" height="500" rx="50" fill="#171c2b"/><circle cx="250" cy="240" r="190" fill="url(#g)" opacity=".2"/><path d="M95 500V410Q100 310 250 310Q400 310 405 410V500" fill="#7c5cff"/><path d="M212 290H288V355Q250 390 212 355Z" fill="#c88f6d"/><ellipse cx="250" cy="220" rx="91" ry="108" fill="#e0a681"/><path d="M159 225Q120 95 250 90Q365 90 345 210L320 160Q265 190 185 155L180 230Z" fill="#121725"/><path d="M184 213H235V243H184ZM265 213H316V243H265Z" fill="none" stroke="#192130" stroke-width="9"/><path d="M235 224H265" stroke="#192130" stroke-width="6"/><path d="M220 277Q250 299 280 277" fill="none" stroke="#824b3b" stroke-width="6" stroke-linecap="round"/><text x="250" y="458" font-family="monospace" font-size="23" fill="#fff" text-anchor="middle">&lt; always curious /&gt;</text></svg>')
for i in range(9):
 a,b=cases[i%4][2:4]
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>'+rect(0,0,600,450,'#141925',0)
 if i%3==0:
  for j in range(7):s+=f'<ellipse cx="300" cy="225" rx="{175-j*19}" ry="{145-j*12}" fill="none" stroke="url(#g)" stroke-width="14" transform="rotate({j*13+i*12} 300 225)"/>'
 elif i%3==1:
  s+=rect(110,85,380,280,'#222a3b',24)+text(140,127,'DESIGN / '+str(i+1),12,'#cbd4e3')+text(140,195,['Aa','01','km.'][i//3],68,'#fff',700)
  for j in range(5):s+=rect(140+j*58,235,46,70,a,10).replace(f'fill="{a}"',f'fill="{a}" opacity="{1-j*.16}"')
 else:
  for j in range(5):s+=rect(140+j*25,110+j*19,260,190,'url(#g)',20,'#ffffff50')
  s+=text(290,270,'Make it feel right.',20,'#fff',700)
 s+=text(24,422,f'EXPERIMENT {i+1:02d}',11,'#c7cee0')+'</svg>'
 (p/f'play-{i+1}.svg').write_text(s)
print('Original SVG assets written')
