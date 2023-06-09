
# Example of what nodes look like under the hood
# They look like dictionaries that point to other dictionaries
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None

            }
        }
    }
}

print(head["next"]["value"])
