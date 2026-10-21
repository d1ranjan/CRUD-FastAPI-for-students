def sample_student(email="alex@example.com"):
    return {
        "name": "Alex Student",
        "date_of_birth": "2005-04-12",
        "email": email,
        "phone": "9876543210",
        "course": "Computer Science",
        "address": "Kolkata"
    }


def test_create_and_get_student(client):
    response = client.post("/students", json=sample_student())
    assert response.status_code == 201
    student = response.json()
    assert student["id"] == 1
    assert student["name"] == "Alex Student"

    fetched = client.get("/students/1")
    assert fetched.status_code == 200
    assert fetched.json()["email"] == "alex@example.com"


def test_list_and_filter_students(client):
    client.post("/students", json=sample_student())
    client.post("/students", json=sample_student("sam@example.com"))
    assert len(client.get("/students").json()) == 2
    assert len(client.get("/students", params={"name": "Alex"}).json()) == 2
    assert len(client.get("/students", params={"course": "Science"}).json()) == 2


def test_update_student(client):
    client.post("/students", json=sample_student())
    response = client.patch("/students/1", json={"course": "AI & ML"})
    assert response.status_code == 200
    assert response.json()["course"] == "AI & ML"


def test_delete_student(client):
    client.post("/students", json=sample_student())
    response = client.delete("/students/1")
    assert response.status_code == 204
    assert client.get("/students/1").status_code == 404


def test_validation_duplicate_and_missing_records(client):
    assert client.post("/students", json={"name": ""}).status_code == 422
    client.post("/students", json=sample_student())
    assert client.post("/students", json=sample_student()).status_code == 409
    assert client.get("/students/999").status_code == 404
