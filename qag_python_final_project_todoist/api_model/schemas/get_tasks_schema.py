GET_TASKS_SCHEMA = {
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "content": {"type": "string"},
                    "due_string": {"type": ["string", "null"]},
                    "priority": {"type": "integer"},
                },
                "required": ["id", "content"],
                "additionalProperties": True,
            },
        },
        "next_cursor": {"type": ["string", "null"]},
    },
    "required": ["results", "next_cursor"],
    "additionalProperties": False,
}
