def answer_question(question, document):

    if document:
        return (
            "PDF Answer:\n\n"
            + document[:1500]
        )

    replies = {
        "hi": "Hello bro 👋",
        "hello": "Hello!",
        "who are you": "I am your AI Research Assistant",
        "how are you": "I'm running fine 🚀"
    }

    return replies.get(
        question.lower(),
        "Ask anything or upload a PDF."
    )



