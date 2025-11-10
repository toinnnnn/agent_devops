import asyncio
from app.agents.devops_architecture_agent import DevOpsArchitectureAgent

async def main():
    agent = DevOpsArchitectureAgent()

    payload = {
        "devops_backlog": """
        - Criar pipeline de CI com testes automatizados
        - Configurar CD com deploy automatizado em staging e produção
        - Implementar infraestrutura como código com Terraform
        - Adicionar monitoramento com Prometheus e Grafana
        - Configurar logs centralizados com ELK
        - Implementar segurança com scanners SAST e gerenciamento de secrets
        """
    }

    def logger(msg):
        print(msg)

    print("\n🚀 Executando DevOpsArchitectureAgent...\n")
    result = await agent.run(payload, logger, "demo-task")
    print("\n✅ Resultado final:\n")
    print(result["devops_architecture"])

if __name__ == "__main__":
    asyncio.run(main())
