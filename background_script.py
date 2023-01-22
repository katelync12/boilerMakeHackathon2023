from typing import List
import trending

if __name__ == "__main__":
    # 1) Webdriver scrape twitter
    source: str = trending.get_source_with_webdriver()
    topics: List[str] = trending.get_trending(source)

    # 1.5) Find the trending *names*
