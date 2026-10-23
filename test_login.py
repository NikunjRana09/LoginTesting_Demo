def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"


def test_valid_login():
    assert login("admin", "admin123") == "Login successful"


def test_invalid_login():
    assert login("admin", "wrong123") == "Invalid credentials"


if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    print("All login tests passed!")

print("Login test execution completed.")