import time
import openai
openai.api_key = "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"

from utils import split_based_on_lines
from utils import prostprocess_code_results

def cust_beautify_code(code_str, base_prompt):
    #generate first results
    # response_first = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo-16k",
    #         messages=[
    #             {"role": "system", "content": base_prompt + code_str}
    #         ]
    #     )

    response_first = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", temperature = 0,
        messages=[
            {"role": "system", "content": base_prompt},
            {"role": "user", "content":  code_str}
        ]
    )

    if response_first['choices'][0]['finish_reason'] == "stop":
        print("resopnse only first go")
        print("code_str", code_str)
        print(response_first)
        return response_first.choices[0]['message']['content']

    else:

        list_clips = split_based_on_lines(code_str)
        list_clips = [x for x in list_clips if len(x.strip())>0]
        print("len(list_clips)", len(list_clips))
        list_results = []
        for c in list_clips:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",temperature = 0,
                messages=[
                    {"role": "system", "content": base_prompt},
                    {"role": "user", "content": c}
                ]
            )
            #
            if response['choices'][0]['finish_reason'] == "stop":
                list_results.append(response.choices[0]['message']['content'])
            else:
                list_results.append(c)

            time.sleep(1)

            # print("inide chatgpt")

        return "\n".join(list_results)

def basic_call(code_str, base_prompt):
    if len(code_str)>0:

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": base_prompt},
                {"role": "user", "content": code_str}
            ]
        )

        return response.choices[0]['message']['content']

    else:
        return ""




