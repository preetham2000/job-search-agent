import sys
import time

from dotenv import load_dotenv

from job_search_agent.classifier import JobClassifier
from job_search_agent.profile import load_candidate_profile


def main():
    load_dotenv()

    print("\nJob Search Agent - v0")
    print("=====================\n")

    print("Paste the job description below.")

    job_description = sys.stdin.read().strip()

    if not job_description:
        print("No job description provided.")
        return
    
    print(f"Received job description ({len(job_description)} characters).")
    print("Classifying...\n")

    profile = load_candidate_profile()

    classifier = JobClassifier()

    # Just for debugging, print the length of the job description and whether it contains staffing info
    print(f"JD length: {len(job_description)} characters")
    print(
        "Staffing info present:",
        "Staffing and Recruiting" in job_description,
    )

    start_time = time.time()

    result = classifier.classify(job_description=job_description, candidate=profile,)
    inference_time = time.time() - start_time

    print("\nClassification")
    print("==============\n")

    print(result.model_dump_json(indent=2))
    print(f"\nInference time: {inference_time:.2f} seconds")


if __name__ == "__main__":
    main()