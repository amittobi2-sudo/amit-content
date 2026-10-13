import json, os, re, sys, html
G = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, G)
from articles import ARTICLES
from articles_a import ARTICLES_A
from articles_b import ARTICLES_B, LANDINGS
OUT, BASE = sys.argv[1], sys.argv[2].rstrip('/')
PUB = "2026-10-13"
ALL_ARTICLES = ARTICLES + ARTICLES_A + ARTICLES_B
def sec(n): return open(f"{G}/sec_{n}.html", encoding="utf-8").read()
CSS = open(f"{G}/style.css", encoding="utf-8").read()

# ---------- section patches (audit fixes) ----------
HERO = sec("hero").replace('<h1>עמית טובי.<br><span>10 עסקים, 150 עובדים</span><br>ושיטה אחת שנולדה מהשטח.</h1>',
  '<h1>עמית טובי. <br><span>10 עסקים, 150 עובדים</span> <br>ושיטה אחת שנולדה מהשטח.</h1>')
HERO = HERO.replace('</p>\n  <div class="stats"', ' <a href="/about/" style="color:var(--signal)">הסיפור המלא ←</a></p>\n  <div class="stats"',1)
BUS = sec("businesses")
BUS = re.sub(r'<td><a href="https://www\.facebook\.com/[^"]*"[^>]*>לוצ\'נה דיסיטי מעלה אדומים</a></td>', '<td><a href="/businesses/luciana/">לוצ\'נה דיסיטי מעלה אדומים</a></td>', BUS)
BUS = re.sub(r'<td><a href="https://www\.instagram\.com/ameat_chef/"[^>]*>ameat</a></td>', '<td><a href="/businesses/ameat/">ameat</a></td>', BUS)
BUS = BUS.replace('<td>Breezy</td>','<td><a href="/businesses/breezy/">Breezy</a></td>').replace('<td>גלידרייה</td>','<td><a href="/articles/hefsed-shel-2-milyon/">גלידרייה</a></td>').replace('<td>פרקטי ייעוץ עסקי</td>','<td><a href="/prakti/">פרקטי ייעוץ עסקי</a></td>')
COMM = sec("community").replace("בעלי עסקים שעמית ליווה","לקוחות פרקטי ייעוץ עסקי")
RES = sec("results"); REV = sec("reviews"); FAQ = sec("faq")
def teaser_cards(section, n, link, label):
    cards = re.findall(r'<div class="case">.*?</div>(?=\s*<div class="case">|\s*</div>)', section, re.S)
    head = re.search(r'(<section id="\w+"><div class="wrap">\s*<div class="stack">.*?</div>)', section, re.S).group(1)
    return head + '<div class="grid2">' + "".join(cards[:n]) + f'</div><p><a class="btn" href="{link}">{label}</a></p></div></section>'
HOME_RES = teaser_cards(RES, 4, "/results/", "כל התוצאות ←")
HOME_REV = teaser_cards(REV, 3, "/reviews/", "כל ההמלצות ←")

# ---------- schema ----------
PERSON = {"@type":"Person","@id":BASE+"/#amit-tobi","name":"עמית טובי","givenName":"עמית","familyName":"טובי",
 "alternateName":["Amit Tobi","Amit Tubi","Amit Toby","Amit Tovi"],"url":BASE+"/","mainEntityOfPage":BASE+"/about/",
 "image":BASE+"/img/og.png","jobTitle":["יזם","יועץ עסקי","מרצה"],
 "description":"יזם, יועץ עסקי ומרצה ישראלי. הקים, ניהל או היה שותף ביותר מ-10 עסקים, ניהל במצטבר יותר מ-150 עובדים וליווה יותר מ-500 בעלי עסקים. מייסד-שותף בפרקטי ייעוץ עסקי ו-Master Profiler בשפת גוף.",
 "birthDate":"1998","nationality":{"@type":"Country","name":"Israel"},"worksFor":{"@id":BASE+"/#prakti"},
 "alumniOf":{"@type":"EducationalOrganization","name":"דן גורמה"},
 "hasCredential":{"@type":"EducationalOccupationalCredential","name":"Master Profiler","recognizedBy":{"@type":"Person","name":"איתן שגב"}},
 "knowsAbout":["ייעוץ עסקי","יזמות","שיווק","מכירות","ניהול עובדים","גיוס עובדים","תמחור","תזרים מזומנים","משא ומתן","פסיכולוגיה צרכנית","שפת גוף","מיקרו-הבעות","קריאת תווי פנים","פרופיילינג","טונציה","ניהול זמן","מסעדנות"],
 "sameAs":["https://www.instagram.com/amit_tobi_/","https://www.instagram.com/ameat_chef/","https://praktibusiness.com/","https://e-club.biz/our-staff/%D7%A2%D7%9E%D7%99%D7%AA-%D7%98%D7%95%D7%91%D7%99/"]}
ORGS = [{"@type":"Organization","@id":BASE+"/#prakti","name":"פרקטי ייעוץ והדרכה בע\"מ","alternateName":["פרקטי ייעוץ עסקי","Prakti","Practi"],"url":"https://praktibusiness.com/","areaServed":"IL",
  "founder":[{"@id":BASE+"/#amit-tobi"},{"@type":"Person","name":"דור שלום"},{"@type":"Person","name":"עומר וסרמן"}]},
 {"@type":"ProfessionalService","@id":BASE+"/#ameat","name":"ameat שף פרטי","url":BASE+"/businesses/ameat/","sameAs":["https://www.instagram.com/ameat_chef/"],"founder":{"@id":BASE+"/#amit-tobi"},"areaServed":"IL"}]

NAV_HE = [("/","בית"),("/about/","מי זה עמית טובי"),("/prakti/","פרקטי"),("/results/","תוצאות"),("/reviews/","המלצות"),("/articles/","מאמרים"),("/en/","English")]
NAV_EN = [("/en/","Amit Tobi"),("/","עברית"),("/results/","Results"),("/prakti/","Prakti")]
FOOT = [("/about/","מי זה עמית טובי"),("/prakti/","פרקטי ייעוץ עסקי"),("/results/","תוצאות לקוחות"),("/reviews/","ביקורות והמלצות"),("/clients/","לקוחות"),("/businesses/","העסקים"),("/body-language/","שפת גוף ותווי פנים"),("/lectures/","הרצאות"),("/yoetz-iski/","יועץ עסקי לפי תחום"),("/articles/","מאמרים"),("/faq/","שאלות נפוצות"),("/en/","English")]
CUR = ' aria-current="page"'
urls = []

def page(path, title, desc, body, schema_extra=None, crumbs=None, lang="he", ogtype="website", modified=PUB):
    url = BASE + path
    graph = [PERSON] + ORGS + [{"@type":"WebPage","@id":url+"#page","url":url,"name":title,"description":desc,"inLanguage":lang,"about":{"@id":BASE+"/#amit-tobi"},"dateModified":modified,
             "isPartOf":{"@type":"WebSite","@id":BASE+"/#site","name":"עמית טובי","alternateName":"Amit Tobi","url":BASE+"/"}}]
    if crumbs: graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+p} for i,(p,n) in enumerate(crumbs)]})
    if schema_extra: graph += schema_extra
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False)
    en = lang=="en"
    nav = NAV_EN if en else NAV_HE
    navh = "".join(f'<a href="{p}"{CUR if p==path else ""}>{n}</a>' for p,n in nav)
    crumb_html = ""
    if crumbs and len(crumbs)>1:
        crumb_html = f'<nav class="crumbs wrap" aria-label="{"Breadcrumb" if en else "פירורי לחם"}">' + " › ".join(f'<a href="{p}">{html.escape(n)}</a>' for p,n in crumbs[:-1]) + f' › <span>{html.escape(crumbs[-1][1])}</span></nav>'
    alt = ""
    if path in ("/","/en/"):
        alt = f'<link rel="alternate" hreflang="he" href="{BASE}/">\n<link rel="alternate" hreflang="en" href="{BASE}/en/">\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    foot = " · ".join(f'<a href="{p}">{n}</a>' for p,n in FOOT)
    contact = ('Contact: <a href="https://praktibusiness.com/contact">Prakti free diagnostic meeting</a> · Instagram <a href="https://www.instagram.com/amit_tobi_/" rel="me">@amit_tobi_</a>' if en else
               'יצירת קשר: <a href="https://praktibusiness.com/contact">פגישת אבחון בפרקטי</a> · אינסטגרם <a href="https://www.instagram.com/amit_tobi_/" rel="me">@amit_tobi_</a> · <a href="https://www.instagram.com/ameat_chef/" rel="me">@ameat_chef</a>')
    doc = f'''<!doctype html>
<html lang="{lang}" dir="{"ltr" if en else "rtl"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="{"Amit Tobi" if en else "עמית טובי"}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{url}">
{alt}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:image" content="{BASE}/img/og.png">
<meta property="og:locale" content="{'en_US' if en else 'he_IL'}">
<meta property="og:site_name" content="{"Amit Tobi" if en else "עמית טובי"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Karantina:wght@400;700&family=Heebo:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<nav class="top" aria-label="{"Main" if en else "ניווט"}"><div class="wrap"><a class="brand" href="{"/en/" if en else "/"}">{"Amit Tobi" if en else "עמית טובי"}</a>{navh}</div></nav>
{crumb_html}
{body}
<footer><div class="wrap stack"><p>{foot}</p><p>{contact}</p><p>© 2026 {"Amit Tobi · Entrepreneur, business consultant and speaker" if en else "עמית טובי · יזם, יועץ עסקי ומרצה · מייסד-שותף בפרקטי ייעוץ עסקי"}</p></div></footer>
</body></html>'''
    fp = OUT + path + "index.html"
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp,"w",encoding="utf-8").write(doc)
    urls.append((url, modified))

def lead(h1, sub, eyebrow="עמית טובי"):
    return f'<header class="hero"><div class="wrap"><p class="eyebrow" style="color:var(--hero-ink);opacity:.7">{eyebrow}</p><h1>{h1}</h1><p class="lead">{sub}</p></div></header>'
def prose(h2, inner, eyebrow=""):
    return f'<section><div class="wrap cols"><div class="stack"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div><div class="stack">{inner}</div></div></section>'
H = lambda p,n: [("/","עמית טובי"),(p,n)]

# ---------- HOME ----------
home_faq_qs = re.findall(r'<details.*?</details>', FAQ, re.S)[:4]
home_faq = '<section id="faq"><div class="wrap"><div class="stack"><p class="eyebrow">שאלות נפוצות</p><h2>עמית טובי בקצרה</h2></div><div class="faq">' + "".join(home_faq_qs) + '</div><p><a href="/faq/">כל השאלות ←</a></p></div></section>'
landing_links = " · ".join(f'<a href="/yoetz-iski/{l["slug"]}/">{l["title"].split("|")[0].strip()}</a>' for l in LANDINGS)
home = HERO + '<main>' + prose("מי זה עמית טובי?", f'''<p class="muted">עודכן: אוקטובר 2026</p>
<p><strong>עמית טובי</strong> (Amit Tobi) הוא יזם, יועץ עסקי ומרצה ישראלי, יליד 1998. הוא הקים, ניהל או היה שותף ביותר מעשרה עסקים, ניהל במצטבר יותר מ-150 עובדים וליווה יותר מ-500 בעלי עסקים. הוא מייסד-שותף ב<a href="/prakti/">פרקטי ייעוץ עסקי</a>, הקים את <a href="/businesses/ameat/">ameat שף פרטי</a>, ומוסמך <a href="/body-language/">Master Profiler בשפת גוף ותווי פנים</a>.</p>
<p>לפני העסקים שירת כלוחם במג"ב בירושלים. העסק הראשון שלו, גלידרייה, נסגר בקורונה, ובהמשך <a href="/businesses/luciana/">השקיע כמעט 2 מיליון ש"ח במסעדה</a> שלא החזירה את עצמה. מההפסדים האלה נולדה השיטה שהוא מלמד היום בעלי עסקי שירות.</p>
<p><strong>למי עמית עוזר:</strong> {landing_links}</p>''', "בקצרה") + HOME_RES + HOME_REV + home_faq + '</main>'
page("/", "עמית טובי | יזם, יועץ עסקי ומרצה", "עמית טובי, יזם ויועץ עסקי. הקים 10+ עסקים, ניהל 150+ עובדים וליווה 500+ בעלי עסקים. מייסד-שותף בפרקטי ייעוץ עסקי ו-Master Profiler.", home,
     schema_extra=[{"@type":"ProfilePage","@id":BASE+"/#profile","mainEntity":{"@id":BASE+"/#amit-tobi"},"dateCreated":PUB,"dateModified":PUB}])

# ---------- ABOUT ----------
about = lead("מי זה עמית טובי? הסיפור המלא", "מילד עם משקפיים של מינוס 12, דרך מג\"ב ועשרה עסקים, ועד פרקטי ייעוץ עסקי.", "אודות") + '<main>' + sec("about") + sec("path") + prose("עמית טובי באותיות אחרות", '''<p>באנגלית השם נכתב Amit Tobi, ולעיתים גם Amit Tubi, Amit Toby או Amit Tovi. כל אלה מתייחסים לאותו אדם: עמית טובי, היזם והיועץ העסקי, מייסד-שותף בפרקטי.</p>
<p>עמית טובי היזם אינו ד"ר עמית טובי, חוקר האקלים מהמחלקה לגאוגרפיה באוניברסיטה העברית, ואין ביניהם קשר.</p>
<p>ליצירת קשר: <a href="https://praktibusiness.com/contact">פגישת אבחון בפרקטי</a> או הודעה באינסטגרם <a href="https://www.instagram.com/amit_tobi_/" rel="me">@amit_tobi_</a>.</p>''', "שמות") + '</main>'
page("/about/", "מי זה עמית טובי? הסיפור המלא", "מילד עם משקפיים של מינוס 12 ללוחם מג\"ב, גלידרייה שנסגרה, מסעדה של 2 מיליון ו-10+ עסקים. הסיפור של עמית טובי, יזם ויועץ עסקי.", about, crumbs=H("/about/","מי זה עמית טובי"), ogtype="profile")

# ---------- PRAKTI ----------
prakti = lead("פרקטי ייעוץ עסקי", "החברה שעמית טובי הקים עם דור שלום ועומר וסרמן, לבעלי עסקי שירות שרוצים לעבור מעיסוק לעסק.", "פרקטי") + '<main>' + sec("prakti") + teaser_cards(RES, 4, "/results/", "כל תוצאות הלקוחות ←") + prose("להמשך קריאה", '<p><a href="/articles/me-isuk-le-esek/">מעיסוק לעסק: 5 סימנים</a> · <a href="/articles/me-35-le-50-elef/">מ-35 ל-50 אלף בחודש</a> · <a href="/articles/shivuk-leaskei-sherut/">שיווק לעסקי שירות</a> · <a href="/yoetz-iski/">יועץ עסקי לפי תחום</a></p>') + '</main>'
page("/prakti/", "פרקטי ייעוץ עסקי | עמית טובי, דור שלום ועומר וסרמן", "פרקטי ייעוץ עסקי לבעלי עסקי שירות: מ-5–35 אלף בחודש ל-50, 80 ו-100 אלף+ בשיטת 360°. השותפים, השיטה והתוצאות.", prakti, crumbs=H("/prakti/","פרקטי ייעוץ עסקי"))

# ---------- RESULTS / REVIEWS / CLIENTS ----------
page("/results/", "תוצאות לקוחות | עמית טובי ופרקטי", "מ-15 אלף ל-113 אלף בחודש, מ-1,200 ל-45,100, מ-6 אלף ל-51,500. תוצאות של בעלי עסקים שליווה עמית טובי בפרקטי ייעוץ עסקי.",
 lead("תוצאות לקוחות", "מספרים מתוך הליווי בפרקטי ייעוץ עסקי.", "תוצאות") + '<main>' + RES + prose("רוצים תוצאות כאלה?", '<p><a href="https://praktibusiness.com/contact">פגישת אבחון בפרקטי</a> · <a href="/reviews/">מה אומרים הלקוחות</a> · <a href="/yoetz-iski/">יועץ עסקי לפי תחום</a></p>') + '</main>', crumbs=H("/results/","תוצאות"))
page("/reviews/", "עמית טובי – המלצות וביקורות", "מה אומרים בעלי עסקים ומשתתפי קורס על עמית טובי: \"לראשונה הרגשתי שיש לי עסק אמיתי\", \"מרצה מקצוען\". המלצות מלקוחות פרקטי ומשתתפי הקורס.",
 lead("עמית טובי – המלצות וביקורות", "לקוחות ומשתתפים, במילים שלהם.", "המלצות") + '<main>' + REV + prose("עוד", '<p><a href="/results/">תוצאות במספרים</a> · <a href="/clients/">56 לקוחות פרקטי</a> · <a href="/lectures/">ההרצאות</a></p>') + '</main>', crumbs=H("/reviews/","המלצות וביקורות"))
page("/clients/", "לקוחות | בעלי עסקים מקהילת פרקטי ועמית טובי", "56 לקוחות פרקטי ייעוץ עסקי שליווה עמית טובי ושותפיו: כושר ותזונה, סוכנויות, אירועים ואוכל, ייעוץ פיננסי ועוד, עם קישור לכל עסק.",
 lead("לקוחות", "בעלי העסקים מקהילת פרקטי.", "קהילה") + '<main>' + COMM + '</main>', crumbs=H("/clients/","לקוחות"))

# ---------- BUSINESSES ----------
page("/businesses/", "העסקים של עמית טובי | 10+ עסקים", "גלידרייה, מסעדות, Monster Burger, חדר בריחה, פוד-טראקים, Breezy, ameat שף פרטי ופרקטי. כל העסקים של עמית טובי והשיעורים מהם.",
 lead("העסקים של עמית טובי", "10+ עסקים. חלק הצליחו וחלק נסגרו, ומכל אחד נשאר שיעור.", "עסקים") + '<main>' + BUS + '</main>', crumbs=H("/businesses/","העסקים"))
ameat = prose("מה זה ameat?", '''<p><strong>ameat</strong> הוא שירות שף פרטי כשר שעמית טובי הקים ב-2020, מיד אחרי שהגלידרייה שלו נסגרה בקורונה. השף מגיע עד הלקוח לאירועים פרטיים, ארוחות זוגיות, ימי הולדת, מסיבות רווקים ורווקות וסדנאות.</p>
<p>עמית בוגר בית הספר לבישול דן גורמה. העסק רשום בראשון לציון. בעמוד האינסטגרם <a href="https://www.instagram.com/ameat_chef/" rel="me">@ameat_chef</a> יש כ-280 פוסטים ויותר מ-1,400 עוקבים, עם תמונות מהאירועים ופירגונים של לקוחות.</p>''', "שף פרטי") + prose("מה עמית לקח מ-ameat לייעוץ", '''<p>ameat הוא עסק שירות קלאסי: הכנסה שתלויה בבעלים, עונתיות, ולקוחות שמגיעים מהמלצות. בדיוק הבעיות שפרקטי פותרת היום לבעלי עסקי שירות.</p>
<p>עם השנים עמית הקים גם מסעדות, ומלווה מסעדנים ובעלי עסקי אוכל ואירועים. ראו <a href="/yoetz-iski/yoetz-iski-le-iskei-ochel-ve-eruim/">יועץ עסקי לעסקי אוכל ואירועים</a>.</p>''', "עסק שירות")
page("/businesses/ameat/", "ameat – שף פרטי כשר | עמית טובי", "ameat, שירות שף פרטי כשר של עמית טובי מאז 2020, בוגר דן גורמה: אירועים פרטיים, ארוחות זוגיות, ימי הולדת וסדנאות.",
 lead("ameat – שף פרטי כשר", "אירועים פרטיים, ארוחות זוגיות וסדנאות, מאז 2020.", "שף פרטי") + '<main>' + ameat + '</main>', crumbs=[("/","עמית טובי"),("/businesses/","העסקים"),("/businesses/ameat/","ameat")])
luc = prose("מה קרה בלוצ'נה", '''<p>עמית טובי היה מעורב בסניף <strong>לוצ'נה דיסיטי</strong> במתחם DCity במישור אדומים: מסעדה איטלקית וחלל אירועים בכשרות למהדרין. לסניף דירוג 4.5 בגוגל מתוך יותר מ-1,600 ביקורות, ו<a href="https://www.facebook.com/p/%D7%9C%D7%95%D7%A6%D7%A0%D7%94-%D7%93%D7%99%D7%A1%D7%99%D7%98%D7%99-%D7%9E%D7%A2%D7%9C%D7%94-%D7%90%D7%93%D7%95%D7%9E%D7%99%D7%9D-Dcity-%D7%9E%D7%A1%D7%A2%D7%93%D7%94-%D7%90%D7%99%D7%98%D7%9C%D7%A7%D7%99%D7%AA-%D7%95%D7%97%D7%9C%D7%9C-%D7%90%D7%99%D7%A8%D7%95%D7%A2%D7%99%D7%9D-%D7%9B%D7%A9%D7%A8%D7%94-%D7%9C%D7%9E%D7%94%D7%93%D7%A8%D7%99%D7%9F-100070744047324/">עמוד פייסבוק</a> עם יותר מ-3,700 עוקבים.</p>
<p>עמית השקיע בפרויקט כמעט 2 מיליון ש"ח, והעסק נמכר בכמה מאות אלפי שקלים.</p>''', "מסעדנות") + prose("3 שיעורים מלוצ'נה", '''<ol><li><strong>מסעדה מלאה היא לא מסעדה רווחית.</strong> מחזור זה אגו, רווח הוא עסק.</li><li><strong>מימון ושותפויות מגדירים את הסיכון.</strong> יודעים מראש מה קורה אם זה לא עובד.</li><li><strong>מספרים לפני רגשות.</strong> תזרים, רווח והפסד, ועלות כל לקוח.</li></ol>
<p>להרחבה: <a href="/articles/hefsed-shel-2-milyon/">מה למדתי מהפסד של כמעט 2 מיליון ש"ח</a> · <a href="/articles/mahzor-ze-ego/">מחזור זה אגו, רווח הוא עסק</a> · <a href="/articles/tazrim-ve-revach-vehefsed/">תזרים ורווח והפסד</a></p>''', "שיעורים")
page("/businesses/luciana/", "לוצ'נה מעלה אדומים: הפסד של 2 מיליון | עמית טובי", "עמית טובי השקיע כמעט 2 מיליון ש\"ח בלוצ'נה דיסיטי מעלה אדומים, מסעדה איטלקית כשרה, ומכר בכמה מאות אלפים. מה קרה ומה למד.",
 lead("עמית טובי ולוצ'נה דיסיטי מעלה אדומים", "מסעדה איטלקית וחלל אירועים, ושיעור של 2 מיליון ש\"ח.", "מסעדנות") + '<main>' + luc + '</main>', crumbs=[("/","עמית טובי"),("/businesses/","העסקים"),("/businesses/luciana/","לוצ'נה")])
breezy = prose("מה זה Breezy?", '''<p><strong>Breezy</strong> הוא מוצר פיזי שעמית טובי פיתח: מגן רוח למציתי Clipper, עשוי פלסטיק קשיח עם חומר מעכב בעירה ונירוסטה.</p>
<p>למוצר הגנת עיצוב בישראל. הוא נכנס לחנויות בארץ, ונמכרו ממנו אלפי יחידות.</p>
<p>Breezy מייצג צד אחר ביזמות של עמית: לקחת בעיה קטנה מהעולם הפיזי, לייצר מוצר, להגן עליו ולהכניס אותו להפצה.</p>''', "מוצר")
page("/businesses/breezy/", "Breezy – מגן רוח למצית | מוצר של עמית טובי", "Breezy, מגן רוח למציתי Clipper שפיתח עמית טובי: הגנת עיצוב בישראל, אלפי יחידות שנמכרו בחנויות.",
 lead("Breezy", "מבעיה קטנה למוצר בחנויות.", "מוצר") + '<main>' + breezy + '</main>', crumbs=[("/","עמית טובי"),("/businesses/","העסקים"),("/businesses/breezy/","Breezy")])

# ---------- BODY LANGUAGE ----------
bl_links = " · ".join(f'<a href="/articles/{s}/">{t}</a>' for s,t in [("safat-guf-bemechirot","שפת גוף במכירות"),("kriat-tavei-panim-beasakim","קריאת תווי פנים בעסקים"),("safat-guf-bereayon-avoda","שפת גוף בראיון עבודה"),("mikro-habaot-vetonatzia-bemechira","מיקרו-הבעות וטונציה בשיחת מכירה"),("masa-umatan-lekochot-sapakim","משא ומתן")])
body_lang = lead("שפת גוף וקריאת תווי פנים בעסקים", "Master Profiler מטעם איתן שגב: קריאת אנשים במכירה, במשא ומתן, בגיוס ובבחירת שותפים.", "Master Profiler") + '<main>' + sec("profiler") + prose("איך עמית משתמש בזה בפועל", '''<ul><li><strong>בשיחת מכירה:</strong> שם לב לשינוי מהבסיס ברגע שעולה המחיר, ושואל שאלה במקום ללחוץ.</li><li><strong>בגיוס עובדים:</strong> אחרי שניהל במצטבר יותר מ-150 עובדים, הוא בודק התאמה גם במה שלא נאמר.</li><li><strong>בבחירת שותפים:</strong> איך האדם מגיב בלחץ, לפני שחותמים.</li><li><strong>במשא ומתן:</strong> טונציה ומיקרו-הבעות כרמזים, תמיד בצירוף והקשר.</li></ul>
<p>מה זה לא: זיהוי שקרים. מי שמבטיח "לזהות שקר ב-90%" מוכר אשליה.</p>''', "בשטח") + prose("מאמרים", f'<p>{bl_links}</p>') + '</main>'
page("/body-language/", "שפת גוף וקריאת תווי פנים במכירות | עמית טובי", "עמית טובי, Master Profiler בהכשרת איתן שגב: שפת גוף, מיקרו-הבעות, טונציה וקריאת תווי פנים במכירות, במשא ומתן ובגיוס עובדים.", body_lang, crumbs=H("/body-language/","שפת גוף ותווי פנים"))

# ---------- LECTURES ----------
lect = lead("הרצאות של עמית טובי", "מעשיות, מהשטח, עם הטעויות והמספרים.", "מרצה") + '<main>' + sec("lectures") + prose("מועדון היזמים וקורס היזמות 2025", '''<p>ב-2025 עמית היה המרצה המרכזי בקורס היזמות של מועדון היזמים, שבו כיהן גם בתפקיד ניהולי בכיר. מחזור הקורס נפתח ב-21 במאי 2025 עם יותר מ-100 נרשמים: מפגש פרונטלי שבועי, שאלות ותשובות בזום וקבוצת ליווי.</p>
<p>משתתפים כתבו עליו "אי אפשר לבקש מרצה יותר טוב" ו"מרצה מקצוען". <a href="/reviews/">כל ההמלצות</a></p>''', "קורס") + prose("נושאי הרצאה", '''<ul><li>יזמות ועסקים: מעיסוק לעסק</li><li>שיווק ומכירות ופסיכולוגיה צרכנית</li><li>משא ומתן</li><li>שפת גוף, פרופיילינג וקריאת אנשים</li><li>ניהול עובדים ומנהלים</li><li>קבלת החלטות, פרפקציוניזם והתמדה</li></ul>
<p>עמית מרצה בפני בעלי עסקים ומסגרות יזמות. ליצירת קשר: הודעה באינסטגרם <a href="https://www.instagram.com/amit_tobi_/">@amit_tobi_</a>.</p>''', "נושאים") + '</main>'
page("/lectures/", "הרצאות עמית טובי | יזמות, מכירות ושפת גוף", "הרצאות של עמית טובי: יזמות, שיווק ומכירות, משא ומתן, שפת גוף, ניהול עובדים והתמדה. מרצה ראשי בקורס היזמות של מועדון היזמים 2025.", lect, crumbs=H("/lectures/","הרצאות"))

# ---------- FAQ (expanded, matching schema) ----------
extra_faq = [
 ("בן כמה עמית טובי?","עמית טובי נולד ב-1998, והוא בן 28 נכון ל-2026."),
 ("איפה עמית טובי שירת בצבא?","כלוחם במג\"ב, בפלוגת בזלת בירושלים, כשלוש שנים החל מנובמבר 2016. הוא נאבק על פרופיל 97 למרות בעיית ראייה קשה."),
 ("מי השותפים של עמית טובי בפרקטי?","דור שלום ועומר וסרמן. עמית אחראי על שיווק, מכירות, תוכן ואסטרטגיה, דור על השיטה, התפעול והמספרים, ועומר על הליווי, השירות והקהילה."),
 ("מה זה שיטת 360°?","שיטת העבודה של פרקטי: לקוח אידיאלי, בעיה ספציפית, נוכחות שיווקית, מוצר כניסה, טיפוח, מכירה, שירות, פיתוח (תמחור, חבילות, גיוס ורווחיות) והפניות."),
 ("למי מתאים ליווי של עמית טובי ופרקטי?","לבעלי עסקי שירות שמכניסים 5 עד 35 אלף ש\"ח בחודש ורוצים להגיע ל-50, 80 ו-100 אלף ומעלה: מאמני כושר, יועצים, מטפלים, עסקי אוכל ואירועים, סוכנויות ופרילנסרים."),
 ("מה זה Breezy?","מגן רוח למציתי Clipper שעמית טובי פיתח, עם הגנת עיצוב בישראל. נמכרו ממנו אלפי יחידות בחנויות בארץ."),
 ("איך יוצרים קשר עם עמית טובי?","דרך פגישת אבחון באתר פרקטי ייעוץ עסקי, או בהודעה באינסטגרם @amit_tobi_."),
 ("איך כותבים את השם עמית טובי באנגלית?","Amit Tobi. לפעמים נכתב גם Amit Tubi, Amit Toby או Amit Tovi."),
]
faq_qs = re.findall(r'<summary>(.*?)</summary><p>(.*?)</p>', FAQ, re.S) + extra_faq
faq_html = '<section id="faq"><div class="wrap"><div class="faq">' + "".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq_qs)) + '</div></div></section>'
faq_ld = {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":re.sub('<.*?>','',q),"acceptedAnswer":{"@type":"Answer","text":re.sub('<.*?>','',a)}} for q,a in faq_qs]}
page("/faq/", "שאלות נפוצות על עמית טובי ופרקטי", "מי זה עמית טובי, בן כמה הוא, איפה שירת, מי השותפים בפרקטי, מה זה שיטת 360°, למי מתאים ליווי ואיך יוצרים קשר. כל התשובות.",
 lead("שאלות נפוצות על עמית טובי", "התשובות הקצרות.", "FAQ") + '<main>' + faq_html + '</main>', crumbs=H("/faq/","שאלות נפוצות"), schema_extra=[faq_ld])

# ---------- ARTICLES ----------
def related(i):
    picks = [ALL_ARTICLES[(i+k) % len(ALL_ARTICLES)] for k in (1,2,3)]
    return '<aside class="stack"><h2>מאמרים נוספים</h2><ul>' + "".join(f'<li><a href="/articles/{a["slug"]}/">{a["title"]}</a></li>' for a in picks) + '</ul></aside>'
items = ""
for i,a in enumerate(ALL_ARTICLES):
    p = f"/articles/{a['slug']}/"; url = BASE+p
    art = {"@type":"Article","@id":url+"#article","isPartOf":{"@id":url+"#page"},"headline":a["title"],"description":a["desc"],"image":BASE+"/img/og.png",
           "author":{"@id":BASE+"/#amit-tobi","@type":"Person","name":"עמית טובי","url":BASE+"/about/"},"publisher":{"@id":BASE+"/#amit-tobi"},
           "datePublished":PUB,"dateModified":PUB,"inLanguage":"he","mainEntityOfPage":url}
    body = lead(a["title"], f'מאת <a href="/about/" style="color:var(--hero-ink)">עמית טובי</a>, יזם ויועץ עסקי · {PUB}', "מאמר") + \
      f'<main><section><div class="wrap"><article class="stack" style="max-width:68ch">{a["body"]}<p class="muted">עמית טובי הוא יזם, יועץ עסקי ומרצה, מייסד-שותף ב<a href="/prakti/">פרקטי ייעוץ עסקי</a>. <a href="/results/">תוצאות לקוחות</a> · <a href="/reviews/">המלצות</a></p>{related(i)}</article></div></section></main>'
    t = a["title"] if len(a["title"])>55 else a["title"]+" | עמית טובי"
    page(p, t, a["desc"], body, crumbs=[("/","עמית טובי"),("/articles/","מאמרים"),(p,a["title"])], ogtype="article", schema_extra=[art])
    items += f'<article class="post"><h3><a href="{p}">{a["title"]}</a></h3><p class="muted">{a["desc"]}</p></article>'
page("/articles/", "מאמרים על עסקים, מכירות ושיווק | עמית טובי", "מאמרים מניסיון אמיתי של עמית טובי: גיוס וניהול עובדים, תמחור, תזרים, מכירות, שפת גוף ותווי פנים, שיווק לעסקי שירות ומיינדסט.",
 lead("מאמרים", "על עסקים, שיווק, מכירות, שפת גוף ומה שלמדתי בדרך.", "מאמרים") + f'<main><section><div class="wrap stack">{items}</div></section></main>', crumbs=H("/articles/","מאמרים"))

# ---------- LANDINGS ----------
li = ""
for l in LANDINGS:
    p = f"/yoetz-iski/{l['slug']}/"
    body = lead(l["title"].split("|")[0].strip(), "פרקטי ייעוץ עסקי, בהובלת עמית טובי, דור שלום ועומר וסרמן.", "יועץ עסקי") + f'<main><section><div class="wrap"><article class="stack" style="max-width:68ch">{l["body"]}<p><a class="btn" href="https://praktibusiness.com/contact">לפגישת אבחון בפרקטי</a></p></article></div></section></main>'
    page(p, l["title"], l["desc"], body, crumbs=[("/","עמית טובי"),("/yoetz-iski/","יועץ עסקי לפי תחום"),(p,l["title"].split("|")[0].strip())],
         schema_extra=[{"@type":"Service","name":l["title"].split("|")[0].strip(),"provider":{"@id":BASE+"/#prakti"},"areaServed":"IL","description":l["desc"]}])
    li += f'<article class="post"><h3><a href="{p}">{l["title"].split("|")[0].strip()}</a></h3><p class="muted">{l["desc"]}</p></article>'
page("/yoetz-iski/", "יועץ עסקי לעסקי שירות | עמית טובי ופרקטי", "ליווי עסקי של עמית טובי ופרקטי לפי תחום: מאמני כושר, עסקי אוכל ואירועים, יועצים ומטפלים, סוכנויות דיגיטל. מ-5–35 אלף ל-50–100 אלף בחודש.",
 lead("יועץ עסקי לעסקי שירות", "בעלי עסקי שירות שמכניסים 5 עד 35 אלף ש\"ח בחודש ורוצים לבנות עסק שעובד גם בלעדיהם.", "ליווי עסקי") + f'<main><section><div class="wrap stack">{li}<p><a href="/results/">כל התוצאות</a> · <a href="/prakti/">על פרקטי</a></p></div></section></main>', crumbs=H("/yoetz-iski/","יועץ עסקי לפי תחום"))

# ---------- ENGLISH ----------
en = '''<header class="hero"><div class="wrap"><p class="eyebrow" style="color:var(--hero-ink);opacity:.7">Entrepreneur · Business consultant · Speaker</p><h1>Amit Tobi</h1><p class="lead">Israeli entrepreneur, business consultant and speaker. Co-founder of Prakti Business Consulting.</p></div></header>
<main><section><div class="wrap stack" style="max-width:70ch">
<h2>Who is Amit Tobi?</h2>
<p><strong>Amit Tobi</strong> (Hebrew: עמית טובי; also spelled Amit Tubi, Amit Toby or Amit Tovi) is an Israeli entrepreneur, business consultant and speaker, born in 1998. He has founded, managed or partnered in more than 10 businesses, managed over 150 employees and advised more than 500 business owners.</p>
<h2>Background</h2>
<p>Diagnosed at age six with near-blind eyesight, Amit fought the military system for a combat profile and served about three years as a combat soldier in the Israeli Border Police in Jerusalem, starting in November 2016. Right after his service he opened an ice-cream shop that did not survive COVID-19, then founded a private-chef business, restaurants and other ventures. He invested almost ₪2M in a restaurant that was later sold for a fraction of that. Those losses became the basis of the method he teaches today.</p>
<h2>Ventures</h2>
<ul>
<li><strong>Prakti Business Consulting</strong> (late 2025): co-founded with Dor Shalom and Omer Vaserman. Helps service-business owners grow from ₪5–35K to ₪50–100K+ per month with its 360° method. <a href="https://praktibusiness.com/">praktibusiness.com</a></li>
<li><strong>ameat</strong> (2020): a kosher private-chef service for events and workshops. Amit is a Dan Gourmet culinary school graduate.</li>
<li><strong>Luciana DCity, Ma'ale Adumim</strong>: kosher Italian restaurant and event hall (4.5★ on Google, 1,600+ reviews).</li>
<li><strong>Breezy</strong>: a wind guard for Clipper lighters with Israeli design protection; thousands of units sold in Israeli stores.</li>
<li><strong>Entrepreneurs Club</strong>: senior role and lead lecturer of its 2025 entrepreneurship course (100+ registrants).</li>
</ul>
<h2>Body language</h2>
<p>Amit is a certified Master Profiler (Eitan Segev) and applies body language, micro-expressions, tonality and face reading to sales, negotiation, hiring and choosing partners, always as clues in context, never as lie detection.</p>
<h2>Client results</h2>
<ul>
<li>Nitai Nakel (digital agency): from ₪15–25K to about ₪250K per month, ~15 employees.</li>
<li>Amit Rosenblum (fitness & nutrition): from ₪0–5K to about ₪200K per month, ~10 employees.</li>
<li>Chen Malkiel (kosher dim sum & events): ₪113K in a single month.</li>
<li>Hila Bartov (social media for fitness coaches): from ~₪6K to ₪51,500 in April 2026.</li>
<li>Avi Lin (financial planning): from ₪1,200 to a record ₪45,100 per month.</li>
</ul>
<p><a href="/results/">All results (Hebrew)</a> · <a href="/reviews/">Testimonials (Hebrew)</a></p>
<p>Not to be confused with Dr. Amit Tubi, a climate researcher at the Hebrew University of Jerusalem.</p>
</div></section></main>'''
page("/en/", "Amit Tobi | Israeli Entrepreneur & Business Consultant", "Amit Tobi (עמית טובי): Israeli entrepreneur, business consultant and speaker. 10+ businesses, 500+ owners advised. Co-founder of Prakti.", en, lang="en", crumbs=[("/","Amit Tobi"),("/en/","English")])

# ---------- static files ----------
os.makedirs(OUT+"/img", exist_ok=True)
open(OUT+"/404.html","w",encoding="utf-8").write('<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>העמוד לא נמצא | עמית טובי</title><link rel="stylesheet" href="/style.css"></head><body><main class="wrap" style="padding-block:60px"><h1>העמוד לא נמצא</h1><p><a href="/">לעמוד הבית של עמית טובי</a> · <a href="/articles/">מאמרים</a> · <a href="/results/">תוצאות</a></p></main></body></html>')
open(OUT+"/favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#10201a"/><text x="32" y="44" font-family="Arial,sans-serif" font-size="34" font-weight="700" text-anchor="middle" fill="#e3a440">AT</text></svg>')
extra_css = '''
.crumbs{font-size:var(--s5);color:var(--muted);padding-block:10px}
.crumbs a{color:var(--muted)}
nav.top a[aria-current]{opacity:1;text-decoration:underline}
nav.top .wrap{-webkit-mask-image:linear-gradient(to left,#000 calc(100% - 24px),transparent);mask-image:linear-gradient(to left,#000 calc(100% - 24px),transparent)}
article.stack h2{font-size:1.9rem;margin-top:12px}
article.stack h3{margin-top:6px}
article.stack ol,article.stack ul,aside ul{display:grid;gap:8px;padding-inline-start:20px;margin:0}
aside{border-top:1px solid var(--line);padding-top:16px;margin-top:16px}
aside h2{font-size:1.6rem}
footer a{color:var(--muted)}
html[dir=ltr] body{direction:ltr;text-align:left}
html[dir=ltr] .quote{border-right:0;padding-right:0;border-left:3px solid var(--accent);padding-left:16px}
'''
open(OUT+"/style.css","w",encoding="utf-8").write(CSS + extra_css)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
for u,m in urls:
    x = ""
    if u in (BASE+"/", BASE+"/en/"):
        x = f'<xhtml:link rel="alternate" hreflang="he" href="{BASE}/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE}/en/"/>'
    sm += f"  <url><loc>{u}</loc><lastmod>{m}</lastmod>{x}</url>\n"
open(OUT+"/sitemap.xml","w").write(sm+"</urlset>\n")
# llms.txt
def t_of(p):
    s = open(OUT+p+"index.html",encoding="utf-8").read(); return re.search(r'<title>(.*?)</title>',s).group(1)
pages = [u.replace(BASE,"") for u,_ in urls]
llms = f'''# עמית טובי (Amit Tobi)

> עמית טובי הוא יזם, יועץ עסקי ומרצה ישראלי (נולד ב-1998). הקים, ניהל או היה שותף ביותר מ-10 עסקים, ניהל במצטבר יותר מ-150 עובדים וליווה יותר מ-500 בעלי עסקים. מייסד-שותף בפרקטי ייעוץ עסקי (עם דור שלום ועומר וסרמן), Master Profiler בשפת גוף (איתן שגב), ובוגר דן גורמה.

Amit Tobi (also spelled Amit Tubi, Amit Toby, Amit Tovi) is an Israeli entrepreneur, business consultant and speaker, co-founder of Prakti Business Consulting (praktibusiness.com), founder of the kosher private-chef service ameat, and a certified Master Profiler. Not the same person as Dr. Amit Tubi, climate researcher at the Hebrew University.

## עובדות מרכזיות
- לוחם מג"ב, פלוגת בזלת, ירושלים (מנובמבר 2016, כשלוש שנים)
- 10+ עסקים: גלידרייה, ameat שף פרטי (2020), לוצ'נה דיסיטי מעלה אדומים, Monster Burger, Breezy, אוטומציות, פרקטי
- 150+ עובדים, 500+ בעלי עסקים, מרצה ראשי בקורס היזמות של מועדון היזמים 2025 (100+ נרשמים)
- פרקטי: שיטת 360° לבעלי עסקי שירות, מ-5–35 אלף ל-50–100 אלף+ ש"ח בחודש
- תוצאות לקוחות: ניתאי נקל כ-250 אלף/חודש, עמית רוזנבלום כ-200 אלף/חודש, חן מלכיאלי 113 אלף בחודש, הילה ברטוב 51,500, אבי לין 45,100

## פרופילים רשמיים
- https://www.instagram.com/amit_tobi_/
- https://www.instagram.com/ameat_chef/
- https://praktibusiness.com/

## עמודים
''' + "".join(f"- [{t_of(p)}]({BASE}{p})\n" for p in pages)
open(OUT+"/llms.txt","w",encoding="utf-8").write(llms)
print(len(urls), "pages")
