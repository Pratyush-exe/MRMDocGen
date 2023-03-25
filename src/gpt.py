import openai
import os

openai.api_key = "U2HJ83bf10TycQmUFgzyT3BlbkFJoZJc36gQBWd0ajl4H4Ed" # have to chage this 


def getResp(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    print(response)
    return response["choices"][0]["text"]


def getTextGPT(info):
    result = {}
    for query in info.keys():
        result[query] = getResp(
            "Explain this text and concepts used in it properly: "
            + info[query]
        )

    return result
