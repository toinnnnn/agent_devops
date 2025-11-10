from ..provider import call_ai

class DevOpsDocumentationAgent:
    name = "DevOpsDocumentationAgent"

    async def run(self, payload: dict, logger, task_id: str, provider=None):
        logger(f"[{task_id}] [{self.name}] Criando documentação DevOps...")

        architecture = payload.get("devops_architecture", "")
        backlog = payload.get("devops_backlog", "")
        prompt = (
            "Você é um technical writer especializado em DevOps, Cloud e SRE.\n\n"
            "Transforme arquitetura + backlog em um documento DEVOPS claro, cobrindo:\n"
            "• Visão geral da estratégia DevOps do projeto;\n"
            "• Componentização (CI/CD, IaC, observabilidade, segurança, ambientes, automações);\n"
            "• Fluxo operacional completo (código → build → testes → deploy → monitoramento → incidentes);\n"
            "• Mapa de funcionalidades DEVOPS (backlog → componentes operacionais);\n"
            "• Instruções iniciais para começar (bootstrap do ambiente DevOps);\n"
            "• Recomendações de milestones para adoção DevOps nas primeiras sprints.\n\n"
            "Retorne em Markdown.\n\n"
            f"ARQUITETURA:\n{architecture}\n\nBACKLOG:\n{backlog}"
        )

        documentation = await call_ai(prompt)
        logger(f"[{task_id}] [{self.name}] Documentação DevOps gerada.")
        return {"devops_documentation": documentation}
