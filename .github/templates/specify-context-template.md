# Specify Context Document

> **Purpose:** Aggregates Business Analysis + Requirements Engineering outputs for `/speckit.specify`
> **Created by:** Requirements Engineer Agent
> **Used by:** `/speckit.specify` command

---

## How to Use

1. **Complete BA + RE Phase** using your agents
2. **Fill this template** with extracted information
3. **Copy-paste the Prompt Section** into `/speckit.specify`
4. **Attach Source Documents** as context if needed

---

## 📋 Prompt for /speckit.specify

Copy everything between the markers below:

<!-- SPECIFY PROMPT START -->

### Feature: {FEATURE_NAME}

**Problem Statement:**
{Extract from BA: Executive Summary → Problem Statement}
{2-3 sentences describing the problem being solved}

**Target Users:**
{Extract from BA: Section 4 - User Personas}
- **Primary:** {Persona 1 name and role}
- **Secondary:** {Persona 2 name and role (if applicable)}

**Core Functionality:**
{Extract from RE: User Stories - summarize main capabilities}
1. {User Story 1 - Als [Rolle] möchte ich [Aktion] um [Nutzen]}
2. {User Story 2}
3. {User Story 3}
{Add more as needed, 3-7 stories ideal}

**Success Criteria (What "Done" Looks Like):**
{Extract from RE: Tech-agnostic Success Criteria}
- {Criterion 1 - measurable, no technology terms}
- {Criterion 2}
- {Criterion 3}
{Examples:}
- Users can complete primary task in under 3 clicks
- System handles 100 concurrent users without degradation
- 95% task completion rate in user testing

**Scope:**
- **In Scope:**
  - {Feature 1 from RE Feature list}
  - {Feature 2}
  - {Feature 3}
- **Out of Scope:**
  - {Explicitly excluded item 1}
  - {Explicitly excluded item 2}

**Key Constraints:**
{Extract from BA: Constraints section}
- {Constraint 1 - e.g., "Must integrate with existing auth system"}
- {Constraint 2 - e.g., "Budget limited to $X/month infrastructure"}
- {Constraint 3 - e.g., "Launch deadline: Q2 2025"}

**Dependencies:**
{Extract from RE: Dependencies section}
- {External system or team dependency 1}
- {External system or team dependency 2}

**Assumptions:**
{Extract from RE: Assumptions section}
- {Assumption 1}
- {Assumption 2}

<!-- SPECIFY PROMPT END -->

---

## 📎 Source Documents Reference

### From Business Analyst Agent:

| Document | Location | Key Sections to Reference |
|----------|----------|---------------------------|
| Business Analysis | `docs/business-analysis.md` | Executive Summary, Section 4 (Users), Section 9 (Features) |
| Constitution Draft | `docs/constitution-draft.md` | All (use for `/speckit.constitution`) |

### From Requirements Engineer Agent:

| Document | Location | Key Sections to Reference |
|----------|----------|---------------------------|
| Epic | `requirements/epics/EPIC-{XXX}-{slug}.md` | Hypothesis Statement, Business Outcomes |
| Features | `requirements/features/FEATURE-{XXX}-*.md` | User Stories, Success Criteria, NFRs |
| Architect Handoff | `requirements/handoff/architect-handoff.md` | ASRs, Constraints |

---

## ✅ Pre-Specify Checklist

Before using this document with `/speckit.specify`, verify:

### Content Quality
- [ ] Problem statement is clear and concise (2-3 sentences)
- [ ] User personas are specific (not just "users")
- [ ] User stories follow "Als/möchte/um" format
- [ ] Success criteria are **technology-agnostic**
- [ ] Scope boundaries are explicit

### Success Criteria Validation
- [ ] NO technology terms (OAuth, Redis, PostgreSQL, etc.)
- [ ] All criteria are measurable
- [ ] Criteria focus on user outcomes, not implementation

**❌ Bad Examples (contain tech):**
- "Response time < 200ms using Redis caching"
- "OAuth 2.0 authentication required"
- "Data stored in PostgreSQL with indexes"

**✅ Good Examples (tech-agnostic):**
- "Users experience response times under 2 seconds"
- "Secure authentication using industry-standard protocols"
- "System supports queries across 100,000+ records efficiently"

### Completeness
- [ ] All mandatory sections filled
- [ ] Source documents linked
- [ ] Assumptions documented
- [ ] Dependencies identified

---

## 🔄 Post-Specify Actions

After running `/speckit.specify`:

1. **Review generated spec.md** for accuracy
2. **Run `/speckit.clarify`** if ambiguities remain
3. **Proceed to Architect Agent** with spec.md as additional context
4. **Create plan-context.md** after architecture phase

---

## 📝 Template Variables

Replace these placeholders:

| Variable | Source | Example |
|----------|--------|---------|
| `{FEATURE_NAME}` | Epic/Feature Title | "Customer Self-Service Portal" |
| `{SCOPE}` | BA Document | "PoC" or "MVP" |
| `{XXX}` | Auto-increment | "001", "002" |
| `{slug}` | Feature name slugified | "customer-portal" |

---

## 🔗 Integration with Spec Kit

This document maps to Spec Kit's spec-template.md:

| This Template Section | → | Spec Kit spec.md Section |
|-----------------------|---|--------------------------|
| Problem Statement | → | Problem Context |
| Target Users | → | User Context |
| Core Functionality | → | User Stories |
| Success Criteria | → | Success Criteria |
| Scope In/Out | → | Scope & Boundaries |
| Constraints | → | Constraints |
| Dependencies | → | Dependencies |
| Assumptions | → | Assumptions |

---

**Version:** 1.0
**Compatible with:** Spec Kit v0.0.90+
**Last Updated:** {DATE}