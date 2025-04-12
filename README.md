# Keystroke Typing Speed Analyzer

This Flask web application records and analyzes a user's typing speed based on the time between keystrokes. It classifies the user as a **Fast Typer**, **Moderate Typer**, or **Slow Typer** and logs the session data for future analysis.


## 🚀 Features

- Records keystrokes and timestamps via a web interface.
- Analyzes average time between keystrokes.
- Filters out long pauses (e.g., >3 seconds) to prevent skewed results.
- Classifies typing speed:
  - ⏱️ **Fast Typer**: < 0.2 seconds per key
  - 🕰️ **Moderate Typer**: 0.2 - 0.5 seconds per key
  - 🐢 **Slow Typer**: > 0.5 seconds per key
- Saves keystroke data into timestamped logs (optional).

---


## 🧰 Tech Stack

- Python 3.x
- Flask
- HTML/CSS/JS (frontend)
- Pandas & NumPy for optional data processing

---


## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/VedashreeTakle/keystroke-analyzer.git
cd keystroke-analyzer
