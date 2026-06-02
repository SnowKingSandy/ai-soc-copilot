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

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Built as a portfolio project to showcase:
- Production-grade Python backend architecture
- AI/LLM integration
- Multi-agent systems with LangGraph
- RESTful API design
- Database modeling
- Software engineering best practices

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review sample logs for examples

---

## ⭐ Show Your Support

If this project helps you, please give it a star! ⭐

---

**Last Updated**: June 2, 2026  
**Version**: 1.0.0  
**Status**: Active Development
