---
name: Business Analyst Quality Standards
applyTo: "docs/business-analysis*.md, docs/constitution-draft.md"
description: "Qualitätsregeln für Business Analysis Dokumente und Constitution Drafts"
---

# Business Analyst - Quality Standards

Diese Instructions werden automatisch angewendet beim Arbeiten mit Business Analysis Dokumenten.

---

## 📁 Unterstützte Dateitypen

```
✅ docs/business-analysis.md
✅ docs/business-analysis-*.md
✅ docs/constitution-draft.md
```

---

## 🎯 Qualitätsziele

### Für den Requirements Engineer
Der RE muss **sofort starten** können mit:
- ✅ Klarem Problem Statement
- ✅ Identifizierten User Personas
- ✅ Priorisierten Key Features
- ✅ Dokumentierten Constraints
- ✅ Definiertem Scope (In/Out)

### Für Spec Kit Integration
Wenn Spec Kit genutzt wird:
- ✅ constitution-draft.md für `/speckit.constitution`
- ✅ Projekt-weite Prinzipien extrahiert
- ✅ Non-Negotiables identifiziert

---

## 🔍 Validierungen nach Scope

### Simple Test (Scope A)

**Minimum erforderlich:**
```
✅ Problem Statement (1-2 Sätze)
✅ User Context (wer nutzt es?)
✅ Hauptfunktionalität (was soll es tun?)
✅ Erfolgskriterien (wann ist es fertig?)
```

**Validierungs-Check:**
```markdown
CHECK für Simple Test:

1. ✅ Problem klar beschrieben?
2. ✅ User identifiziert?
3. ✅ Funktionalität definiert?
4. ✅ Definition of Done vorhanden?

Score: [X]/4 - Minimum 3/4 für RE-Ready
```

### Proof of Concept (Scope B)

**Erforderliche Sections:**
```
✅ Executive Summary
✅ Problem Statement
✅ User Analysis (mind. 1 Persona)
✅ Hypothesis (was validieren wir?)
✅ Success Criteria
✅ Scope (In/Out)
✅ Constraints
✅ Risks (technische Risiken)
✅ Akzeptable Technical Debt
```

**Validierungs-Check:**
```markdown
CHECK für PoC:

1. ✅ Hypothesis klar formuliert?
2. ✅ Technische Risiken identifiziert?
3. ✅ Erfolgskriterien messbar?
4. ✅ Out-of-Scope explizit?
5. ✅ Akzeptable Shortcuts dokumentiert?

Score: [X]/5 - Minimum 4/5 für RE-Ready
```

### Minimum Viable Product (Scope C)

**Vollständige Sections erforderlich:**
```
✅ Executive Summary
✅ Business Context (As-Is, To-Be, Gap)
✅ Stakeholder Analysis (Map + Key Stakeholders)
✅ User Analysis (2-3 Personas)
✅ Problem Analysis (Statement, Root Causes, Impact)
✅ Goals & Objectives (Business Goals, User Goals, KPIs)
✅ Scope Definition (In, Out, Assumptions, Constraints)
✅ Risk Assessment
✅ Requirements Overview (Functional, Non-Functional, Key Features)
✅ Next Steps
```

**Validierungs-Check:**
```markdown
CHECK für MVP:

1. ✅ Business Context vollständig?
2. ✅ Stakeholder Map vorhanden?
3. ✅ Mind. 2 User Personas?
4. ✅ KPIs mit Baseline + Target?
5. ✅ In-Scope vs Out-of-Scope explizit?
6. ✅ Constraints dokumentiert?
7. ✅ Risiken identifiziert?
8. ✅ Key Features priorisiert (P0/P1/P2)?

Score: [X]/8 - Minimum 7/8 für RE-Ready
```

---

## 🏛️ Constitution Draft Validierung (Spec Kit)

### Wann erforderlich?
- User hat bestätigt, dass Spec Kit genutzt wird
- ODER User fragt explizit nach constitution-draft.md

### Pflicht-Sections:

```markdown
CHECK constitution-draft.md:

1. ✅ Development Principles Section vorhanden?
   - Code Quality Standards
   - Architecture Principles
   - Technology Constraints

2. ✅ Quality Standards Section vorhanden?
   - Performance Baselines
   - Security Requirements
   - UX Standards

3. ✅ Compliance Section vorhanden?
   - Applicable Regulations
   - Data Requirements

4. ✅ Process Requirements vorhanden?
   - Review Gates
   - Documentation Standards
   - Deployment Requirements
```

### Validierung: Non-Negotiables

```markdown
⚠️ KRITISCH: Non-Negotiables müssen klar sein!

CHECK: Folgende müssen beantwortet sein:
- [ ] Test-first development: Ja/Nein
- [ ] Code review required: Ja/Nein
- [ ] Minimum code coverage: X%
- [ ] Applicable regulations: [Liste]
- [ ] Data residency: [Region/keine]

Wenn unklar → Frage User explizit!
```

### Fehlermeldung bei unvollständiger Constitution:

```
⚠️ Constitution Draft unvollständig

Datei: docs/constitution-draft.md
Problem: 2 kritische Sections fehlen

Fehlend:
  ❌ Compliance Section - KRITISCH für Spec Kit
  ❌ Process Requirements - Wird für /speckit.plan benötigt

Aktion erforderlich:
  Kläre mit User:
  1. Gibt es Compliance-Anforderungen (GDPR, HIPAA, etc.)?
  2. Welche Review Gates sind erforderlich?
```

---

## 📊 Quality Scoring

### Gesamt-Score Berechnung

```
Simple Test:  4 Checks  → RE-Ready bei ≥75% (3/4)
PoC:          5 Checks  → RE-Ready bei ≥80% (4/5)
MVP:          8 Checks  → RE-Ready bei ≥87% (7/8)

+ Spec Kit Bonus:
  Constitution Draft vollständig: +10%
  Non-Negotiables alle beantwortet: +5%
```

### Score-Meldungen

**RE-Ready:**
```
✅ Business Analysis RE-Ready!

Score: [X]% ({passed}/{total} Checks)
Scope: {Simple Test / PoC / MVP}

Vollständige Sections:
  ✅ {Section 1}
  ✅ {Section 2}
  [...]

Spec Kit Status:
  ✅ constitution-draft.md erstellt
  ✅ Non-Negotiables vollständig

→ Bereit für Übergabe an Requirements Engineer
```

**Nicht Ready:**
```
❌ Business Analysis NICHT RE-Ready

Score: [X]% ({passed}/{total} Checks)
Problem: {Anzahl} kritische Sections fehlen

Fehlend:
  ❌ {Section 1} - {Warum kritisch}
  ❌ {Section 2} - {Warum kritisch}

Aktion erforderlich:
  1. {Konkrete Aktion 1}
  2. {Konkrete Aktion 2}

→ Behebe Fehler vor Übergabe an RE
```

---

## 🚫 Anti-Patterns

### ❌ Technische Lösungen vorschreiben

```
FALSCH (BA sollte nicht):
"Wir brauchen eine React-App mit PostgreSQL-Datenbank"
"Die API sollte REST sein mit JWT-Authentication"

RICHTIG (BA sollte):
"Wir brauchen eine moderne Web-Anwendung"
"Sichere Authentifizierung ist erforderlich"
```

### ❌ Vage Problem Statements

```
FALSCH:
"Die aktuelle Lösung ist nicht gut"
"User sind unzufrieden"

RICHTIG:
"Der aktuelle Prozess dauert 5 Stunden pro Woche und erzeugt 20% Fehlerrate"
"User brechen den Checkout-Prozess in 40% der Fälle ab"
```

### ❌ Fehlende Quantifizierung

```
FALSCH (KPIs):
"Schnellere Bearbeitung"
"Weniger Fehler"

RICHTIG (KPIs):
| KPI | Baseline | Target | Timeframe |
| Bearbeitungszeit | 5h/Woche | 1h/Woche | 3 Monate |
| Fehlerrate | 20% | <5% | 6 Monate |
```

### ❌ Unklarer Scope

```
FALSCH:
"Das System sollte auch X können" (ohne In/Out-of-Scope)

RICHTIG:
In Scope:
- Feature A
- Feature B

Out of Scope:
- Feature X (geplant für Phase 2)
- Feature Y (bewusst ausgeschlossen wegen...)
```

---

## 🔄 Feedback-Loop mit User

### Wenn Informationen fehlen:

```markdown
💬 Rückfrage an User:

Mir fehlen noch folgende Informationen für ein vollständiges 
Business Analysis Dokument:

1. **User Personas:** Wer sind die primären Nutzer?
   - Rolle/Job Title?
   - Hauptziele?
   - Aktuelle Pain Points?

2. **Success Metrics:** Wie messen wir Erfolg?
   - Aktuelle Baseline?
   - Zielwerte?
   - Zeitrahmen?

Können wir diese Punkte klären?
```

### Wenn Scope unklar:

```markdown
💬 Scope-Klärung benötigt:

Du hast {Feature X} erwähnt. Ich bin unsicher ob das:

A) ✅ In Scope für dieses Projekt ist
B) ❌ Out of Scope (später/nie)
C) ❓ Nice-to-have (wenn Zeit)

Was trifft zu?
```

---

## 📋 Handoff Checkliste für RE

### Standard Handoff:

```markdown
## Handoff an Requirements Engineer

**Projekt:** {Name}
**Scope:** {Simple Test / PoC / MVP}
**BA-Dokument:** docs/business-analysis.md

### Key Information für RE:

**Problem Statement:**
{Kurze Zusammenfassung}

**Primary Users:**
- {Persona 1}: {Hauptziel}
- {Persona 2}: {Hauptziel}

**Key Features (priorisiert):**
| Priority | Feature |
| P0 | {Feature 1} |
| P1 | {Feature 2} |

**Constraints:**
- {Constraint 1}
- {Constraint 2}

**Offene Fragen:**
- {Frage 1}
- {Frage 2}

### RE Action Items:
1. [ ] EPIC erstellen (wenn PoC/MVP)
2. [ ] FEATURE-*.md für jedes Key Feature
3. [ ] Success Criteria (tech-agnostisch!) definieren
4. [ ] specify-context.md erstellen (wenn Spec Kit)
```

### Spec Kit Handoff (zusätzlich):

```markdown
## Spec Kit Integration

**Constitution Draft:** docs/constitution-draft.md
- Status: ✅ Vollständig / ⚠️ Unvollständig

**Für /speckit.constitution:**
1. Review constitution-draft.md
2. Finalisiere offene {placeholder} Items
3. Nutze als Input für /speckit.constitution

**Für RE Agent:**
- Erstelle specify-context.md nach Feature-Definition
- Achte auf tech-agnostische Success Criteria!
```

---

## ✅ Abschluss-Validierung

Vor Übergabe an RE, führe finale Validierung durch:

```markdown
## Finale BA Validierung

### Dokument-Qualität
- [ ] Alle Pflicht-Sections vorhanden (scope-spezifisch)
- [ ] Problem Statement klar und quantifiziert
- [ ] User identifiziert und beschrieben
- [ ] Scope explizit (In/Out)
- [ ] Constraints dokumentiert
- [ ] Key Features priorisiert

### Spec Kit (wenn applicable)
- [ ] constitution-draft.md erstellt
- [ ] Non-Negotiables beantwortet
- [ ] Compliance Requirements dokumentiert

### Handoff-Ready
- [ ] Summary für RE erstellt
- [ ] Offene Fragen dokumentiert
- [ ] Nächste Schritte definiert

---

**Score:** [X]%
**Status:** {RE-Ready / Nicht Ready}
```

---

**Version:** 2.0 (mit Spec Kit Integration)
**Focus:** Business Analysis + Constitution Draft
**Quality Gate:** RE-Ready Validation