# Feature: {Name}

> **Feature ID**: FEATURE-{XXX}
> **Epic**: EPIC-{XXX} - {Epic Name}
> **Priority**: [P0-Critical / P1-High / P2-Medium]
> **Effort Estimate**: [S / M / L]
> **Status**: [Draft / In Review / Approved / In Progress / Done]

---

## Feature Description

{1-2 Absätze: Was ist das Feature und warum wird es benötigt?}
{Beschreibe den Business Value und User Benefit.}

---

## Benefits Hypothesis

**Wir glauben dass** {Beschreibung des Features}
**Folgende messbare Outcomes liefert:**
- {Outcome 1 mit Metrik}
- {Outcome 2 mit Metrik}

**Wir wissen dass wir erfolgreich sind wenn:**
- {Erfolgs-Metrik 1}
- {Erfolgs-Metrik 2}

---

## User Stories

### Story 1: {Name}
**Als** {User-Rolle - spezifisch, nicht "User"}
**möchte ich** {Funktionalität - konkret und actionable}
**um** {Business-Wert} zu erreichen

**Acceptance Criteria:**
- [ ] {Testbares Kriterium 1}
- [ ] {Testbares Kriterium 2}

### Story 2: {Name}
**Als** {User-Rolle}
**möchte ich** {Funktionalität}
**um** {Business-Wert} zu erreichen

**Acceptance Criteria:**
- [ ] {Testbares Kriterium 1}
- [ ] {Testbares Kriterium 2}

### Story 3: {Name}
**Als** {User-Rolle}
**möchte ich** {Funktionalität}
**um** {Business-Wert} zu erreichen

**Acceptance Criteria:**
- [ ] {Testbares Kriterium 1}

---

## 📊 Success Criteria (Tech-Agnostic) - FÜR SPEC KIT

> ⚠️ **KRITISCH: KEINE Technologie-Begriffe in dieser Section!**
> Diese Kriterien gehen in specify-context.md für /speckit.specify
> 
> **VERBOTEN:** OAuth, JWT, REST, API, PostgreSQL, Redis, ms, HTTP, etc.
> **ERLAUBT:** User-Outcomes, Verhalten, wahrgenommene Performance

| ID | Criterion | Target | Measurement Method |
|----|-----------|--------|-------------------|
| SC-01 | {User-outcome basiertes Kriterium} | {Zielwert} | {Wie wird gemessen} |
| SC-02 | {Verhalten, nicht Implementierung} | {Zielwert} | {Wie wird gemessen} |
| SC-03 | {Performance als User-Erlebnis} | {Zielwert} | {Wie wird gemessen} |
| SC-04 | {Zuverlässigkeit aus User-Sicht} | {Zielwert} | {Wie wird gemessen} |

### Beispiele für Tech-Agnostic Success Criteria

| ✅ RICHTIG (tech-agnostisch) | ❌ FALSCH (technisch) |
|-----------------------------|----------------------|
| Users complete login in under 10 seconds | OAuth 2.0 login response < 200ms |
| System handles 100 concurrent users without degradation | Kubernetes auto-scaling at 80% CPU |
| Data queries return within user-acceptable time | PostgreSQL indexed queries < 50ms |
| User actions are authenticated securely | JWT token validation on all endpoints |
| Frequently accessed data loads instantly | Redis cache hit rate > 95% |
| System available during business hours | 99.9% uptime SLA |
| User data is protected from unauthorized access | AES-256 encryption at rest |
| Changes to data are traceable | Audit log entries for all mutations |

### Validation Checklist

- [ ] Kein Success Criterion enthält Technologie-Begriffe
- [ ] Alle Kriterien sind aus User-Perspektive formuliert
- [ ] Alle Kriterien sind messbar
- [ ] Alle Kriterien sind verständlich für Business Stakeholder

---

## 🔧 Technical NFRs (für Architekt) - TECHNOLOGIE ERLAUBT

> Diese Section DARF und SOLL technische Details enthalten!
> Diese Kriterien gehen in architect-handoff.md für Architect Agent
> Der Architekt nutzt diese für ADR-Erstellung und arc42

### Performance

| Requirement | Target | Measurement | Notes |
|-------------|--------|-------------|-------|
| Response Time | < {X} ms für {Y}% der Requests | APM/Monitoring | {Kontext} |
| Throughput | {X} req/sec sustained | Load Test | {Peak: Y req/sec} |
| Resource Usage | Max {X} CPU, {Y} MB RAM | Container Metrics | {Per Instance} |
| Database Query Time | < {X} ms für {Y}% | Query Analyzer | {Für komplexe Queries} |

### Security

| Requirement | Specification | Standard/Protocol | Notes |
|-------------|--------------|-------------------|-------|
| Authentication | {Methode} | OAuth 2.0 / JWT / Session | {Provider: X} |
| Authorization | {Model} | RBAC / ABAC | {Rollen: X, Y, Z} |
| Data Encryption - Transit | {Methode} | TLS 1.3 | {Certificate: X} |
| Data Encryption - Rest | {Methode} | AES-256 | {Key Management: X} |
| Compliance | {Standard} | GDPR Art. {X} / SOC2 / HIPAA | {Specific Requirements} |

### Scalability

| Requirement | Target | Strategy | Notes |
|-------------|--------|----------|-------|
| Concurrent Users | {X} users | {Horizontal/Vertical} | {Peak: Y} |
| Data Volume | {X} GB/TB | {Partitioning/Sharding} | {Growth: Y/month} |
| Growth Rate | {X}% pro Jahr | {Auto-scaling} | {Trigger: Y} |

### Availability

| Requirement | Target | Strategy | Notes |
|-------------|--------|----------|-------|
| Uptime | {X}% ({Y}h Downtime/Jahr) | {HA Strategy} | {Maintenance Windows} |
| RTO (Recovery Time) | {X} Minuten | {Backup Strategy} | {Failover: X} |
| RPO (Recovery Point) | {X} Minuten | {Replication} | {Backup Frequency} |

### Maintainability

| Requirement | Target | Standard | Notes |
|-------------|--------|----------|-------|
| Code Coverage | > {X}% | {Testing Framework} | {Critical Paths: Y%} |
| Documentation | {Standard} | OpenAPI / AsyncAPI | {Auto-generated: Y/N} |
| Logging | {Level} | Structured JSON | {Retention: X days} |
| Monitoring | {Metrics} | Prometheus / CloudWatch | {Alerts: X} |

---

## 🏛️ Architecture Considerations

### Architecturally Significant Requirements (ASRs)

> ASRs sind NFRs die fundamentale Architektur-Entscheidungen beeinflussen

🔴 **CRITICAL ASR #1**: {Beschreibung}
- **Warum ASR**: {Begründung warum architektur-relevant}
- **Impact**: {Welche Architektur-Entscheidungen werden benötigt?}
- **Quality Attribute**: [Performance / Security / Scalability / Availability / etc.]
- **Constraint**: {Technische oder Business Constraints}
- **ADR Required**: Ja

🔴 **CRITICAL ASR #2**: {Beschreibung}
- **Warum ASR**: {Begründung}
- **Impact**: {Architektur-Impact}
- **Quality Attribute**: {Attribute}
- **Constraint**: {Constraints}
- **ADR Required**: Ja

🟡 **MODERATE ASR #1**: {Beschreibung}
- **Warum ASR**: {Begründung}
- **Impact**: {Architektur-Impact}
- **Quality Attribute**: {Attribute}
- **ADR Required**: Optional

### Context & Boundaries

**Interagierende Systeme:**
| System | Direction | Protocol | Purpose |
|--------|-----------|----------|---------|
| {System A} | Inbound/Outbound/Both | REST/Events/etc. | {Purpose} |
| {System B} | Inbound/Outbound/Both | REST/Events/etc. | {Purpose} |

**Data Flow:**
```
[User] → [Frontend] → [API Gateway] → [Backend Service] → [Database]
                                    ↓
                              [External API]
```

### Constraints

| Type | Constraint | Source | Negotiable |
|------|------------|--------|------------|
| Technology | {Muss X verwenden} | {Constitution/ADR} | Nein |
| Platform | {Cloud Provider X} | {Business Decision} | Nein |
| Compliance | {GDPR/HIPAA/etc.} | {Legal} | Nein |
| Budget | {Max $X/month} | {Finance} | Teilweise |
| Timeline | {Deadline: X} | {Business} | Teilweise |

### Open Questions für Architekt

> Diese Fragen MUSS der Architekt beantworten

- ❓ {Technische Entscheidung die Architekt treffen muss}
- ❓ {Architektur-Pattern-Frage}
- ❓ {Integration-Strategie-Frage}
- ❓ {Trade-off Entscheidung}

---

## ✅ Definition of Done

### Functional Requirements
- [ ] Alle User Stories implementiert
- [ ] Alle Success Criteria erfüllt und verifiziert
- [ ] Edge Cases behandelt

### Quality Requirements
- [ ] Unit Tests geschrieben (Coverage > {X}%)
- [ ] Integration Tests bestanden
- [ ] E2E Tests bestanden (wenn applicable)
- [ ] Security Scan bestanden (keine Critical/High)
- [ ] Performance Tests bestanden (wenn ASR)

### Review Gates
- [ ] Architecture Review abgeschlossen (ADR-compliant)
- [ ] Code Review abgeschlossen (min. 1 Approval)
- [ ] Security Review abgeschlossen (wenn Security ASR)
- [ ] UAT bestanden

### Documentation
- [ ] API Dokumentation aktualisiert
- [ ] README aktualisiert
- [ ] Changelog aktualisiert
- [ ] Architecture Diagrams aktualisiert (wenn Änderungen)

### Deployment
- [ ] Deployed in Staging
- [ ] Smoke Tests in Staging bestanden
- [ ] Deployed in Production
- [ ] Monitoring/Alerts konfiguriert

---

## Dependencies

### Feature Dependencies

| Feature | Dependency Type | Status | Impact if Blocked |
|---------|----------------|--------|-------------------|
| FEATURE-{XXX} | Blocks / Blocked by | {Status} | {Impact} |

### External Dependencies

| System/Team | Dependency | Due Date | Owner | Status |
|-------------|------------|----------|-------|--------|
| {System} | {Was wird benötigt} | {Date} | {Owner} | {Status} |

---

## Assumptions

> Annahmen die validiert werden müssen

| # | Assumption | Validation Method | Validated |
|---|------------|-------------------|-----------|
| 1 | {Annahme 1} | {Wie validieren} | [ ] |
| 2 | {Annahme 2} | {Wie validieren} | [ ] |

---

## Out of Scope

> Explizit NICHT Teil dieses Features

| Item | Reason | Planned For |
|------|--------|-------------|
| {Item 1} | {Warum out-of-scope} | Phase 2 / Never / {Feature Y} |
| {Item 2} | {Warum out-of-scope} | Phase 2 / Never / {Feature Y} |

---

## Spec Kit Integration Notes

> Nur relevant wenn Spec Kit genutzt wird

### Success Criteria für specify-context.md

Diese Success Criteria werden in `specify-context.md` übernommen:
- SC-01: {Copy from Tech-Agnostic section}
- SC-02: {Copy from Tech-Agnostic section}
- SC-03: {Copy from Tech-Agnostic section}

### Technical NFRs für plan-context.md

Diese NFRs werden in `plan-context.md` übernommen (nach Architect Phase):
- Performance: {Summary}
- Security: {Summary}
- Scalability: {Summary}

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {Date} | RE Agent | Initial draft |
| 1.1 | {Date} | {Author} | {Changes} |

---

**Created by:** Requirements Engineer Agent
**Ready for:** Architect Agent
**Spec Kit:** Success Criteria ready for /speckit.specify