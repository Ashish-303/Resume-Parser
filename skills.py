import re

# -------------------------------
# Try loading Google Vertex AI
# -------------------------------
VERTEX_AVAILABLE = False
try:
    from vertexai.language_models import TextEmbeddingModel
    import vertexai
    vertexai.init()
    model = TextEmbeddingModel.from_pretrained("text-embedding-004")
    VERTEX_AVAILABLE = True
except:
    VERTEX_AVAILABLE = False


# -------------------------------
# Skill Database
# -------------------------------
TECH_SKILLS = [
    "python","java","c","c++","javascript","typescript","react","node",
    "django","flask","spring","html","css","bootstrap",
    "kotlin","swift","android","ios",
    "sql","mysql","postgres","mongodb","firebase",
    "machine learning","deep learning","nlp","data science","ai",
    "tensorflow","keras","pytorch","scikit-learn","opencv",
    "power bi","tableau",
    "git","github","devops","docker","kubernetes","linux","jenkins",
    "aws","gcp","azure"
]

SOFT_SKILLS = [
    "leadership","communication","teamwork","time management",
    "problem solving","critical thinking","presentation",
    "collaboration","adaptability"
]


# -------------------------------
# Helper: Normalize text
# -------------------------------
def clean_text(text):
    return re.sub(r"\s+", " ", text.lower())


# -------------------------------
# Rule-Based Skill Extractor
# -------------------------------
def rule_based_skill_extractor(text):
    text = clean_text(text)

    found = set()

    for skill in TECH_SKILLS + SOFT_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found.add(skill)

    return sorted(list(found))


# -------------------------------
# Vertex AI Skill Extractor (Semantic)
# -------------------------------
def vertex_skill_extractor(text):
    """
    Uses embeddings to semantically detect skills.
    Works even when resume says:
    "Experience building neural networks"
    → Detects "deep learning"
    """
    try:
        emb_resume = model.get_embeddings([text])[0].values

        results = []
        for skill in TECH_SKILLS:
            emb_skill = model.get_embeddings([skill])[0].values
            score = sum(a*b for a, b in zip(emb_resume, emb_skill))
            results.append((skill, score))

        results.sort(key=lambda x: x[1], reverse=True)

        top = [s for s, sc in results[:15] if sc > 0.5]

        return sorted(list(set(top)))
    except:
        return rule_based_skill_extractor(text)


# -------------------------------
# Public Function
# -------------------------------
def extract_skills(text):
    if VERTEX_AVAILABLE:
        return vertex_skill_extractor(text)

    return rule_based_skill_extractor(text)
