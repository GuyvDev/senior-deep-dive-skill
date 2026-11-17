<div dir="rtl">

# Senior Deep Dive — מדריך בעברית

**Skill שמסביר ארכיטקטורה, מושגים טכניים והחלטות הנדסיות ברמת Senior/Staff — בעומק גבוה, בלי להפוך את התשובה להסבר שורה־שורה על הקוד.**

[English README](README.md) · [קובץ ה־Skill](skills/senior-deep-dive/SKILL.md) · [דוגמאות](skills/senior-deep-dive/references/examples.md) · [בדיקות](evals/README.md)

## במה הוא שונה מפרומפט רגיל?

הסוכן בודק את החלקים הרלוונטיים בפרויקט, מסביר **מה הבעיה, איך המנגנון באמת עובד, למה נבחרה הארכיטקטורה, מה האלטרנטיבות ומתי הן עדיפות**, ומוסיף דוגמאות מספריות וזרימת מידע. הוא מפריד בין מידע שמאומת בקוד לבין הסברים תיאורטיים או הסקות.

**High-level אינו אומר שטחי.** העומק מתבטא במנגנונים, בהנחות, בקבלת החלטות ובהשפעות של שינוי אילוצים — לא בסקירת כל פונקציה.

## הפעלה אוטומטית ושליטה מפורשת

כל אפשרות היא עצמאית. אם לא מציינים ערך, הסוכן בוחר אוטומטית לפי השאלה.

| הגדרה | אפשרויות | מה המשמעות? |
| --- | --- | --- |
| `depth` | `auto`, `deep`, `very-deep` | עמוק או עמוק מאוד — עם הרחבת הנחות, הוכחות, כשלי קצה והשפעות מערכתיות |
| `focus` | `auto`, `balanced`, `mechanisms`, `tradeoffs`, `theory`, `all` | מאוזן, זרימה ומנגנונים, החלטות ושיקולי תכנון, תיאוריה/מתמטיקה או כל הסוגים הרלוונטיים |
| `examples` | `auto`, `numeric`, `flow`, `both` | דוגמה מספרית, מעבר מידע בין שלבים או שניהם |
| `mode` | `auto`, `explain`, `critique` | הסבר או ביקורת ארכיטקטונית מבוססת ראיות |
| `language` | `auto`, `he`, `en` | עברית/אנגלית — אוטומטית לפי השאלה |

## דוגמאות

```text
תסביר לי למה אנחנו משתמשים ב-Reranking בפרויקט,
מה ההבדל מ-Retrieval, ומה המחיר מבחינת Latency.
```

```text
עומק=עמוק מאוד; דגש=מנגנונים; דוגמאות=מספרים וזרימה
איך תמונה עוברת בין שלבי ה-CUDA pipeline, ומה הגבולות בין CPU ו-GPU?
```

```text
focus=theory examples=numeric
תסביר בצורה מתמטית למה LayerNorm ו-BatchNorm שונים בהשפעתם על אימון Transformers.
```

```text
mode=critique focus=all
האם תכנון ה-Queue הזה אמין מול retries, duplicates ו-worker crashes?
```

## התקנה

לשימוש קבוע עם Codex או Cursor (Linux/macOS):

```bash
git clone https://github.com/GuyvDev/senior-deep-dive-skill.git
cd senior-deep-dive-skill
mkdir -p ~/.agents/skills
cp -R skills/senior-deep-dive ~/.agents/skills/
```

ל־Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/senior-deep-dive ~/.claude/skills/
```

להתקנה בפרויקט ספציפי העתיקו את תיקיית `senior-deep-dive` אל `.agents/skills/` (או `.claude/skills/` עבור Claude Code). לאחר ההתקנה אפשר לבקש הסבר בשפה טבעית, ובסוכנים תומכים להפעיל את ה־Skill במפורש בשמו.

> ההוראות מניחות שהמאגר כבר פורסם ב־GitHub. אפשר גם להעתיק את הקבצים מתוך ה־ZIP המקומי בלי GitHub.

## בדיקות ומגבלות

```bash
python3 -m unittest discover -s tests -v
```

הבדיקות האוטומטיות בודקות את מבנה ה־Skill, ההגדרות, הקישורים והתאמת כיסוי 17 תרחישי בדיקה. כדי לוודא ש־LLM אמיתי עומד בהנחיות, צריך להריץ בנפרד את הבדיקות המתוארות ב־[`evals/README.md`](evals/README.md). אין כאן טענה שנמדדה הצלחה אצל כל מודל.

ה־Skill לא יוצר גישה למאגרים חסומים, לא ממציא מדידות, ולא אמור לשנות את הקוד רק כדי להסביר אותו.

רישיון: MIT. 

</div>
