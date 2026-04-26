from tools import search_web, scrape_page

class ResearchAgent:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
        self.steps = 0

    def decide_next_query(self):
        if self.steps == 0:
            return f"{self.name} biography"
        elif self.steps == 1:
            return f"{self.name} career history"
        elif self.steps == 2:
            return f"{self.name} leadership style"
        else:
            return None

    def categorize(self, text):
        text_lower = text.lower()

        if "born" in text_lower:
            self.memory.add("bio", text)
        if "career" in text_lower or "worked" in text_lower:
            self.memory.add("career", text)
        if "company" in text_lower or "ceo" in text_lower:
            self.memory.add("company", text)
        if "leader" in text_lower or "style" in text_lower:
            self.memory.add("insights", text)

    def run(self):
        while True:
            query = self.decide_next_query()
            if not query:
                break

            print(f"\n[Agent] Searching: {query}")

            links = search_web(query)

            for link in links:
                print(f"[Agent] Visiting: {link}")
                content = scrape_page(link)

                if content:
                    self.memory.add_source(link)
                    self.categorize(content)

            self.steps += 1

        return self.memory.get_all()