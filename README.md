
# MMA SaaS Boilerplate (MVP + module placeholders)

This is a minimal starter project for an MMA SaaS platform with placeholders for Analytics, Scouting and AI modules.
It contains a basic FastAPI backend, a React + Vite frontend, an AI folder and a `docker-compose.yml` to run everything locally.

## What is included
- backend/ (FastAPI) with basic auth and player profile endpoints
- frontend/ (React + Vite + Tailwind) with auth & simple dashboard pages
- ai-analytics/ (placeholder for notebooks, models and pipelines)
- docker-compose.yml for local dev
- README with quick start

## Quick start (requires Docker & Docker Compose)
```bash
git clone <this-repo>
cd mma_saas_boilerplate
docker-compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000 (OpenAPI: /docs)

## Notes
- This is a boilerplate: fill in real ML models, DB migrations, production config and secrets before deploying.
- Secrets in docker-compose are for development only.


## Next steps added by assistant
1. **Database & Alembic**: alembic scaffolding is added in `backend/alembic/`. Configure `alembic.ini` and `env.py` for your production DB and run migrations.
2. **Telemetry (Realtime)**: WebSocket endpoint at `/telemetry/ws`. For production-scale ingestion use Kafka/aiokafka and a stream processor.
3. **ML model**: A dummy model trainer `ai-analytics/simple_model.py` is included. Run it to save a model:
   ```bash
   python ai-analytics/simple_model.py
   ```
   Then the API `/ml/predict` will be able to load `ai-analytics/models/simple_model.joblib` and return predictions.
4. **CI/CD**: GitHub Actions workflow at `.github/workflows/ci.yml` builds backend and frontend. Add tests and deployment steps as needed.
