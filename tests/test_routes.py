def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client,two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "Red Planet"
    }

def test_planet_no_data(client):
    #Act
    response=client.get("/planets/9999")
    response_body=response.get_json()
    #Assert
    assert response.status_code == 404
    assert response_body == None

def test_get_planets(client,two_saved_planets):
    #Act
    response=client.get("/planets")
    response_body=response.get_json()
    #Assert
    assert response.status_code == 200
    assert len(response_body)== 2

def test_post_planets(client):
    response=client.post("/planets",json={"name":"Jupiter", "description": "green"})
    response_body=response.get_data().decode('utf-8')
    print(response_body)
    #Assert
    assert response.status_code == 201
    assert response_body== "Planet Jupiter successfully created"