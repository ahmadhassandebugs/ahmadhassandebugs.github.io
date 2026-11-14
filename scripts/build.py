"""Build the portfolio with Python 3's standard library only."""
from pathlib import Path
import re, html, shutil, datetime, hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
shutil.copytree(ROOT/'assets', OUT/'assets')
(OUT/'.nojekyll').touch()
STYLE_FILE='style.'+hashlib.sha256((ROOT/'style.css').read_bytes()).hexdigest()[:12]+'.css'
shutil.copyfile(ROOT/'style.css', OUT/STYLE_FILE)
def esc(s): return html.escape(str(s), quote=True)
def source(p):
    text=p.read_text(encoding="utf-8"); parts=text.split('---',2)
    return (dict(re.findall(r'^([\w-]+):\s*(.*)$',parts[1],re.M)),parts[2].strip()) if len(parts)==3 else ({},text)
def inline(s):
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)',r'<em>\1</em>',s)
def markdown(s):
    blocks=[]
    for b in re.split(r'\n\s*\n',s):
        b=b.strip()
        if not b: continue
        if b.startswith('```'):
            blocks.append('<pre><code>'+esc(b.strip('`').strip())+'</code></pre>')
        elif re.match(r'^\d+\. ',b):
            blocks.append('<ol>'+''.join('<li>'+inline(re.sub(r'^\d+\. ', '', x))+'</li>' for x in b.splitlines())+'</ol>')
        elif b.startswith('#'):
            m=re.match(r'(#{1,6})\s+(.+)',b); blocks.append(f'<h{len(m[1])}>{inline(m[2])}</h{len(m[1])}>' if m else inline(b))
        elif b.startswith('- '): blocks.append('<ul>'+''.join('<li>'+inline(x[2:])+'</li>' for x in b.splitlines() if x.startswith('- '))+'</ul>')
        elif b.startswith('<'): blocks.append(inline(b))
        else: blocks.append('<p>'+inline(b)+'</p>')
    return '\n'.join(blocks)
def page(title,body,path='',active='home',desc='Ahmad Hassan — Senior Software Engineer at TikTok. Applied AI, systems, and networking.'):
    dest=OUT/path/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True)
    nav=''.join(f'<a {"aria-current=page" if active==key else ""} href="{url}">{label}</a>' for key,url,label in [('home','/','About'),('blog','/blog/','Blog'),('pub','/#publications','Publications'),('cv','/assets/pdf/ahmad_hassan_cv.pdf','CV')])
    dest.write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} · Ahmad Hassan</title><meta name="description" content="{esc(desc)}"><link rel="stylesheet" href="/{STYLE_FILE}"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%231d514a'/%3E%3Ctext x='32' y='43' text-anchor='middle' font-family='serif' font-size='38' fill='white'%3Ea%3C/text%3E%3C/svg%3E"></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="/">ahmad hassan<span>.</span></a><nav aria-label="Main navigation">{nav}</nav></header><main id="main">{body}</main><footer><span>Ahmad Hassan</span><span>Built simply. Written personally.</span><a href="mailto:ahmadhassansandhu@gmail.com">Get in touch ↗</a></footer></body></html>''', encoding="utf-8")
posts=[]
for p in sorted((ROOT/'_posts').glob('*.md'),reverse=True):
    meta,body=source(p)
    slug=p.stem[11:]; url='/blog/'+slug+'/'
    meta['display_date']=datetime.date.fromisoformat(meta.get('date', p.stem[:10])[:10]).strftime('%B %d, %Y')
    posts.append((meta,url))
    page(meta['title'],f'<article class="article"><a class="back" href="/blog/">← All writing</a><p class="eyebrow">{meta["display_date"]} · {max(1,round(len(body.split())/200))} min read</p><h1>{esc(meta["title"])}</h1><div class="prose">{markdown(body)}</div></article>','blog/'+slug,'blog')
writing=''.join(f'<a class="post" href="{u}"><span class="date">{esc(m["display_date"].upper())}</span><div><h3>{esc(m["title"])}</h3><p>{esc(m.get("description",""))}</p></div><span aria-hidden="true">↗</span></a>' for m,u in posts)
page('Blog','<section class="blog-head"><p class="eyebrow">Notes from the work</p><h1>Writing<span>.</span></h1><p class="lede">Short reflections on engineering, applied AI, and finding my way after a PhD. One idea at a time.</p></section>'+writing,'blog','blog')
news=[('<time datetime="2026-05">May 2026</time>','Joined <strong>TikTok</strong> as a Senior Software Engineer on the AI Governance team.')]
for p in sorted((ROOT/'_news').glob('*.md'),reverse=True):
    m,b=source(p); date=m['date'][:10]; year,month=map(int,date.split('-')[:2]); label=datetime.date(year,month,1).strftime('%b %Y')
    b=re.sub(r'<span[^>]*>(.*?)</span>',r'\1',b,flags=re.S).replace('<br>',' ')
    news.append((f'<time datetime="{date}">{label}</time>',inline(b)))
newshtml=''.join(f'<li>{d}<div>{b}</div></li>' for d,b in news)
bib=(ROOT/'_bibliography/papers.bib').read_text(); pubs=[]
for entry in re.split(r'\n@',bib)[1:]:
    def field(name):
        m=re.search(r'\b'+name+r'\s*=\s*\{([^}]+)\}',entry); return m[1] if m else ''
    if field('selected')!='true': continue
    links=' '.join(f'<a href="{esc(url)}">{label} ↗</a>' for label,url in [('Paper','/assets/pdf/'+field('pdf')),('DOI',field('url'))] if url)
    pubs.append(f'<li><span class="venue">{esc(field("abbr"))} {esc(field("year"))}</span><h3>{esc(field("title"))}</h3><p class="authors">{esc(field("author").replace(" and ","; "))}</p><div class="paper-links">{links}</div></li>')
about='''<section class="intro"><div><p class="eyebrow">Systems thinking. Applied AI.</p><h1>Ahmad<br>Hassan<span>.</span></h1><p class="role">Senior Software Engineer at <a href="https://www.tiktok.com/">TikTok ↗</a></p><p class="previous">Previously: Samsung · HPE · USC · UMN · LUMS</p><div class="social"><a href="mailto:ahmadhassansandhu@gmail.com">Email ↗</a><a href="https://www.linkedin.com/in/ahmadhassandebugs/">LinkedIn ↗</a><a href="https://github.com/ahmadhassandebugs">GitHub ↗</a><a href="https://scholar.google.com/citations?user=2y0cZ1wAAAAJ">Scholar ↗</a></div></div><figure><img src="/assets/img/profile_pic_2.jpg" alt="Ahmad Hassan" width="320" height="380"><figcaption>Engineer. Researcher. Always curious.</figcaption></figure></section><section class="about-text"><p>At TikTok, I'm on the <strong>AI Governance</strong> team. We build algorithms and infrastructure for offline <strong>evaluation</strong> and online <strong>alignment</strong> of fairness-related behavior in large vision, language, and multimodal models. I work on both the ML/algo side and the systems/backend side.</p><p>I earned my Ph.D. at USC, advised by Prof. <a href="https://www-users.cse.umn.edu/~fengqian/index.html">Feng Qian</a>. My graduate research combined <strong>systems, networking, and machine learning</strong>. I designed and evaluated cross-layer systems that trade off user experience, network performance, and device energy. Most of that work was anchored in large-scale measurements, with an emphasis on systems that would survive real deployment.</p></section>'''
page('About',about+'<section id="news"><div class="section-title"><h2>News</h2><span>Milestones & updates</span></div><ul class="news">'+newshtml+'</ul></section><section><div class="section-title"><h2>Writing</h2><a href="/blog/">All posts ↗</a></div>'+writing+'</section><section id="publications"><div class="section-title"><h2>Selected publications</h2><a href="https://scholar.google.com/citations?user=2y0cZ1wAAAAJ">Google Scholar ↗</a></div><ol class="publications">'+''.join(pubs)+'</ol></section>')
def redirect(path, target):
    dest=OUT/path/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page moved</title><link rel="canonical" href="{esc(target)}"><meta http-equiv="refresh" content="0;url={esc(target)}"><a href="{esc(target)}">Continue to the page</a></html>', encoding='utf-8')
for p in (ROOT/'_posts').glob('*.md'):
    redirect('blog/'+p.stem[:4]+'/'+p.stem[11:], '/blog/'+p.stem[11:]+'/')
redirect('publications','/#publications')
redirect('news','/#news')
redirect('about','/')
redirect('cv','/assets/pdf/ahmad_hassan_cv.pdf')
# Retain existing project URLs linked from news and publications.
for p in (ROOT/'_projects').glob('*.md'):
    m,b=source(p); slug=p.stem
    if slug in ('opcm','wixor'):
        # Keep the detailed research pages, replacing Jekyll-only figure tags.
        raw=p.read_text(encoding='utf-8').split('---',2)[1]
        styles=raw.split('_styles: >',1)[1] if '_styles: >' in raw else ''
        b=re.sub(r'<!--.*?-->', '', b, flags=re.S)
        b=re.sub(r'## Demo Videos\n.*?(?=\n## |\Z)', '', b, flags=re.S)
        def figure(match):
            attrs=dict(re.findall(r'(\w+)=\"([^\"]*)\"',match[1]))
            return '<img src="/'+esc(attrs.get('path',''))+'" alt="'+esc(attrs.get('title',''))+'" loading="lazy">'
        b=re.sub(r'{% include figure.liquid (.*?) %}', figure, b)
        b+='\n\n[Read the paper](/assets/pdf/'+('opcm_conext25.pdf' if slug=='opcm' else 'wixor_conext24.pdf')+')'
        page(m.get('title',slug),'<style>'+styles+'</style><article class="project"><div class="project-content">'+markdown(b)+'</div></article>','projects/'+slug)
page('Projects','<section class="blog-head"><h1>Projects<span>.</span></h1><p><a href="/projects/opcm/">OPCM</a> · <a href="/projects/wixor/">Wixor</a></p></section>','projects')
page('Page not found','<section class="blog-head"><h1>Page not found.</h1><p><a href="/">Return to the homepage →</a></p></section>','404')
shutil.copyfile(OUT/'404/index.html',OUT/'404.html')
shutil.copyfile(ROOT/'robots.txt', OUT/'robots.txt')
if (ROOT/'CNAME').exists(): shutil.copyfile(ROOT/'CNAME',OUT/'CNAME')
print(f'Built {len(list(OUT.rglob("*.html")))} pages; {len(pubs)} selected publications; {len(news)} news items.')
