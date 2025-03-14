from flask import Flask, request, jsonify
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

app = Flask(__name__)

@app.route("/api/openapiRequest", methods=["POST"])
def hello_world():
    data = request.get_json()

    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing prompt in the request"}), 400

    system_context = "You are a helpful assistant who explains things in a way that a 5-year-old would understand."
    response = get_openai_response(prompt, system_context)

    if response:
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Failed to get a response from OpenAI"}), 500


def get_openai_response(prompt: str, system_context: str = None):
    try:
        chat = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.9,
            openai_api_key="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"
        )

        messages = []

        if system_context:
            messages.append(SystemMessage(content=system_context))

        messages.append(HumanMessage(content=prompt))

        response = chat.invoke(messages)

        return response.content

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
