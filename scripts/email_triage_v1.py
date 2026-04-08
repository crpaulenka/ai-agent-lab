from dataclasses import dataclass
from typing import List


@dataclass
class Email:
    sender: str
    subject: str
    body: str


@dataclass
class TriageResult:
    priority: str
    reasons: List[str]


URGENT_KEYWORDS = [
    "legal",
    "attorney",
    "lawsuit",
    "insurance",
    "claim",
    "injury",
    "accident",
    "fire",
    "flood",
    "leak",
    "water intrusion",
    "security",
    "police",
    "emergency",
    "unsafe",
    "hazard",
]

IMPORTANT_KEYWORDS = [
    "vendor",
    "proposal",
    "contract",
    "board",
    "meeting",
    "resident",
    "violation",
    "compliance",
    "project",
    "maintenance",
    "invoice",
    "inspection",
]


def classify_email(email: Email) -> TriageResult:
    text = f"{email.sender} {email.subject} {email.body}".lower()

    reasons = []

    for keyword in URGENT_KEYWORDS:
        if keyword in text:
            reasons.append(f"Matched urgent keyword: {keyword}")

    if reasons:
        return TriageResult("Urgent", reasons)

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text:
            reasons.append(f"Matched important keyword: {keyword}")

    if reasons:
        return TriageResult("Important", reasons)

    return TriageResult(
        "Routine",
        ["No urgent or important keywords matched."]
    )


def summarize_email(email: Email, result: TriageResult):
    print("\n---------------------------")
    print(f"From: {email.sender}")
    print(f"Subject: {email.subject}")
    print(f"Priority: {result.priority}")
    print("Reasons:")

    for reason in result.reasons:
        print(f"- {reason}")


def main():

    sample_emails = [

        Email(
            sender="association.counsel@example.com",
            subject="Legal demand regarding resident dispute",
            body="Please review this matter today."
        ),

        Email(
            sender="pool.vendor@example.com",
            subject="Updated maintenance proposal",
            body="Attached is the new service proposal."
        ),

        Email(
            sender="resident@example.com",
            subject="Clubhouse hours question",
            body="Can you confirm weekend hours?"
        ),

    ]

    print("\n=== MORNING EMAIL TRIAGE SUMMARY ===")

    for email in sample_emails:

        result = classify_email(email)

        summarize_email(email, result)


if __name__ == "__main__":
    main()