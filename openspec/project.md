# Project Context

## Purpose
IoT Data Analysis and Application — Homework 3.

Describe the learning and product goals for this assignment. For example:
- Ingest time-series sensor data and perform preprocessing (cleaning, resampling, feature extraction).
- Build analytics (statistics, anomaly detection, simple ML) and visualize results.
- Optionally connect to a live data source (e.g., MQTT) and stream results to a dashboard.

Fill in your specific goals here:
- [ ] ...
- [ ] ...

## Tech Stack
Select your primary technologies and add versions.

- Runtime & Language
  - [ ] Python (e.g., 3.11)
  - [ ] Node.js (e.g., 20.x)
  - [ ] Other: ____________

- Data & Analytics
  - [ ] Pandas / NumPy
  - [ ] SciPy / scikit-learn
  - [ ] Jupyter / IPython
  - [ ] Other: ____________

- Ingestion & Messaging
  - [ ] MQTT (e.g., Mosquitto)
  - [ ] HTTP/REST
  - [ ] File-based CSV/JSON/Parquet

- Storage
  - [ ] Local filesystem
  - [ ] SQLite / DuckDB
  - [ ] Time-series DB (InfluxDB / TimescaleDB)

- Visualization
  - [ ] Matplotlib / Seaborn
  - [ ] Plotly / Dash
  - [ ] Web UI (React/Vite) + Charts (ECharts/Recharts)

Record concrete selections and versions:
```
Python 3.11, Pandas 2.x, NumPy 1.x, Matplotlib 3.x, scikit-learn 1.x
```

## Project Conventions

### Code Style
Choose the conventions that apply.

- Python: `black` (line length 88), `isort`, `flake8`/`ruff`, type hints with `mypy`
- JavaScript/TypeScript: `prettier`, `eslint` (airbnb/base), `tsconfig` strict
- Naming: snake_case for files/modules (Python), PascalCase for classes, lowerCamelCase for variables/functions

Add specifics (formatters, rules, CI hooks):
```
Formatter: black + isort; Lint: ruff; Types: mypy (strict optional)
```

### Architecture Patterns
- Data pipeline stages: ingest → validate → transform → analyze → visualize
- Separation: `ingest/`, `processing/`, `models/`, `viz/`, `cli/`
- Config via `.env`/config file; avoid hardcoding paths

If different, document your chosen patterns here:
```
Pattern: ________
Rationale: ________
```

### Testing Strategy
- Unit tests for transforms and analytics (e.g., pytest or jest)
- Deterministic fixtures/sample datasets committed under `data/sample/`
- Property tests where applicable (e.g., invariants on resampling)
- Smoke tests for CLI/entrypoints

Specify tools and minimum coverage if required:
```
Tests: pytest; Coverage target: 80%
```

### Git Workflow
- Branching: trunk-based (`main`) or Git Flow; choose one
- Commits: Conventional Commits (e.g., `feat:`, `fix:`, `chore:`)
- PRs required before merge; squash-merge preferred

Define your exact choices:
```
Workflow: trunk-based; Conventional Commits; squash merges
```

## Domain Context
Provide domain knowledge relevant to IoT data for HW3.
- Sensor types: [e.g., temperature, humidity, accelerometer]
- Sampling rate and units: [e.g., 1Hz, °C, %]
- Expected data quality issues: [missing values, spikes, drift]
- Datasets/benchmarks used: [paths/links]

Notes:
```
Sensors: __________
Sampling: __________
Units: ____________
```

## Important Constraints
- Runtime/OS constraints: [Windows/macOS/Linux, local only]
- No external network if restricted; offline-first
- Performance: handle N records/sec or files up to size X
- Academic integrity or grading requirements: _________

## External Dependencies
List required services/APIs and local tooling.
- MQTT broker (e.g., Mosquitto) → host/port: _______
- Databases (InfluxDB/Timescale/SQLite) → connection details: _______
- Visualization servers (e.g., Dash/Streamlit/Grafana): _______

Access/config:
```
.env keys: MQTT_URL=..., DB_URL=...
```
