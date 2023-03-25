import openai
import os

openai.api_key = "API"


def getResp(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(response)
    return response["choices"][0]['text']


def getTextGPT(info):
    return {
            "problem": getResp("Explain this problem statement properly: " + info["problem"]),
            "model_name": getResp("Explain the model description and techs mentioned here properly: " + info["model_name"]),
            "public_info": getResp("Explain this public information given properly: " + info["public_info"]),
            "assumptions": getResp("Explain this assumptions properly: " + info["assumptions"]),
            "assumptions_reasons": getResp("Explain this reason for assumptions properly: " + info["assumptions_reasons"])
           }
