from fastapi import FastAPI
from .agents.backlog_agent import BacklogAgent
from .agents.architecture_agent import ArchitectureAgent
from .agents.documentation_agent import DocumentationAgent
from .agents.reviewer_agent import ReviewerAgent

app = FastAPI()

@app.post("/backlog")
async def backlog(payload: dict):
    agent = BacklogAgent()
    return await agent.run(payload, print, "task-backlog")

@app.post("/architecture")
async def architecture(payload: dict):
    agent = ArchitectureAgent()
    return await agent.run(payload, print, "task-architecture")

@app.post("/documentation")
async def documentation(payload: dict):
    agent = DocumentationAgent()
    return await agent.run(payload, print, "task-documentation")

@app.post("/review")
async def review(payload: dict):
    agent = ReviewerAgent()
    return await agent.run(payload, print, "task-review")