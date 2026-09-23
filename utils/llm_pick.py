from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


def pick_llm(level: str):

    if level.lower() == "low":
        return ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0
        )

    elif level.lower() == "medium":
        return ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )

    elif level.lower() == "high":
        return ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0
        )

    else:
        raise ValueError(f"Unsupported level: {level}")


if __name__ == "__main__":
    llm = pick_llm("low")

    response = llm.invoke(
        "What is the capital of France?"
    )

    print(response.content)