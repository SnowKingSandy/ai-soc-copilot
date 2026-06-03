# AI SOC Copilot 🛡️

An **AI-powered Security Operations Center (SOC) Copilot** that analyzes security logs, detects threats, investigates incidents, and generates automated incident reports using large language models and intelligent agent workflows.

> **Built for recruiters**: Production-grade architecture with FastAPI backend, LangGraph agents, Gemini LLM integration, and a clean modular structure.

---

## 🎯 Features

✅ **Log Analysis** - Parse and analyze security logs in real-time  
✅ **Threat Detection** - AI-powered threat identification using Gemini  
✅ **Incident Management** - Track, store, and retrieve security incidents  
✅ **Automated Reports** - Generate detailed incident reports automatically  
✅ **Agent Workflow** - Multi-agent LangGraph orchestration (Detector → Investigator → Reporter)  
✅ **REST API** - FastAPI endpoints with full documentation  
✅ **Database Persistence** - SQLAlchemy ORM with SQLite backend  
✅ **Production Ready** - Proper separation of concerns, error handling, and logging  

---

## 📁 Project Structure

```
ai-soc-copilot/
│
├── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── api/                     # API endpoints
│   │   │   ├── logs.py              # Log analysis endpoint
│   │   │   ├── incidents.py         # Incident management endpoints
│   │   │   └── health.py            # Health check endpoint
│   │   │
│   │   ├── agents/                  # LangGraph agents
│   │   │   ├── threat_detector.py   # Threat detection agent
│   │   │   ├── investigator.py      # Investigation agent
│   │   │   ├── reporter.py          # Report generation agent
│   │   │   └── graph.py             # Agent workflow orchestration
│   │   │
│   │   ├── services/                # Business logic
│   │   │   ├── llm_service.py       # Gemini LLM integration
│   │   │   ├── rag_service.py       # RAG/knowledge retrieval
│   │   │   ├── parser_service.py    # Log parsing
│   │   │   ├── severity_service.py  # Risk/severity scoring
│   │   │   └── incident_service.py  # Incident management
│   │   │
│   │   ├── schemas/                 # Pydantic models
│   │   │   ├── log_schema.py        # Log request/response
│   │   │   ├── incident_schema.py   # Incident data model
│   │   │   └── response_schema.py   # API response models
│   │   │
│   │   ├── models/                  # SQLAlchemy models
│   │   │   ├── incident.py          # Incident DB model
│   │   │   └── user.py              # User DB model
│   │   │
│   │   ├── core/                    # Configuration & constants
│   │   │   ├── config.py            # App configuration
│   │   │   ├── prompts.py           # LLM prompts
│   │   │   └── constants.py         # Global constants
│   │   │
│   │   ├── main.py                  # FastAPI app
│   │   ├── database.py              # Database setup
│   │   └── knowledge_base/          # Threat intelligence data
│   │
│   ├── tests/                        # Unit & integration tests
│   ├── requirements.txt              # Python dependencies
│   ├── .env                          # Environment variables (template)
│   └── venv/                         # Virtual environment
│
├── frontend/                         # (Future) React/Next.js frontend
│
├── infrastructure/                   # (Future) Docker, K8s configs
│
├── docs/                            # Documentation
│   ├── architecture.md              # System architecture
│   ├── api_design.md                # API documentation
│   ├── agent_flow.md                # Agent workflow docs
│   └── screenshots/                 # Demo screenshots
│
├── sample_logs/                     # Example security logs
│   ├── brute_force.log
│   ├── malware.log
│   ├── phishing.log
│   └── ransomware.log
│
├── docker-compose.yml               # (Future) Multi-container setup
├── .gitignore                       # Git ignore rules
├── README.md                        # This file
└── LICENSE                          # MIT License
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- Gemini API key ([get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-soc-copilot.git
   cd ai-soc-copilot
   ```

2. **Create virtual environment**
   ```bash
   cd backend
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Gemini API key
   ```

5. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access API**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 📝 API Endpoints

### POST `/analyze`
Analyze a security log and generate an incident report.

**Request:**
```json
{
  "log_text": "Failed login attempt from 192.168.1.100 for user admin"
}
```

**Response:**
```json
{
  "incident_id": "uuid-here",
  "severity": "high",
  "threat_type": "brute_force_attack",
  "description": "Detected multiple failed login attempts...",
  "recommended_actions": ["block_ip", "alert_soc_team", ...],
  "timestamp": "2024-06-02T10:30:00Z"
}
```

### GET `/incidents`
Retrieve all stored incidents.

### GET `/incidents/{incident_id}`
Retrieve a specific incident.

### DELETE `/incidents/{incident_id}`
Delete an incident.

### GET `/health`
Health check endpoint.

### GET `/stats`
Get analytics and statistics.

---

## 🤖 Agent Workflow

The system uses **LangGraph** to orchestrate multiple AI agents:

```
┌─────────────────────┐
│  Security Log Input │
└──────────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │  Threat Detector│ ◄── Analyzes log for threats
    │     Agent       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  Investigator   │ ◄── Deep investigation & context
    │     Agent       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │    Reporter     │ ◄── Generates formatted report
    │     Agent       │
    └────────┬────────┘
             │
             ▼
    ┌──────────────────┐
    │Incident Response │
    │     Returned     │
    └──────────────────┘
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI |
| **Agent Orchestration** | LangGraph |
| **LLM** | Google Gemini |
| **Database** | SQLAlchemy + SQLite |
| **API Documentation** | Swagger/OpenAPI |
| **Testing** | pytest |
| **Environment** | Python 3.9+ |
| **Deployment** | Docker (ready) |

---

## 📚 Documentation

- [Architecture](docs/architecture.md) - System design and components
- [API Design](docs/api_design.md) - Endpoint specifications
- [Agent Flow](docs/agent_flow.md) - LangGraph workflow details

---

## 📊 Sample Data

Example security logs are provided in `sample_logs/`:
- `brute_force.log` - Failed login attempts
- `malware.log` - Malware detection signatures
- `phishing.log` - Phishing attempt indicators
- `ransomware.log` - Ransomware activity patterns

Test the API with these files:
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"log_text": "YOUR_LOG_TEXT_HERE"}'
```

---

## 🔑 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Gemini API
GEMINI_API_KEY=your_api_key_here

# App
APP_NAME=AI SOC Copilot
DEBUG=true
LOG_LEVEL=INFO

# Database
DATABASE_URL=sqlite:///./soc.db

# LLM Settings
LLM_MODEL=gemini-pro
LLM_TEMPERATURE=0.3
```

---

## 🧪 Testing

Run tests:
```bash
cd backend
pytest tests/ -v
```

---

## 🚀 Deployment

### Docker (Coming Soon)
```bash
docker-compose up -d
```

### Production Checklist
- [ ] Add authentication (JWT/API keys)
- [ ] Set up PostgreSQL for production
- [ ] Configure CORS properly
- [ ] Add rate limiting
- [ ] Set up monitoring & logging
- [ ] Deploy frontend
- [ ] Set up CI/CD pipeline

---

## 📈 Roadmap

- [x] Core API with log analysis
- [x] Agent orchestration with LangGraph
- [x] Incident database storage
- [ ] Advanced threat detection
- [ ] RAG knowledge base integration
- [ ] React frontend dashboard
- [ ] Real-time log streaming
- [ ] Machine learning anomaly detection
- [ ] Multi-tenant support
- [ ] Kubernetes deployment

---

## Versioned Changelog

### V1 — Initial project structure (commit: `V1 - Initial project structure`)
- Date: initial work
- What: Created the base repo layout and placeholder backend files to define boundaries and goals:
  - `backend/app/` (api, services, schemas, models, core)
  - `docs/`, `sample_logs/`, and initial `.gitignore`, `LICENSE`
- Status: Foundation established for backend-first development.

### V1.1 — Frontend scaffold (commit: `V1.1 - Add Next.js frontend scaffold and install UI dependencies`)
- Date: follow-up milestone
- What: Added a Next.js TypeScript frontend scaffold and installed primary UI dependencies:
  - Created `frontend/` Next.js app (TypeScript) using `create-next-app`
  - Installed `axios`, `recharts`, and `lucide-react`
  - Created top-level `src/` scaffolding for `app/`, `components/`, `services/`, and `types/`
- Status: Frontend scaffold ready; no production logic yet.

### V1.2 — Dashboard v1 and frontend integration (commit: `V1.2 - Dashboard with basic incident stats and frontend scaffold`)
- Date: June 3, 2026
- What: Implemented the initial dashboard page and wired basic frontend scaffolding into the repository:
  - `frontend/src/app/dashboard/page.tsx` — dashboard page that fetches `/stats` from the backend (displays a JSON preview)
  - Small UI components scaffold under `frontend/src/components/`
  - `frontend/src/services/api.ts` — axios client (baseURL set to backend URL during development)
  - Committed frontend build files and moved app folder content into `frontend/src/app` to match Next.js app directory conventions
- Status: Dashboard v1 is live locally (visit `http://localhost:3000/dashboard`) and repository updated

---

## Recommended Commit / Release Naming

- `V1 - Initial project structure`
- `V1.1 - Add Next.js frontend scaffold and install UI dependencies`
- `V1.2 - Dashboard with basic incident stats and frontend scaffold`

Use semantic, versioned commit messages for clarity when recruiters or reviewers inspect history.

---

## Next Milestones

- Implement `/stats` backend endpoint returning aggregate incident counts.
- Replace dummy dashboard display with visually formatted `StatsCard` components and `IncidentTable` connected to `/incidents` endpoints.
- Add tests, CI pipeline, and a production-ready database (Postgres) plus Docker setup.

---

If you want, I can also add a `CHANGELOG.md` and tag a GitHub release for `v1.2`.

**Last Updated**: June 3, 2026

