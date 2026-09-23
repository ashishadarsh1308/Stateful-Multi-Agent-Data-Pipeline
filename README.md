# 🤖 Stateful Multi-Agent Data Pipeline

An **end-to-end Agentic AI Data Assistant** that enables users to interact with databases and perform data analysis using natural language.

The system uses a **stateful multi-agent architecture** where a Parent Data Agent acts as an orchestrator and delegates tasks to specialized agents such as an **SQL Analyst Agent** and an **ETL Analyst Agent**.

The project combines **LangChain, LangGraph, PostgreSQL, Pydantic, ReAct, Context Engineering, and AI-as-a-Judge** to build a modular and reliable data intelligence system.

---

## 🚀 Key Features

* 🤖 **Multi-Agent Architecture**

  * Parent Data Agent orchestrates specialized sub-agents.
  * Router-based task delegation.

* 🗄️ **SQL Analyst Agent**

  * Converts natural language into SQL queries.
  * Dynamically injects database schema and metadata.
  * Executes read-only database operations.

* 🔐 **AI-as-a-Judge Security**

  * Validates generated SQL queries before execution.
  * Prevents destructive operations such as `DELETE`, `DROP`, `UPDATE`, and `INSERT`.
  * Provides an additional LLM-based safety layer.

* 🔄 **ETL Analyst Agent**

  * Handles Python-based data extraction and transformation.
  * Enables workflows that go beyond traditional SQL querying.

* 🧠 **Context Engineering**

  * Dynamically provides table schemas, columns, metadata, and relevant database context to the LLM.
  * Improves SQL generation accuracy.

* 🔁 **ReAct Architecture**

  * Enables iterative reasoning and tool execution.
  * Agents can reason → act → observe → reason until the task is completed.

* 💾 **Stateful Workflows**

  * LangGraph manages agent state and transitions.
  * Pydantic models provide structured state management.

* 📊 **Extensible Architecture**

  * Designed to support future visualization tools, APIs, additional agents, and data sources.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      User Query      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Parent Data Agent  │
                         │     / Router         │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐
        │ SQL Analyst     │ │ ETL Analyst     │ │ Future Agents │
        │ Agent           │ │ Agent           │ │ / Tools       │
        └────────┬────────┘ └────────┬────────┘ └───────────────┘
                 │                   │
                 ▼                   ▼
        ┌─────────────────┐ ┌─────────────────┐
        │ Context         │ │ Python Data     │
        │ Engineering     │ │ Processing      │
        └────────┬────────┘ └────────┬────────┘
                 │                   │
                 ▼                   │
        ┌─────────────────┐           │
        │ SQL Generation  │           │
        └────────┬────────┘           │
                 ▼                    │
        ┌─────────────────┐           │
        │ AI-as-a-Judge   │           │
        │ SQL Validation  │           │
        └────────┬────────┘           │
                 │                    │
                 ▼                    ▼
        ┌─────────────────────────────────────┐
        │             Data Layer              │
        │             PostgreSQL              │
        └──────────────────┬──────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Analysis / Final │
                  │     Response     │
                  └──────────────────┘
```

---

## 🧠 Agent Workflow

A typical request follows this workflow:

```text
User
 │
 ▼
Parent Agent
 │
 ├── SQL-related request ──► SQL Analyst
 │                              │
 │                              ▼
 │                       Schema / Metadata
 │                              │
 │                              ▼
 │                        SQL Generation
 │                              │
 │                              ▼
 │                       AI-as-a-Judge
 │                              │
 │                     ┌────────┴────────┐
 │                     │                 │
 │                   Safe             Unsafe
 │                     │                 │
 │                     ▼                 ▼
 │                Execute SQL       Regenerate /
 │                     │             Reject
 │                     ▼
 │                 Database
 │
 └── ETL request ─────────► ETL Analyst
                                │
                                ▼
                         Extract / Transform
                                │
                                ▼
                            Analysis
```

---

## 🛠️ Technology Stack

| Technology        | Purpose                                      |
| ----------------- | -------------------------------------------- |
| **Python**        | Core development language                    |
| **LangChain**     | LLM and tool integration                     |
| **LangGraph**     | Stateful agent orchestration                 |
| **PostgreSQL**    | Relational database                          |
| **Pydantic**      | Structured state and data validation         |
| **LLM**           | Natural language understanding and reasoning |
| **ReAct**         | Reasoning and tool execution architecture    |
| **Groq**          | LLM inference                                |
| **Python/Pandas** | ETL and data processing                      |
| **Git/GitHub**    | Version control                              |

---

## 📂 Project Structure

```text
Stateful-Multi-Agent-Data-Pipeline/
│
├── Agents/
│   ├── parent_agent.py
│   ├── sql_agent.py
│   └── etl_agent.py
│
├── Models/
│   └── schema.py
│
├── Tools/
│   ├── database_tools.py
│   └── etl_tools.py
│
├── utils/
│   ├── database.py
│   └── llm_pick.py
│
├── graph/
│   └── workflow.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> Folder names may vary depending on the implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashishadarsh1308/Stateful-Multi-Agent-Data-Pipeline.git

cd Stateful-Multi-Agent-Data-Pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

host=localhost
port=5432
database=postgres
user=postgres
password=your_password
```

**Never commit `.env` to GitHub.**

Use `.env.example` to document required environment variables:

```env
GROQ_API_KEY=

host=
port=
database=
user=
password=
```

---

## 🗄️ PostgreSQL Setup

Make sure PostgreSQL is installed and running.

Create the required database:

```sql
CREATE DATABASE postgres;
```

Configure the database credentials in `.env`.

The SQL Analyst Agent can then inspect database metadata and generate queries based on the available schema.

---

## ▶️ Running the Project

After configuring the environment:

```bash
python main.py
```

The assistant can then receive natural-language data requests.

Example:

```text
Show me the top 10 customers by total revenue.
```

The system can:

```text
Understand request
       ↓
Route to SQL Analyst
       ↓
Retrieve database context
       ↓
Generate SQL
       ↓
Validate SQL with AI Judge
       ↓
Execute safe query
       ↓
Analyze result
       ↓
Return response
```

---

## 💬 Example Queries

### SQL Analytics

```text
How many customers are in the database?
```

```text
Show the top 10 products by revenue.
```

```text
What was the total sales for each month?
```

```text
Which region generated the highest revenue?
```

### ETL Tasks

```text
Load this dataset and clean missing values.
```

```text
Transform the dataset and calculate the average sales per region.
```

```text
Analyze this CSV and identify unusual values.
```

---

## 🔐 AI-as-a-Judge

One of the important components of the system is the **AI-as-a-Judge** mechanism.

Instead of directly executing an LLM-generated SQL query:

```text
LLM
 │
 ▼
Generated SQL
 │
 ▼
AI Judge
 │
 ├── SAFE ─────► Database
 │
 └── UNSAFE ──► Reject / Regenerate
```

The judge evaluates the query against predefined safety rules.

For example, queries containing destructive operations such as:

```sql
DROP
DELETE
UPDATE
INSERT
ALTER
TRUNCATE
```

can be rejected.

This provides an additional protection layer between the LLM and the database.

> AI validation should complement, not replace, conventional database permissions and security controls.

---

## 🧠 Context Engineering

The SQL Agent does not rely only on the user's question.

Relevant database information is dynamically added to the LLM context:

```text
User Question
      +
Database Schema
      +
Table Names
      +
Column Names
      +
Column Metadata
      +
Relevant Context
      ↓
     LLM
      ↓
Generated SQL
```

This approach helps the model understand the actual structure of the database and reduces incorrect SQL generation.

---

## 🔄 ReAct Architecture

The system follows the **Reasoning + Acting** paradigm.

Conceptually:

```text
        ┌──────────────┐
        │    Reason    │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     Act      │
        │  Tool Call   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   Observe    │
        │ Tool Result  │
        └──────┬───────┘
               │
               └──────────────► Reason
```

This allows the agent to perform multiple tool calls when solving a complex task instead of generating a single response.

---

## 🧩 Why LangGraph?

LangGraph is used to represent the agent workflow as a **stateful graph**.

Each node performs a specific operation:

```text
START
  │
  ▼
Router
  │
  ├────► SQL Agent
  │         │
  │         ▼
  │      SQL Judge
  │         │
  │         ▼
  │      Database
  │
  └────► ETL Agent
            │
            ▼
         Analysis
            │
            ▼
           END
```

The graph structure makes the system easier to extend with additional agents, tools, validation steps, and decision points.

---

## 📌 Key Concepts Demonstrated

This project demonstrates practical implementation of:

* Agentic AI
* Multi-Agent Systems
* LangChain
* LangGraph
* ReAct Agents
* Router Architecture
* Stateful Workflows
* Context Engineering
* Tool Calling
* SQL Generation
* SQL Safety Validation
* AI-as-a-Judge
* ETL Pipelines
* PostgreSQL
* Pydantic State Models
* LLM Orchestration
* Modular Agent Design

---

## 🔮 Future Enhancements

Potential extensions include:

* 📊 Automatic data visualization
* 📈 Chart generation agents
* 🔍 Advanced SQL query optimization
* 📄 PDF/Excel data ingestion
* 🌐 External API tools
* 🧠 RAG-based business knowledge
* 📝 Query history and audit logs
* 🔐 Role-based database permissions
* 🧪 Automated agent evaluation
* 📡 Streaming agent responses
* 🖥️ Web-based UI
* 🔗 MCP-based tool integration

---

## 🎯 Project Objective

The goal of this project is to demonstrate how **Agentic AI can be applied to real-world data workflows** by combining LLM reasoning, specialized agents, database tools, state management, validation, and ETL capabilities into a single modular system.

Rather than building a single monolithic AI assistant, the architecture separates responsibilities across specialized agents, making the system easier to maintain, validate, and extend.

---

## 👨‍💻 Author

**Ashish Kumar Adarsh**

Interested in **Generative AI, Agentic AI, LLMs, RAG, and AI Engineering**.

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ and exploring the architecture to understand how stateful multi-agent systems can be designed for real-world data applications.
