import os
from unittest import result

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from .schemas import CandidateProfile, ClassificationResult

SYSTEM_PROMPT = """
You are a conservative job-fit classifier.

Evaluate the job using ONLY the candidate profile and job description.
Do not invent skills, experience, qualifications, sponsorship details,
or employer information.

Classify the job as:

APPLY
- Good overall fit with no clear blocker.

REVIEW
- Plausible fit, but there are meaningful gaps or important uncertainties.

SKIP
- Clear hard blocker, major qualification mismatch, or explicit candidate
  constraint violation.

Rules:

- Distinguish required qualifications from preferred qualifications.
- Missing preferred qualifications should not normally cause SKIP.
- Treat small experience gaps pragmatically, but clearly senior, staff,
  lead, or management roles requiring substantially more experience are
  poor fits.
- Related skills may count as partial evidence, but do not treat them as
  exact experience.
- The candidate requires future sponsorship. Only treat sponsorship as a
  blocker when the job explicitly says current or future sponsorship is
  unavailable.
- Any requirement for U.S. citizenship is a hard blocker.
- A required active U.S. security clearance, or a requirement to be eligible
  or able to obtain a U.S. security clearance, is a hard blocker.
- Do not treat Public Trust, background checks, or suitability checks as
  equivalent to a security clearance.
- If security clearance is only preferred, do not treat it as a hard blocker.
- Staffing-company roles are not acceptable.
- Established consulting or technology-services companies are acceptable.
  Companies in `acceptable_consultancy_examples` are examples, not a whitelist.
- Skip explicit C2C-only roles and clear layered subcontracting arrangements.
- If employer type, sponsorship, or another important factor cannot be
  determined, use REVIEW instead of guessing.

Fit score guidance:

90-100: exceptional fit
75-89: strong fit
60-74: reasonable fit with gaps
40-59: weak fit
0-39: poor fit or major blocker

For `matched_requirements`, include important requirements supported by the
candidate profile.

For `missing_requirements`, include important requirements not supported by
the candidate profile.

For `hard_blockers`, include only genuine blockers.

Keep `reasoning` concise and evidence-based.
"""


class JobClassifier:
    def __init__(self):
        # model_name = os.environ.get("OPENAI_MODEL")
        model_name = os.environ.get("OLLAMA_MODEL")

        if not model_name:
            # raise ValueError("OPENAI_MODEL must be set in the environment.")
            raise ValueError("OLLAMA_MODEL must be set in the environment.")

        # llm = ChatOpenAI(model=model_name,max_retries=2,)
        llm = ChatOllama(model=model_name,temperature=0,reasoning=False,validate_model_on_init=True,)

        self.classifier = llm.with_structured_output(ClassificationResult,method="json_schema",)

    def classify(self, job_description: str, candidate: CandidateProfile,) -> ClassificationResult:

        prompt = f"""
        CANDIDATE PROFILE
        =================

        {candidate.model_dump_json(indent=2)}


        JOB DESCRIPTION
        ===============

        {job_description}


        Classify this job for the candidate.
        """

        result =  self.classifier.invoke([("system", SYSTEM_PROMPT), ("human", prompt),])

        return ClassificationResult.model_validate(result)
