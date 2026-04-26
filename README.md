# AI Agent Assignment

## Overview

Implementation of two autonomous AI agents performing real-life tasks: internet researching, tool utilization, and output reporting.

---

## Assignment 1: Autonomous Research Agent

An agent capable of multi-step internet researching regarding a particular CEO or founder.

### Features

* Query creation
* Web browsing and scraping
* Memory structuring
* Iterative data collection
* Reporting (`report.md`)

---

## Assignment 2: Developer Assistant Agent

An agent utilizing AI capabilities to analyze and improve given code.

### Features

* Explanation of code fragments
* Bugs and issues detection
* Recommendations for improvement
* Generation of refactored code

---

## Tech stack

* Python
* OpenAI API
* Requests
* BeautifulSoup

---

## Installation

Dependencies installation:

```bash
pip install -r requirements.txt
```

API key configuration (Windows):

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Restart terminal.

---

## Usage

### Assignment 1

```bash
cd assignment1
python main.py
```

### Assignment 2

```bash
cd assignment2
python main.py
```

---

## Notes

* API keys are absent from security reasons
* Modular architecture implemented
