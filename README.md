# COM6104 Local AI Agent
A simple local AI agent built with Python and Ollama for my COM6104 assignment.

---

## Core Features
- **Two distinct tools**: 
  1.  Document Analysis (TXT/PPT reader + summarizer)
  2.  Task Manager (to-do list + timer)
- **Short-term memory**: Records all interaction history
- **Multi-step reasoning**: Reads documents first, then generates summaries

---

## How to Run
1.  Install dependencies:
    pip install python-pptx ollama

2.  Run the agent:
    python agent.py

3.  Available commands:
    - read txt / summarize txt
    - read ppt / summarize ppt
    - add task [your task] / list tasks
    - timer [seconds]
    - show memory
    - exit to quit
