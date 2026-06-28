from dataclasses import dataclass, field
from datetime import datetime, timezone

def _now() -> datetime:
    return datetime.now(timezone.utc)

@dataclass
class Customer:
    id:int
    first_name:str
    last_name:str
    email:str
    sign_at:datetime = field(default_factory=_now)

    def __post_init__(self) -> None:
        if not self.first_name.strip() or not self.last_name.strip() or not self.email.strip():
            raise ValueError("cannot be empty !!")
         
        self.first_name=self.first_name.strip()
        self.last_name=self.last_name.strip()
        self.email=self.email.strip()
        
