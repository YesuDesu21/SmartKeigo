# SmartKeigo

# 🚀 Keigo Master (ビジネス日本語コーチ)

An AI-powered, multi-agent assistant designed for high-context, high-fidelity Japanese linguistic refinement. The platform accepts casual, unstructured, or raw vernacular Japanese inputs and processes them through an isolated, multi-agent pipeline to produce flawless, context-aware *Keigo* (polite business Japanese) for emails, presentations, or difficult conversations while providing structural stylistic explanations back to the operator.

---

## 🤖 Multi-Agent Architecture

The system utilizes a state-driven, sequential-cyclical multi-agent layout where each block maintains distinct system prompts and functional isolation to guarantee zero-drift conversions.

[User Input] ──> [1. Language Analyzer] ──> [2. Keigo Translator] ──> [3. Culture Reviewer] ──> [Final Output]
^                                                    │
└─────────────────── (Rejection Loop) ───────────────┘

### The Crew

1. **The Language Analyzer (分析担当)**
   * **Role:** Input Deconstruction and Feature Extraction.
   * **Goal:** Identifies core messaging intent, maps the precise hierarchy relationships (e.g., Client, Senior Executive, Coworker), and evaluates current tone levels before passing clean context to downstream blocks.

2. **The Keigo Specialist (敬語翻訳担当)**
   * **Role:** Core Linguistic Transformation Engine.
   * **Goal:** Re-architects text into exact *Sonkeigo* (respectful), *Kenjougo* (humble), or *Teineigo* (polite) based strictly on vector flags passed by the upstream Analyzer.

3. **The Cultural Coach & Reviewer (文化・推敲担当)**
   * **Role:** Qualitative Validation & Edge-Case Verification.
   * **Goal:** Reviews output against corporate conventions (such as proper *Aisatsu* seasonal greetings and corporate humility patterns). If formatting flaws are found, it utilizes back-routing states to rerun generation cycles.

---

## 🧱 Graph Orchestration

### Framework Choice: **LangGraph (Python)**

While sequential architectures work well for Western syntaxes, Japanese business prose often requires non-linear correction loops. For example, if the *Cultural Coach* determines a phrase is subtly unnatural given the recipient's corporate tier, it redirects the processing path back to the *Keigo Specialist*. 

**LangGraph** makes this possible by enabling:
* Stateful multi-step loops and cyclical agent paths.
* Consistent variable storage across human-in-the-loop validation steps.
* Fine-grained edge controls to prevent conversational state dilution.

---

## 💻 The 100% Free Production Tech Stack

Built around enterprise-grade developer tiers that require zero financial investment, minimizing operating costs while ensuring premium Japanese processing accuracy.

| Component | Technology | Optimization & Free Tier Details |
| :--- | :--- | :--- |
| **Core LLM Engine** | **Google Gemini 1.5 Flash** (via Google AI Studio) | **Free Tier:** ~15 RPM developer limits.<br>**Why:** Massive context windows coupled with exceptional native, highly fluent Japanese capabilities matching modern flagship standards. |
| **Agent Framework** | **LangGraph Ecosystem** | **Free:** Open-source MIT License.<br>**Why:** State graph routing suited for multi-turn validation loops. |
| **Vector DB (RAG)** | **Pinecone** or **Supabase Cloud** | **Free Tier:** 1 standard free index (Pinecone) or free web-hosted PostgreSQL tier (Supabase). Used for low-latency corporate template matching. |
| **Embeddings** | **Cohere Embed v3** | **Free Tier:** Complimentary Developer Trial API keys.<br>**Why:** The `embed-multilingual-v3.0` algorithm is highly optimized for non-Latin character spacing and complex Japanese kanji syntax. |
| **App Interface** | **Streamlit** or **Chainlit** | **Free:** Open-source UI libraries with free hosting via Streamlit Cloud or Hugging Face Spaces. Supports crisp, native Japanese character rendering out of the box. |

### To Run:
```
streamlit run "c:/Users/doria/Visual Studio Code/SmartKeigo/my-agent-app/app.py"
```