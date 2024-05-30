import requests


def get(_):
    response = requests.models.Response
    response.status_code = 200
    response.json = {"id": "1234"}
    return response


def get_user_id(username):
    resp = get(f"https://api.github.com/users/{username}")
    if resp.status_code == 200:
        return "OK", resp.json.get("id")
    else:
        return "Error", resp.status_code


match get_user_id("john"):
    case ("OK", id):
        print(f"Your id is {id}")
    case ("Error", error_code):
        print(f"Sorry, we got an error: {error_code}")
