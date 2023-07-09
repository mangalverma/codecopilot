


def prostprocess_code_results():

    return






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