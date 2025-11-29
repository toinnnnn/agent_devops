from fastapi import FastAPI
from .agents.backlog_agent import DevOpsBacklogAgent
from .agents.architecture_agent import DevOpsArchitectureAgent
from .agents.documentation_agent import DevOpsDocumentationAgent
from .agents.reviewer_agent import DevOpsReviewerAgent

app = FastAPI()

@app.post("/backlog")
async def backlog(payload: dict):
    agent = DevOpsBacklogAgent()
    return await agent.run(payload, print, "task-backlog")

@app.post("/architecture")
async def architecture(payload: dict):
    agent = DevOpsArchitectureAgent()
    return await agent.run(payload, print, "task-architecture")

@app.post("/documentation")
async def documentation(payload: dict):
    agent =DevOpsDocumentationAgent()
    return await agent.run(payload, print, "task-documentation")

@app.post("/review")
async def review(payload: dict):
    agent = DevOpsReviewerAgent()
    return await agent.run(payload, print, "task-review")
