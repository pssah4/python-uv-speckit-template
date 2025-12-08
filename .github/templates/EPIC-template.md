# Epic: {Name}

> **Epic ID**: EPIC-{XXX}
> **Business Alignment**: docs/business-analysis.md
> **Scope**: [PoC / MVP]
> **Spec Kit Integration**: [Ja / Nein]
> **Status**: [Draft / In Review / Approved]

---

## Epic Hypothesis Statement

> Format: SAFe Epic Hypothesis Statement

**FÜR** {Zielkunden-Segment - spezifisch, nicht "User"}
**DIE** {Bedarf/Problem haben - klar beschrieben}
**IST DAS** {Produkt/Lösung - Lösung benannt}
**EIN** {Produktkategorie - kategorisiert}
**DAS** {Hauptnutzen bietet - quantifiziert}
**IM GEGENSATZ ZU** {Alternative - Wettbewerb genannt}
**UNSERE LÖSUNG** {primäre Differenzierung - USP klar}

---

## Business Outcomes (messbar)

> Alle Outcomes MÜSSEN Baseline, Target und Timeframe haben!

| Outcome | Baseline (aktuell) | Target (Ziel) | Timeframe |
|---------|-------------------|---------------|-----------|
| {Outcome 1} | {Wert} | {Wert} (+X%) | {Monate} |
| {Outcome 2} | {Wert} | {Wert} (-X%) | {Monate} |
| {Outcome 3} | {Wert} | {Wert} | {Monate} |

**Beispiele:**
- Conversion Rate: 12% → 18% (+50%) innerhalb 6 Monate
- Support-Tickets: 200/Woche → 120/Woche (-40%) innerhalb 3 Monate
- Time-to-Market: 8 Wochen → 4 Wochen (-50%) innerhalb 6 Monate

---

## Leading Indicators (Frühindikatoren)

> Frühindikatoren zeigen ob wir auf dem richtigen Weg sind

| Indicator | Measurement | Target | Check Frequency |
|-----------|-------------|--------|-----------------|
| {Indikator 1} | {Wie messen} | {Zielwert} | [Weekly/Biweekly] |
| {Indikator 2} | {Wie messen} | {Zielwert} | [Weekly/Biweekly] |

---

## MVP Features

| Feature ID | Name | Priority | Effort | Status |
|------------|------|----------|--------|--------|
| FEATURE-001 | {Name} | P0-Critical | M | Not Started |
| FEATURE-002 | {Name} | P0-Critical | L | Not Started |
| FEATURE-003 | {Name} | P1-High | M | Not Started |
| FEATURE-004 | {Name} | P1-High | S | Not Started |
| FEATURE-005 | {Name} | P2-Medium | S | Not Started |

**Priority Legend:**
- **P0-Critical**: MVP funktioniert nicht ohne dieses Feature
- **P1-High**: Wichtig für vollständige User Experience
- **P2-Medium**: Wertsteigernd, aber nicht essentiell für Launch

**Effort Legend:**
- **S (Small)**: 1-2 Sprints
- **M (Medium)**: 3-5 Sprints
- **L (Large)**: 6+ Sprints

---

## Explizit Out-of-Scope

> Diese Features sind BEWUSST nicht Teil des MVPs

| Feature | Reason | Planned For |
|---------|--------|-------------|
| {Feature X} | {Begründung} | Phase 2 / Never |
| {Feature Y} | {Begründung} | Phase 2 / Never |
| {Feature Z} | {Begründung} | Phase 2 / Never |

---

## Dependencies

### Internal Dependencies

| Dependency | Team/System | Impact if Delayed | Mitigation |
|------------|-------------|-------------------|------------|
| {Dependency 1} | {Team} | {Impact} | {Plan B} |

### External Dependencies

| Dependency | Owner | Due Date | Risk Level |
|------------|-------|----------|------------|
| {External System/API} | {Owner} | {Date} | [High/Medium/Low] |

---

## Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| {Risk 1} | [H/M/L] | [H/M/L] | {Maßnahme} |
| {Risk 2} | [H/M/L] | [H/M/L] | {Maßnahme} |
| {Risk 3} | [H/M/L] | [H/M/L] | {Maßnahme} |

---

## Technical Debt (nur PoC!)

> Dokumentiere bewusst akzeptierte Shortcuts

| Shortcut | Description | MVP Conversion Impact | Remediation Effort |
|----------|-------------|----------------------|-------------------|
| {Shortcut 1} | {Was wird übersprungen} | {Was muss für MVP gemacht werden} | [S/M/L] |
| {Shortcut 2} | {Was wird übersprungen} | {Was muss für MVP gemacht werden} | [S/M/L] |

**Impact Summary:**
- Total Remediation Effort: {X} Sprints geschätzt
- Critical Debt Items: {Y}
- Acceptable for PoC: [Ja/Nein]

---

## Spec Kit Integration

> Nur wenn Spec Kit genutzt wird

### Documents for Spec Kit

| Phase | Document | Purpose |
|-------|----------|---------|
| Constitution | `docs/constitution-draft.md` | Input für /speckit.constitution |
| Specify | `requirements/handoff/specify-context.md` | Input für /speckit.specify |
| Plan | `requirements/handoff/plan-context.md` | Input für /speckit.plan |

### Workflow

```
1. BA: constitution-draft.md → /speckit.constitution
2. RE: specify-context.md → /speckit.specify
3. Architect: plan-context.md → /speckit.plan
4. Developer: ISSUEs oder /speckit.tasks → /speckit.implement
```

---

## Traceability

### To Business Analysis

| Section | BA Document Reference |
|---------|----------------------|
| Problem Statement | docs/business-analysis.md → Section 2 |
| Users | docs/business-analysis.md → Section 4 |
| Key Features | docs/business-analysis.md → Section 9.3 |
| Constraints | docs/business-analysis.md → Section 7.4 |

### From Epic to Features

| Feature | Epic Section |
|---------|-------------|
| FEATURE-001 | MVP Features Row 1 |
| FEATURE-002 | MVP Features Row 2 |

---

## Approval

| Role | Name | Date | Status |
|------|------|------|--------|
| Business Owner | {Name} | {Date} | [Pending/Approved] |
| Product Owner | {Name} | {Date} | [Pending/Approved] |
| Technical Lead | {Name} | {Date} | [Pending/Approved] |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {Date} | {Author} | Initial draft |
| 1.1 | {Date} | {Author} | {Changes} |

---

**Created by:** Requirements Engineer Agent
**Next Step:** Create FEATURE-*.md for each MVP Feature