import os
import pdfplumber

try:
    from google.cloud import vision
    VISION_AVAILABLE = True
except:
    VISION_AVAILABLE = False


def extract_text_with_google_vision(file_path):
    client = vision.ImageAnnotatorClient()

    with open(file_path, "rb") as f:
        content = f.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    if response.error.message:
        raise Exception(response.error.message)

    return response.full_text_annotation.text


def extract_text_with_pdfplumber(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()


def extract_text_from_pdf(file_path):
    use_google = (
        VISION_AVAILABLE and
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") and
        os.path.exists(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
    )

    if use_google:
        try:
            return extract_text_with_google_vision(file_path)
        except Exception:
            return extract_text_with_pdfplumber(file_path)

    return extract_text_with_pdfplumber(file_path)
