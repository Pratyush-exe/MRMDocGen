import openai
import os


openai.api_key = "" # Fetch from a .env file 


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
    return {
            "overview": getResp("Explain this problem statement properly: " + info["overview"]),
            "data_prep": getResp("Explain the steps taken in data preparations properly: " + info["data_prep"]),
            "model_name": info["model_name"],
            "model_methadology": getResp("Explain this public information given properly: " + info["model_methadology"]),
            "assumptions": getResp("Explain this assumptions properly: " + info["assumptions"]),
            "conclusion": getResp("Explain this reason for assumptions properly: " + info["conclusion"])
           }
