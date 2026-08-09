# Hi, I’m Anton 👋

**Senior Data Engineer | Healthcare AI | Trustworthy Data Systems**

I design and build **reliable data and AI systems** for healthcare, research, and other high-stakes domains where trust matters.

Professionally, I’m a Senior Data Engineer with deep experience in **data ingestion, analytics infrastructure, orchestration, and platform reliability**. Independently, I’m building projects at the boundary of **healthcare data engineering, applied AI, privacy-preserving systems, and human-centered tooling**.

The common thread in my work is simple: complex systems should be understandable, reproducible, and useful to the people who depend on them.

I care about systems that:

* work reliably at scale,
* protect sensitive data,
* make uncertainty visible,
* and remain understandable to both technical and non-technical users.

Writing and notes: [antonrasmussen.com](https://antonrasmussen.com)

---

## 🧠 Current Focus

I’m currently building independent projects around:

* **Verified / goal-directed agent harnesses** for long-horizon healthcare data-engineering tasks — measuring and reducing **false completion** (claimed success that fails an independent oracle), with synthetic fixtures only
* **Measurement choices that dominate apparent LLM reliability** — prompt templates, scoring rules, calibration, and quantization effects in biomedical models
* **Privacy-preserving data engineering** and clinical / biomedical workflows
* **Edge-ready and local-first AI systems**
* **Explainable, reproducible ML and experiment harnesses**
* **Agentic tooling** for data platforms and research workflows

I’m especially interested in the practical middle ground between production engineering and applied research: turning messy data, fragile workflows, and vague questions into systems that can be tested, explained, and improved.

A long-term thread across this work is **Careful Intelligence** — my personal effort to explore trustworthy, privacy-aware AI systems that are useful in the real world, not just impressive in demos.

---

## 🛠️ Technical Stack

**Languages**
Python, SQL, Bash, Java, TypeScript, JavaScript
*(comfortable learning new languages when the system demands it)*

**Data Engineering & Orchestration**
Dagster, Apache Spark, dbt, Pandas, Hadoop ecosystem

**Cloud & Storage**
Google Cloud Platform, GCS, BigQuery, Datastore, Azure SQL, SQL Server, Teradata, Informix

**Analytics, Visualization & Geospatial**
Tableau, Vega-Lite, Matplotlib, GeoPandas, OpenRefine

**AI / ML Areas I Work Around**
LLM evaluation, model calibration, quantization, prompt stability, agent evaluation / verification gates, de-identification, NER, reproducible experiment harnesses

**Tooling & Automation**
GitHub Actions scheduled pipelines · local-first SQLite tooling · CLI-first research utilities

**Practices I Care About**
Idempotent pipelines · data validation · observability · schema evolution · reproducibility · de-identification · operational clarity · human review loops · independent verification over self-reported success

---

## 🏥 Professional Experience

### **Senior Data Engineer – Data Ingestion**

**Cityblock Health | Feb 2024 – Present**

* Design and evolve **multi-source, multi-format ingestion pipelines** for HIPAA-protected healthcare data
* Lead and support migration toward **Dagster-based orchestration**, improving reliability, extensibility, and developer velocity
* Build validation, profiling, quarantine, and review workflows that balance automation with human oversight
* Collaborate across analytics, clinical, implementation, and platform teams to make complex data systems more usable and trustworthy
* Work on operational visibility for ingestion workflows, including review paths for unknown, anomalous, or unconfigured inbound files

---

### **Data Engineer – Data Infrastructure**

**Cityblock Health | Feb 2022 – Feb 2024**

* Built robust, idempotent ETL pipelines supporting analytics, operations, and clinical workflows
* Helped improve data quality, reliability, and maintainability across shared data infrastructure
* Supported ingestion and transformation patterns for healthcare data from multiple external sources

---

### **Software Engineer III – Pharmacy Data & Analytics**

**Walmart Global Tech | Dec 2019 – Feb 2022**

* Developed large-scale analytics systems for pharmacy operations
* Worked with big-data platforms and production streaming/batch pipelines
* Built data-driven applications and dashboards supporting operational and analytical decision-making

---

## 📌 Selected Projects

### **Verified Goal-Directed Harnesses for Healthcare Data Engineering Agents**

Research prototype for measuring — and reducing — **false completion** in long-horizon agentic data-engineering work: the agent (or wrapper) reports success while an independent oracle shows the goal was not satisfied. Goals live outside the agent as machine-readable criteria; only an independent verifier can grant success. Framed around “when done isn’t.” Everything is synthetic fixtures (data, schemas, tickets, logs) — a measurement instrument, not a clinical product, and not a claim of production or HIPAA readiness.

### **[AI Video Pipeline](https://github.com/antonrasmussen/ai-video-pipeline)**

CLI pipeline that turns a hand-authored shot manifest into a narrated video: Runway for text-to-video generation, ElevenLabs for narration, ffmpeg for local assembly — no manual editing, no UI work in either service. Cost-gated by design, with a free local rehearsal proving the assembly before any paid generation runs. Its own ~80-second teaser was produced end to end by the tool it demonstrates.

### **Quantization Effects on Biomedical LLM Reliability**

Preprint [*Quantization Effects on Biomedical LLM Reliability*](https://arxiv.org/abs/2608.03854) (Rasmussen & Qin) — AAAI 2026 Fall Symposium manuscript. Controlled evaluation of biomedical and general Mistral-7B variants on PubMed RCT under FP16, INT8, and INT4, showing that **prompt templates and scoring rules** can dominate apparent calibration and accuracy comparisons. Frozen course provenance (class-code protocol, not the paper source of truth): [cs781-s26](https://github.com/antonrasmussen/cs781-s26).

### **[UAP Signal](https://github.com/antonrasmussen/uap-signal)**

Python CLI for tracking what is actually new in UAP/UFO-related releases and coverage. Pulls from official and news sources, applies rule-based source trust logic, uses LLMs for summaries and novelty scoring, caches locally in SQLite, and runs a daily release watch with report email plus a weekly digest.

### **Federal opportunity lead pipeline**

Automated pipeline over the official SAM.gov Opportunities API: configurable search profiles, rules-based explainable scoring, deduplication and amendment detection, document parsing, and daily email reports. Kept as a generic, archived automation pattern — adapt the profile and run on a schedule.

### **[Molapse Recorder](https://github.com/antonrasmussen/molapse-recorder)**

Local-first vector stroke recorder for scientific drawings. Designed to record stylus strokes as structured vector data rather than pixels, then replay/export high-resolution transparent timelapses for video editing workflows. Currently in early capture-core development.

### **Secure Healthcare Data Management Framework**

Spark-based ingestion framework using **NER-driven masking and de-identification** for secure handling of clinical text and structured healthcare data.

### **Enhanced Ingestion & Validation Workflow**

Dagster-orchestrated ingestion system with automated validation, quarantine paths, profiling, and review workflows for unconfigured or anomalous data.

### **Pharmacy Analytics Dashboards**

Interactive dashboards and data applications supporting pharmacy stakeholders with operational and analytical decision-making.

---

## 🎓 Education & Research Background

* **M.S. in Computer Science** — Old Dominion University
* Research and project interests:
  * trustworthy AI infrastructure and agent verification
  * healthcare data systems
  * privacy-preserving ML
  * edge / local-first AI
  * biomedical LLM evaluation and calibration measurement
  * reproducible applied research workflows

I’m no longer focused on coursework. My attention now is on building a body of independent work: practical systems, research-informed prototypes, and technical writing that connect my healthcare data engineering background with the next generation of trustworthy AI tools.

---

## 🔍 Currently Exploring

* Agent verification, false completion, and goal-directed harnesses for data-engineering agents
* Model compression, quantization, calibration measurement, and inference efficiency
* Local-first and edge-ready AI deployment
* Agentic workflows for data engineering and research
* Hardware tinkering: Arduino, sensors, instrumentation, and small systems
* Security and privacy as design constraints, not afterthoughts

---

## 🧭 Personal Notes

* **Former Persian Linguist**, U.S. Army 🇺🇸
* Lifelong reader; happiest in libraries and used bookstores 📚
* Drums, guitar, piano
* Pinball, live music, comedy, and learning things the hard way

---

## 🤝 Let’s Connect

Site: [antonrasmussen.com](https://antonrasmussen.com)

If you’re interested in:

* healthcare data platforms,
* trustworthy AI and verified agent systems,
* privacy-preserving systems,
* biomedical LLM evaluation,
* or building tools that people can actually understand and depend on,

feel free to explore my public repositories or reach out via the site.
