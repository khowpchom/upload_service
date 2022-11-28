# from fastapi.testclient import TestClient
# from tests.endpoints import API_V1_STR


# def test_create_item(client: TestClient) -> None:
#     data = {"title": "Foo", "description": "Fighters"}
#     response = client.post(
#         f"{API_V1_STR}/upload/", files=data,
#     )
#     assert response.status_code == 200
#     content = response.json()
#     assert content["title"] == data["title"]
#     assert content["description"] == data["description"]
#     assert "id" in content
#     assert "owner_id" in content