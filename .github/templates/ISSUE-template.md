# ISSUE-{XXX}: {Title}

> **Feature:** FEATURE-{XXX} - {Feature Name}
> **Type:** [Feature / Bug / Tech Debt / Spike / Documentation]
> **Effort:** [S: <1 day / M: 1-2 days / L: 2-3 days]
> **Priority:** [P0-Critical / P1-High / P2-Medium / P3-Low]
> **Status:** [Backlog / Ready / In Progress / In Review / Done]

---

## ⚠️ Atomicity Check

> ISSUEs MÜSSEN atomar sein: 1-3 Tage maximale Bearbeitungszeit

**Self-Check vor dem Erstellen:**
- [ ] Kann in 1-3 Tagen abgeschlossen werden
- [ ] Hat max. 5 Acceptance Criteria
- [ ] Betrifft max. 2-3 API Endpoints
- [ ] Betrifft max. 2 Entitäten
- [ ] Titel enthält kein "und" (z.B. "Setup AND Configure AND Test")

**Wenn einer dieser Checks NEIN ist → ISSUE aufteilen!**

---

## Description

{Kurze, prägnante Beschreibung was implementiert werden soll}

**Context:**
{Warum ist diese Implementierung notwendig? Welches Problem löst sie?}

**User Story Reference:**
> Als {Rolle} möchte ich {Funktionalität} um {Nutzen}

---

## Acceptance Criteria

> Alle Kriterien müssen testbar sein (pass/fail)

- [ ] {Konkretes, testbares Kriterium 1}
- [ ] {Konkretes, testbares Kriterium 2}
- [ ] {Konkretes, testbares Kriterium 3}
- [ ] Error handling implementiert für {Szenarien}
- [ ] Logging implementiert für {wichtige Aktionen}

**Beispiele für gute Acceptance Criteria:**
- ✅ "POST /api/users returns 201 with user object on success"
- ✅ "POST /api/users returns 400 with validation errors for invalid email"
- ✅ "User entity has fields: id, email, name, created_at"
- ❌ "API works correctly" (zu vage)
- ❌ "Good error handling" (nicht testbar)

---

## Technical Requirements

### Architecture Constraints (ADR References)

> Jedes ISSUE MUSS mindestens 1 ADR referenzieren!

| ADR | Relevant Decision | Constraint for this ISSUE |
|-----|-------------------|---------------------------|
| ADR-{XXX} | {Entscheidung} | {Was muss beachtet werden} |
| ADR-{YYY} | {Entscheidung} | {Was muss beachtet werden} |

**Beispiel:**
| ADR | Relevant Decision | Constraint |
|-----|-------------------|------------|
| ADR-001 | Use FastAPI | All endpoints must use FastAPI routers |
| ADR-002 | Use PostgreSQL | Use SQLAlchemy 2.0 for data access |
| ADR-003 | OAuth 2.0 | Endpoints require Bearer token validation |

### API Contract (wenn relevant)

```yaml
# OpenAPI-style specification
endpoint: {HTTP Method} {Path}
description: {What this endpoint does}
request:
  headers:
    Authorization: Bearer {token}
  body:
    type: object
    properties:
      field1:
        type: string
        required: true
      field2:
        type: integer
        required: false
response:
  success:
    status: 200/201/204
    body:
      type: object
      properties:
        id: string
        field1: string
  error:
    400:
      description: Validation error
      body: { errors: [{field, message}] }
    401:
      description: Unauthorized
    404:
      description: Not found
```

### Data Model (wenn relevant)

```
Entity: {EntityName}
├── id: UUID (PK)
├── field1: string (required, max 255)
├── field2: integer (optional)
├── created_at: timestamp (auto)
├── updated_at: timestamp (auto)
└── relations:
    └── {RelatedEntity}: {relationship type}

Indexes:
├── idx_{entity}_field1 (field1)
└── idx_{entity}_created (created_at)

Constraints:
├── unique (field1)
└── check (field2 > 0)
```

### Technology Stack (aus ADRs)

| Component | Technology | Version | Notes |
|-----------|------------|---------|-------|
| Language | {z.B. Python} | {z.B. 3.11+} | ADR-001 |
| Framework | {z.B. FastAPI} | {z.B. 0.104+} | ADR-001 |
| Database | {z.B. PostgreSQL} | {z.B. 15} | ADR-002 |
| ORM | {z.B. SQLAlchemy} | {z.B. 2.0} | ADR-002 |

---

## Implementation Notes

### Suggested Approach

> Empfohlene Schritte für die Implementierung

1. **Setup** (optional): {Vorbereitende Schritte}
2. **Data Layer**: {Entity/Repository erstellen}
3. **Business Logic**: {Service Layer implementieren}
4. **API Layer**: {Endpoint implementieren}
5. **Tests**: {Test Cases schreiben}
6. **Documentation**: {API Docs aktualisieren}

### Code Structure

```
src/
├── {module}/
│   ├── models/
│   │   └── {entity}.py          # SQLAlchemy Model
│   ├── repositories/
│   │   └── {entity}_repository.py
│   ├── services/
│   │   └── {entity}_service.py
│   ├── api/
│   │   └── {entity}_router.py   # FastAPI Router
│   └── schemas/
│       └── {entity}_schema.py   # Pydantic Schemas
└── tests/
    └── {module}/
        ├── test_{entity}_repository.py
        └── test_{entity}_router.py
```

### Edge Cases

> Wichtige Edge Cases die behandelt werden müssen

| Edge Case | Expected Behavior | Test Case |
|-----------|-------------------|-----------|
| {Edge Case 1} | {Wie soll System reagieren} | {Test Name} |
| {Edge Case 2} | {Wie soll System reagieren} | {Test Name} |
| {Edge Case 3} | {Wie soll System reagieren} | {Test Name} |

### Security Considerations

- [ ] Input Validation: {Welche Felder validieren}
- [ ] Authorization: {Welche Rollen haben Zugriff}
- [ ] Rate Limiting: {Wenn applicable}
- [ ] Audit Logging: {Welche Aktionen loggen}

---

## Testing Requirements

### Unit Tests

| Test Case | Description | Priority |
|-----------|-------------|----------|
| test_{function}_success | Happy path | P0 |
| test_{function}_invalid_input | Validation | P0 |
| test_{function}_not_found | 404 handling | P1 |
| test_{function}_unauthorized | Auth check | P1 |

**Coverage Target:** > {X}% für dieses ISSUE

### Integration Tests

| Test Case | Description | Dependencies |
|-----------|-------------|--------------|
| test_{endpoint}_e2e | Full flow test | Database |
| test_{endpoint}_with_{external} | External integration | {Service} |

### Manual Testing Checklist

- [ ] Happy path funktioniert
- [ ] Error cases zeigen korrekte Meldungen
- [ ] Performance akzeptabel
- [ ] Logs sind aussagekräftig

---

## Dependencies

### Blocked By

| ISSUE | Description | Status | ETA |
|-------|-------------|--------|-----|
| ISSUE-{XXX} | {Warum blockiert} | {Status} | {Datum} |

### Blocks

| ISSUE | Description | Impact if Delayed |
|-------|-------------|-------------------|
| ISSUE-{YYY} | {Was wird blockiert} | {Impact} |

### External Dependencies

| Dependency | Owner | Status | Notes |
|------------|-------|--------|-------|
| {System/API} | {Team} | {Status} | {Notes} |

---

## Definition of Done

### Code
- [ ] Code implementiert gemäß Acceptance Criteria
- [ ] Code folgt ADR Constraints
- [ ] Code ist selbst-dokumentierend (klare Namen)
- [ ] Keine TODO/FIXME ohne zugehöriges ISSUE

### Tests
- [ ] Unit Tests geschrieben (Coverage > {X}%)
- [ ] Integration Tests geschrieben (wenn required)
- [ ] Alle Tests grün

### Quality
- [ ] Linting passed
- [ ] Type Checking passed (wenn applicable)
- [ ] Security Scan passed
- [ ] Performance acceptable

### Review
- [ ] Self-Review durchgeführt
- [ ] Code Review (min. 1 Approval)
- [ ] Architecture-compliant (ADR check)

### Documentation
- [ ] API Docs aktualisiert (wenn API Änderung)
- [ ] README aktualisiert (wenn Setup Änderung)
- [ ] Inline Comments für komplexe Logik

### Deployment
- [ ] PR merged to main
- [ ] Deployed to Staging
- [ ] Smoke Test in Staging passed
- [ ] Ready for Production Deployment

---

## Spec Kit Compatibility Note

> Diese ISSUEs können /speckit.tasks ERSETZEN oder ERGÄNZEN

**Option A: Skip /speckit.tasks (Empfohlen)**
- Nutze diese ISSUEs direkt mit Developer Agent
- ISSUEs sind bereits atomar (1-3 Tage)
- ISSUEs haben ADR References
- ISSUEs haben klare Acceptance Criteria

**Option B: Zusätzlich /speckit.tasks**
- Nutze /speckit.tasks für weitere Granularität
- Kann zusätzliche Tasks generieren
- Vergleiche mit vorhandenen ISSUEs

---

## Notes

{Zusätzliche Hinweise, Kontext, oder Referenzen}

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {Date} | Architect Agent | Initial draft |
| 1.1 | {Date} | {Author} | {Changes} |

---

**Created by:** Architect Agent
**Ready for:** Developer Agent
**ADR Compliance:** Verified