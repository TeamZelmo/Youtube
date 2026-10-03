import os
import sys
import feedparser
import requests
from dotenv import load_dotenv
from google import genai

# Local testing ke liye .env load karega (GitHub Actions me repo secrets use honge)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def get_india_trending_topics(limit: int = 5) -> list[dict]:
    """Google Trends India RSS feed se top trending topics fetch karta hai."""
    rss_url = "https://trends.google.com/trending/rss?geo=IN"
    feed = feedparser.parse(rss_url)

    topics = []
    for entry in feed.entries[:limit]:
        title = entry.title
        summary = entry.get("summary", "")
        approx_traffic = entry.get("ht_approx_traffic", "Trending")

        topics.append({
            "title": title,
            "summary": summary,
            "traffic": approx_traffic
        })

    return topics


def analyze_with_ai(topics: list[dict]) -> str:
    """Gemini API ka use karke deep YouTube video concept breakdown generate karta hai."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable set nahi hai.")

    client = genai.Client(api_key=GEMINI_API_KEY)

    raw_topics_text = ""
    for idx, item in enumerate(topics, 1):
        raw_topics_text += f"{idx}. {item['title']} (Searches: {item['traffic']})\n"

    system_instruction = (
        "Aap ek expert YouTube Strategist aur Viral News Researcher hain. "
        "Aapka kaam raw trending topics ko high-converting YouTube ideas aur actionable details me badalna hai. "
        "Language clear Hinglish/Hindi rakhein jo creator ko turant actionable understanding de."
    )

    prompt = f"""
    Niche aaj ke India ke top trending topics hain:
    {raw_topics_text}

    Inme se top 3 sabse engaging aur viral topics select karein aur har topic ke liye ye exact structured breakdown dein:

    ---
    ### 🔥 [Rank & Topic Name]
    * **Kya hua hai (Full Context):** 2-3 sentences me poori ghatna/khabar clearly explain karein.
    * **Log kyun search kar rahe hain (Why it's trending):** Main trigger factor kya hai?
    * **YouTube Video Angle & Target Audience:** Viewer isme kya dekhna chahega?
    * **Click-worthy Titles (3 variations):** 1 curiosity-based, 1 analytical, 1 direct hook.
    * **60-Second Short / Reel Hook & Outline:**
      - 0-5s: Opening punchline/visual hook
      - 5-45s: Core explanation & twists
      - 45-60s: Call to action / Question to audience
    ---

    Format clean Markdown me rakhein bina excessive emojis ke.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "system_instruction": system_instruction,
            "temperature": 0.4
        }
    )

    return response.text


def send_telegram_message(text: str):
    """Report ko Telegram par send karta hai. Telegram ke 4096 character limit ko split handle karta hai."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("TELEGRAM_BOT_TOKEN ya TELEGRAM_CHAT_ID missing hain.")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    max_length = 4000  # Safe margin under 4096 chars limit

    chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]

    for chunk in chunks:
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": chunk,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }
        res = requests.post(url, json=payload, timeout=20)
        if not res.ok:
            # Agar markdown formatting parse error de, fallback to plain text
            payload.pop("parse_mode", None)
            requests.post(url, json=payload, timeout=20)


def main():
    print("[1/3] Fetching Google Trends...")
    topics = get_india_trending_topics(limit=5)
    if not topics:
        print("Koi trending topics nahi mile.")
        return

    print(f"[2/3] Analyzing {len(topics)} topics with Gemini AI...")
    report = analyze_with_ai(topics)

    print("[3/3] Sending report to Telegram...")
    header = "🚀 *DAILY TRENDING TOPICS & YOUTUBE BREAKDOWN*\n\n"
    send_telegram_message(header + report)
    print("Done! Daily report Telegram par bhej di gayi hai.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)
