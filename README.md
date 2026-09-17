# Job Search and Sort Agent

An AI-assisted job discovery and analysis tool designed to streamline the job-search process by collecting, structuring, filtering, and ranking job opportunities based on a candidate's profile and preferences.

The project will combine deterministic filtering with LLM-based analysis to evaluate job descriptions, identify relevant skills and requirements, detect potential mismatches, and prioritize opportunities that are worth reviewing.

The initial version focuses on analyzing individual job descriptions and producing structured job information and match assessments. Future iterations will add automated job ingestion, deduplication, persistent storage, scheduled searches, alerts, and a user interface.

## Planned Features

* Extract structured information from job descriptions
* Categorize jobs by role and seniority
* Identify required and preferred skills
* Compare job requirements against a candidate profile
* Detect hard constraints and potential disqualifiers
* Rank jobs based on relevance and fit
* Deduplicate listings from multiple sources
* Track previously discovered jobs
* Send alerts for newly discovered high-relevance opportunities

## Initial Tech Stack

* Python
* OpenAI API
* LangGraph
* LangChain OpenAI
* Pydantic
* Beautiful Soup
* Requests
* pytest
* uv for dependency and environment management

> This project is currently under active development. The first milestone is a small end-to-end pipeline that accepts a job description, extracts structured requirements, and evaluates it against a candidate profile.
