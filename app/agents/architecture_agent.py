from ..provider import call_ai

class DevOpsArchitectureAgent:
    name = "DevOpsArchitectureAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Definindo arquitetura DevOps...")

        backlog = payload.get("devops_backlog", "")
        prompt = (
            "Você é um arquiteto DevOps, Cloud e SRE com ampla experiência.\n\n"
            "Com base no backlog, descreva uma ARQUITETURA DEVOPS COMPLETA, cobrindo:\n\n"
            "• Infraestrutura (AWS/GCP/Azure, containers, Kubernetes, serverless, redes, VPCs, gateways);\n"
            "• Padrão de IaC (Terraform, módulos, reusabilidade, pipelines de infra);\n"
            "• Pipelines CI/CD detalhados (build, testes, deploy, gates, promoções, artefatos);\n"
            "• Observabilidade (Prometheus, Grafana, Loki, ELK, OpenTelemetry, alerting);\n"
            "• Estratégias SRE (SLIs, SLOs, error budgets, incident management);\n"
            "• DevSecOps (scanners, secrets, rota segura de deploy, políticas, RBAC, IAM);\n"
            "• Governança e compliance;\n"
            "• Monitoramento de custos e FinOps;\n"
            "• Estratégia de ambientes (dev/stage/prod) e fluxo de promoção;\n"
            "• Backup, restore, disaster recovery, resiliência;\n"
            "• Principais riscos, gargalos e pontos de atenção.\n\n"
            "Retorne em Markdown estruturado por seções.\n\n"
            f"BACKLOG:\n{backlog}"
        )

        architecture = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Arquitetura DevOps gerada.")
        return {"devops_architecture": architecture}
