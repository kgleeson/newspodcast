from gtts import gTTS
import feedparser
import time


def parse_indo():
    data = feedparser.parse("https://www.independent.ie/breaking-news/rss/")
    return [i.title for i in data["entries"] if "Soccer" not in i.category]


def parse_rte():
    data = feedparser.parse("https://www.rte.ie/feeds/rss/?index=/news/")
    return [". ".join([i.title, "".join(i.summary)]) for i in data["entries"][:5]]


def main():
    feed = parse_rte()
    with open(f"RTE-{time.strftime('%Y%m%d-%H%M')}.mp3", "wb") as f:
        for item in feed:
            print(item)
            gTTS(item, lang="en", tld="ie").write_to_fp(f)


if __name__ == "__main__":
    main()
