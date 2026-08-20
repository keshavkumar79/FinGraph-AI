# FinGraph AI

> **AI-powered financial crime network detection and investigation platform.**

FinGraph AI detects suspicious financial activity by analyzing **transaction networks and behavioral patterns**, rather than evaluating transactions in isolation.

## Problem

Modern financial crime is increasingly distributed across multiple accounts and transactions. Traditional transaction-level rules can miss:

- Multi-hop fund movement
- Circular transaction flows
- Layering patterns
- Mule-account behavior
- Abnormal transaction velocity
- Coordinated account networks

## Solution

FinGraph AI models financial activity as a **directed transaction graph**:

```text
Account A ──→ Account B ──→ Account C
     ↑                         │
     └─────────────────────────┘
```

The platform combines **graph analytics, deterministic detection, anomaly detection, and explainable risk scoring** to identify and investigate suspicious networks.

## Core Capabilities

- **Transaction Graph Modeling** — represent accounts as nodes and transactions as directed edges.
- **Circular Flow Detection** — identify suspicious multi-account cycles.
- **Account Intelligence** — calculate transaction volume, flow, and connectivity features.
- **Velocity Analysis** — detect unusually rapid movement of funds.
- **Mule Account Detection** — identify abnormal inbound/outbound transaction behavior.
- **Layering Detection** — analyze multi-hop transaction patterns.
- **Anomaly Detection** — identify behavioral outliers using unsupervised ML.
- **Explainable Risk Scoring** — provide a 0–100 risk score with interpretable contributing signals.
- **Investigation Graph** — enable investigators to trace suspicious financial networks.

## Architecture

```text
                 Transaction Data
                        │
                        ▼
                Data Preprocessing
                        │
                        ▼
              Transaction Graph
                  NetworkX
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Rules       Graph Signals    ML Models
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  Risk Engine
                        │
                        ▼
              Explainable Findings
                        │
                        ▼
             Investigation Dashboard
```

## Tech Stack

**Backend**

- Python
- FastAPI
- Pydantic
- Pandas
- NumPy

**Graph & ML**

- NetworkX
- Scikit-learn
- Graph-based feature engineering
- Unsupervised anomaly detection

**Frontend**

- React
- Cytoscape.js / D3.js

**Planned Infrastructure**

- PostgreSQL
- Neo4j
- Docker

## Project Structure

```text
fingraph-ai/
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── config.py
│   └── main.py
├── data/
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Clone

```bash
git clone <repository-url>
cd fingraph-ai
```

### 2. Create environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Current API

| Endpoint | Purpose |
|---|---|
| `GET /` | API status |
| `GET /health` | Health check |
| `POST /transactions/` | Ingest transaction data |
| `GET /accounts/{account_id}` | Account-level transaction analysis |
| `GET /investigations/circular-flows` | Detect circular transaction patterns |

## Example

Input:

```text
A → B  ₹50,000
B → C  ₹48,000
C → D  ₹45,000
D → A  ₹40,000
```

FinGraph AI identifies the cycle:

```text
A → B → C → D → A
```

and produces an investigation finding such as:

```json
{
  "pattern": "CIRCULAR_FLOW",
  "risk": "HIGH",
  "accounts": ["A", "B", "C", "D"]
}
```

## Roadmap

- [x] FastAPI backend
- [x] Transaction ingestion
- [x] Graph-based transaction modeling
- [x] Circular-flow detection
- [x] Account-level analytics
- [ ] Transaction velocity detection
- [ ] Mule-account detection
- [ ] Layering detection
- [ ] Behavioral anomaly detection
- [ ] Unified risk-scoring engine
- [ ] Explainable AI investigation layer
- [ ] Interactive financial network visualization
- [ ] Persistent database / graph storage
- [ ] AI Investigation Copilot
- [ ] Production deployment

## Responsible AI

FinGraph AI is designed as an **investigation-support system**, not an autonomous decision-maker.

Risk scores should be treated as signals for further investigation rather than definitive evidence of financial crime. Production deployment would require appropriate privacy controls, data governance, fairness evaluation, human oversight, and regulatory compliance.

## Status

**Prototype / Active Development**

FinGraph AI is currently being developed as a hackathon prototype with a focus on graph-based financial crime detection and explainable investigation workflows.

## License

To be defined.
