# Pipeline CI/CD com GitHub Actions

## Objetivo
Implementar uma pipeline CI/CD utilizando GitHub Actions com análise de segurança CodeQL, testes automatizados e simulação de deploy.

## Tecnologias Utilizadas
- Python 3.11
- GitHub Actions
- Pytest
- Flake8
- CodeQL

## Estrutura do Projeto

Pipeline-Fatec-Idirley/
│
├── .github/
│   ├── workflows/
│   │   └── ci-cd-pipeline.yml
│   └── codeql-config.yml
│
├── tests/
│   └── test_main.py
│
├── main.py
├── requirements.txt
└── README.md

## Etapas da Pipeline
1. Análise de segurança com CodeQL
2. Testes automatizados com Pytest
3. Verificação de qualidade com Flake8
4. Simulação de Deploy

## Testes Realizados

### Teste 1 - Código Seguro
Pipeline executada com sucesso.

### Teste 2 - Vulnerabilidade
Foi inserida uma vulnerabilidade do tipo SQL Injection utilizando concatenação insegura de query SQL.

O GitHub Security identificou a vulnerabilidade através do CodeQL.

### Teste 3 - Correção
A vulnerabilidade foi removida e a pipeline voltou a executar normalmente.

## Resultado Final
Pipeline CI/CD funcionando corretamente com validação automática de segurança, testes e deploy.