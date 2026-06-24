# Keigo Master (ビジネス日本語コーチ)

An AI-powered, multi-agent assistant designed for high-context, high-fidelity Japanese linguistic refinement. The platform accepts casual, unstructured, or raw vernacular Japanese inputs and processes them through an isolated, multi-agent pipeline to produce flawless, context-aware *Keigo* (polite business Japanese) for emails, presentations, or difficult conversations while providing structural stylistic explanations back to the operator.

## 🤖 Multi-Agent Architecture

The system utilizes a state-driven, sequential-cyclical multi-agent layout where each block maintains distinct system prompts and functional isolation to guarantee zero-drift conversions.

```
[User Input] ──> [1. Language Analyzer] ──> [2. Keigo Translator] ──> [3. Culture Reviewer] ──> [Final Output]
^                                                    │
└─────────────────── (Rejection Loop) ───────────────┘
```

### The Crew

1. **The Language Analyzer (分析担当)**
   - **Role:** Input Deconstruction and Feature Extraction
   - **Goal:** Identifies core messaging intent, maps the precise hierarchy relationships (e.g., Client, Senior Executive, Coworker), and evaluates current tone levels before passing clean context to downstream blocks

2. **The Keigo Specialist (敬語翻訳担当)**
   - **Role:** Core Linguistic Transformation Engine
   - **Goal:** Re-architects text into exact *Sonkeigo* (respectful), *Kenjougo* (humble), or *Teineigo* (polite) based strictly on vector flags passed by the upstream Analyzer

3. **The Cultural Coach & Reviewer (文化・推敲担当)**
   - **Role:** Qualitative Validation & Edge-Case Verification
   - **Goal:** Reviews output against corporate conventions (such as proper *Aisatsu* seasonal greetings and corporate humility patterns). If formatting flaws are found, it utilizes back-routing states to rerun generation cycles

## 💻 Tech Stack

Built around enterprise-grade developer tiers that require zero financial investment, minimizing operating costs while ensuring premium Japanese processing accuracy.

| Component | Technology | Free Tier Details |
| :--- | :--- | :--- |
| **Core LLM Engine** | **Llama 3.3 70B** (via Groq) | **Free Tier:** High-speed inference with generous rate limits<br>**Why:** Exceptional multilingual capabilities including Japanese with fast response times |
| **Agent Framework** | **LangGraph** | **Free:** Open-source MIT License<br>**Why:** State graph routing suited for multi-turn validation loops |
| **Vector DB (RAG)** | **Pinecone** | **Free Tier:** 1 standard free index with serverless pricing<br>**Why:** Low-latency corporate template matching with 1024-dimensional vectors |
| **Embeddings** | **Cohere Embed v3** | **Free Tier:** Complimentary Developer Trial API keys<br>**Why:** The `embed-multilingual-v3.0` algorithm is highly optimized for Japanese kanji syntax |
| **App Interface** | **Streamlit** | **Free:** Open-source UI library with free hosting via Streamlit Cloud<br>**Why:** Crisp, native Japanese character rendering out of the box |

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Obtain API Keys

You'll need free API keys from the following services:

**1. Groq (for Llama 3.3)**
- Visit [https://console.groq.com/](https://console.groq.com/)
- Sign up for a free account
- Navigate to API Keys section
- Create a new API key
- Copy the key (starts with `gsk_`)

**2. Cohere (for embeddings)**
- Visit [https://dashboard.cohere.com/](https://dashboard.cohere.com/)
- Sign up for a free account
- Navigate to API Keys section
- Create a new API key
- Copy the key

**3. Pinecone (for vector database)**
- Visit [https://app.pinecone.io/](https://app.pinecone.io/)
- Sign up for a free account
- Navigate to API Keys section
- Copy your API key (starts with `pcsk_`)

### Step 2: Clone and Navigate

```bash
# Navigate to the project directory
cd SmartKeigo/my-agent-app
```

### Step 3: Install Dependencies

```bash
# Install required Python packages
pip install -r ../requirements.txt

# Install the project in editable mode
pip install -e .
```

### Step 4: Configure Environment Variables

Create a `.env` file in the `my-agent-app` directory:

```bash
# On Windows
notepad .env

# On Mac/Linux
touch .env
```

Add your API keys to the `.env` file:

```text
GROQ_API_KEY=gsk_your_actual_groq_key_here
COHERE_API_KEY=your_actual_cohere_key_here
PINECONE_API_KEY=pcsk_your_actual_pinecone_key_here
```

**Important:** Replace the placeholder values with your actual API keys obtained in Step 1.

### Running the Application

**Option 1: Streamlit UI (Recommended)**
```bash
streamlit run app.py
```

**Option 2: LangGraph Server (for development/debugging)**
```bash
pip install "langgraph-cli[inmem]"
langgraph dev
```

Then open [LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/) to visualize and debug the graph.

## Project Structure

```
my-agent-app/
├── src/
│   └── agent/
│       ├── agent.py      # Agent node implementations (Analyzer, Specialist, Coach)
│       ├── graph.py      # LangGraph workflow definition
│       ├── state.py      # State management (KeigoState)
│       └── utils.py      # RAG utilities (Pinecone + Cohere embeddings)
├── app.py                # Streamlit frontend
├── .env                  # API keys (not in git)
└── pyproject.toml        # Project configuration
```

## How It Works

1. **User Input**: Casual Japanese text is entered via the Streamlit UI
2. **Language Analyzer**: Extracts intent and identifies the target audience (client, boss, coworker)
3. **Keigo Specialist**: Transforms the text using RAG-retrieved business templates and applies appropriate honorifics
4. **Cultural Coach**: Validates the output against business etiquette standards
5. **Loop**: If validation fails, the workflow routes back to the Specialist for refinement
6. **Output**: Final polished Keigo text with cultural context explanations

## Development

While iterating on your graph in LangGraph Studio, you can edit past state and rerun your app from previous states to debug specific nodes. Local changes will be automatically applied via hot reload.

For more advanced features and examples, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/).

