import re
import spacy

# Load NLP model (kept for future improvements, not required now)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None


# ---------- BASIC EXTRACTORS ----------
def extract_email(text):
    m = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return m.group() if m else None


def extract_phone(text):
    patterns = [
        r"\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}",
        r"\+?\d{1,3}[\s\-\.]?\d{3,4}[\s\-\.]?\d{4,6}"
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group().strip()
    return None


def extract_links(text):
    linkedin = None
    github = None

    li = re.search(r"(https?://)?(www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+", text)
    gh = re.search(r"(https?://)?(www\.)?github\.com/[a-zA-Z0-9_-]+", text)

    if li:
        linkedin = li.group()
    if gh:
        github = gh.group()

    return linkedin, github


# ---------- NAME FROM EMAIL (CLEANED) ----------
def extract_name_from_email(email):
    if not email:
        return None

    username = email.split("@")[0]

    # remove numbers and symbols
    username = re.sub(r"[0-9._\-]", "", username)

    # remove spaces just in case
    username = username.strip()

    # if empty return None
    return username if username else None


# ---------- PUBLIC FUNCTION ----------
def extract_basic_info(text):
    email = extract_email(text)
    linkedin, github = extract_links(text)

    return {
        "name": extract_name_from_email(email),
        "email": email,
        "phone": extract_phone(text),
        "linkedin": linkedin,
        "github": github
    }
