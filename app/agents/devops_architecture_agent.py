from ..provider import call_ai

class DevOpsArchitectureAgent:
    name = "DevOpsArchitectureAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Definindo arquitetura DevOps...")

        backlog = payload.get("devops_backlog", "")
        prompt = (
            "Você é um arquiteto DevOps, Cloud e SRE experiente.\n\n"
            "Com base no backlog, descreva uma ARQUITETURA DEVOPS completa, incluindo:\n"
            "• Infraestrutura cloud (AWS, GCP, Azure);\n"
            "• Containers e Kubernetes;\n"
            "• CI/CD (pipelines, testes, deploy);\n"
            "• Infraestrutura como código (Terraform);\n"
            "• Observabilidade (logs, métricas, traces, alertas);\n"
            "• DevSecOps (scanners, IAM, secrets, RBAC);\n"
            "• Estratégias SRE e confiabilidade;\n"
            "• Riscos, gargalos e recomendações.\n\n"
            f"BACKLOG:\n{backlog}\n\n"
            "Retorne em Markdown com seções organizadas."
        )

        architecture = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Arquitetura DevOps gerada.")
        return {"devops_architecture": architecture}
