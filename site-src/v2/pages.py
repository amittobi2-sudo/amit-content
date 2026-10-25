# -*- coding: utf-8 -*-
"""New v2 pages: free-content hub + topic pages, press kit, businesses gallery, lectures upgrade. Facts only from facts.md."""
import html as H

CONTACT = "https://praktibusiness.com/contact"
IG = "https://www.instagram.com/amit_tobi_/"
MAIL = "mailto:amittobi@gmail.com?subject=%D7%94%D7%96%D7%9E%D7%A0%D7%AA%20%D7%94%D7%A8%D7%A6%D7%90%D7%94"
MAILP = "mailto:amittobi@gmail.com?subject=%D7%A4%D7%A0%D7%99%D7%99%D7%94%20%D7%9E%D7%94%D7%AA%D7%A7%D7%A9%D7%95%D7%A8%D7%AA"

TOPICS = [
 {"slug":"safat-guf","name":"שפת גוף","title":"שפת גוף בעסקים: מדריכים חינם | עמית טובי",
  "desc":"מדריכים חינם של עמית טובי, Master Profiler מטעם איתן שגב: שפת גוף, מיקרו-הבעות, טונציה ותווי פנים במכירה, בראיון עבודה ובמשא ומתן.",
  "h1":"שפת גוף בעסקים","sub":"מה באמת אפשר לקרוא אצל מי שמולך, ומה לא. כל המדריכים במקום אחד, בחינם.",
  "intro":"<p>אני Master Profiler מטעם איתן שגב. בגיל שש כמעט לא ראיתי, אז למדתי מוקדם לקרוא את מי שעומד מולי. היום זה כלי עבודה בכל פגישת מכירה, ראיון עבודה ומשא ומתן.</p><p>כלל אחד לפני הכל: שפת גוף היא כלי להעלות השערות ולשאול שאלה טובה בזמן הנכון. היא לא גלאי שקרים, ומי שמבטיח לך את זה מוכר אשליה.</p>",
  "arts":["safat-guf-bemechirot","mikro-habaot-vetonatzia-bemechira","kriat-tavei-panim-beasakim","safat-guf-bereayon-avoda"],
  "more":[("/body-language/","שפת גוף ופרופיילינג: העמוד המלא")],
  "faq":[("אפשר לזהות שקר לפי שפת גוף?","לא. אין תנועה או מבנה פנים של שקרן. מה שכן עובד: לזהות שינוי בהתנהגות של אדם ביחס לעצמו, ולשאול שאלה טובה ברגע הזה."),
         ("איפה שפת גוף הכי עוזרת בעסק?","במכירה, בראיונות עבודה ובמשא ומתן. היא אומרת לי מתי לעצור, מתי לשאול שאלה נוספת ומתי לתת לאדם זמן.")]},
 {"slug":"psichologia-shivukit","name":"פסיכולוגיה שיווקית","title":"פסיכולוגיה שיווקית לעסקים קטנים: מדריכים חינם | עמית טובי",
  "desc":"עמית טובי על פסיכולוגיה שיווקית לעסקי שירות: למה אנשים קונים, בידול, תמחור ומסר. מדריכים חינם מניסיון של 10+ עסקים.",
  "h1":"פסיכולוגיה שיווקית","sub":"שיווק מתחיל מלהבין למה בן אדם קונה. מדריכים חינם לבעלי עסקי שירות.",
  "intro":"<p>הקמתי יותר מ-10 עסקים, וברובם הטעות הייתה אותה טעות: דיברתי על מה שאני מוכר, ולא על מה שהלקוח מרגיש. \"שיווק מתחיל מלהבין למה בן אדם קונה.\"</p><p>כאן ריכזתי את מה שאני מלמד על מסר, בידול ותמחור. \"בידול נולד מבעיה ספציפית או מקהל ספציפי.\" כשאתה מדבר לכולם, אף אחד לא מרגיש שאתה מדבר אליו.</p>",
  "arts":["mekorot-shivuk","kopiraiting-leaskei-sherut","shivuk-leaskei-sherut","tamchur-asakei-sherut","me-isuk-le-esek","mahzor-ze-ego","perfektzionizm-baesek"],
  "more":[("/results/","תוצאות של לקוחות שיישמו את זה")],
  "faq":[("מה זה פסיכולוגיה שיווקית בעסק קטן?","להבין מה הלקוח מרגיש לפני שהוא קונה: מה כואב לו, כמה זה עולה לו, ולמה הוא עוד לא פתר את זה. משם בונים הצעה ומסר."),
         ("למה כל כך חשוב לבחור קהל ספציפי?","כי בידול נולד מבעיה ספציפית או מקהל ספציפי. מסר שמדבר לכולם לא נוגע באף אחד.")]},
 {"slug":"mechirot","name":"מכירות","title":"מכירות בלי לחץ: מדריכים חינם | עמית טובי",
  "desc":"עמית טובי על מכירות לעסקי שירות: שיחת מכירה שבנויה משאלות, התנגדויות, משא ומתן, מיקרו-הבעות וטונציה. מדריכים חינם.",
  "h1":"מכירות","sub":"מכירה טובה בנויה משאלות. בלי לחץ, בלי טריקים, עם שיטה.",
  "intro":"<p>\"מכירה טובה בנויה משאלות.\" בשיחת מכירה אני עוזר ללקוח להגדיר את הבעיה, להבין כמה היא עולה לו, לראות למה עוד לא פתר אותה, ורק אז לראות את הפתרון.</p><p>מעיין ב., דולה שהשתתפה בקורס שלי, יישמה את זה יום אחרי השיעור. לקוחה חזרה אליה תוך פחות משעה ובחרה בליווי המלא, ב-6,000 ש\"ח. כאן כל המדריכים על מכירה, התנגדויות ומשא ומתן.</p>",
  "arts":["mechira-mi-sheelot","masa-umatan-lekochot-sapakim","mikro-habaot-vetonatzia-bemechira","safat-guf-bemechirot","me-35-le-50-elef"],
  "more":[("/reviews/","מה אומרים משתתפים ולקוחות")],
  "faq":[("איך מוכרים בלי להרגיש דוחף?","שואלים במקום לשכנע. כשהלקוח מגדיר בעצמו את הבעיה ואת המחיר שלה, ההחלטה שלו, לא שלך."),
         ("מה עושים כשלקוח אומר \"יקר לי\"?","שואלים: יקר ביחס למה? לרוב זה אומר שהערך עוד לא ברור, לא שהמחיר גבוה מדי.")]},
 {"slug":"instagram","name":"עמוד אינסטגרם","title":"אינסטגרם לעסקי שירות: מדריכים חינם | עמית טובי",
  "desc":"עמית טובי על אינסטגרם לעסקי שירות: ביו, תוכן, הנעה לפעולה ומוצר כניסה שהופכים עוקבים ללקוחות. מדריכים חינם.",
  "h1":"עמוד אינסטגרם","sub":"עוקבים זה נחמד. לקוחות זה עסק. איך הופכים עמוד אינסטגרם למקור לידים.",
  "intro":"<p>אינסטגרם הוא לא המטרה. הוא הדרך של הלקוח להכיר אותך, לסמוך עליך ולעשות צעד ראשון. בלי מסר ברור ובלי צעד הבא, גם הרבה עוקבים לא מביאים כסף.</p><p>אופק, משתתף בקורס שלי, עלה ביום אחד מ-570 ל-645 עוקבים וסגר לקוח לפיילוט. כאן ריכזתי את מה שאני מלמד על ביו, תוכן והנעה לפעולה.</p>",
  "arts":["shivuk-beinstagram-leaskei-sherut","kopiraiting-leaskei-sherut","mekorot-shivuk","mutzar-knisa-daf-nechita-webinar"],
  "more":[(IG,"האינסטגרם שלי: @amit_tobi_")],
  "faq":[("כמה עוקבים צריך כדי למכור באינסטגרם?","פחות ממה שנדמה. מה שקובע הוא מסר ברור לקהל ספציפי וצעד הבא פשוט, לא מספר העוקבים."),
         ("מה לשים בביו של עסק שירות?","למי אתה עוזר, באיזו בעיה, ומה הצעד הבא: מוצר כניסה, פגישה או הודעה.")]},
 {"slug":"mutzar-pitayon","name":"מוצר פיתיון","title":"מוצר פיתיון ומוצר כניסה: מדריך חינם | עמית טובי",
  "desc":"עמית טובי על מוצר פיתיון (מוצר כניסה), דף נחיתה ווובינר: המשפך שמביא לידים כל שבוע לעסקי שירות. מדריכים חינם.",
  "h1":"מוצר פיתיון","sub":"הצעד הראשון שהלקוח עושה איתך, בלי סיכון. והמשפך שמביא לידים כל שבוע.",
  "intro":"<p>בשיטת 360° שלנו בפרקטי, מוצר כניסה הוא שלב קבוע: משהו קטן, חינמי או זול, שפותר בעיה אחת אמיתית ומכניס את הלקוח למערכת שלך. \"אם בכל חודש אתה מתחיל מאפס, אין לך מערכת.\"</p><p>כאן כל מה שכתבתי על מוצר כניסה, דף נחיתה ווובינר, ואיך מחברים אותם למכירה.</p>",
  "arts":["mutzar-knisa-daf-nechita-webinar","mashpech-shivuk","shivuk-begoogle-leaskei-sherut","madadei-shivuk"],
  "more":[("/prakti/","שיטת 360° בפרקטי")],
  "faq":[("מה זה מוצר פיתיון?","מוצר כניסה: משהו קטן, חינמי או זול, שפותר בעיה אחת אמיתית ובונה אמון לפני המכירה הגדולה."),
         ("מה ההבדל בין מוצר פיתיון להנחה?","הנחה מורידה את הערך של המוצר הראשי. מוצר פיתיון נותן ערך נפרד, ומכין את הלקוח להחלטה הבאה.")]},
 {"slug":"nihul-vekesef","name":"ניהול, כסף וצמיחה","title":"ניהול עובדים, תזרים וצמיחה: מדריכים חינם | עמית טובי",
  "desc":"עמית טובי על ניהול עובדים, גיוס, תזרים מזומנים, שותפויות וניהול זמן. מדריכים חינם מניסיון של 150+ עובדים ו-10+ עסקים.",
  "h1":"ניהול, כסף וצמיחה","sub":"מה למדתי מ-150 עובדים, 10 עסקים ומסעדה של כמעט 2 מיליון.",
  "intro":"<p>\"מחזור זה אגו. רווח הוא עסק.\" את המשפט הזה למדתי בדרך הקשה, בגלידרייה שלא שרדה את הקורונה ובמסעדה שנמכרה בכמה מאות אלפים אחרי השקעה של כמעט 2 מיליון.</p><p>כאן ריכזתי את מה שאני מלמד על עובדים, גיוס, תזרים, שותפויות וזמן.</p>",
  "arts":["pituach-iski-veskeil","madadei-shivuk","nihul-ovdim-150","giyus-oved-rishon","tazrim-ve-revach-vehefsed","eich-bohrim-shutaf","nihul-zman-baal-esek","hefsed-shel-2-milyon","taoyot-bepticha-shel-esek-rishon","motivatzia-hasrat-erech","tzava-profil-97-yazmut"],
  "more":[("/businesses/","העסקים שלי")],
  "faq":[("מתי נכון לגייס עובד ראשון?","כשאתה יודע בדיוק איזו משימה הוא לוקח ממך, ואיך תמדוד אותו. \"מה שלא נמדד קשה לשפר.\""),
         ("מה ההבדל בין מחזור לרווח?","מחזור הוא כל מה שנכנס. רווח הוא מה שנשאר. עסק עם מחזור גדול יכול להפסיד כסף כל חודש.")]},
]
ICONS = {"safat-guf":"◉","psichologia-shivukit":"◈","mechirot":"◆","instagram":"◎","mutzar-pitayon":"◇","nihul-vekesef":"▲"}

def e(s): return H.escape(s, quote=False)

def art_cards(slugs, by_slug):
    out=""
    for s in slugs:
        a=by_slug.get(s)
        if not a: continue
        out+=f'<a class="card" href="/articles/{s}/" data-r><span class="k">מאמר</span><h3>{a["title"]}</h3><p>{a["desc"]}</p><span class="go">לקריאה ←</span></a>'
    return out

def ctaband(h, p, href=CONTACT, label="לפגישת אבחון חינם"):
    return f'<section><div class="wrap"><div class="ctaband" data-r><div><h2>{h}</h2><p class="muted" style="margin-top:12px">{p}</p></div><a class="btn" href="{href}">{label} <span class="arr">←</span></a></div></div></section>'

def free_hub(lead):
    cards="".join(f'<a class="topic" href="/free/{t["slug"]}/" data-r><span class="cnt">חינם · {len(t["arts"])} מדריכים</span><span class="ic" aria-hidden="true">{ICONS[t["slug"]]}</span><h3>{t["name"]}</h3><p>{t["sub"]}</p></a>' for t in TOPICS)
    body = lead("תכנים חינם", "כל מה שאני מלמד בליווי ובקורסים, מחולק לנושאים. מאמרים ומדריכים שאפשר ליישם כבר היום, בלי הרשמה ובלי תשלום.", "ספריית תכנים") + \
      f'<main><section><div class="wrap"><div class="hub stag hub6">{cards}</div></div></section>' + \
      ctaband("רוצה שנעשה את זה יחד?","בפגישת אבחון חינם בפרקטי בודקים את מקורות הלקוחות, התמחור וצוואר הבקבוק של העסק שלך.") + '</main>'
    return body

def free_topic(t, lead, by_slug):
    more=" · ".join(f'<a href="{u}">{e(n)}</a>' for u,n in t["more"])
    faq="".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in t["faq"])
    others="".join(f'<a class="card" href="/free/{o["slug"]}/"><span class="k">נושא</span><h3>{o["name"]}</h3><p>{o["sub"]}</p><span class="go">לנושא ←</span></a>' for o in TOPICS if o["slug"]!=t["slug"])
    body = lead(t["h1"], t["sub"], "תכנים חינם") + \
      f'<main><section><div class="wrap cols"><div class="stack"><p class="eyebrow">בקצרה</p><h2>למה זה חשוב</h2></div><div class="stack">{t["intro"]}<p>{more}</p></div></div></section>' + \
      f'<section><div class="wrap"><div class="head"><div><p class="eyebrow">המדריכים</p><h2>{len(t["arts"])} מדריכים חינם</h2></div></div><div class="cards">{art_cards(t["arts"],by_slug)}</div></div></section>' + \
      f'<section><div class="wrap"><div class="stack" style="margin-bottom:24px"><p class="eyebrow">שאלות נפוצות</p><h2>שאלות ותשובות</h2></div><div class="faq">{faq}</div></div></section>' + \
      f'<section><div class="wrap"><div class="stack" style="margin-bottom:24px"><p class="eyebrow">עוד נושאים</p><h2>להמשיך ללמוד</h2></div><div class="cards">{others}</div></div></section>' + \
      ctaband("רוצה ליווי אישי?","פגישת אבחון חינם בפרקטי ייעוץ עסקי, לבעלי עסקי שירות.") + '</main>'
    faq_ld={"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in t["faq"]]}
    return body, faq_ld

GALLERY = [
 ("g-8","biz-luciana","לוצ'נה","מסעדה ואולם אירועים כשר במעלה אדומים. 4.5 כוכבים ב-1,604 ביקורות בגוגל."),
 ("g-4","biz-luciana-truck","פודטראק לוצ'נה","דוכן הפיצה במתחם."),
 ("g-4","biz-ameat","ameat","שף פרטי כשר, מאז 2020."),
 ("g-4","biz-grillbar","Grill Bar","פופ-אפ גריל במתחם של לוצ'נה."),
 ("g-4","biz-luciana-hall","אולם האירועים","אירועים במתחם של לוצ'נה."),
 ("g-6","biz-gelato","הגלידרייה","העסק הגדול הראשון. 14 עד 16 שעות ביום."),
 ("g-6","biz-monster","Monster Burger","אחד ממיזמי האוכל בדרך."),
 ("g-4","biz-escape","חדר בריחה \"החתונה\"","ראשון לציון. 70 דקות, 2 עד 7 משתתפים."),
 ("g-4","biz-kiosk","קיוסק","עוד מיזם אוכל, עוד שיעור בתפעול."),
 ("g-4","tv-galit-yoav","בטלוויזיה","התארחתי ב\"גלית ויואב\" כבעלים של לוצ'נה."),
]
def gallery():
    return '<section><div class="wrap"><div class="head"><div><p class="eyebrow">מהשטח</p><h2>ככה זה נראה באמת</h2></div></div><div class="gallery">' + \
      "".join(f'<figure class="{c}" data-r><img src="/img/{i}.webp" alt="{e(t)}" loading="lazy" decoding="async"><figcaption><b>{e(t)}</b>{e(d)}</figcaption></figure>' for c,i,t,d in GALLERY) + '</div></div></section>'

SPEAK_TOPICS = [("יזמות","מה באמת בונה עסק, ומה רק נראה כמו עסק. מ-10+ עסקים, כולל אלה שנסגרו."),
 ("שיווק ומכירות","למה אנשים קונים, ואיך בונים שיחת מכירה שבנויה משאלות."),
 ("פסיכולוגיה צרכנית","מה קורה בראש של הלקוח רגע לפני שהוא אומר כן."),
 ("משא ומתן","עם לקוחות, ספקים ושותפים. מה עובד בשטח."),
 ("שפת גוף ופרופיילינג","Master Profiler: לקרוא את מי שמולך, בלי להפוך את זה לגלאי שקרים."),
 ("ניהול עובדים ומנהלים","מה למדתי מ-150+ עובדים. גיוס, אחריות ומדידה."),
 ("קבלת החלטות ופרפקציוניזם","איך יוצאים לפעולה עם גרסה טובה מספיק."),
 ("התמדה","\"אין הטיפה חוצבת בסלע מכוח עוצמתה, אלא מכוח התמדתה.\"")]

def lectures_extra():
    cards="".join(f'<div class="card" data-r><span class="k">נושא</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a,b in SPEAK_TOPICS)
    quotes="".join(f'<figure class="q"><p>{e(t)}</p><span>{e(w)}</span></figure>' for t,w in [("אי אפשר לבקש מרצה יותר טוב","משתתפת בקורס היזמות"),("מרצה מקצוען","משתתף בקורס היזמות"),("הראש שלי לא הפסיק לעבוד","משתתף בקורס היזמות"),("פתחת לי עולם","משתתפת בקורס היזמות"),("המפגש הפיל לי אסימונים.","נתנאל ש."),("הגעתי לקורס רגע לפני שהתייאשתי.","גאולה ל.")])
    return f'<section><div class="wrap"><div class="head"><div><p class="eyebrow">נושאים</p><h2>על מה אני מדבר</h2></div></div><div class="cards">{cards}</div></div></section>' + \
      f'<section class="quotes"><div class="wrap"><div class="head"><div><p class="eyebrow">מהקהל</p><h2>מה אמרו משתתפים</h2></div></div></div><div class="qrow"><div class="qtrack">{quotes}</div></div></section>' + \
      '<section><div class="wrap"><a class="card" href="/course/" data-r style="max-width:720px"><span class="k">קורס</span><h3>קורס היזמות: 12 שיעורים</h3><p>מה לומדים בקורס, ומה קרה למשתתפים.</p><span class="go">לסילבוס ←</span></a></div></section>' + \
      ctaband("רוצה הרצאה לארגון או לאירוע?","כתבו לי ל-amittobi@gmail.com עם תאריך, קהל ונושא, ואחזור אליכם.", MAIL, "להזמנת הרצאה במייל")

BIO_HE_S = "עמית טובי הוא יזם, יועץ עסקי ומרצה. הקים יותר מ-10 עסקים, ניהל יותר מ-150 עובדים וליווה יותר מ-500 בעלי עסקים. מייסד-שותף בפרקטי ייעוץ עסקי ו-Master Profiler מטעם איתן שגב."
BIO_HE_L = "עמית טובי (Amit Tobi), יליד 1998, הוא יזם, יועץ עסקי ומרצה ישראלי. אחרי שירות קרבי במג\"ב בירושלים פתח גלידרייה שלא שרדה את הקורונה, הקים את ameat, שירות שף פרטי כשר, והשקיע כמעט 2 מיליון ש\"ח במסעדת לוצ'נה במעלה אדומים. לאורך הדרך הקים, ניהל או היה שותף ביותר מ-10 עסקים וניהל יותר מ-150 עובדים. ב-2025 לימד קורס יזמות עם יותר מ-100 נרשמים, ובסוף 2025 הקים עם דור שלום ועומר וסרמן את פרקטי ייעוץ עסקי, שמלווה בעלי עסקי שירות. עמית הוא Master Profiler מטעם איתן שגב ומרצה על יזמות, מכירות, פסיכולוגיה צרכנית, שפת גוף וניהול עובדים."
BIO_EN = "Amit Tobi (born 1998) is an Israeli entrepreneur, business consultant and speaker. He has founded, managed or partnered in more than 10 businesses, managed over 150 employees and advised over 500 business owners. He is the co-founder of Prakti Business Consulting and a certified Master Profiler (Eitan Segev)."

def press(lead):
    kit=[("press-amit-tobi-1","דיוקן"),("press-amit-tobi-2","ידיים שלובות"),("press-amit-tobi-3","חיוך"),("press-prakti-founders","מייסדי פרקטי")]
    kith="".join(f'<a href="/img/{f}.webp" download><img src="/img/{f}.webp" alt="עמית טובי, {e(n)}" loading="lazy"><span>{e(n)} · הורדה</span></a>' for f,n in kit)
    bios="".join(f'<div class="bio" data-r><button class="copy" data-copy>העתקה</button><p class="eyebrow">{e(h)}</p><p style="margin-top:10px" {"dir=ltr" if en else ""}>{e(t)}</p></div>' for h,t,en in [("ביו קצר",BIO_HE_S,False),("ביו מלא",BIO_HE_L,False),("English bio",BIO_EN,True)])
    facts="".join(f'<li><b>{e(a)}</b> {e(b)}</li>' for a,b in [("שם","עמית טובי (Amit Tobi)"),("תפקיד","יזם, יועץ עסקי ומרצה"),("חברה","פרקטי ייעוץ עסקי (מייסד-שותף, עם דור שלום ועומר וסרמן)"),("הסמכה","Master Profiler, איתן שגב"),("במספרים","10+ עסקים, 150+ עובדים, 500+ בעלי עסקים"),("בטלוויזיה","\"גלית ויואב\", כבעלים של מסעדת לוצ'נה"),("קשר","amittobi@gmail.com"),("נושאי הרצאה","יזמות, מכירות, פסיכולוגיה צרכנית, משא ומתן, שפת גוף, ניהול עובדים")])
    return lead("ערכת מדיה", "ביו, תמונות ועובדות לעיתונאים, לפודקאסטים ולמארגני אירועים. החומרים מיועדים לשימוש תקשורתי, עם קרדיט לעמית טובי.", "לתקשורת", "amit-portrait", "עמית טובי, תמונת סטודיו") + \
      f'<main><section><div class="wrap"><div class="head"><div><p class="eyebrow">ביוגרפיה</p><h2>ביו מוכן להעתקה</h2></div></div><div class="stack">{bios}</div></div></section>' + \
      f'<section><div class="wrap"><div class="head"><div><p class="eyebrow">תמונות</p><h2>תמונות ברזולוציה גבוהה</h2></div></div><div class="kit">{kith}</div></div></section>' + \
      f'<section><div class="wrap cols"><div class="stack"><p class="eyebrow">עובדות</p><h2>בקצרה</h2></div><ul class="stack" style="list-style:none">{facts}</ul></div></section>' + \
      ctaband("ראיון, פודקאסט או הרצאה?","מייל: amittobi@gmail.com, או הודעה באינסטגרם @amit_tobi_.", MAILP, "לפנייה במייל") + '</main>'


STAGES = [
 ("שלב 1","מהרעיון לשיטה",[
   ("למצוא את הבעיה הנכונה",["לזהות בעיה כואבת ואמיתית","לבחור קהל ונישה מדויקים","לבדוק מי עוד פותר את זה","משפט אחד: אני עוזר ל... ש... באמצעות..."],"עסק טוב מתחיל מבעיה אמיתית של קהל מדויק, לא מרעיון יפה."),
   ("לבנות שיטה משלך",["למפות את הידע והניסיון שלך","לעבוד הפוך: מהתוצאה אחורה לשלבים","פיילוט עם אנשים אמיתיים","לאסוף המלצות נכון"],"שיטה ברורה יוצרת ביטחון אצלך ואמון אצל הלקוח, ופיילוט בודק אותה בשטח.")]),
 ("שלב 2","הצעה שקל לקנות",[
   ("לנסח הצעה שמדברת תוצאה",["תכונה, תועלת ותועלת עמוקה","במה אתה שונה","תהליך עבודה בשלבים","כלים ובונוסים שמוסיפים ערך"],"לקוחות לא קונים מה שאתה עושה, הם קונים מה שהם מקבלים."),
   ("מחיר, דחיפות ואחריות",["לתמחר לפי ערך ולבדוק רווחיות","מוגבלות אמיתית בזמן או בכמות","אחריות שמורידה סיכון","שם לעסק או לשיטה, ובסיס מול רואה חשבון ועורך דין"],"המחיר משקף את השינוי שהלקוח מקבל, לא את השעות שלך.")]),
 ("שלב 3","שיווק שמביא פניות",[
   ("למי, מה ואיפה",["לקוח אידיאלי מדויק","לנסח את הכאב, התוצאה והמכשול","לבחור ערוצי שיווק","תוכנית פעולה ומינוף תוכן אחד לכמה מקומות"],"שיווק מתחיל מלדעת למי מדברים, ולהיות איפה שהוא נמצא."),
   ("מוצר פיתיון",["הבטחה קטנה וממוקדת","לבחור פורמט: מדריך, סרטון, שיחה","קריאה פשוטה לפעולה","מה עושים אחרי שהשאירו פרטים"],"הפיתיון לא מוכר. הוא נותן טעימה ופותח דלת."),
   ("טיפוח עד שהלקוח מוכן",["ערך, קשר, אמון ואז רכישה","תוכן קבוע למי שעוד לא קנה","קהילה","להישאר בתודעה בלי לרדוף"],"רוב האנשים לא קונים מיד. מי שנשאר בתודעה, מקבל אותם כשהם מוכנים.")]),
 ("שלב 4","מכירה בלי לחץ",[
   ("ביטחון במכירה",["ביטחון בעצמך","ביטחון במה שאתה מוכר","ביטחון בלקוח וביכולת שלו להחליט"],"מי שבטוח בערך שלו לא צריך לדחוף."),
   ("שיחת מכירה שבנויה משאלות",["להבין למה הוא פנה","לזקק את הבעיה ומה היא עולה לו","להציג פתרון מותאם עם סיפורי הצלחה","הצעה, התלבטויות וסגירה","מעקב אחרי שיחה שלא נסגרה"],"במכירה לא משכנעים. מבינים, ומובילים לצעד ברור."),
   ("מה שקורה מאחורי הקלעים",["טון דיבור ושפת גוף","מערכת לניהול לידים","יעדים ושגרת מכירות","שליטה עצמית ברגעים לחוצים"],"מכירה טובה נשענת על שאלות טובות, מספרים ושגרה.")]),
 ("שלב 5","שירות שמייצר צמיחה",[
   ("שירות שמשאיר לקוחות",["לעודד שימוש ולהסיר מכשולים","לבקש משוב ולשפר","קהילת לקוחות","לחזור ללקוחות עבר"],"שיפור קטן בשירות משנה את כל החוויה."),
   ("להגדיל רווח מלקוחות קיימים",["העלאת מחירים ומסלולים","הצעות המשך והצעות משלימות","לבנות שגרה של הפניות","תוכן וסרטונים שמספרים מי אתה"],"קל יותר להרוויח מלקוח מרוצה מאשר להביא לקוח חדש.")]),
]
def course(lead):
    n=0; blocks=""
    for code,name,lessons in STAGES:
        items=""
        for t,tops,tk in lessons:
            n+=1
            items+=f'<details><summary><span style="color:var(--red2);font-family:var(--f-display);font-size:28px;margin-inline-end:14px">{n:02d}</span>{e(t)}</summary><ul style="margin:14px 0 8px;padding-inline-start:22px;color:var(--muted);display:grid;gap:6px">' + "".join(f'<li>{e(x)}</li>' for x in tops) + f'</ul><p><strong style="color:var(--ink)">השורה התחתונה:</strong> {e(tk)}</p></details>'
        blocks+=f'<div style="margin-bottom:46px"><p class="eyebrow">{code}</p><h3 style="font-family:var(--f-display);font-size:clamp(36px,4vw,56px);line-height:1;margin:8px 0 10px">{e(name)}</h3><div class="faq">{items}</div></div>'
    res = "".join(f'<div class="case" data-r><span class="num">{e(a)}</span><h3>{e(w)}</h3><p class="muted">{e(d)}</p></div>' for a,w,d in [
        ("4+2","צ'לי ק., מאפרת","\"4 לידים ו-2 סגירות רק מהיום.\""),
        ("6,000 ₪","מעיין ב., דולה","יום אחרי השיעור יישמה, ולקוחה בחרה בליווי המלא."),
        ("+75","אופק","עוקבים ביום אחד, מ-570 ל-645, ולקוח לפיילוט."),
        ("5-6","גאולה ל., מנטורית","נשים גייסה לתוכנית אחרי שנה של תקיעות."),
        ("1","נתנאל ש.","לקוח ראשון בתשלום.")])
    quotes = "".join(f'<figure class="q"><p>{e(t)}</p><span>משתתפ/ת בקורס</span></figure>' for t in ["אי אפשר לבקש מרצה יותר טוב","מרצה מקצוען","הראש שלי לא הפסיק לעבוד","פתחת לי עולם"])
    body = lead("קורס היזמות", "מהרעיון ועד לקוחות שמביאים לקוחות. חמישה שלבים, שנים-עשר שיעורים, וכלים שמיישמים כבר באותו שבוע.", "קורס", "amit-portrait-smile", "עמית טובי, מרצה בקורס היזמות") + \
      '<main><section><div class="wrap cols"><div class="stack"><p class="eyebrow">בקצרה</p><h2>על הקורס</h2></div><div class="stack">' + \
      '<p>ב-2025 לימדתי קורס יזמות. המחזור נפתח ב-21 במאי 2025 עם יותר מ-100 נרשמים. כל שיעור בנוי כמו שאני עובד עם בעלי עסקים: כלי אחד, משימה אחת, ויישום מיידי.</p>' + \
      '<p>הקורס עובר בחמישה שלבים: רעיון ושיטה, הצעה, שיווק, מכירה, ושירות שמייצר צמיחה. אותו סדר שבו אני בונה עסקים מאז הגלידרייה.</p></div></div></section>' + \
      f'<section><div class="wrap"><div class="head"><div><p class="eyebrow">הסילבוס</p><h2>5 שלבים, 12 שיעורים</h2></div></div>{blocks}</div></section>' + \
      f'<section><div class="wrap"><div class="head"><div><p class="eyebrow">תוצאות</p><h2>מה קרה למשתתפים</h2><p class="muted" style="margin-top:12px">הודעות שמשתתפי מחזור מאי 2025 שלחו לקבוצת הקורס.</p></div><a class="more" href="/reviews/">כל ההמלצות ←</a></div><div class="grid2">{res}</div></div></section>' + \
      f'<section class="quotes"><div class="qrow"><div class="qtrack">{quotes}</div></div></section>' + \
      ctaband("רוצה את הקורס לארגון או לקבוצה?","כתבו לי ל-amittobi@gmail.com, ואחזור עם פרטים.", MAIL, "לפנייה במייל") + '</main>'
    ld = {"@type":"Course","name":"קורס היזמות של עמית טובי","description":"קורס יזמות בחמישה שלבים: רעיון ושיטה, הצעה, שיווק, מכירה ושירות שמייצר צמיחה.","inLanguage":"he","provider":{"@type":"Person","name":"עמית טובי"},
          "hasCourseInstance":{"@type":"CourseInstance","courseMode":"blended","startDate":"2025-05-21","instructor":{"@type":"Person","name":"עמית טובי"}}}
    return body, ld
