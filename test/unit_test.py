import pytest
import requests


def test_bot_exists():
    url = "https://api.botpress.cloud/v1/admin/bots/cb04040a-afe7-4168-8dfb-fa82b8066571"

    headers = {
        "x-bot-id": "cb04040a-afe7-4168-8dfb-fa82b8066571",
        "Authorization": "Bearer bp_pat_wkasDKlXXSVS5qycHaNlOzQSpcsDz5FVEAS5",
    }

    response = requests.get(url, headers=headers)

    # Verifica se o bot existe
    assert response.status_code == 200, f"A solicitação falhou com o código de status {response.status_code}"

    # Verifica se o ID do bot existe
    assert "cb04040a-afe7-4168-8dfb-fa82b8066571" in response.text, "Bot nao existe, ou autenticaçao falhou'"

    # Se todas as verificações passarem, imprima a resposta
    print("Requisição bem-sucedida!")

