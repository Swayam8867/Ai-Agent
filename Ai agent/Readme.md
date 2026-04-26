**Assignment**
AI Agents

This assignment will feature two AI agent systems, both focusing on automation, process efficiency, and development productivity. Specifically, I would like to demonstrate the capabilities of an agent system by completing multi-step tasks.

**Assignment 1: Autonomous Research Agent**
Description

An AI agent that conducts structured research over the Internet regarding a specific CEO or founder.

**Characteristics**
1)Automatically generates search queries
2)Finds and parses information from web pages
3)Categorizes gathered information in its memory
4)Conducts several iterative steps of learning
5)Creates a structured report based on the obtained data

**Process**
1)Input the name of the CEO/founder
2)Conducts several iterations of searching
3)Extracts information from web pages
4)Categorizes information (bio, career, company, insights)
5)Outputs a report (report.md)


**Assignment 2: Developer Assistance Agent**
Description

A software development assistant powered by AI to help with coding and give suggestions about codes.

**Features**
1)Code functionality
2)Code errors and bugs
3)Suggestions on code improvement
4)Improved codes generated
**Flow**
1)Inputting codes
2)Sending codes to AI
3)Response processing
4)Code analysis output
**Technology Stack**
1)Python
2)OpenAI API
Requests
BeautifulSoup

**Setup Steps**
1. Installing Dependencies
pip install -r requirements.txt
2. Setting API Key

Please set your API key for OpenAI in your environment variables.

Windows:

setx OPENAI_API_KEY "Your_API_Key_Here"

Once you have installed the API key in Windows, please restart your terminal window.

How to Run
Assignment 1
cd assignment1
python main.py
Assignment 2
cd assignment2
python main.py
Output
Assignment 1
Output file is report.md
Assignment 2
Output in terminal window