# Job Search and Sort Agent

An AI-assisted job analysis tool for evaluating job descriptions against a candidate profile and quickly deciding which opportunities are worth reviewing.

The project combines structured candidate information with LLM-based analysis to identify relevant skills, experience requirements, potential gaps, and blockers, then produces a structured recommendation for each job.

## v0 — Local Job Classification

**v0 is complete.**

The current version focuses on a simple local workflow:

```text
Job Description
      ↓
Candidate Profile
      ↓
Local Open-Source LLM
      ↓
Structured Job Assessment
```

A job description is pasted manually into the application and evaluated against a local candidate profile.

The classifier produces a structured assessment containing:

* `decision`: `APPLY`, `REVIEW`, or `SKIP`
* `fit_score`: overall job-profile match score
* `role_family`: detected role category
* `matched_requirements`: requirements supported by the candidate profile
* `missing_requirements`: requirements not represented in the candidate profile
* `hard_blockers`: potential disqualifying requirements
* `reasoning`: explanation of the recommendation

v0 intentionally keeps the pipeline small and local. It does not include job scraping, automatic applications, persistent storage, alerts, RAG, or a user interface.

## Current Tech Stack

* Python
* Ollama
* Qwen3.5
* LangChain Ollama (`ChatOllama`)
* Pydantic
* python-dotenv
* uv for dependency and environment management

The project is structured so that additional model providers and job-processing stages can be introduced in later versions.

## Project Structure

```text
job-search-agent/
├── app/
│   └── main.py
│
├── src/
│   └── job_search_agent/
│       ├── __init__.py
│       ├── classifier.py
│       ├── profile.py
│       └── schemas.py
│
├── data/
│   └── profile.example.json
│
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

Local files such as `.env` and `data/profile.json` are created during setup and should remain excluded from Git.

## Prerequisites

You will need:

* Python 3.12 or later
* Git
* `uv`
* Ollama

## Installing uv

`uv` is used for Python dependency and virtual-environment management.

### macOS / Linux

Install `uv` using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify the installation:

```bash
uv --version
```

You may need to restart your terminal before the `uv` command becomes available.

Alternatively, if Homebrew is installed:

```bash
brew install uv
```

## Clone the Repository

```bash
git clone <repository-url>
cd job-search-agent
```

Replace `<repository-url>` with the URL of this repository.

## Set Up the Python Environment

The repository contains `pyproject.toml` and `uv.lock`, so `uv` can recreate the project environment and install the required dependencies.

Run:

```bash
uv sync
```

This creates a local virtual environment:

```text
.venv/
```

and installs the dependencies defined by the project.

### Activating the Virtual Environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activation is optional when using `uv run`, since `uv` automatically executes commands inside the project environment.

## Environment Configuration

Create a local `.env` file from the provided example:

```bash
cp .env.example .env
```

The Ollama model used by the application can be configured in `.env`.

For example:

```env
OLLAMA_MODEL=qwen3.5:9b
```

The `.env` file is intended for local configuration and should not be committed to Git.

## Install and Run Ollama

v0 runs against local open-source models through Ollama.

Install Ollama from:

```text
https://ollama.com/
```

Verify the installation:

```bash
ollama --version
```

Pull the default model used by the project:

```bash
ollama pull qwen3.5:9b
```

Available Ollama models can be viewed at:

```text
https://ollama.com/search
```

Make sure Ollama is running before starting the application.

The model can be changed through the `OLLAMA_MODEL` value in `.env`.

## Candidate Profile

The repository includes a generic sample candidate profile:

```text
data/profile.example.json
```

Create your local profile by copying the example:

```bash
cp data/profile.example.json data/profile.json
```

Then edit:

```text
data/profile.json
```

with your own:

* Target roles
* Experience
* Education
* Skills
* Location preferences
* Sponsorship requirements

`profile.example.json` contains only generic example data and remains in the repository as a reference configuration.

`profile.json` contains the actual candidate information used by the application and should remain local and excluded from Git.

## Running v0

From the repository root:

```bash
uv run python app/main.py
```

Alternatively, activate the virtual environment first:

```bash
source .venv/bin/activate
```

and run:

```bash
python app/main.py
```

Paste a job description when prompted.

The application loads the local candidate profile, sends the job and profile information to the configured Ollama model, validates the response against the structured output schema, and displays the resulting job assessment.

## Example Workflow

```text
1. Find a job posting
        ↓
2. Copy the job description
        ↓
3. Run the application
        ↓
4. Paste the job description
        ↓
5. Local LLM analyzes the job
        ↓
6. Review decision, score,
   matches, gaps, and blockers
```

The purpose of v0 is to establish and validate the core job-classification pipeline before adding additional automation around it.

## Current Scope

Included in v0:

* Manual job-description input
* Candidate-profile loading
* Local open-source LLM inference
* Structured and validated LLM output
* Role-family classification
* Job/profile comparison
* Match scoring
* Requirement-match identification
* Missing-requirement identification
* Hard-blocker detection
* `APPLY`, `REVIEW`, or `SKIP` recommendation
* Configurable local Ollama model

Not included in v0:

* Automated job scraping
* Browser automation
* Automatic job applications
* RAG
* Embeddings or vector databases
* Persistent job database
* Deduplication
* Scheduled searches
* Notifications
* Web UI
* Multi-agent workflows

These features are intentionally outside the scope of the initial version.

## Development Philosophy

The project is being developed incrementally.

Each version should solve a concrete job-search problem while keeping the system small enough to remain practical for personal use.

The goal is not to automate the entire application process. Instead, the agent should reduce the amount of time spent manually reading and comparing job descriptions so that more time can be spent on high-value applications.

## Status

**v0: Complete**
