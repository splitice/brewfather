from typing import Optional

class custom_stream_data:
    name: str
    temp: Optional[float]
    temp_unit: Optional[str]
    gravity: Optional[float]

    def __init__(self, name: str) -> None:
        self.name = name
        self.gravity = None
