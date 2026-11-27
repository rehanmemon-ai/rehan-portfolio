# ConnectHub — Live Demonstration Script & Shot List

Concise 3-minute walkthrough script and demonstration shot list for presenting the ConnectHub Real-Time AI Messaging Engine.

---

## 1. Demo Pre-Flight Checklist

- **Live Application URL:** [https://connecthub-web-w89e.onrender.com](https://connecthub-web-w89e.onrender.com)
- **GitHub Repository:** [https://github.com/rehanmemon-ai/ConnectHub-Messaging_Platform](https://github.com/rehanmemon-ai/ConnectHub-Messaging_Platform)
- **Browser Windows:** Open two side-by-side incognito browser windows to show two active users communicating over WebSockets.
- **Backend Architecture:** FastAPI ASGI service with PostgreSQL persistence, in-memory WebSocket connection state, Gemini room summarization, and room-scoped Python cosine search over JSONB embeddings.

---

## 2. 3-Minute Presentation Walkthrough

### Act 1: Architecture & Trade-offs (0:00 – 0:45)
- Walk through `diagrams/connecthub-pipeline.svg`:
  - FastAPI handles REST auth and `/ws/{room_id}` WebSockets.
  - Async SQLAlchemy persists room history to PostgreSQL.
  - Presence is tracked cleanly in single-process memory (prototype scale).

### Act 2: Real-Time WebSockets & Presence (0:45 – 1:30)
- Send a message in Window 1 and observe real-time delivery, typing status, and presence updates in Window 2.

### Act 3: Gemini Room Summaries & JSONB Search (1:30 – 2:30)
- Trigger **"Summarize Room"** to demonstrate synchronous request-route Gemini catch-up summarization.
- Execute a room query demonstrating PostgreSQL JSONB embedding cosine comparison in Python (noting exact search fallback when AI API keys are disabled).

### Act 4: Automated Test Suite (2:30 – 3:00)
- Present verified suite coverage (`QA_RESULTS.md`): `97` backend `pytest` unit/integration tests, `21` React `Vitest` tests, and `3` Playwright end-to-end scenarios.

---

## 3. Shot List & Timings

| Shot # | Screen View | Target Focus | Duration |
| :---: | :--- | :--- | :---: |
| **01** | Architecture Diagram | FastAPI ASGI, WebSockets, PostgreSQL, Gemini, JSONB search | 45 sec |
| **02** | Dual Split Browser | Live WebSocket message delivery & typing indicators | 45 sec |
| **03** | Room Summary Modal | Synchronous Gemini summary generation route | 35 sec |
| **04** | Room Search UI | JSONB cosine vector similarity / exact keyword search | 25 sec |
| **05** | Test Runner Output | 97 pytest + 21 Vitest + 3 Playwright tests | 30 sec |
