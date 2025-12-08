# Project Constitution Draft

> **Purpose:** Input für `/speckit.constitution`
> **Created by:** Business Analyst Agent
> **Project:** {Projektname}
> **Date:** {YYYY-MM-DD}
> **Scope:** [Simple Test / PoC / MVP]

---

## 🎯 Purpose of This Document

Dieses Dokument definiert die **nicht-verhandelbaren Prinzipien** für das gesamte Projekt.
Es wird als Input für Spec Kit's `/speckit.constitution` Command verwendet.

**Wie zu verwenden:**
1. Review diesen Draft mit Stakeholdern
2. Ersetze alle {placeholders} mit konkreten Werten
3. Entferne nicht-zutreffende Sections (markiert mit [Optional])
4. Nutze als Input für `/speckit.constitution`

---

## Development Principles

### Code Quality Standards

| Principle | Value | Negotiable | Notes |
|-----------|-------|------------|-------|
| Test-first development | [Required / Recommended / Optional] | Nein | {Notes} |
| Minimum code coverage | {X}% | Nein | {Critical paths: Y%} |
| Code review required | [All PRs / Critical only / Optional] | Nein | {Min. approvers: X} |
| Linting required | [Strict / Standard / None] | Nein | {Tool: ESLint/Ruff/etc.} |
| Type checking | [Strict / Standard / None] | Ja | {Tool: TypeScript/mypy/etc.} |

### Coding Standards

| Standard | Specification | Tool |
|----------|---------------|------|
| Formatting | {Prettier / Black / etc.} | Auto-format on save |
| Naming conventions | {camelCase / snake_case / etc.} | Linter rules |
| Commit messages | {Conventional Commits / Free-form} | {Commitlint / None} |
| Branch naming | {feature/*, bugfix/*, etc.} | {Branch protection rules} |

### Documentation Standards

| Documentation | Required | Tool/Format |
|---------------|----------|-------------|
| README | Ja | Markdown |
| API Documentation | [Ja / Nein] | {OpenAPI / AsyncAPI / GraphQL Schema} |
| Architecture Docs | [Ja / Nein] | {arc42 / C4 / etc.} |
| ADRs | [Ja / Nein] | MADR Format |
| Inline Comments | [Required für komplexe Logik / Optional] | {Language standard} |

---

## Architecture Principles

### Modularity

| Principle | Value | Rationale |
|-----------|-------|-----------|
| Feature modularity | [Standalone libraries / Monolith ok / Microservices] | {Begründung} |
| Coupling | [Loose coupling required / Acceptable for PoC] | {Begründung} |
| Dependency direction | [Inward / Clean Architecture / N/A] | {Begründung} |

### Interface Requirements

| Interface | Required | Specification |
|-----------|----------|---------------|
| CLI interface | [Ja / Nein] | {Für welche Funktionen} |
| REST API | [Ja / Nein] | {OpenAPI version} |
| GraphQL API | [Ja / Nein] | {Schema-first / Code-first} |
| Event-driven | [Ja / Nein] | {Message format: CloudEvents / etc.} |

### Repository Structure

| Aspect | Decision | Notes |
|--------|----------|-------|
| Repository type | [Monorepo / Polyrepo] | {Tool: Nx / Turborepo / None} |
| Package manager | {npm / yarn / pnpm / pip / poetry} | Version: {X} |
| Workspace structure | {Beschreibung} | {Example: apps/, libs/, packages/} |

---

## Quality Standards

### Performance Baselines

> Diese sind projekt-weite MINIMUM Standards, nicht Feature-spezifisch

| Metric | Baseline | Measurement | Notes |
|--------|----------|-------------|-------|
| Response time (user-perceived) | < {X} seconds | User survey / RUM | {Kontext} |
| Page load time | < {X} seconds | Lighthouse | {First Contentful Paint} |
| API response time | < {X} ms | APM | {95th percentile} |
| Build time | < {X} minutes | CI/CD metrics | {Full build} |

### Availability Targets

| Environment | Uptime | Maintenance Window | Notes |
|-------------|--------|-------------------|-------|
| Production | {X}% | {Wann erlaubt} | {SLA: X} |
| Staging | {X}% | {Flexible} | {Testing environment} |

### Error Budget

| Metric | Budget | Measurement Period |
|--------|--------|-------------------|
| Allowed downtime | {X} hours/month | Rolling 30 days |
| Error rate | < {X}% | Rolling 7 days |

---

## Security & Compliance

### Authentication & Authorization

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| Authentication standard | [OAuth 2.0 / OIDC / SAML / Session / None] | {Provider: X} |
| Authorization model | [RBAC / ABAC / None] | {Roles: X, Y, Z} |
| MFA required | [Ja / Nein / Optional] | {For: Admins / All users} |
| Session management | {Beschreibung} | {Timeout: X minutes} |

### Data Protection

| Requirement | Specification | Standard |
|-------------|---------------|----------|
| Encryption in transit | [Required / Optional] | TLS {version} |
| Encryption at rest | [Required / Optional] | {AES-256 / etc.} |
| PII handling | {Beschreibung} | {Anonymization / Pseudonymization} |
| Data retention | {X} days/months/years | {Automatic deletion: Ja/Nein} |
| Audit logging | [Required / Optional] | {Retention: X years} |

### Compliance Requirements

| Regulation | Applicable | Key Requirements | Notes |
|------------|------------|------------------|-------|
| GDPR | [Ja / Nein] | {Specific articles} | {EU users: Ja/Nein} |
| CCPA | [Ja / Nein] | {Specific requirements} | {CA users: Ja/Nein} |
| HIPAA | [Ja / Nein] | {Specific requirements} | {Healthcare data: Ja/Nein} |
| PCI-DSS | [Ja / Nein] | Level {1-4} | {Payment processing: Ja/Nein} |
| SOC 2 | [Ja / Nein] | Type {I/II} | {Enterprise customers: Ja/Nein} |

### Data Residency

| Requirement | Specification |
|-------------|---------------|
| Data must stay in | {Region/Country / No restriction} |
| Backup location | {Same region / Different region} |
| Processing location | {Same region / Anywhere} |

---

## Process Requirements

### Review Gates

| Gate | Required | Approvers | Criteria |
|------|----------|-----------|----------|
| Architecture review | [Ja / Nein] | {Role} | {Wann: New ADR / Major change} |
| Security review | [Ja / Nein] | {Role} | {Wann: Auth changes / Data handling} |
| Performance review | [Ja / Nein] | {Role} | {Wann: New endpoints / DB changes} |
| Code review | [Ja / Nein] | {Min. X approvers} | {All PRs / Critical only} |
| UAT | [Ja / Nein] | {Role} | {Before Production} |

### CI/CD Requirements

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| CI pipeline | [Required / Optional] | {Tool: GitHub Actions / etc.} |
| Automated tests in CI | [Required / Optional] | {Blocking: Ja/Nein} |
| Security scanning | [Required / Optional] | {Tool: Snyk / Trivy / etc.} |
| Automated deployment | [Required / Optional] | {Environments: Staging / Prod} |
| Rollback capability | [Required / Optional] | {Strategy: Blue-green / Canary} |

### Environment Strategy

| Environment | Purpose | Deployment | Access |
|-------------|---------|------------|--------|
| Development | Local development | Manual | Developers |
| Staging | Integration testing | Automatic on PR merge | Team |
| Production | Live system | Manual approval | Limited |

---

## Technology Constraints

### Required Technologies

> Diese Technologien MÜSSEN verwendet werden

| Category | Technology | Version | Rationale |
|----------|------------|---------|-----------|
| Language | {z.B. Python} | {z.B. 3.11+} | {Team expertise / Standard} |
| Framework | {z.B. FastAPI} | {z.B. 0.100+} | {Performance / Features} |
| Database | {z.B. PostgreSQL} | {z.B. 15+} | {ACID / Features} |
| Cloud | {z.B. Azure} | N/A | {Enterprise agreement} |

### Forbidden Technologies

> Diese Technologien dürfen NICHT verwendet werden

| Technology | Reason | Alternative |
|------------|--------|-------------|
| {Technology 1} | {Reason: Security / License / etc.} | {Alternative} |
| {Technology 2} | {Reason} | {Alternative} |

### Preferred Technologies

> Diese Technologien werden EMPFOHLEN (nicht verpflichtend)

| Category | Technology | Rationale |
|----------|------------|-----------|
| State Management | {z.B. Zustand} | {Simple, performant} |
| Testing | {z.B. pytest} | {Team familiarity} |
| Logging | {z.B. structlog} | {JSON structured logs} |

---

## Team & Communication [Optional]

### Team Structure

| Role | Count | Responsibilities |
|------|-------|-----------------|
| Tech Lead | {X} | Architecture decisions, code review |
| Developer | {X} | Implementation, testing |
| QA | {X} | Testing, quality assurance |
| DevOps | {X} | CI/CD, infrastructure |

### Communication

| Channel | Purpose | Tool |
|---------|---------|------|
| Daily updates | Sync | {Slack / Teams / etc.} |
| Design discussions | Async | {GitHub Discussions / etc.} |
| Documentation | Async | {Confluence / Notion / GitHub} |

---

## Usage Instructions

### For /speckit.constitution

1. **Review** diesen Draft
2. **Ersetze** alle {placeholder} Werte
3. **Entferne** nicht-zutreffende Sections
4. **Kopiere** relevante Sections in `/speckit.constitution`:

```
/speckit.constitution

Create project constitution with these principles:

Development:
- Test-first: {Required/Optional}
- Coverage: {X}%
- Code review: {All PRs/Critical only}
- Linting: {Strict/Standard}

Architecture:
- Modularity: {Standalone libraries/Monolith}
- API-first: {REST/GraphQL/None}
- Repository: {Monorepo/Polyrepo}

Quality:
- Response time: < {X} seconds
- Uptime: {X}%
- Build time: < {X} minutes

Security:
- Authentication: {OAuth 2.0/OIDC/Session}
- Encryption: {Required/Optional}
- Compliance: {GDPR/HIPAA/PCI-DSS/None}

Process:
- Architecture review: {Required/Optional}
- Security review: {Required/Optional}
- CI/CD: {Required/Optional}

Technology:
- Required: {Language}, {Framework}, {Database}
- Forbidden: {List}
```

### Validation Checklist

- [ ] Alle {placeholder} ersetzt
- [ ] Stakeholder haben reviewed
- [ ] Keine widersprüchlichen Anforderungen
- [ ] Compliance Requirements vollständig
- [ ] Technology Constraints realistisch

---

## References

| Document | Location | Purpose |
|----------|----------|---------|
| Business Analysis | docs/business-analysis.md | Source of requirements |
| Stakeholder Input | {Meeting notes / Confluence} | Approval documentation |
| Industry Standards | {Links} | Compliance reference |

---

## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {Date} | BA Agent | Initial draft from interview |
| 1.1 | {Date} | {Stakeholder} | {Review comments addressed} |

---

**Created by:** Business Analyst Agent
**Next Step:** Review → Finalize → /speckit.constitution