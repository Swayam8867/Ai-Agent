class Memory:
    def __init__(self):
        self.data = {
            "bio": [],
            "career": [],
            "company": [],
            "insights": [],
            "sources": []
        }

    def add(self, category, content):
        if category in self.data:
            self.data[category].append(content)

    def add_source(self, url):
        self.data["sources"].append(url)

    def get_all(self):
        return self.data