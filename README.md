# Refinement Agents with GitHub Spec Kit Integration

> **AI-Powered Software Development Workflow** - From idea to production-ready code through structured, quality-gated phases.

A comprehensive system of specialized AI agents that guide software development from initial business concept through requirements engineering, architecture design, implementation, and debugging. Built for GitHub Copilot with automated quality gates and validation.

---

## 🎯 What This Is

**Digital Innovation Agents** transforms how software is built by providing a structured, agent-based workflow that ensures quality at every stage. Instead of jumping straight into code, projects follow a systematic path:

```
Business Idea → Requirements → Architecture → GithHub Spec Kit
     ↓              ↓              ↓              
   BA Agent    RE Agent    Architect Agent  
```

Each agent specializes in one phase, has built-in quality checks, and produces standardized outputs that feed into the next phase.
```
┌─────────────────────────────────────────────────────────────────────┐
│                     INTEGRATED WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PHASE 1: Discovery                                                 │
│  ═══════════════════════════════════                                │
│                                                                     │
│    👔 BA Agent Interview                                            │
│         ↓                                                           │
│    📄 business-analysis.md                                          │
│    📄 constitution-draft.md  ←── for Spec Kit)                      │
│         ↓                                                           │
│    📋 RE Agent                                                      │
│         ↓                                                           │
│    📄 EPIC-*.md (PoC/MVP)                                           │
│    📄 FEATURE-*.md + Success Criteria (tech-agnostic)               │
│    📄 specify-context.md  ←── Handoff Template                      │
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
│  PHASE 3: Architecture                                              │
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
│    OPTION B: Own created ISSUEs (recommended)                       │
│         Skip /speckit.tasks                                         │
│         Developer Agent arbeitet ISSUE-*.md ab                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 The Five Three Refinement Agents

### 1. **Business Analyst** (`@business-analyst`)
**Role:** Transform raw ideas into structured business requirements

**When to use:**
- Starting a new project from scratch
- Have a problem but unclear on the solution
- Need to explore requirements systematically

**Input:** Raw project idea or problem description  
**Output:** `docs/business-analysis/BA-[PROJECT].md`

**Key Features:**
- Scope detection (Simple Test / PoC / MVP)
- Structured interviews (5-50 questions based on scope)
- Jobs-to-be-Done analysis
- Value proposition development
- Success metrics definition

---

### 2. **Requirements Engineer** (`@requirements-engineer`)
**Role:** Convert business analysis into architect-ready requirements

**When to use:**
- Have a business analysis document
- Need structured epics and features
- Ready to define technical requirements

**Input:** Business Analysis document OR direct user input -> select mode und just type "continue"  
**Output:**
- `requirements/epics/EPIC-*.md`
- `requirements/features/FEATURE-*.md`
- `requirements/handoff/architect-handoff.md`

**Key Features:**
- Epic creation with hypothesis statements
- Feature breakdown with acceptance criteria
- NFR quantification (Performance, Security, Scalability)
- **ASR identification** (Architecture-Significant Requirements)
- Comprehensive architect handoff package

**Quality Gate 1 (QG1):**
- ✅ All NFRs quantified (with numbers!)
- ✅ All ASRs identified and marked (🔴/🟡)
- ✅ Acceptance criteria testable
- ✅ Architect handoff complete

---

### 3. **Architect** (`@architect`)
**Role:** Design technical architecture and create developer-ready issues

**When to use:**
- Requirements are complete (QG1 passed)
- Need architectural decisions documented
- Ready to plan implementation

**Input:** `requirements/handoff/architect-handoff.md`  
**Output:**
- `docs/decisions/ADR-*.md` (Architecture Decision Records in MADR format)
- `docs/arc42/ARC42-DOCUMENTATION.md` (arc42 architecture docs)
- `backlog/ISSUE-*.md` (Developer-ready issues)
- `backlog/Backlog.md` (Single source of truth for work breakdown)

**Key Features:**
- Adaptive complexity (Simple Test / PoC / MVP)
- ADR creation with research (web_search + @azure)
- arc42 documentation (sections 1-7 for MVP)
- Atomic issue creation (1-3 days each)
- System design with Mermaid diagrams

**Quality Gate 2 (QG2):**
- ✅ ADRs for all major decisions (MADR format, 3+ options)
- ✅ arc42 complete for scope
- ✅ Atomic issues created (clear single responsibility)
- ✅ Backlog.md created (work overview)
- ✅ Developer handoff complete

---

## 🚀 Getting Started

### Prerequisites

- **GitHub Copilot** with Chat enabled
- **Docker** installed
- Understanding of your project scope (Simple Test / PoC / MVP)

## 🔧 Configuration

This Template is provided as Docker Devcontainer.

1. **„Use this template“** → create new Repo erstellen (e.g. `my-spec-project`)
3. local: 
```bash
git clone https://github.com/<your-user>/my-spec-project.git 
cd my-spec-project 
code .
```    
4. In VS Code: „Reopen in Container“
5. Ignore the Spec Kit Setup, you are already setu up and ready to start.

For use of Spec Kit please review official Spec Kit documentation: https://github.com/github/spec-kit/blob/main/README.md

### Quick Start

**Option 1: Starting from Scratch (No Requirements)**

```
Step 1: Use @business-analyst
→ Conducts structured discovery interview
→ Creates business analysis document

Step 2: Use @requirements-engineer  
→ Reads BA document
→ Creates epics, features, architect handoff

Step 3: Use @architect
→ Creates ADRs, arc42 docs, issues
→ Prepares backlog

Step 4: Use @developer
→ Implements issues with mandatory tests

Step 5: Use @debugger (if tests fail)
→ Fixes issues systematically
```

**Option 2: Starting with Requirements**

```
Skip @business-analyst

Step 1: Use @requirements-engineer directly
→ Conducts scope-specific intake
→ Creates epics, features, handoff

[Continue with Steps 3-5 above]
```

**Option 3: Starting with Architecture**

```
Skip @business-analyst and @requirements-engineer

Step 1: Use @architect with your requirements
→ Creates architecture artifacts

[Continue with Steps 4-5 above]
```

---
---

## 🎯 Key Principles

### 1. **Adaptive Complexity**
Architecture depth matches project scope:
- **Simple Test:** Minimal (hours-days)
- **PoC:** Focused (1-4 weeks)
- **MVP:** Comprehensive (2-6 months)

### 2. **Quality Gates**
No phase proceeds until quality criteria met:
- **QG1:** Requirements ready for architecture
- **QG2:** Architecture ready for development
- **QG3:** Code ready for production
- **QGD:** Bugs fixed without regressions

### 3. **Test-First Development**
- Write tests AS you code (not after)
- Execute ALL tests (not just affected)
- 100% pass rate OR error log created
- Coverage ≥90% maintained

### 4. **Clean Separation**
- **BA:** WHAT problem (business view)
- **RE:** WHAT to build (requirements view)
- **Architect:** HOW to structure (architectural view)
- **Developer:** HOW to implement (code view)
- **Debugger:** WHY it failed (root cause view)

### 5. **Atomic Work Units**
- Issues are small (1-3 days max)
- Single responsibility per issue
- Clear acceptance criteria
- Independent and testable

---

## 📊 Quality Standards

### Requirements Engineering
- ✅ All NFRs quantified (no vague "fast" or "secure")
- ✅ All ASRs identified and marked (🔴 Critical / 🟡 Moderate)
- ✅ Acceptance criteria testable (pass/fail)
- ✅ Traceability to business goals

### Architecture
- ✅ ADRs in MADR format (3+ options, pros/cons, research links)
- ✅ arc42 complete for scope (Simple Test: skip, PoC: 1,3,4, MVP: 1-7)
- ✅ Issues atomic (1-3 days each)
- ✅ Backlog.md as single source of truth

---


## 🎓 Best Practices

### When to Use Which Agent

**Use @business-analyst when:**
- ❓ Starting with a vague idea
- 🆕 New project from scratch
- 🤔 Need to explore problem space

**Use @requirements-engineer when:**
- 📄 Have business analysis document
- ✍️ Have clear requirements but need structure
- 🎯 Want to skip discovery and jump to features

**Use @architect when:**
- 🏗️ Requirements complete (QG1 passed)
- 📋 Need technical design decisions
- 🔧 Ready to plan implementation

**Use @developer when:**
- 💻 Architecture complete (QG2 passed)
- 📝 Have developer-ready issues
- 🧪 Ready to implement with tests

**Use @debugger when:**
- 🐛 Tests failing
- 📋 Have error log from Developer
- 🔍 Need systematic root cause analysis

### Common Pitfalls to Avoid

❌ **DON'T:**
- Skip quality gates (they catch problems early!)
- Write code without tests
- Use vague NFRs ("fast", "secure")
- Create oversized issues (>3 days)
- Commit with failing tests

✅ **DO:**
- Follow the workflow sequentially
- Let each agent do its job
- Quantify all NFRs with numbers
- Keep issues atomic (1-3 days)
- Run ALL tests before commit

---

## 🤝 Contributing

This is an evolving system. Contributions welcome for:
- New agent types
- Improved validation rules
- Additional templates
- Documentation improvements
- Bug fixes

---

## 📄 License

MIT License

Copyright (c) 2025 Sebastian Hanke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---


