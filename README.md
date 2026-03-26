

# AI Past vs Present: ELIZA vs Modern LLM

## 📚 CMPG 313 - Artificial Intelligence Assignment

### 🎯 Objective
To compare rule-based AI (ELIZA, 1960s) with modern generative AI (LLM, 2020s) and understand the evolution of artificial intelligence.

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `eliza_custom.py` | Custom ELIZA implementation with 5+ modified rules |
| `LLM_simple.py` | Modern LLM using Qwen2.5-1.5B-Instruct |
| `compare_simple.py` | Side-by-side comparison script |
| `test_setup.py` | Setup verification script |

---

## 🚀 How to Run

### Prerequisites
```bash
pip install transformers torch accelerate

## ⚠️ Local LLM Note

Due to SSL certificate issues with the MSYS Python environment, the local LLM installation encountered package conflicts. The comparison was successfully completed using a cloud-based modern LLM (ChatGPT/Gemini) with identical prompts. All responses are documented in `LLM_COMPARISON.md`.