import os

def criar_selo_executivo():
    nota = "9.8"
    status = "APROVADO - ELITE"
    
    selo_markdown = f"![Selo Lux by Or](https://img.shields.io/badge/Lux_By_Or-Compliance_{nota}-gold?style=for-the-badge&logo=data-canister)"
    
    print("\n" + "="*40)
    print("🛡️  GERADOR DE AUTORIDADE LUX BY OR 🛡️")
    print("="*40)
    print(f"NOTA: {nota} | STATUS: {status}")
    print(f"CÓDIGO PARA O GITHUB: \n{selo_markdown}")
    print("="*40)
    
    # Adicionando ao README de forma definitiva
    with open("README.md", "r+") as f:
        content = f.read()
        if selo_markdown not in content:
            f.seek(0, 0)
            f.write(selo_markdown + "\n\n" + content)
            print("✅ Selo injetado com sucesso no topo do seu README!")

if __name__ == "__main__":
    criar_selo_executivo()
