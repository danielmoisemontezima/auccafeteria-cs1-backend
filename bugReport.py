"""
===============================================================
This file is showing the codebase of the entity "Bug Report"
===============================================================

-> What is the Bug report?

The bug report is a space where the user submits suggestions to the developer
for improving the services

"""

#IMPORTS
from dataclasses import dataclass, field
from datetime import timezone, datetime
from enum import Enum
import uuid

def _now() -> datetime:
    return datetime.now(timezone.utc)

class BugReportStatus(Enum):
    #The status of the program

    PENDING ="pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class BugReport:
    #Where the project lives

    title : str
    description : str= ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: BugReportStatus = field(default=BugReportStatus.PENDING)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)

    #Where all the business rules are implemented

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Bug report title cannot be empty")
        self.title = self.title.strip()

    def newReport(self) -> None:
        #When creating a new bug report

        if self.status != BugReportStatus.PENDING:
            raise ValueError(
                f"Cannot start a report that is '{self.status.value}'. "
                "Only PENDING reports can be started."
            )
        self.status = BugReportStatus.IN_PROGRESS
        self.updated_at = _now()

    def completeReport(self) -> None:
        #When a bug report is completed

        if self.status == BugReportStatus.COMPLETED:
            raise ValueError("Report is already completed.")
        self.status = BugReportStatus.COMPLETED
        self.updated_at = _now()

    def updateReport(self, title: str | None = None, description: str | None = None) -> None:
        #When updating a bug report

        if self.status == BugReportStatus.COMPLETED:
            raise ValueError("Cannot edit a completed report.")
        if title is not None:
            if not title.strip():
                raise ValueError("Report title cannot be empty")
            self.title = title.strip()
        if description is not None:
            self.description = description
        self.updated_at = _now()

    def is_completed(self) -> bool:
        return self.status == BugReportStatus.COMPLETED

    def is_pending(self) -> bool:
        return self.status == BugReportStatus.PENDING

    def is_in_progress(self) -> bool:
        return self.status == BugReportStatus.IN_PROGRESS


