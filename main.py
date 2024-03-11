import logging
import os
import sys

import colorlog
import dotenv
import numpy as np
from openai import OpenAI
from openai.types import Embedding

cwd = os.getcwd()

sys.path.append(cwd)

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

dotenv.load_dotenv()

assert os.environ.get("OPENAI_API_KEY") is not None

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

ideal = """
function add(a, b) {
    return a + b;
}
"""

generated = """
function add(a, b) {
    return a - b;
}
"""


def embeddings(string_or_tokens: str | list) -> list[Embedding] | None:
    logger.info("Getting embeddings from OpenAI.")
    try:
        result = client.embeddings.create(
            input=string_or_tokens,
            model="text-embedding-3-large"
        )
        logger.info("Successfully generated embeddings.")
        return result.data
    except Exception as e:
        logger.error(f"Error: {e}")
        return None


def main():
    logger.info("Starting embeddings program.")

    ideal_embedding = embeddings(ideal)
    generated_embedding = embeddings(generated)

    vec1 = np.array(ideal_embedding[0].embedding)
    vec2 = np.array(generated_embedding[0].embedding)

    cosine_similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    logger.info(f"Cosine similarity: {cosine_similarity}")

    logger.info("Finished. Closing down now.")


if __name__ == "__main__":
    main()
