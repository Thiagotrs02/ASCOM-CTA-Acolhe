from rapidfuzz import process, fuzz

def test_busca_antiduplicacao_fonetica():
    nome_buscado = "Joao da Silva"
    banco_dados = ["João da Silva Santos", "João da Silva Junior", "Maria Oliveira"]
    
    resultados = process.extract(nome_buscado, banco_dados, scorer=fuzz.WRatio, limit=2)
    
    # Verifica se o primeiro resultado tem mais de 80% de similaridade
    assert resultados[0][0] == "João da Silva Santos"
    assert resultados[0][1] >= 80

def test_busca_sem_correspondencia():
    nome_buscado = "Carlos Eduardo"
    banco_dados = ["João da Silva Santos", "Maria Oliveira"]
    
    resultados = process.extract(nome_buscado, banco_dados, scorer=fuzz.WRatio, limit=1)
    assert resultados[0][1] < 50