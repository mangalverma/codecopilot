import openai
import io
import streamlit as st
from git import Repo

from cust_beautify_code import cust_beautify_code
def load_files_from_github(url):
    if url:
     Repo.clone_from(url,'/git_clones')


def beautify_code(code_str):
    # Process and edit the code here
    if code_str:
        processed_code = cust_beautify_code(code_str)
    else:
        processed_code = "Please Enter Code"
    return processed_code


def get_code_score(code):
    if code:
        return "Your Score is 10/100"
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

def add_comments(code):
    if code:
        return "Comment Code will be here"
    else:
        return "Please add Code"

def get_alternate_code(code):
    if code:
        return "altername code will be here"
    else:
        return "please add code"

def process_documentation(code):
    if code:
        return "your doc will be here"
    else:
        return "please add code"

def get_time_complexity(code):
    if code:
        return "time complexit will be showm here"
    else:
        return "please provide code"

def get_code_testcases(code):
    if code:
        return "code testcases will be here"
    else:
        return  "please provide code"


def get_code_snippets(code):
    if code:
        return "suggested code will be here"
    else:
        return "please add text"

