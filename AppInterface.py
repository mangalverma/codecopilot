import streamlit as st
# from audio_recorder_streamlit import audio_recorder
from audiorecorder import audiorecorder
import openai
from GPTworkers import *
import io
from code_editor import code_editor


openai.api_key = "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"
st.set_page_config(initial_sidebar_state="expanded",layout="wide",page_title='CodeCoPilot')




def main():

    st.title('Code CoPilot')
    response = ''
    left_container,right_container = st.columns([1,1])
    with left_container:
        with st.container():
            text_area = st.empty()
            code = text_area.text_area(label='Enter your code', value='', height=600)
            uploaded_file = st.file_uploader("Choose a file [.py]")

            if uploaded_file is not None:
                if not uploaded_file.name.endswith('.py'):
                    warning_box = st.text_input('WARNING',"Choose valid File")
                    st.write(warning_box)
                else:
                    # To read file as bytes:
                    # bytes_data = uploaded_file.getvalue()

                    # To convert to a string based IO:
                    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))

                    # To read file as string:
                    string_data = stringio.read()
                    text_area.text_area(label='Enter your code', value=string_data,height=600)
                    code = string_data

                # Can be used wherever a "file-like" object is accepted:
            # col1, col2, col3= st.columns([0.5, 0.5, 0.5])
            # scol1, scol2, scol3 = st.columns([0.5, 0.5,0.5])
            # tcol1,tcol2,tcol3 = st.columns([0.5,0.5,0.5])
            # with tcol3:
            #     audio_bytes = audiorecorder("Click to Record", "Recording......")
            #     # audio_bytes = audio_recorder(text=" ", icon_size='2x')
            #     if len(audio_bytes) > 0:
            #         # st.audio(audio_bytes, format="audio/wav")
            #         response = processed_audio(audio_bytes, text_area)
            #
            # with col1:
            #     if st.button('Get Score'):
            #         response = get_code_score(code)
            # with col2:
            #     if st.button('Beautify Code'):
            #         response = beautify_code(code)
            # with col3:
            #     if st.button('Add Comments'):
            #         response = add_comments(code)
            #
            #
            # with scol1:
            #     if st.button('Get time Complexity'):
            #         response = get_time_complexity(code)
            # with scol2:
            #     if st.button('write test cases'):
            #         response = get_code_testcases(code)
            # with scol3:
            #     if st.button('Generate Documentation'):
            #         response = process_documentation(code)
            #
            # with tcol1:
            #     if st.button('suggest alternative code'):
            #         response = get_alternate_code(code)
            # with tcol2:
            #     if st.button('suggest code snippets'):
            #         response = get_code_snippets(code)


    with st.sidebar:

        if st.button('Clone From Github'):
            github_url = st.text_input('Enter Github public URL', '')
            if len(github_url)>0:
                load_files_from_github(github_url)

        audio_bytes = audiorecorder("Click to Record", "Recording......")
        if uploaded_file is None or len(audio_bytes)>=1:
                        # audio_bytes = audio_recorder(text=" ", icon_size='2x')
                if len(audio_bytes) > 0:
                         # st.audio(audio_bytes, format="audio/wav")
                    code = get_audio_text(audio_bytes)
                    text_area = text_area.empty()
                    text_area.text_area(label='Enter your code', value=code, height=600)
                    response = get_code_snippets(code)
        if st.button('Get Score'):
            response = get_code_score(code)
        if st.button('Beautify Code'):
            response = beautify_code(code)
        if st.button('Add Comments'):
            response = add_comments(code)

        if st.button('Get time Complexity'):
            response = get_time_complexity(code)
        if st.button('write test cases'):
            response = get_code_testcases(code)
        if st.button('Generate Documentation'):
            response = process_documentation(code)

        if st.button('Suggest alternative code'):
            response = get_alternate_code(code)
        if st.button('Suggest code snippets'):
            response = get_code_snippets(code)
    with right_container:
        with st.container():
                st.markdown('Processed code:')
                code_editor(response,height="580px")
                # print(code)


if __name__ == '__main__':
    main()
