---
name: Architect Quality Standards
applyTo: "architecture/adr/**/*.md, docs/ARC42-DOCUMENTATION.md, requirements/handoff/plan-context.md"
description: "Qualitätsregeln für Architecture Decision Records, arc42 und SpecKit Integration"
---

# Architect - Quality Standards

Diese Instructions werden automatisch angewendet beim Arbeiten mit ADRs und arc42 Dokumentation.

> **Ziel:** Vollständige Architektur-Dokumentation die /speckit.plan optimal bedienen kann.

---

## 📁 Unterstützte Dateitypen

```
✅ architecture/adr/ADR-*.md
✅ docs/ARC42-DOCUMENTATION.md
✅ requirements/handoff/plan-context.md
✅ requirements/handoff/speckit-handoff.md
```

---

## 🎯 Qualitätsziele

### Für Spec Kit Integration
- ✅ plan-context.md enthält alle technischen Constraints für /speckit.plan
- ✅ ADRs erklären WARUM Entscheidungen getroffen wurden (Kontext für SpecKit)
- ✅ arc42 Section 8 liefert das Data Model für data-model.md
- ✅ Tech Stack ist so präzise, dass SpecKit keine Annahmen treffen muss

---

## 🔍 ADR Validierung

### Dateinamen-Konvention

```javascript
const pattern = /^ADR-\d{3}-[a-z0-9-]+\.md$/;

// Gültig:
✅ ADR-001-backend-framework-selection.md
✅ ADR-002-database-choice.md
✅ ADR-015-authentication-strategy.md

// Ungültig:
❌ adr-001.md (lowercase prefix)
❌ ADR-1-framework.md (nicht 3-stellig)
❌ ADR-001-Backend Framework.md (Leerzeichen)
```

### Pflicht-Sections für ADRs

```markdown
CHECK beim Speichern:

1. ✅ Header vollständig?
   - Status: [Proposed/Accepted/Deprecated/Superseded]
   - Date: YYYY-MM-DD
   - Deciders: Mindestens 1

2. ✅ Context Section?
   - Problem beschrieben
   - Triggering ASR referenziert (wenn vorhanden)
   - Quality Attribute genannt

3. ✅ Decision Drivers?
   - Mindestens 2 Drivers

4. ✅ Considered Options?
   - Mindestens 2 Optionen
   - Jede Option hat Pros und Cons

5. ✅ Decision?
   - Gewählte Option benannt
   - Begründung vorhanden

6. ✅ Consequences?
   - Positive Konsequenzen
   - Negative Konsequenzen/Trade-offs
   - Risks (wenn vorhanden)

7. ✅ Implementation Notes? (optional aber empfohlen)
```

### ADR-ASR Traceability

```markdown
CHECK: Hat jedes Critical ASR ein ADR?

Aus Features:
🔴 ASR: Response Time < 200ms → ADR-003: Caching Strategy ✅
🔴 ASR: 10,000 concurrent users → ADR-005: Scaling Architecture ✅
🔴 ASR: GDPR Compliance → ADR-007: Data Architecture ✅
🟡 ASR: Audit Logging → (kein ADR - ok für Moderate)

Fehlermeldung wenn Critical ASR ohne ADR:
❌ Critical ASR ohne ADR gefunden!

ASR: "Response Time < 200ms for 95th percentile"
Source: FEATURE-001-user-dashboard.md
Quality Attribute: Performance

Aktion erforderlich:
  Erstelle ADR für dieses ASR:
  → architecture/adr/ADR-{XXX}-performance-optimization.md
```

---

## 🔍 arc42 Validierung nach Scope

### Simple Test (Minimal)

```markdown
PFLICHT-SECTIONS:
✅ Section 1: Introduction and Goals (1.1, 1.2)
✅ Section 3: Context and Scope (3.1 Business Context)
✅ Section 4: Solution Strategy (Technology Decisions)

OPTIONAL:
○ Section 5: Building Block View
○ Section 8: Crosscutting Concepts
```

### Proof of Concept (Moderate)

```markdown
PFLICHT-SECTIONS:
✅ Section 1: Introduction and Goals (vollständig)
✅ Section 3: Context and Scope (3.1 + 3.2)
✅ Section 4: Solution Strategy (vollständig)
✅ Section 5: Building Block View (Level 1)
✅ Section 8: Crosscutting Concepts (8.1 Domain Model)

OPTIONAL:
○ Section 6: Runtime View
○ Section 7: Deployment View
○ Section 9: Architecture Decisions (Tabelle)
○ Section 11: Risks
```

### MVP (Vollständig)

```markdown
PFLICHT-SECTIONS:
✅ Section 1: Introduction and Goals (vollständig)
✅ Section 2: Constraints (falls vorhanden)
✅ Section 3: Context and Scope (vollständig)
✅ Section 4: Solution Strategy (vollständig)
✅ Section 5: Building Block View (Level 1 + 2)
✅ Section 6: Runtime View (kritische Szenarien)
✅ Section 7: Deployment View
✅ Section 8: Crosscutting Concepts (vollständig)
✅ Section 9: Architecture Decisions (ADR Tabelle)
✅ Section 10: Quality Requirements
✅ Section 11: Risks and Technical Debt
✅ Section 12: Glossary
```

### Fehlermeldung bei fehlenden Sections

```
❌ arc42 Documentation unvollständig für MVP Scope

Datei: docs/ARC42-DOCUMENTATION.md
Scope: MVP
Problem: 3 Pflicht-Sections fehlen

Vorhanden:
  ✅ Section 1: Introduction and Goals
  ✅ Section 3: Context and Scope
  ✅ Section 4: Solution Strategy
  ✅ Section 5: Building Block View
  ❌ Section 6: Runtime View - FEHLT
  ❌ Section 7: Deployment View - FEHLT
  ✅ Section 8: Crosscutting Concepts
  ❌ Section 10: Quality Requirements - FEHLT

Aktion erforderlich:
  1. Erstelle Section 6 mit kritischen Runtime-Szenarien
  2. Erstelle Section 7 mit Deployment Diagram
  3. Erstelle Section 10 mit Quality Scenarios
```

---

## 🔍 plan-context.md Validierung

### Pflicht-Sections

```markdown
CHECK requirements/handoff/plan-context.md:

1. ✅ Technical Stack Section?
   - Backend (Language, Framework, Database, ORM)
   - Frontend (wenn applicable)
   - Infrastructure (Cloud, Deployment, CI/CD)
   - API & Integration

2. ✅ Architecture Style?
   - Pattern genannt
   - Quality Goals (Top 3)

3. ✅ Key Architecture Decisions?
   - Mindestens 3 ADRs zusammengefasst
   - Jeder mit Rationale

4. ✅ Data Model?
   - Core Entities
   - Relationships

5. ✅ External Integrations?
   - System, Type, Protocol, Purpose

6. ✅ Performance & Security?
   - Mit konkreten Zahlen
   - Technische Details erlaubt
```

### ADR Summary Tabelle

```markdown
CHECK: ADR Summary vorhanden?

| ADR | Title | Status | Impact |
|-----|-------|--------|--------|
| ADR-001 | Backend Framework | Accepted | High |
| ADR-002 | Database Choice | Accepted | High |
| ADR-003 | Auth Strategy | Accepted | High |

Mindestens 3 ADRs müssen gelistet sein!
```

### Consistency Check

```markdown
CHECK: plan-context.md konsistent mit ADRs?

Vergleiche:
- Tech Stack in plan-context.md
- Decisions in ADR-*.md

Inkonsistenz gefunden:
⚠️ plan-context.md inkonsistent mit ADRs!

plan-context.md sagt: "Database: MySQL"
ADR-002 sagt: "Decision: PostgreSQL"

Aktion: Korrigiere plan-context.md oder update ADR-002
```

---

## 🔍 Spec Kit Compatibility Check

### plan-context.md ist Ready wenn:

```
✅ Alle Pflicht-Sections vorhanden
✅ Tech Stack vollständig (Backend, Frontend, Infrastructure)
✅ Mindestens 3 ADRs in Summary
✅ Data Model definiert
✅ Performance & Security mit Zahlen
✅ Prompt für /speckit.plan copy-paste ready
```

### ADRs sind Ready für Spec Kit wenn:

```
✅ Alle Critical ASRs haben ADRs
✅ ADRs haben vollständige Rationale
✅ ADRs referenzieren Quality Attributes
✅ ADRs können als Kontext für /speckit.plan dienen
```

### Erfolgs-Meldung

```
✅ SPEC KIT PLAN READY!

Documents:
  ✅ plan-context.md vollständig
  ✅ 5 ADRs verfügbar als Kontext
  ✅ arc42 Sections 4, 5, 8 vollständig

Nächste Schritte:
  1. Copy prompt aus plan-context.md
  2. Attach ADRs + arc42 als Kontext
  3. Run /speckit.plan
  4. Review: plan.md, research.md, data-model.md
```

---

## 📊 Quality Scoring

### ADR Quality Score

```
| Kriterium | Gewichtung |
|-----------|------------|
| Vollständige Sections | 30% |
| ASR Reference | 20% |
| Multiple Options considered | 20% |
| Clear Rationale | 20% |
| Implementation Notes | 10% |

Minimum für Approval: 70%
```

---

## 🚫 Anti-Patterns

### ❌ ADR ohne Alternativen

```
FALSCH:
## Considered Options
We chose React because it's popular.

RICHTIG:
## Considered Options

### Option 1: React
- ✅ Large ecosystem
- ✅ Team experience
- ❌ Heavy bundle size

### Option 2: Vue
- ✅ Smaller bundle
- ✅ Easy learning curve
- ❌ Less team experience

### Option 3: Svelte
- ✅ Smallest bundle
- ❌ Newer, less mature ecosystem
- ❌ No team experience
```

### ❌ plan-context.md ohne konkrete Werte

```
FALSCH:
### Performance & Security
- Fast response times
- Secure authentication
- Good scalability

RICHTIG:
### Performance & Security
- Response Time: < 200ms for 95th percentile
- Authentication: OAuth 2.0 via Azure AD B2C
- Scalability: 1,000 concurrent, auto-scale to 10,000
```

---

## ✅ Checkliste vor Handoff

### Für Spec Kit

```
- [ ] plan-context.md erstellt
- [ ] Tech Stack vollständig dokumentiert
- [ ] ADR Summary Table vorhanden
- [ ] Data Model definiert
- [ ] Performance/Security mit konkreten Zahlen
- [ ] Prompt für /speckit.plan ready
- [ ] speckit-handoff.md erstellt
```

---

**Version:** 2.1 (Spec Kit Optimized)
**Focus:** ADR Quality + plan-context.md
**Quality Gate:** Spec Kit Readiness
