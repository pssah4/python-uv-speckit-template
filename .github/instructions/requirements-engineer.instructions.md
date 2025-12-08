---
name: Requirements Engineer Quality Standards
applyTo: "requirements/epics/**/*.md, requirements/features/**/*.md, requirements/handoff/**/*.md"
description: "Qualitätsregeln für Requirements Engineering - Epics, Features und Spec Kit Integration"
---

# Requirements Engineer - Quality Standards

Diese Instructions werden automatisch angewendet beim Arbeiten mit Epic-, Feature- und Handoff-Dateien.

> **Ziel:** Der Architekt kann **sofort** mit ADRs starten UND /speckit.specify hat tech-agnostische Success Criteria.

---

## 📁 Unterstützte Dateitypen

```
✅ requirements/epics/EPIC-*.md
✅ requirements/features/FEATURE-*.md
✅ requirements/handoff/architect-handoff.md
✅ requirements/handoff/specify-context.md
```

---

## 🎯 Qualitätsziele

### Für den Architekten
- ✅ Klar identifizierte ASRs (🔴/🟡)
- ✅ Quantifizierte NFRs (mit Zahlen!)
- ✅ Dokumentierte Constraints
- ✅ Priorisierte Open Questions

### Für Spec Kit Integration
- ✅ **Tech-agnostische Success Criteria** (KRITISCH!)
- ✅ specify-context.md für /speckit.specify
- ✅ Klare Scope Boundaries

---

## 🔴 KRITISCH: Tech-Agnostic Success Criteria Validation

### Verbotene Begriffe in Success Criteria

Diese Begriffe dürfen NICHT in der "Success Criteria (Tech-Agnostic)" Section erscheinen:

```javascript
const FORBIDDEN_TERMS = [
  // Authentication/Authorization
  'OAuth', 'JWT', 'SAML', 'OpenID', 'OIDC', 'Bearer', 'Token',
  
  // API/Protocol
  'REST', 'GraphQL', 'gRPC', 'WebSocket', 'HTTP', 'HTTPS', 'API',
  'JSON', 'XML', 'YAML', 'endpoint', 'request', 'response',
  
  // Database
  'SQL', 'NoSQL', 'PostgreSQL', 'MySQL', 'MongoDB', 'Redis',
  'Elasticsearch', 'DynamoDB', 'query', 'index', 'table',
  
  // Frontend
  'React', 'Angular', 'Vue', 'Svelte', 'JavaScript', 'TypeScript',
  'CSS', 'HTML', 'DOM', 'component', 'state management',
  
  // Backend
  'Python', 'Java', 'Node', 'FastAPI', 'Express', 'Spring',
  'Django', 'Flask', 'microservice', 'serverless', 'lambda',
  
  // Infrastructure
  'Docker', 'Kubernetes', 'K8s', 'AWS', 'Azure', 'GCP',
  'container', 'pod', 'cluster', 'load balancer', 'CDN',
  
  // Performance (technical)
  'ms', 'millisecond', 'latency', 'throughput', 'req/sec',
  'cache', 'caching', 'Redis', 'Memcached',
  
  // Security (technical)
  'TLS', 'SSL', 'AES', 'encryption', 'hash', 'bcrypt',
  'RBAC', 'ABAC', 'firewall', 'WAF',
  
  // Messaging
  'Kafka', 'RabbitMQ', 'SQS', 'pub/sub', 'message queue',
  'event-driven', 'async', 'webhook'
];
```

### Validierung bei Feature-Speicherung

```markdown
CHECK Success Criteria Section:

Für jedes Kriterium:
1. ✅ Enthält KEINE verbotenen Begriffe?
2. ✅ Fokussiert auf User-Outcome?
3. ✅ Messbar ohne Technologie-Wissen?
4. ✅ Verständlich für Business Stakeholder?

WENN verbotener Begriff gefunden:
❌ Validation Error anzeigen
→ Umformulierung vorschlagen
```

### Fehlermeldung bei Tech-Begriff in Success Criteria

```
❌ Success Criteria enthält Technologie-Begriff

Datei: FEATURE-042-user-authentication.md
Section: Success Criteria (Tech-Agnostic)
Problem: Technologie-Begriff gefunden

Gefunden:
  ❌ "Response time < 200ms via Redis caching"
       └── Enthält: "ms", "Redis", "caching"
  
  ❌ "OAuth 2.0 authentication required"
       └── Enthält: "OAuth", "2.0"

Korrektur-Vorschläge:
  ✅ "Users experience sub-second response times"
  ✅ "Secure authentication using industry-standard protocols"

WARUM: Spec Kit's /speckit.specify erfordert tech-agnostische Kriterien.
       Technische Details gehören in die "Technical NFRs" Section.
```

### Transformation Guide: Tech → Tech-Agnostic

| ❌ Technical (verboten) | ✅ Tech-Agnostic (erlaubt) |
|------------------------|---------------------------|
| Response time < 200ms | Users experience sub-second response |
| OAuth 2.0 authentication | Secure authentication using industry standards |
| PostgreSQL with indexes | System efficiently handles 100K+ records |
| REST API with JSON | Machine-readable interface for integrations |
| 99.9% uptime SLA | System available during business hours with minimal interruptions |
| Redis caching | Frequently accessed data loads instantly |
| RBAC authorization | Users only see data relevant to their role |
| TLS 1.3 encryption | Data transmitted securely |
| Kubernetes auto-scaling | System handles traffic spikes without degradation |
| WebSocket real-time | Users see updates without refreshing |

---

## 🔍 Feature-Level Validierung

### Pflicht-Sections für Features

```markdown
CHECK beim Speichern:

1. ✅ Feature Description vorhanden? (1-2 Absätze)
2. ✅ Benefits Hypothesis vollständig?
3. ✅ User Stories vorhanden? (min. 1-3)
4. ✅ Success Criteria (Tech-Agnostic) Section vorhanden?
   - ✅ Alle Kriterien tech-frei?
   - ✅ Messbar?
   - ✅ User-outcome fokussiert?
5. ✅ Technical NFRs Section vorhanden?
   - Performance (mit Zahlen)
   - Security (spezifisch)
   - Scalability (messbar)
   - Availability (Uptime %)
6. ✅ ASRs identifiziert? (🔴/🟡)
7. ✅ Definition of Done vollständig?
```

### Success Criteria Format

```markdown
## 📊 Success Criteria (Tech-Agnostic)

> ⚠️ KEINE Technologie-Begriffe! Diese gehen in specify-context.md

| ID | Criterion | Target | Measurement |
|----|-----------|--------|-------------|
| SC-01 | {User-outcome} | {Wert} | {Methode} |
| SC-02 | {Verhalten} | {Wert} | {Methode} |

BEISPIELE - RICHTIG:
| SC-01 | User task completion rate | > 95% | UAT testing |
| SC-02 | Perceived response time | < 2 seconds | User survey |
| SC-03 | Concurrent user support | 100 users | Load testing |
| SC-04 | Data query efficiency | 100K records | Synthetic data test |

BEISPIELE - FALSCH (werden rejected):
| SC-01 | API response time | < 200ms | Monitoring | ← "API", "ms"
| SC-02 | OAuth login success | > 99% | Logs | ← "OAuth"
```

### Technical NFRs Format

```markdown
## 🔧 Technical NFRs (für Architekt)

> Diese Section DARF technische Details enthalten!

### Performance
- **Response Time**: < 200ms für 95% der Requests
- **Throughput**: 100 req/sec sustained
- **Caching**: Redis mit 5min TTL für hot data

### Security
- **Authentication**: OAuth 2.0 via Azure AD
- **Authorization**: RBAC mit 3 Rollen
- **Encryption**: TLS 1.3 in transit, AES-256 at rest

### Scalability
- **Concurrent Users**: 1,000 (auto-scale to 10,000)
- **Data Volume**: 10GB initial, 5GB/month growth
- **Horizontal Scaling**: Kubernetes HPA

### Availability
- **Uptime**: 99.9% (8.7h downtime/year)
- **RTO**: 15 minutes
- **RPO**: 5 minutes
```

---

## 🔍 Epic-Level Validierung (PoC & MVP)

### Pflicht-Sections für Epics

```markdown
CHECK beim Speichern:

1. ✅ Epic Hypothesis Statement vollständig? (7/7 Komponenten)
2. ✅ Business Outcomes quantifiziert?
3. ✅ Leading Indicators definiert?
4. ✅ MVP Features Liste vorhanden? (min. 3)
5. ✅ Features priorisiert? (P0/P1/P2)
6. ✅ Out-of-Scope explizit?
7. ✅ Dependencies dokumentiert?
8. ✅ Risks identifiziert?
9. ✅ Technical Debt dokumentiert? (nur PoC)
```

### Epic Hypothesis Statement Check

```markdown
Pflicht-Komponenten:

✅ FÜR [Zielkunden-Segment]
✅ DIE [Bedarf/Problem haben]
✅ IST DAS [Produkt/Lösung]
✅ EIN [Produktkategorie]
✅ DAS [Hauptnutzen bietet]
✅ IM GEGENSATZ ZU [Alternative]
✅ UNSERE LÖSUNG [Differenzierung]

ALLE 7 müssen vorhanden sein!
```

---

## 🔍 specify-context.md Validierung

### Pflicht-Sections

```markdown
CHECK requirements/handoff/specify-context.md:

1. ✅ Problem Statement vorhanden? (2-3 Sätze)
2. ✅ Target Users spezifisch? (nicht "Users")
3. ✅ Core Functionality als User Stories?
4. ✅ Success Criteria Section vorhanden?
   - ✅ ALLE Kriterien tech-agnostisch?
   - ✅ Keine FORBIDDEN_TERMS?
5. ✅ Scope In/Out definiert?
6. ✅ Constraints dokumentiert?
7. ✅ Dependencies gelistet?
8. ✅ Assumptions dokumentiert?
```

### Automatische Tech-Begriff-Prüfung

```markdown
SCAN specify-context.md für verbotene Begriffe:

Bei Fund:
❌ specify-context.md enthält Technologie-Begriffe!

Gefunden in "Success Criteria" Section:
  Line 42: "OAuth 2.0 authentication" 
           └── Verboten: OAuth
  Line 45: "Response < 200ms"
           └── Verboten: ms

Diese Begriffe verhindern korrektes /speckit.specify!

Aktion erforderlich:
  1. Ersetze technische Begriffe durch User-Outcomes
  2. Verschiebe technische Details in Technical NFRs
  3. Re-validiere specify-context.md
```

---

## 📊 Quality Gate: Spec Kit Ready Check

### Feature ist Spec Kit Ready wenn:

```
✅ Success Criteria Section vorhanden
✅ ALLE Success Criteria tech-agnostisch
✅ Keine FORBIDDEN_TERMS in Success Criteria
✅ Kriterien sind messbar
✅ Kriterien fokussieren auf User-Outcomes
✅ Technical NFRs separat dokumentiert
```

### specify-context.md ist Ready wenn:

```
✅ Alle Pflicht-Sections vorhanden
✅ Problem Statement klar (2-3 Sätze)
✅ User Personas spezifisch
✅ User Stories im "Als/möchte/um" Format
✅ Success Criteria ALLE tech-agnostisch
✅ Scope Boundaries explizit
✅ Keine FORBIDDEN_TERMS im gesamten Dokument
```

### Erfolgs-Meldung

```
✅ SPEC KIT READY!

Datei: requirements/handoff/specify-context.md
Status: Alle Validierungen bestanden

Success Criteria Validation:
  ✅ 5/5 Kriterien tech-agnostisch
  ✅ Keine verbotenen Begriffe gefunden
  ✅ Alle Kriterien messbar

Nächster Schritt:
  → Copy prompt aus specify-context.md
  → Paste in /speckit.specify
  → Optional: Attach source documents als Kontext
```

### Fehler-Meldung

```
❌ NICHT SPEC KIT READY

Datei: requirements/handoff/specify-context.md
Problem: Tech-Begriffe in Success Criteria

Gefunden:
  ❌ SC-02: "OAuth 2.0 login" → Enthält "OAuth"
  ❌ SC-04: "API response < 200ms" → Enthält "API", "ms"

Korrektur erforderlich:
  SC-02: ✅ "Secure user authentication"
  SC-04: ✅ "Users experience instant feedback"

Nach Korrektur erneut validieren!
```

---

## 🚫 Anti-Patterns

### ❌ Tech-Begriffe in Success Criteria

```
FALSCH (Success Criteria Section):
"OAuth 2.0 authentication with JWT tokens"
"REST API response < 200ms"
"PostgreSQL queries with proper indexes"

RICHTIG (Success Criteria Section):
"Secure user authentication"
"Users experience instant response"
"System handles large datasets efficiently"
```

### ❌ Success Criteria ohne Messbarkeit

```
FALSCH:
"Good user experience"
"Fast performance"
"Secure system"

RICHTIG:
"95% task completion rate in UAT"
"Users perceive response as instant (<2 sec)"
"No unauthorized data access in security audit"
```

### ❌ Implementierungs-Details in Success Criteria

```
FALSCH:
"Use Redis for caching"
"Implement microservices architecture"
"Deploy on Kubernetes"

RICHTIG:
"Frequently accessed data loads instantly"
"System components can scale independently"
"System handles traffic spikes gracefully"
```

---

## 🔄 Workflow mit Spec Kit

### RE Agent Workflow

```
1. BA-Dokument lesen
2. Epic erstellen (wenn PoC/MVP)
3. Features erstellen:
   - Success Criteria (TECH-AGNOSTISCH!)
   - Technical NFRs (für Architekt)
4. specify-context.md erstellen
5. Validierung durchführen
6. Handoff an Architect
```

### Spec Kit Integration Points

```
RE Agent Output              → Spec Kit Input
─────────────────────────────────────────────
Success Criteria (tech-agnostic) → /speckit.specify
Technical NFRs               → Architect → /speckit.plan
Features                     → spec.md context
Constraints                  → constitution.md
```

---

## ✅ Checkliste vor Handoff

### An Architect

```
- [ ] Alle Features haben Success Criteria (tech-agnostic)
- [ ] Alle Features haben Technical NFRs (quantifiziert)
- [ ] Alle ASRs identifiziert (🔴/🟡)
- [ ] architect-handoff.md erstellt
- [ ] Open Questions dokumentiert
```

### Für Spec Kit

```
- [ ] specify-context.md erstellt
- [ ] KEINE Tech-Begriffe in Success Criteria
- [ ] Prompt für /speckit.specify copy-paste ready
- [ ] Source Documents referenziert
- [ ] Pre-Specify Checklist durchgeführt
```

---

**Version:** 2.0 (mit Spec Kit Integration)
**Focus:** Tech-agnostische Success Criteria + NFR-Trennung
**Quality Gate:** Spec Kit Ready Validation