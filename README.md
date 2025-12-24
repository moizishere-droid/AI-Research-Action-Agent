# 🤖 AI Agent Tool Kit (Streamlit + LangChain)

## 🚀 Overview

**AI Agent Tool Kit** is an interactive **Streamlit-based AI assistant** powered by **LangChain** and **OpenAI**.
It combines **tool-calling**, **conversation memory**, and **persistent storage** into a single lightweight application.

This project demonstrates **real-world AI agent architecture**, not just chat.

---

## ✨ What Can This Agent Do?

The agent can intelligently decide when to:

* 🌐 **Search the web** for real-time information
* 🧮 **Solve mathematical expressions**
* 💾 **Save important notes permanently**
* 📖 **Read previously saved notes**
* 🧠 **Remember conversation context** (during the session)

All actions happen automatically based on user intent.

---

## ⚡ Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/moizishere-droid/AI-Research-Action-Agent.git
cd AI-Research-Action-Agent

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
streamlit run app.py
```

🔑 Enter your **OpenAI API key** in the sidebar and start chatting.

---

## 🛠️ Built-In Tools

| Tool              | Purpose                       | Example                            |
| ----------------- | ----------------------------- | ---------------------------------- |
| 🔍 **Web Search** | Fetch real-time information   | “Latest AI research trends”        |
| 🧮 **Calculator** | Evaluate math expressions     | “(234 × 56) + 89”                  |
| 💾 **Save Note**  | Store information permanently | “Save note: Finish project report” |
| 📖 **Read Notes** | Retrieve all saved notes      | “Show my saved notes”              |

The agent **automatically selects** the correct tool.

---

## 🧠 Memory Architecture

### 🟡 Session Memory (Temporary)

* Stored in **Streamlit session state**
* Maintains conversation context
* ❌ Lost on page refresh
* Ideal for flowing conversations

### 🟢 Persistent Notes (Permanent)

* Saved in `agent_save.txt`
* ✅ Survives app restart
* Used for long-term information

| Type        | Persistence | Use Case            |
| ----------- | ----------- | ------------------- |
| Chat Memory | ❌ Temporary | Contextual replies  |
| Notes       | ✅ Permanent | Important reminders |

---

## 💬 Example Prompts

```
🔍 Search for current AI regulations
🧮 Calculate (45 * 12) + 7
💾 Save note: Review LangChain agents tomorrow
📖 Read all my notes
💬 What did I ask you earlier?
```

---

## 🗂️ Project Structure

```
ai-agent-toolkit/
│
├── app.py              # Main Streamlit application
├── agent_save.txt      # Persistent notes file
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🎮 How It Works (High Level)

1. **User inputs a query**
2. **LLM analyzes intent**
3. **Appropriate tool is selected**
4. **Tool executes**
5. **Response returned**
6. **Memory updated**

This is a **true AI agent loop**, not hard-coded logic.

---

## 🔐 Privacy & Security

* 🔑 API key stored only in session memory
* 💾 Notes saved locally on your machine
* 🚫 No external storage or tracking
* 📡 Only OpenAI API is called

---

## 🧹 Reset Options

* **Clear chat memory** → Sidebar → *Clear Memory*
* **Delete all notes** → Remove `agent_save.txt`

