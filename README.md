CodeGuardian AI 

A system of intelligent agents that operate on code repositories, PRs, and CI/CD pipelines to provide context-aware insights, recommendations, and automation for development teams. The system is orchestrated by an MCP (Multi-Agent Control Platform) which manages agents, context, and communication.

flowchart TB
  A[GitHub Repo<br/>1) Developer opens or updates PR] -->|GitHub webhook POST /webhook| B[Express Backend (Node.js)<br/>• /webhook route<br/>• Extract diff + queue job (Redis/BullMQ)]
  B --> C[MCP (Model Context Protocol Layer)<br/>• Repo context, security rules, static analysis results<br/>• Builds structured prompt]
  C --> D[GPT-5 / LLM Engine<br/>• Analyzes diff<br/>• Detects SQL injection, hardcoded creds, missing validation]
  D --> E[Express + GitHub API<br/>• Receives AI response<br/>• POST /repos/:owner/:repo/pulls/:pull_number/comments<br/>• Log to DB (Postgres/MongoDB)]
  E --> F[Dashboard UI (Optional)<br/>• PRs reviewed, risk categories, agent confidence]
