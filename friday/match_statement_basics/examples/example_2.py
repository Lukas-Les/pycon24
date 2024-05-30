success_response = {
    "data": {
        "hero": {
            "name": "R2-D2",
            "heroFriends": [
                {
                    "id": "1000",
                    "name": "Luke Skywalker"
                },
                {
                    "id": "1002",
                    "name": None
                },
                {
                    "id": "1003",
                    "name": "Leia Organa"
                }
            ]
        }
    }
}

with_none_response = {
    "data": {
        "hero": {
            "name": "R2-D2",
            "heroFriends": [
                {
                    "id": "1000",
                    "name": "Luke Skywalker"
                },
                None,
                {
                    "id": "1002",
                    "name": None
                },
                {
                    "id": "1003",
                    "name": "Leia Organa"
                }
            ]
        }
    }
}

error_response = {
    "errors": [
        {
            "message": "Name for character with ID 1002 could not be fetched",
            "locations": [{"line": 6, "column": 7}],
            "patch": ["hero", "heroFriends", 1, "name"]
        }
    ],
}


def do_api_call():
    return success_response
    # return with_none_response
    # return error_response


match do_api_call():
    case {"errors": errors}:
        for error in errors:
            print(error)
    case {"data": {"hero": {"heroFriends": friends}}} if None not in friends:
        for friend in friends:
            print(friend)
    case {"data": {"hero": {"name": name}}}:
        print(f"{name} has a None friend :/")

a = 1
