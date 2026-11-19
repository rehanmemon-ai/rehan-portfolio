# ConnectHub — Live Demonstration Script & Shot List

This document provides a concise 3-minute technical walkthrough script and demonstration shot list for presenting the ConnectHub Real-Time AI Messaging Engine to recruiters and hiring managers.

---

## 1. Demo Pre-Flight Checklist

- **Live Application URL:** [https://connecthub-web-w89e.onrender.com](https://connecthub-web-w89e.onrender.com)
- **GitHub Repository:** [https://github.com/rehanmemon-ai/Project_Python_Chat_system](https://github.com/rehanmemon-ai/Project_Python_Chat_system)
- **Browser Windows:** Open two side-by-side incognito browser windows to demonstrate two active users communicating in real time over WebSockets.
- **Backend Architecture:** FastAPI ASGI server hosted on Render with Neon Serverless PostgreSQL in Singapore.

---

## 2. 3-Minute Presentation Walkthrough

### Act 1: The Engineering Problem & Architecture (0:00 – 0:45)
- **Spoken Narrative:**
  > *"ConnectHub is an asynchronous, multi-room real-time messaging engine built with Python, FastAPI, and PostgreSQL, designed to combine high-throughput WebSocket communication with context-aware AI capabilities."*
  > *"Rather than relying on external polling or third-party chat widgets, the architecture implements a native ASGI WebSocket connection manager, async SQLAlchemy sessions with connection pooling, and strict role-based access control."*
- **Visual Action:**
  - Display the system architecture pipeline diagram (`diagrams/connecthub-pipeline.svg`).
  - Point to the dual paths: real-time in-memory socket dispatch vs. asynchronous PostgreSQL persistence.

### Act 2: Real-Time WebSockets & In-Memory Presence (0:45 – 1:30)
- **Spoken Narrative:**
  > *"Here we have User A and User B connected to the same project chat room in real time."*
  > *"As User A types, an ephemeral `typing` event is dispatched across the socket manager directly to active room peers without hitting the database, minimizing latency and database I/O."*
  > *"When a message is submitted, it is transactionally committed through async SQLAlchemy and broadcasted to all connected clients with instant DOM updates and read receipt acknowledgement."*
- **Visual Action:**
  - Type in Window 1; show immediate "User A is typing..." indicator appearing in Window 2.
  - Send message in Window 1; verify zero-latency arrival in Window 2.

### Act 3: AI Summarization & JSONB Semantic Search (1:30 – 2:30)
- **Spoken Narrative:**
  > *"When a team member enters a busy channel after several hours away, they don't need to scroll through hundreds of messages."*
  > *"The Gemini AI Summarization pipeline aggregates the last 50 room messages, validates prompt constraints, and generates an executive room summary."*
  > *"Additionally, for search, each message embedding is indexed into PostgreSQL JSONB columns, allowing bounded vector cosine similarity search calculated directly in Python without requiring external vector database infrastructure for prototype scale."*
- **Visual Action:**
  - Click the **"Summarize Room"** button; show the generated structured summary modal.
  - Execute a search query; show relevant matching messages highlighted by semantic score.

### Act 4: Test Harness & Release Readiness (2:30 – 3:00)
- **Spoken Narrative:**
  > *"The system is thoroughly verified by 97 backend unit and integration tests covering JWT auth, cursor pagination, socket handshakes, and database integrity, alongside 21 frontend Vitest component tests and 3 Playwright end-to-end integration scenarios."*
- **Visual Action:**
  - Show the terminal test execution or the verification section on `connecthub.html`.

---

## 3. Shot List & Presentation Timings

| Shot # | Screen View | Demonstration Target | Duration |
| :---: | :--- | :--- | :---: |
| **01** | Architecture Diagram | ASGI pipeline, WebSockets, PostgreSQL, Gemini RAG | 45 sec |
| **02** | Dual Split Browser | Live WebSocket message dispatch & typing indicators | 45 sec |
| **03** | Room Summary Modal | Gemini 1.5 Flash structured executive summary | 35 sec |
| **04** | Semantic Search UI | JSONB embedding similarity search across room messages | 25 sec |
| **05** | Terminal / Test Suite | 97 backend tests + 21 frontend tests + 3 Playwright tests | 30 sec |
