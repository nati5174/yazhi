A system of intelligent agents that operate on code repositories, PRs, and CI/CD pipelines to provide context-aware insights, recommendations, and automation for development teams. The system is orchestrated by an MCP (Multi-Agent Control Platform) which manages agents, context, and communication.

┌──────────────────────────────────────────────────────────────┐
│                        GitHub Repo                           │
│                                                              │
│ 1️⃣ Developer opens or updates a PR                           │
│     ↓                                                        │
│ 2️⃣ GitHub Webhook triggers → POST /webhook (Express)         │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Express Backend (Node.js)                 │
│                                                              │
│ • /webhook route: receives PR payload                        │
│ • Extracts diff + PR metadata                                │
│ • Pushes job to queue (Redis/BullMQ)                         │
│                                                              │
│  --> calls MCP Context Manager                               │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                MCP (Model Context Protocol Layer)            │
│                                                              │
│ • Manages AI “context packs”:                                │
│    - Repo context (files, history)                           │
│    - Security rules (OWASP, regex patterns, etc.)            │
│    - Static analysis results                                 │
│                                                              │
│ • Sends structured prompt to GPT-5 or LLM                    │
│   for deep reasoning about vulnerabilities                   │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      GPT-5 or LLM Engine                     │
│                                                              │
│ • Analyzes code diff                                         │
│ • Detects patterns like:                                     │
│     - SQL injection risk                                     │
│     - Hardcoded credentials                                  │
│     - Missing input validation                               │
│ • Returns structured output:                                 │
│     { file, line, risk_type, comment_text }                  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      Express + GitHub API                    │
│                                                              │
│ • Receives AI response                                       │
│ • Posts inline review comments via GitHub REST API:          │
│   POST /repos/:owner/:repo/pulls/:pull_number/comments       │
│                                                              │
│ • Logs data to database (MongoDB/Postgres)                   │
└──────────────────────────────────────────────────────────────┘
    
└──────────────────────────────────────────────────────────────┘
