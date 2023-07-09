
import openai
openai.api_key = "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"




def cust_beautify_code(code_str):
    list_clips = split_based_on_lines(code_str)
    list_clips = [x for x in list_clips if len(x.strip())>0]
    list_results = []
    for c in list_clips:

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "please optimize given python code also please provide only code:\n" + c}
            ]
        )
        #
        if response['choices'][0]['finish_reason'] == "stop":

            list_results.append(response.choices[0]['message']['content'])
        else:
            list_results.append(c)
        print("inide chatgpt")

    return "\n".join(list_results)

def split_based_on_lines(code_str):
    split_words = ["def ", "class "]
    list_clips = []

    list_doc_line = code_str.split("\n")

    line_prev_idx = 0

    for i, line in enumerate(list_doc_line):
        flag_split = False
        if "def " in line and line.strip()[-1] == ":" and line.strip()[0] != "#":
            flag_split = True

        elif "class " in line:
            flag_split = True

        if flag_split:
            list_clips.append("\n".join(list_doc_line[line_prev_idx:i]))
            line_prev_idx = i

    if line_prev_idx != i:
        list_clips.append("\n".join(list_doc_line[line_prev_idx:]))

    return list_clips