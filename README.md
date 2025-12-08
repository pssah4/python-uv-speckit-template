# Spec Kit Integration - Implementation Guide

## 📋 Kurze Antwort auf deine Frage

**Ja, du musst einige Anpassungen machen, aber sie sind minimal :**

| Was | Warum | Aufwand |
|-----|-------|---------|
| **BA Agent:** Constitution Draft Section | Spec Kit braucht constitution.md | ~30 min |
| **RE Agent:** Tech-agnostische Success Criteria | /speckit.specify erwartet KEINE Tech-Begriffe | ~45 min |
| **Architect:** Tech Stack Summary | /speckit.plan braucht strukturierten Input | ~30 min |
| **Neue Templates:** specify-context.md, plan-context.md | Strukturierte Handoffs | ~15 min |

**Gesamtaufwand: ~2 Stunden**

---

## 🎯 Der integrierte Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     INTEGRIERTER WORKFLOW                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PHASE 1: Discovery (Deine Agents)                                  │
│  ═══════════════════════════════════                                │
│                                                                     │
│    👔 BA Agent Interview                                            │
│         ↓                                                           │
│    📄 business-analysis.md                                          │
│    📄 constitution-draft.md  ←── NEU (für Spec Kit)                 │
│         ↓                                                           │
│    📋 RE Agent                                                      │
│         ↓                                                           │
│    📄 EPIC-*.md (PoC/MVP)                                           │
│    📄 FEATURE-*.md + Success Criteria (tech-agnostisch) ←── ANGEPASST│
│    📄 specify-context.md  ←── NEU (Handoff Template)                │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════════│
│                                                                     │
│  PHASE 2: Spec Kit Specify                                          │
│  ══════════════════════════                                         │
│                                                                     │
│    /speckit.constitution                                            │
│         Input: constitution-draft.md                                │
│         → constitution.md                                           │
│                                                                     │
│    /speckit.specify [specify-context.md Prompt]                     │
│         Input: specify-context.md als Prompt                        │
│         → spec.md                                                   │
│                                                                     │
│    /speckit.clarify (optional)                                      │
│         → Klärt offene Fragen                                       │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════════│
│                                                                     │
│  PHASE 3: Architecture (Dein Agent)                                 │
│  ══════════════════════════════════                                 │
│                                                                     │
│    🏗️ Architect Agent                                               │
│         Input: spec.md + FEATURE-*.md                               │
│         ↓                                                           │
│    📄 ADR-*.md                                                      │
│    📄 ARC42-DOCUMENTATION.md                                        │
│    📄 ISSUE-*.md (atomic, 1-3 days)                                 │
│    📄 plan-context.md  ←── NEU (Handoff Template)                   │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════════│
│                                                                     │
│  PHASE 4: Spec Kit Plan                                             │
│  ══════════════════════                                             │
│                                                                     │
│    /speckit.plan [plan-context.md Prompt]                           │
│         Input: ADRs + arc42 als Context                             │
│         → plan.md, research.md, data-model.md, contracts/           │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════════│
│                                                                     │
│  PHASE 5: Implementation                                            │
│  ══════════════════════                                             │
│                                                                     │
│    OPTION A: Spec Kit                                               │
│         /speckit.tasks → tasks.md                                   │
│         /speckit.implement → Code                                   │
│                                                                     │
│    OPTION B: Deine ISSUEs (EMPFOHLEN)                               │
│         Skip /speckit.tasks                                         │
│         Developer Agent arbeitet ISSUE-*.md ab                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Kritischste Anpassung: Tech-Agnostische Success Criteria

Dies ist der **wichtigste Punkt** für die Integration:

### Problem

Spec Kit's `/speckit.specify` erwartet Success Criteria **OHNE** Technologie-Begriffe.

Dein RE Agent produziert aktuell NFRs MIT Technologie:

```markdown
❌ AKTUELL (RE Output):
- Response Time: < 200ms für 95% der Requests via Redis Caching
- Authentication: OAuth 2.0 mit Azure AD
- Database: PostgreSQL mit Index auf user_id
```

### Lösung

Der RE Agent muss **zwei Arten** von Kriterien produzieren:

```markdown
✅ NEU: Success Criteria (für /speckit.specify)
- Users experience sub-second response times
- Secure authentication using industry-standard protocols  
- System efficiently handles 100,000+ records

✅ BESTEHEND: Technical NFRs (für /speckit.plan)
- Response Time: < 200ms für 95% via Redis
- Authentication: OAuth 2.0, Azure AD
- Database: PostgreSQL, indexed queries
```

### Validation Rule

```javascript
// Diese Begriffe DÜRFEN NICHT in Success Criteria erscheinen:
const forbiddenInSuccessCriteria = [
  'OAuth', 'JWT', 'REST', 'GraphQL', 'API',
  'Redis', 'PostgreSQL', 'MongoDB', 'MySQL',
  'React', 'Angular', 'Vue', 'Node.js',
  'Docker', 'Kubernetes', 'AWS', 'Azure',
  'ms', 'milliseconds', 'HTTP', 'TLS'
];
```

---

## 📁 Dateien in diesem Package

```
speckit-integration/
├── README.md                              # Diese Datei
├── QUICK-REFERENCE.md                     # ⭐ Schnellreferenz-Karte
├── speckit-integration-analysis.md        # Vollständige Analyse
├── agent-patches-speckit.md               # Übersicht der Änderungen
│
├── agents/                                # Aktualisierte Agent-Definitionen
│   ├── business-analyst.agent.md          # BA mit Constitution Draft
│   ├── requirements-engineer.agent.md     # RE mit Tech-agnostic SC
│   ├── architect.agent.md                 # Architect mit plan-context
│   └── developer.agent.md                 # Developer mit Spec Kit Integration
│
├── instructions/                          # Aktualisierte Quality Standards
│   ├── business-analyst.instructions.md   # BA Validierung + Constitution
│   ├── requirements-engineer.instructions.md # Tech-agnostic Validation
│   └── architect.instructions.md          # ADR/ISSUE/plan-context Validation
│
└── templates/                             # Alle Templates
    ├── EPIC-TEMPLATE.md                   # Epic mit Spec Kit Notes
    ├── FEATURE-TEMPLATE.md                # Feature mit Success Criteria Split
    ├── ISSUE-TEMPLATE.md                  # ISSUE mit ADR References
    ├── constitution-draft-template.md     # Input für /speckit.constitution
    ├── specify-context-template.md        # BA+RE → /speckit.specify
    ├── plan-context-template.md           # Architect → /speckit.plan
    ├── architect-handoff-template.md      # RE → Architect Handoff
    └── developer-handoff-template.md      # Architect → Developer Handoff
```

### Schnellstart

1. **Kopiere `agents/` Dateien** nach `.github/chatmodes/` oder Kilo Code modes
2. **Kopiere `instructions/` Dateien** nach `.github/instructions/`
3. **Kopiere `templates/` Dateien** nach `.github/templates/`
4. **Lies `QUICK-REFERENCE.md`** für den Workflow-Überblick
5. **Fertig!** - Workflow ist Spec Kit-ready

### Datei-Statistik

| Kategorie | Dateien | Gesamtgröße |
|-----------|---------|-------------|
| Agents | 4 | ~54 KB |
| Instructions | 3 | ~35 KB |
| Templates | 8 | ~75 KB |
| Docs | 4 | ~60 KB |
| **Total** | **19** | **~224 KB** |

---

## ✅ Implementation Checklist

### Schritt 1: Templates hinzufügen
- [ ] `specify-context-template.md` nach `.github/templates/` kopieren
- [ ] `plan-context-template.md` nach `.github/templates/` kopieren

### Schritt 2: BA Agent anpassen
- [ ] Constitution Draft Section hinzufügen (siehe agent-patches-speckit.md)
- [ ] Output-Checkliste erweitern

### Schritt 3: RE Agent anpassen
- [ ] Success Criteria Section im FEATURE-TEMPLATE hinzufügen
- [ ] specify-context.md Generation Logic hinzufügen
- [ ] Tech-Agnostic Validation in Instructions hinzufügen

### Schritt 4: Architect Agent anpassen
- [ ] plan-context.md Generation Logic hinzufügen
- [ ] Tech Stack Summary Section im Handoff Template

### Schritt 5: Testen
- [ ] BA → RE Flow mit constitution-draft.md
- [ ] RE → specify-context.md Generation
- [ ] Architect → plan-context.md Generation
- [ ] Full Integration mit Spec Kit Commands

---

## 🎁 Bonus: Deine ISSUEs sind besser als /speckit.tasks

Dein Architect Agent erstellt bereits:
- ✅ Atomic ISSUEs (1-3 Tage)
- ✅ ADR-Referenzen
- ✅ Testbare Acceptance Criteria
- ✅ Developer Guidance

Spec Kit's `/speckit.tasks` ist gut, aber deine ISSUEs sind **präziser**.

**Empfehlung:** Skip `/speckit.tasks` und nutze deine ISSUEs direkt!

---

## 🔗 Links

- [Spec Kit GitHub](https://github.com/github/spec-kit)
- [Spec Kit Documentation](https://github.github.io/spec-kit/)
- [Spec-Driven Development Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)

---

**Erstellt:** 2025-12-08
**Für:** Sebastian's Multi-Agent Workflow + Spec Kit Integration