from ..provider import call_ai

class DevOpsReviewerAgent:
    name = "DevOpsReviewerAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Realizando revisão DevOps final...")

        backlog = payload.get("devops_backlog", "")
        architecture = payload.get("devops_architecture", "")
        documentation = payload.get("devops_documentation", "")
        prompt = (
            "Você é um auditor e revisor sênior especializado em DevOps, Cloud, SRE e SecOps.\n\n"
            "Analise a consistência entre backlog DevOps, arquitetura e documentação.\n\n"
            "Entregue:\n"
            "1) 5 melhorias rápidas e de alto impacto cobrindo CI/CD, IaC, observabilidade, segurança e confiabilidade;\n"
            "2) Inconsistências encontradas entre backlog, arquitetura e documentação;\n"
            "3) Checklist de 10 itens para validar toda a fundação DevOps nas primeiras sprints,\n"
            "   cobrindo: pipelines, infraestrutura, governança, SRE, segurança, monitoramento, custos.\n\n"
            f"BACKLOG:\n{backlog}\n\nARQUITETURA:\n{architecture}\n\nDOCUMENTAÇÃO:\n{documentation}"
        )

        review = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Revisão DevOps concluída.")
        return {"devops_review": review}
