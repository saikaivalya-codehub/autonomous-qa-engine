from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import subprocess, json, os
from llm import generate_tests_from_story
from prioritizer import prioritize
from triage import basic_triage

app = FastAPI(title="Agentic QA Engine")

class StoryIn(BaseModel):
    title: str
    text: str

class GenOut(BaseModel):
    gherkin: str
    playwright: str

class PrioritizeIn(BaseModel):
    tests: List[str]
    changed_paths: List[str] = []

class TriageIn(BaseModel):
    failures: List[Dict[str, Any]]

@app.post("/generate-tests", response_model=GenOut)
def generate_tests(story: StoryIn):
    gherkin, playwright = generate_tests_from_story(story.title, story.text)
    return GenOut(gherkin=gherkin, playwright=playwright)

@app.post("/prioritize")
def prioritize_tests(inp: PrioritizeIn):
    return {"order": prioritize(inp.tests, inp.changed_paths)}

@app.post("/triage")
def triage(inp: TriageIn):
    return basic_triage(inp.failures)

@app.post("/run")
def run_all():
    # run API tests (Karate)
    api = subprocess.run(["mvn", "-q", "test"], cwd="tests-api", capture_output=True, text=True)
    # run UI tests (Playwright)
    ui_install = subprocess.run(["npm", "i"], cwd="tests-ui", capture_output=True, text=True)
    ui = subprocess.run(["npm", "test"], cwd="tests-ui", capture_output=True, text=True)
    return {
        "api_exit": api.returncode,
        "ui_exit": ui.returncode,
        "api_out": api.stdout[-8000:],
        "ui_out": ui.stdout[-8000:],
    }