
import openai
openai.api_key = "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"

from utils import split_based_on_lines
from utils import prostprocess_code_results

def cust_beautify_code(code_str, base_prompt):
    list_clips = split_based_on_lines(code_str)
    list_clips = [x for x in list_clips if len(x.strip())>0]
    list_results = []
    for c in list_clips:

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": base_prompt + c}
            ]
        )
        #
        if response['choices'][0]['finish_reason'] == "stop":
            list_results.append(response.choices[0]['message']['content'])
        else:
            list_results.append(c)

        # print("inide chatgpt")

    return "\n".join(list_results)




