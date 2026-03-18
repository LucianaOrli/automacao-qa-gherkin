#!/bin/bash
echo "Iniciando Testes de QA para Luciana..."
echo "--------------------------------------"
pytest test_profissional.py --html=relatorio_qa.html --self-contained-html -v
echo "--------------------------------------"
echo "CONCLUÍDO! O relatório foi gerado em: relatorio_qa.html"
