# -*- coding: utf-8 -*-
"""Amit Tobi v2 homepage (cinematic). All copy sourced from site-src/facts.md."""
import html as H

CONTACT = "https://praktibusiness.com/contact"

CLIENTS = """קורן צבר|עבדאללה חסדיה|מיכה קורקוס|מוטי קוזלובסקי|ליאור שושן|שגיא עטר|יקיר כהן|קרן אפיאס|רועי אהרוני|אהרון בלטמן|אור בוכבזה|חוי בר זאב|איליי שהרבני|עפר ברקת|אילן גריף|איתי קיין|יובל אזולאי|בר שושן|ירדן שמואלי|ראובן לוריא|פז אוחיון|אור תם|דרור בלוך|דור אופיר|סיון גדליה|יובל ברקוביץ|נתנאל טורגמן|ירדן קדוש|אהרן שחר|עדן ברק|אביאל ממן|אבי לין|ברוך רובין|עידן ממן|ליאור הורוביץ|אלון זוהר|גולן קפל|עידן מזרחי|אסף מור|נתנאל עמר|עינבר גואטה|קים כספי|מאור אלעד|עמית רובינוף|גל סופר|יפעת שמש|חן מלכיאלי|עמית משה|שליו זיו|עמית רוזנבלום|תום עטר|אופק אוריאל""".split("|")

STORY = [
 ("גיל 6","מינוס 12 בעיניים","ראייה של מינוס 10 עד מינוס 12, כמעט עיוורון. משקפיים יקרים, הצקות, משקפיים שבורים.","חוסן נבנה כשאין ברירה."),
 ("ילדות","נגד החרם","עמדתי לצד חבר שהחרימו אותו. משם נולד הרעיון של \"האח הגדול\" לילדים בכיתות א' עד ד'.","עומדים לצד אנשים, גם כשזה לא נוח."),
 ("פרופיל 97","עם מי עוד אפשר לדבר?","למרות הראייה נלחמתי על פרופיל קרבי: מכתבים, רופאים פרטיים, לשכת הגיוס.","תמיד יש עוד מישהו לדבר איתו."),
 ("2016","לוחם מג\"ב","כשלוש שנים בפלוגת בזלת בירושלים. אבן של כ-150 ק\"ג פגעה לי בקסדה.","קמים, ממשיכים."),
 ("גיל 21","הגלידרייה","14 עד 16 שעות ביום, כולל חגים. השקעה של כ-400 אלף ש\"ח. העסק לא שרד את הקורונה.","לעבוד קשה לא אומר להרוויח יותר."),
 ("2020","שף פרטי ויועץ","הקמתי את ameat, שף פרטי כשר, והתחלתי לייעץ. ואז השאלה: האם אני בכלל בעל עסק?","עסק לא אמור להיות תלוי רק בבעלים."),
 ("לוצ'נה","כמעט 2 מיליון","מסעדה ואולם אירועים כשר במעלה אדומים. 4.5 כוכבים ב-1,604 ביקורות בגוגל. נמכרה בכמה מאות אלפים.","מחזור זה אגו. רווח הוא עסק."),
 ("Master Profiler","קורא אנשים","הסמכה מאיתן שגב: שפת גוף, מיקרו-הבעות, תווי פנים, טונציה ופסיכולוגיה של מכירה.","שיווק מתחיל מלהבין למה בן אדם קונה."),
 ("2025","מרצה ראשי","המרצה הראשי של קורס היזמות במועדון היזמים. המחזור נפתח עם יותר מ-100 נרשמים.","אתה לא צריך עוד מוטיבציה. אתה צריך שיטה."),
 ("סוף 2025","פרקטי","הקמתי עם דור שלום ועומר וסרמן את פרקטי ייעוץ עסקי, לבעלי עסקי שירות.","אם בכל חודש אתה מתחיל מאפס, אין לך מערכת."),
]

RESULTS = [
 ("עמית רוזנבלום","כושר ותזונה","200","K","מ-0 עד 5 אלף ש\"ח בחודש, תוך 8 עד 12 חודשים. כ-10 אנשי צוות.",80,"ברגע שלקחתי מנטור שיקצר לי את הדרך"),
 ("ניתאי נקל","סוכנות דיגיטל ווידאו","250","K","מ-15 עד 25 אלף ש\"ח בחודש, תוך 6 עד 10 חודשים. כ-15 עובדים.",100,"הליווי האישי מנע ממני טעויות יקרות מאוד."),
 ("חן מלכיאלי","אירוח אסייתי כשר","113","K","בחודש אחד. ממוצע של 90 אלף ומעלה, אחרי 15 עד 25 אלף.",45,"לראשונה הרגשתי שיש לי עסק אמיתי"),
 ("אבי לין","תכנון פיננסי למשפחות","45,100","","שיא באפריל 2026. בנובמבר: 1,200 ש\"ח.",18,"עברתי ממצב של תקיעות מוחלטת ותסכול"),
 ("הילה ברטוב","סושיאל למאמני כושר","51,500","","באפריל. לפני כן: כ-6,000 ש\"ח בחודש.",21,"תקרת זכוכית ראשונה נשברה"),
 ("רועי אהרוני","כושר ותזונה","50","K+","תוך 2 עד 3 חודשים, אחרי 15 עד 25 אלף לא יציבים.",20,"היום יש לי מנגנון אמיתי שלא תלוי רק בי."),
]

METHOD = [("לקוח אידיאלי","למי בדיוק אתה מוכר"),("בעיה ספציפית","מה כואב לו, וכמה זה עולה לו"),("נוכחות שיווקית","איפה הוא פוגש אותך"),("מוצר כניסה","הצעד הראשון, בלי סיכון"),("טיפוח","קשר עד שהוא מוכן"),("מכירה","שיחה שבנויה משאלות"),("שירות","שהלקוח יישאר"),("פיתוח","תמחור, חבילות, גיוס ורווחיות"),("הפניות","לקוחות שמביאים לקוחות")]

Q1 = [("היום יש לי מנגנון אמיתי שלא תלוי רק בי.","רועי אהרוני, כושר ותזונה"),("הליווי האישי מנע ממני טעויות יקרות מאוד.","ניתאי נקל, סוכנות דיגיטל"),("לראשונה הרגשתי שיש לי עסק אמיתי","חן מלכיאלי, אירוח אסייתי כשר"),("עברתי ממצב של תקיעות מוחלטת ותסכול","אבי לין, ייעוץ פיננסי"),("ברגע שלקחתי מנטור שיקצר לי את הדרך","עמית רוזנבלום, כושר ותזונה"),("לא האמנתי שזה אפשרי.","הילה ברטוב, ניהול סושיאל")]
Q2 = [("4 לידים ו-2 סגירות רק מהיום.","צ'לי ק., מאפרת"),("אתה פשוט מקצוען, ואני לומד ממך המון.","אופק, משתתף בקורס"),("הגעתי לקורס רגע לפני שהתייאשתי.","גאולה ל., מנטורית"),("המפגש הפיל לי אסימונים.","נתנאל ש., משתתף בקורס"),("חברה, סגרנו לקוח ראשון היום, ממש עכשיו. בתשלום.","הילה א., מטפלת"),("אי אפשר לבקש מרצה יותר טוב","משתתפת בקורס היזמות"),("הראש שלי לא הפסיק לעבוד","משתתף בקורס היזמות"),("פתחת לי עולם","משתתפת בקורס היזמות")]

TOPICS = [
 ("◉","שפת גוף","מה באמת אפשר לקרוא בפגישה, ומה לא. מיקרו-הבעות, טונציה ותווי פנים.","/body-language/"),
 ("◈","פסיכולוגיה שיווקית","למה בן אדם קונה, ואיך בונים שיווק שמתחיל משם.","/articles/shivuk-leaskei-sherut/"),
 ("◆","מכירות","מכירה שבנויה משאלות. בלי לחץ, בלי טריקים.","/articles/mechira-mi-sheelot/"),
 ("◎","עמוד אינסטגרם","מה עובד באמת לעסקי שירות, מהביו ועד הפנייה.","/articles/shivuk-beinstagram-leaskei-sherut/"),
 ("◇","מוצר פיתיון","מוצר כניסה, דף נחיתה ווובינר: המשפך שמביא לידים כל שבוע.","/articles/mutzar-knisa-daf-nechita-webinar/"),
]

BIZ = [
 ("ייעוץ עסקי","פרקטי","פעיל","live","הקמתי עם דור שלום ועומר וסרמן. ליווי לבעלי עסקי שירות לפי שיטת 360°.","/prakti/","prakti-founders"),
 ("שף פרטי","ameat","פעיל","live","שף פרטי כשר, מאז 2020. בוגר דן גורמה.","/businesses/ameat/","biz-ameat"),
 ("מסעדה ואולם","לוצ'נה","נמכר","","4.5 כוכבים ב-1,604 ביקורות. כמעט 2 מיליון השקעה, ושיעור על רווח מול מחזור.","/businesses/luciana/","biz-luciana"),
 ("פופ-אפ","Grill Bar","","","פופ-אפ גריל במתחם של לוצ'נה. עוד ניסוי, עוד שיעור.","/businesses/luciana/","biz-grillbar"),
 ("קמעונאות","הגלידרייה","נסגר","","העסק הגדול הראשון. 14 עד 16 שעות ביום, ולא שרד את הקורונה.","/articles/taoyot-bepticha-shel-esek-rishon/","biz-gelato"),
 ("מזון","Monster Burger","","","אחד ממיזמי האוכל בדרך, לצד בית קפה, פודטראקים וקיוסק.","/businesses/","biz-monster"),
 ("בילוי","חדר בריחה \"החתונה\"","","","חדר בריחה בראשון לציון. עוד עסק, ועוד שיעור על תפעול ועובדים.","/businesses/","biz-escape"),
 ("מוצר","Breezy","","","מגן רוח למצית קליפר, עם הגנת עיצוב בישראל. אלפי יחידות נמכרו בחנויות.","/businesses/breezy/",""),
]

SPEAK = [("יזמות","ממה שעובד בשטח"),("שיווק ומכירות","מלמה לקנות ועד סגירה"),("פסיכולוגיה צרכנית","למה בן אדם קונה"),("משא ומתן","עם לקוחות וספקים"),("שפת גוף ופרופיילינג","לקרוא את מי שמולך"),("ניהול עובדים ומנהלים","מניסיון של 150+ עובדים"),("קבלת החלטות ופרפקציוניזם","לצאת לפעולה"),("התמדה","הטיפה שחוצבת בסלע")]

def esc(s): return H.escape(s, quote=False)

def body(faq_html):
    o=[]
    o.append('<div class="progress" aria-hidden="true"></div><div class="spot" aria-hidden="true"></div>')
    o.append(f'<div class="bar">פרקטי ייעוץ עסקי: פגישת אבחון חינם לבעלי עסקי שירות · <a href="{CONTACT}">לקביעת פגישה</a></div>')
    o.append('''<nav class="nav" aria-label="ניווט ראשי"><div class="wrap">
<a class="logo" href="/" aria-label="עמית טובי, דף הבית"><i></i>עמית טובי</a>
<div class="links" id="menu"><a href="/about/">הסיפור</a><a href="#results">תוצאות</a><a href="#free">תכנים חינם</a><a href="#speaking">הרצאות</a><a href="#biz">עסקים</a><a href="/articles/">מאמרים</a><a href="/en/">EN</a></div>
<a class="btn sm" href="%s">פגישת אבחון <span class="arr">←</span></a>
<button class="burger" aria-label="תפריט" aria-controls="menu" aria-expanded="false"><span></span><span></span></button>
</div></nav>''' % CONTACT)
    # HERO
    o.append(f'''<header class="hero"><canvas aria-hidden="true"></canvas><div class="wrap">
<div class="copy">
<p class="eyebrow" data-in>יזם · יועץ עסקי · מרצה</p>
<h1><span class="ln"><span>עמית</span></span><span class="ln"><span>טובי</span></span></h1>
<p class="tag" data-in>עסקים אמיתיים. כסף אמיתי. <em>טעויות אמיתיות.</em></p>
<p class="lead" data-in>הקמתי יותר מ-10 עסקים, ניהלתי יותר מ-150 עובדים וליוויתי יותר מ-500 בעלי עסקים. היום אני עוזר לבעלי עסקי שירות לבנות עסק שלא תלוי רק בהם.</p>
<div class="ctas" data-in><a class="btn" href="{CONTACT}">לפגישת אבחון חינם <span class="arr">←</span></a><a class="btn ghost" href="/about/">הסיפור שלי</a></div>
</div>
<div class="portrait"><div class="ring" aria-hidden="true"></div>
<img src="/img/amit-hero-1100.webp" srcset="/img/amit-hero-700.webp 700w, /img/amit-hero-1100.webp 1100w" sizes="(max-width:1000px) 380px, 560px" width="1100" height="1287" alt="עמית טובי, יזם ויועץ עסקי, בצילום סטודיו" fetchpriority="high">
<div class="badge b1"><b>Master Profiler</b>הסמכה מאיתן שגב</div>
<div class="badge b2"><b>500+</b>בעלי עסקים ליוויתי</div>
</div></div>
<div class="scrollcue" aria-hidden="true">גלילה<i></i></div></header>''')
    o.append('<main>')
    # STATS
    o.append('''<section class="stats" aria-label="במספרים"><div class="wrap">
<div class="stat"><b><span data-count="10">10</span><small>+</small></b><span>עסקים שהקמתי, ניהלתי או הייתי שותף בהם</span></div>
<div class="stat"><b><span data-count="150">150</span><small>+</small></b><span>עובדים לאורך הדרך</span></div>
<div class="stat"><b><span data-count="500">500</span><small>+</small></b><span>בעלי עסקים שליוויתי</span></div>
<div class="stat"><b><span data-count="10">10</span><small>M+</small></b><span>ש"ח מחזור מצטבר בעסקים שלי</span></div>
</div></section>''')
    # MEDIA
    o.append('''<section class="media" aria-label="בתקשורת"><div class="wrap"><figure class="tv" data-r><img src="/img/tv-galit-yoav.webp" width="738" height="415" alt="עמית טובי בתוכנית גלית ויואב, כבעלי מסעדת לוצ'נה מעלה אדומים" loading="lazy"><figcaption><span class="eyebrow">בטלוויזיה</span><b>גלית ויואב</b>התארחתי כבעלים של מסעדת לוצ'נה במעלה אדומים.</figcaption></figure>
<figure class="reel" data-r><video src="/img/reel-luciana.mp4" poster="/img/reel-poster.webp" muted loop playsinline preload="none" data-lazyplay aria-label="מהשטח: הקמה ופתיחה של לוצ'נה"></video><figcaption><span class="eyebrow">מהשטח</span><b>מהשלד לפתיחה</b>ככה נראית הקמה של מסעדה ואולם אירועים.</figcaption></figure>
<figure class="team" data-r><img src="/img/prakti-founders.webp" width="1400" height="933" alt="מייסדי פרקטי ייעוץ עסקי: עמית טובי, דור שלום ועומר וסרמן" loading="lazy"><figcaption><span class="eyebrow">פרקטי</span><b>שלושה מייסדים</b>עמית טובי, דור שלום ועומר וסרמן.</figcaption></figure>
</div></section>''')
    # MARQUEE
    o.append('<div class="marq"><p class="lbl">בעלי עסקים מקהילת פרקטי</p><div class="track">' + "".join(f'<span>{esc(n)}</span>' for n in CLIENTS) + '</div></div>')
    # DOORS
    o.append(f'''<section id="paths"><div class="wrap">
<div class="head"><div><p class="eyebrow">מאיפה מתחילים</p><h2 class="h2" data-r>מה <em>אתה</em> צריך?</h2></div></div>
<div class="doors stag">
<a class="door" href="/prakti/" data-r><span class="n">01</span><h3>יש לי עסק שירות ואני רוצה לגדול</h3><p>מ-5 עד 35 אלף ש"ח בחודש ל-50, 80 ו-100 אלף ומעלה, עם שיטה ולא עם עוד שעות.</p><span class="go"><i>←</i>ליווי בפרקטי</span></a>
<a class="door" href="#speaking" data-r><span class="n">02</span><h3>אני מחפש מרצה לארגון או לאירוע</h3><p>יזמות, מכירות, פסיכולוגיה צרכנית, שפת גוף וניהול עובדים. מהשטח, לא מהספרים.</p><span class="go"><i>←</i>נושאי הרצאות</span></a>
<a class="door" href="#free" data-r><span class="n">03</span><h3>אני רוצה ללמוד בחינם</h3><p>מאמרים ומדריכים על שפת גוף, שיווק, מכירות, אינסטגרם ומוצר כניסה.</p><span class="go"><i>←</i>לתכנים החינמיים</span></a>
</div></div></section>''')
    # MANIFESTO
    o.append('''<section class="mani"><div class="wrap"><blockquote data-hl="משרה.">אם אתה העובד הכי טוב בעסק שלך, אין לך עסק. יש לך משרה.</blockquote><cite>עמית טובי</cite></div></section>''')
    # STORY
    ch = "".join(f'<article class="chap"><span class="yr">{esc(y)}</span><h3>{esc(t)}</h3><p>{esc(p)}</p><p class="lesson">{esc(l)}</p></article>' for y,t,p,l in STORY)
    o.append(f'''<section class="story" id="story" aria-label="הסיפור"><div class="pin">
<div class="intro"><p class="eyebrow">הסיפור</p><h2 class="h2">כל טעות <em>עלתה כסף.</em></h2><p class="sub">ומכל אחת יצא שיעור. <a class="more" href="/about/">הסיפור המלא ←</a></p></div>
<div class="rail">{ch}</div><div class="line" aria-hidden="true"><i></i></div></div></section>''')
    # RESULTS
    cards=""
    for who,what,num,suf,frm,w,q in RESULTS:
        cnt = num.replace(",","")
        numhtml = f'<span data-count="{cnt}">{esc(num)}</span>'
        cards += f'<article class="case" data-r><p class="who">{esc(who)}</p><p class="what">{esc(what)}</p><p class="big"><small>₪</small>{numhtml}{esc(suf)}</p><p class="from">{esc(frm)}</p><div class="meter" aria-hidden="true"><i style="--w:{w}%"></i></div><q>{esc(q)}</q></article>'
    o.append(f'''<section id="results"><div class="wrap">
<div class="head"><div><p class="eyebrow">תוצאות</p><h2 class="h2" data-r>מספרים, <em>לא הבטחות.</em></h2><p class="sub">הכנסה חודשית של לקוחות פרקטי ייעוץ עסקי, לפי הדיווחים שלהם.</p></div><a class="more" href="/results/">כל התוצאות ←</a></div>
<div class="res stag">{cards}</div>
<p class="note">אלה תוצאות של הלקוחות עצמם, לא הבטחה. כל עסק שונה. מקור: סיפורי הצלחה בפרקטי ועדכונים של הלקוחות.</p>
</div></section>''')
    # METHOD
    st="".join(f'<li><span><b>{esc(a)}</b>{esc(b)}</span></li>' for a,b in METHOD)
    o.append(f'''<section class="method" id="method"><div class="wrap">
<div class="wheel" data-r="scale"><svg role="img" aria-label="שיטת 360 מעלות: תשעה שלבים"></svg><div class="core"><div><b>360°</b><span>השיטה</span></div></div></div>
<div><p class="eyebrow">שיטת 360°</p><h2 class="h2" data-r>עסק הוא <em>מערכת.</em></h2><p class="sub">תשעה חלקים שעובדים יחד. כשאחד חסר, אתה מרגיש את זה בכסף.</p><ol class="steps" style="margin-top:30px">{st}</ol></div>
</div></section>''')
    # PROFILER
    o.append('''<section class="prof" id="profiler"><div class="wrap">
<div class="scan" data-r="scale"><img src="/img/amit-face.webp" width="640" height="640" alt="עמית טובי, Master Profiler" loading="lazy"><div class="grid"></div>
<span class="pt" style="top:25%;left:39%" data-l="מתח במצח"></span><span class="pt" style="top:31%;left:31%" data-l="כיוון מבט"></span><span class="pt" style="top:48%;left:39%" data-l="מיקרו-הבעה"></span><span class="pt" style="top:58%;left:51%" data-l="לסת"></span></div>
<div><p class="eyebrow">Master Profiler</p><h2 class="h2" data-r>אני <em>קורא</em> אנשים.</h2>
<p class="sub">בגיל שש כמעט לא ראיתי, אז למדתי לקרוא את מי שעומד מולי. היום זו הסמכה מאיתן שגב, וכלי עבודה בכל פגישת מכירה, ראיון עבודה ומשא ומתן.</p>
<div class="chips"><span>שפת גוף</span><span>מיקרו-הבעות</span><span>תווי פנים</span><span>טונציה</span><span>דפוסי התנהגות</span><span>פסיכולוגיה של מכירה</span></div>
<a class="btn ghost" href="/body-language/">שפת גוף ופרופיילינג <span class="arr">←</span></a></div>
</div></section>''')
    # QUOTES
    r1="".join(f'<figure class="q"><p>{esc(t)}</p><span>{esc(w)}</span></figure>' for t,w in Q1)
    r2="".join(f'<figure class="q"><p>{esc(t)}</p><span>{esc(w)}</span></figure>' for t,w in Q2)
    o.append(f'''<section class="quotes" id="reviews" aria-label="המלצות"><div class="wrap"><div class="head"><div><p class="eyebrow">המלצות</p><h2 class="h2" data-r>מה <em>הם</em> אומרים.</h2></div><a class="more" href="/reviews/">כל ההמלצות ←</a></div></div>
<div class="qrow"><div class="qtrack">{r1}</div></div><div class="qrow rev"><div class="qtrack">{r2}</div></div></section>''')
    # FREE HUB
    tp="".join(f'<a class="topic" href="{u}" data-r><span class="cnt">חינם</span><span class="ic" aria-hidden="true">{i}</span><h3>{esc(t)}</h3><p>{esc(p)}</p></a>' for i,t,p,u in TOPICS)
    o.append(f'''<section id="free"><div class="wrap">
<div class="head"><div><p class="eyebrow">תכנים חינם</p><h2 class="h2" data-r>תיקח. <em>זה בחינם.</em></h2><p class="sub">כל מה שאני מלמד בליווי ובקורסים, מחולק לנושאים. מאמרים, מדריכים וכלים שאפשר ליישם כבר היום.</p></div><a class="more" href="/articles/">כל המאמרים ←</a></div>
<div class="hub stag">{tp}</div></div></section>''')
    # BUSINESSES
    bz="".join(f'<a class="bz{" img" if im else ""}" href="{u}">' + (f'<img src="/img/{im}.webp" alt="{esc(n)}" loading="lazy" decoding="async">' if im else '') + f'<span class="k">{esc(k)}</span>' + (f'<span class="st {c}">{esc(s_)}</span>' if s_ else '') + f'<h3>{esc(n)}</h3><p>{esc(p)}</p></a>' for k,n,s_,c,p,u,im in BIZ)
    o.append(f'''<section id="biz"><div class="wrap">
<div class="head"><div><p class="eyebrow">העסקים</p><h2 class="h2" data-r>10+ עסקים. <em>כל אחד לימד משהו.</em></h2><p class="sub">מסעדות, אוכל, מוצרים, שירותים וטכנולוגיה. חלקם הצליחו, חלקם עלו לי ביוקר.</p></div><a class="more" href="/businesses/">כל העסקים ←</a></div>
<div class="biz">{bz}</div></div></section>''')
    # SPEAKING
    sp="".join(f'<li>{esc(a)}<span>{esc(b)}</span></li>' for a,b in SPEAK)
    o.append(f'''<section class="speak" id="speaking"><div class="wrap">
<div><p class="eyebrow">הרצאות</p><h2 class="h2" data-r>על הבמה, <em>מהשטח.</em></h2><p class="sub">הרצאות לארגונים, לקהילות ולבעלי עסקים. בלי סיסמאות מוטיבציה: סיפורים אמיתיים, מספרים אמיתיים וכלים שעובדים למחרת בבוקר.</p>
<div class="ctas" style="margin-top:30px"><a class="btn" href="/lectures/">להזמנת הרצאה <span class="arr">←</span></a></div></div>
<div><img class="speak-img" src="/img/amit-smile.webp" width="900" height="972" alt="עמית טובי, מרצה" loading="lazy"><ul class="topics-list stag">{sp}</ul></div>
</div></section>''')
    # WHO (entity block)
    o.append('''<section id="who" aria-label="מי זה עמית טובי"><div class="wrap"><div class="who-box" data-r>
<div><p class="eyebrow">בקצרה</p><h2 class="h2" style="font-size:clamp(48px,6vw,84px)">מי זה <em>עמית טובי?</em></h2></div>
<div><p><strong>עמית טובי</strong> (Amit Tobi) הוא יזם, יועץ עסקי ומרצה ישראלי, יליד 1998. הוא הקים, ניהל או היה שותף ביותר מעשרה עסקים, ניהל במצטבר יותר מ-150 עובדים וליווה יותר מ-500 בעלי עסקים.</p>
<p>הוא מייסד-שותף ב<a href="/prakti/">פרקטי ייעוץ עסקי</a> עם דור שלום ועומר וסרמן, Master Profiler בשפת גוף מטעם איתן שגב, ושף פרטי כשר (<a href="/businesses/ameat/">ameat</a>). לפני העסקים שירת כלוחם במג"ב בירושלים.</p>
<ul class="facts"><li><b>תפקיד</b>יזם, יועץ עסקי ומרצה</li><li><b>חברה</b>פרקטי ייעוץ עסקי</li><li><b>הסמכה</b>Master Profiler, איתן שגב</li><li><b>אינסטגרם</b><a href="https://www.instagram.com/amit_tobi_/" rel="me">@amit_tobi_</a></li></ul></div>
</div></div></section>''')
    # FAQ
    o.append(f'<section id="faq"><div class="wrap"><div class="head"><div><p class="eyebrow">שאלות נפוצות</p><h2 class="h2" data-r>שאלות <em>ותשובות.</em></h2></div><a class="more" href="/faq/">כל השאלות ←</a></div><div class="faq">{faq_html}</div></div></section>')
    # FINAL
    o.append(f'''<section class="final"><div class="wrap"><p class="eyebrow">הצעד הבא</p><h2 class="h2" data-r>אתה לא צריך עוד מוטיבציה. <em>אתה צריך שיטה.</em></h2>
<div class="ctas" style="justify-content:center"><a class="btn" href="{CONTACT}">לפגישת אבחון חינם <span class="arr">←</span></a><a class="btn ghost" href="https://www.instagram.com/amit_tobi_/" rel="me">אינסטגרם</a></div></div></section>''')
    o.append('</main>')
    o.append(f'''<footer><div class="wrap"><div class="cols">
<div><a class="logo" href="/"><i></i>עמית טובי</a><p style="margin-top:14px;max-width:320px">יזם, יועץ עסקי ומרצה. מייסד-שותף בפרקטי ייעוץ עסקי.</p></div>
<div><h4>עמית</h4><ul><li><a href="/about/">הסיפור</a></li><li><a href="/businesses/">העסקים</a></li><li><a href="/lectures/">הרצאות</a></li><li><a href="/body-language/">שפת גוף</a></li></ul></div>
<div><h4>ללמוד</h4><ul><li><a href="/articles/">מאמרים</a></li><li><a href="/results/">תוצאות</a></li><li><a href="/reviews/">המלצות</a></li><li><a href="/faq/">שאלות נפוצות</a></li></ul></div>
<div><h4>קשר</h4><ul><li><a href="{CONTACT}">פגישת אבחון בפרקטי</a></li><li><a href="https://www.instagram.com/amit_tobi_/" rel="me">@amit_tobi_</a></li><li><a href="https://www.instagram.com/ameat_chef/" rel="me">@ameat_chef</a></li><li><a href="/en/">English</a></li></ul></div>
</div><p style="margin-top:40px">© 2026 עמית טובי</p><div class="big" aria-hidden="true">AMIT TOBI</div></div></footer>''')
    return "\n".join(o)

def render(base, faq_html, ld_json, title, desc, noindex=True, canonical="/"):
    robots = "noindex, nofollow" if noindex else "index, follow, max-snippet:-1, max-image-preview:large"
    return f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
<meta name="author" content="עמית טובי">
<meta name="robots" content="{robots}">
<meta name="google-site-verification" content="e3FqUDfzGrb3m0-ksrHiiD72oABmCjvkKwo9U9YwtXI" />
<meta name="theme-color" content="#0E0E10">
<link rel="canonical" href="{base}{canonical}">
<link rel="alternate" hreflang="he" href="{base}/">
<link rel="alternate" hreflang="en" href="{base}/en/">
<link rel="alternate" hreflang="x-default" href="{base}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{base}/">
<meta property="og:type" content="profile">
<meta property="og:image" content="{base}/img/og.png">
<meta property="og:locale" content="he_IL">
<meta property="og:site_name" content="עמית טובי">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="image" href="/img/amit-hero-1100.webp" imagesrcset="/img/amit-hero-700.webp 700w, /img/amit-hero-1100.webp 1100w" imagesizes="(max-width:1000px) 380px, 560px" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Karantina:wght@400;700&family=Heebo:wght@400;500;700;800;900&display=swap">
<link rel="stylesheet" href="/v2.css">
<script type="application/ld+json">{ld_json}</script>
</head>
<body>
{body(faq_html)}
<script src="/v2.js" defer></script>
</body></html>'''
