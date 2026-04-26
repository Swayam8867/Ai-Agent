from agent import DevAgent

print("STARTING TEST...")

agent = DevAgent()

code = """def add(a,b)
    return a+b"""

print("SENDING TO AI...")

result = agent.analyze_code(code)

print("\n===== OUTPUT =====\n")
print(result)