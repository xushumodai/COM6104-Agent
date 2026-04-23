import ollama
from pptx import Presentation
import time

short_term_memory = []

def save_memory(content):
    short_term_memory.append(content)
    if len(short_term_memory) > 5:
        short_term_memory.pop(0)

def get_memory():
    return "\n".join(short_term_memory)

# Tool 1: Document Analysis Tool
def read_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Failed to read TXT file."

def read_ppt(file_path):
    try:
        prs = Presentation(file_path)
        all_text = ""
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    all_text += shape.text + " "
        return all_text
    except:
        return "Failed to read PPT file."

def summarize_doc(text):
    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {"role": "user", 
             "content": f"Please summarize the following text in 1-2 short sentences. Do not ask any questions, just output the summary directly: {text}"}
        ]
    )
    return response["message"]["content"]

# Tool 2: Task Management Tool
todo_list = []

def add_task(task):
    todo_list.append(task)
    return f"Task added: {task}"

def list_tasks():
    return "\n".join(todo_list) if todo_list else "No tasks."

def countdown_timer(seconds):
    try:
        sec = int(seconds)
        time.sleep(sec)
        return f"Timer finished! {sec} seconds passed."
    except:
        return "Invalid number for timer."

def agent(input_command):
    save_memory(f"User: {input_command}")
    cmd = input_command.lower()

    if "read txt" in cmd:
        content = read_txt("test.txt")
        reply = f"[TXT Content]\n{content}"
        save_memory(f"Agent: {reply}")
        return reply

    elif "summarize txt" in cmd:
        content = read_txt("test.txt")
        summary = summarize_doc(content)
        reply = f"[TXT Summary]\n{summary}"
        save_memory(f"Agent: {reply}")
        return reply

    elif "read ppt" in cmd:
        content = read_ppt("test.pptx")
        reply = f"[PPT Content]\n{content}"
        save_memory(f"Agent: {reply}")
        return reply

    elif "summarize ppt" in cmd:
        content = read_ppt("test.pptx")
        summary = summarize_doc(content)
        reply = f"[PPT Summary]\n{summary}"
        save_memory(f"Agent: {reply}")
        return reply

    elif "add task" in cmd:
        task = input_command.replace("add task", "").strip()
        reply = add_task(task)
        save_memory(f"Agent: {reply}")
        return reply

    elif "list tasks" in cmd:
        reply = f"[Task List]\n{list_tasks()}"
        save_memory(f"Agent: {reply}")
        return reply

    elif "timer" in cmd:
        sec = input_command.replace("timer", "").strip()
        reply = countdown_timer(sec)
        save_memory(f"Agent: {reply}")
        return reply

    elif "show memory" in cmd:
        return f"[Short-Term Memory]\n{get_memory()}"

    else:
        return (
            "Available Commands:\n"
            "read txt | summarize txt\n"
            "read ppt | summarize ppt\n"
            "add task [your task]\n"
            "list tasks\n"
            "timer [seconds]\n"
            "show memory"
        )

if __name__ == "__main__":
    print("=== COM6104 AI Agent ===")
    print("Two Tools: Document Tool | Task Tool")
    while True:
        user_input = input("\nEnter command: ")
        if user_input == "exit":
            break
        print("\n" + agent(user_input))
