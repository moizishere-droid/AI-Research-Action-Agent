# 🤖 AI Agent Tool Kit

## 🎯 What Does It Do?

An intelligent AI agent that can:
- 🌐 Search the web in real-time
- 🧮 Perform calculations
- 💾 Save important notes forever
- 💬 Remember your conversation

## ⚡ Quick Start
```bash
# 1. Clone
git clone https://github.com/moizishere-droid/AI-Research-Action-Agent.git

# 2. Install
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

Enter your OpenAI API key and start chatting!

## 🔧 What's Inside?

### 4 Powerful Tools

| Tool | What It Does | Example |
|------|--------------|---------|
| 🔍 **Web Search** | Find current info online | "Latest AI breakthroughs" |
| 🧮 **Calculator** | Solve math problems | "Calculate 234 * 56 + 89" |
| 💾 **Save Note** | Store info permanently | "Save note: Call mom tomorrow" |
| 📖 **Read Notes** | View all saved notes | "Show my notes" |

## 📝 Memory Types

### 🧠 Chat Memory (Temporary)
- Keeps conversation context
- ❌ Lost on page refresh
- Perfect for current chat

### 💾 Notes (Permanent)
- Saved to `agent_save.txt`
- ✅ Survives restart
- Great for important info

## 💬 Try These
```
🔍 "Search for weather in New York"
🧮 "What's 15% of 3500?"
💾 "Save note: Project deadline Dec 31"
📖 "Read all my notes"
💬 "Calculate 100 + 50, then multiply by 2"
```

## 🎮 How to Use

1. **Start app** → Enter API key
2. **Type question** → Agent picks right tool
3. **Get answer** → Save if important
4. **Clear memory** → Use sidebar button

## 🔐 Privacy

- API key stored in session only
- Notes saved locally on your machine
- No data sent anywhere except OpenAI API

## 🧹 Reset Everything

- **Clear chat**: Sidebar → "Clear Memory"
- **Delete notes**: Delete `agent_save.txt`

---

