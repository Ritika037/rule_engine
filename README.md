# Rule Engine with AST

A simple 3-tier rule engine application that determines user eligibility based on various attributes using Abstract Syntax Tree (AST) representation.

## Architecture Overview

The application consists of three main tiers:

1. Frontend (UI)
2. Backend (API)
3. Data Layer

### Technology Stack

- Frontend: React with TypeScript
- Backend: Python FastAPI
- Database: PostgreSQL
- Container: Docker

## Database Schema

```sql
-- Rules table
CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Rule attributes catalog
CREATE TABLE attribute_catalog (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    data_type VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Rule evaluation history
CREATE TABLE rule_evaluations (
    id SERIAL PRIMARY KEY,
    rule_id INTEGER REFERENCES rules(id),
    input_data JSONB NOT NULL,
    result BOOLEAN NOT NULL,
    evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Project Structure

```
rule-engine/
├── docker-compose.yml
├── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── types/
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── models/
│   │   ├── parser/
│   │   ├── engine/
│   │   └── api/
│   └── requirements.txt
└── scripts/
    └── init.sql
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rule-engine.git
cd rule-engine
```

2. Start the containers:
```bash
docker-compose up -d
```

3. Initialize the database:
```bash
docker-compose exec db psql -U postgres -f /scripts/init.sql
```

## API Endpoints

### Create Rule
```bash
POST /api/rules
Content-Type: application/json

{
    "name": "Sales Rule",
    "rule_string": "((age > 30 AND department = Sales) OR (age < 25 AND department = Marketing)) AND (salary > 50000 OR experience > 5)"
}
```

### Evaluate Rule
```bash
POST /api/rules/{rule_id}/evaluate
Content-Type: application/json

{
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}
```

### Combine Rules
```bash
POST /api/rules/combine
Content-Type: application/json

{
    "rule_ids": [1, 2]
}
```

## Design Choices

1. **AST Implementation**: Used a recursive Node structure to represent the rule tree, allowing for complex nested conditions.

2. **Rule Parser**: Implemented a custom parser that tokenizes and parses rule strings into AST nodes, handling nested parentheses and operator precedence.

3. **Database Choice**: PostgreSQL was chosen for:
   - JSONB support for flexible rule storage
   - Transaction support for rule modifications
   - Rich querying capabilities

4. **API Design**: REST API with FastAPI for:
   - Type safety with Pydantic models
   - Automatic OpenAPI documentation
   - High performance with async support

## Testing

Run the tests using:
```bash
docker-compose exec backend pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License