import openai
import io
import streamlit as st
from git import Repo
from const_prompts import *

from cust_beautify_code import cust_beautify_code, basic_call
def load_files_from_github(url):
    if url:
     Repo.clone_from(url,'/git_clones')


def beautify_code(code_str):
    # Process and edit the code here
    if code_str:
        processed_code = cust_beautify_code(code_str, PROMPT_beautify_code)
    else:
        processed_code = "Please Enter Code"
    return processed_code


def get_code_score(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_code_score)
    else:
        return "Please Enter Code"

def get_audio_text(audio_bytes):
    if len(audio_bytes)>0:
        f = io.BytesIO(audio_bytes)
        f.name = 'tmp_file.mp3'
        transcription = openai.Audio.transcribe("whisper-1", f, format="mp3")['text']
        return transcription
    else:
        return None

def add_comments(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_add_comments)
    else:
        return "Please add Code"

def get_alternate_code(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_alternate_code)
    else:
        return "please add code"

def process_documentation(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_preprare_doc)
    else:
        return "please add code"

def get_time_complexity(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_space_time_complexity)
    else:
        return "please provide code"

def get_code_testcases(code_str):
    if code_str:
        return cust_beautify_code(code_str, PROMPT_test_cases)
    else:
        return  "please provide code"


def get_code_snippets(code_str):
    if code_str:
        return basic_call(code_str, PROMPT_code_snippet_gen)
    else:
        return "please add text"

