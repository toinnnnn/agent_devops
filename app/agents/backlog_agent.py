from ..provider import call_ai

class DevOpsBacklogAgent:
    name = "DevOpsBacklogAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Gerando backlog completo DevOps...")

        desc = payload.get("description", "")
        prompt = (
            "Você é um especialista sênior em DevOps, SRE, Cloud e Segurança.\n\n"
            "Com base na descrição do projeto, gere um BACKLOG DEVOPS completo contendo 8–15 itens que cubram:\n"
            "- CI/CD (builds, testes, deploy, gates, automações);\n"
            "- Infraestrutura como Código (Terraform, Pulumi, CloudFormation);\n"
            "- Containers e Orquestração (Docker, Kubernetes, Helm);\n"
            "- Observabilidade (logs, métricas, traces, alertas, dashboards);\n"
            "- Segurança (DevSecOps, IAM, RBAC, scanners SAST/DAST, secrets, compliance);\n"
            "- Automação e pipelines operacionais;\n"
            "- Gestão de ambientes (dev, stage, homol, prod);\n"
            "- Estratégias SRE (SLOs, SLIs, incident management, reliability);\n"
            "- FinOps e otimização de custos;\n"
            "- Backup, disaster recovery, versionamento e governança.\n\n"
            "Cada item deve conter: título, descrição, prioridade e justificativa.\n"
            "Retorne em JSON.\n\n"
            f"DESCRIÇÃO DO PROJETO:\n{desc}"
        )

        backlog = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Backlog DevOps gerado.")
        return {"devops_backlog": backlog}
