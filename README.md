A system of intelligent agents that operate on code repositories, PRs, and CI/CD pipelines to provide context-aware insights, recommendations, and automation for development teams. The system is orchestrated by an MCP (Multi-Agent Control Platform) which manages agents, context, and communication.

graph TD

A[GitHub Repo] -->|1️⃣ Developer opens or updates PR| B[Express Backend (Node.js)]
B -->|Webhook triggers → POST /webhook| C[MCP (Model Context Protocol Layer)]
C -->|Sends structured prompt| D[GPT-5 / LLM Engine]
D -->|Returns structured output| E[Express + GitHub API]
E -->|Posts review comments + logs data| F[Dashboard UI (Optional)]

subgraph GitHub
A
end

subgraph Backend
B
E
end

subgraph AI_Processing
C
D
end

subgraph Frontend
F
end

%% Details inside each component
B:::box
C:::box
D:::box
E:::box
F:::box

classDef box fill:#1e293b,stroke:#94a3b8,color:#f1f5f9,rx:10,ry:10

%% Notes
click A "https://github.com" "View GitHub"
click E "https://docs.github.com/en/rest" "GitHub REST API Docs"

