from agent import ResearchAgent
from memory import Memory

def format_output(data, name):
    report = f"# Research Report: {name}\n\n"

    for key, values in data.items():
        report += f"## {key.capitalize()}\n"
        for v in values[:3]:
            report += f"- {v[:200]}...\n"
        report += "\n"

    return report


if __name__ == "__main__":
    name = input("Enter CEO name: ")

    memory = Memory()
    agent = ResearchAgent(name, memory)

    result = agent.run()

    report = format_output(result, name)

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("\n✅ Report generated: report.md")