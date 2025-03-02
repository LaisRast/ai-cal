from datetime import datetime, timezone
from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class AiCalDateTime(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def to_datetime(self) -> datetime:
        return datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
        )


class AiCalEvent(BaseModel):
    """Event information in iCalendar format compliant with RFC 5545 specifications."""

    summary: Optional[str] = Field(
        ..., description="Short summary or title of the event"
    )
    dtstart: Optional[AiCalDateTime] = Field(
        ..., description="Start date and time of the event in UTC"
    )
    dtend: Optional[AiCalDateTime] = Field(
        ..., description="End date and time of the event in UTC"
    )
    dtstamp: AiCalDateTime = Field(
        ..., description="Timestamp of when the event was created, in UTC"
    )
    recurrence_id: Optional[str] = Field(
        ..., description="Identifier for a specific instance of a recurring event"
    )
    sequence: Optional[int] = Field(
        ..., description="Revision sequence number of the event"
    )
    rrule: Optional[Dict[str, str]] = Field(
        ..., description="Recurrence rule as a dictionary (e.g., {'freq': 'DAILY'})"
    )
    rdate: Optional[List[AiCalDateTime]] = Field(
        ..., description="List of additional recurrence dates in UTC"
    )
    exdate: Optional[List[AiCalDateTime]] = Field(
        ..., description="List of exception dates in UTC"
    )
    vevent_class: Optional[str] = Field(
        ...,
        description="Classification of the event (e.g., PUBLIC, PRIVATE, CONFIDENTIAL)",
    )
    created: Optional[AiCalDateTime] = Field(
        ..., description="Date and time when the event was created, in UTC"
    )
    description: Optional[str] = Field(
        ..., description="Detailed description of the event"
    )
    geo_latitude: Optional[float] = Field(
        ..., description="Latitude geographic position of the event"
    )
    geo_longitude: Optional[float] = Field(
        ..., description="Longitude geographic position of the event"
    )
    last_modified: Optional[AiCalDateTime] = Field(
        ..., description="Date and time when the event was last modified, in UTC"
    )
    location: Optional[str] = Field(..., description="Physical location of the event")
    organizer: Optional[str] = Field(
        ..., description="Email address of the event organizer in mailto: format"
    )
    priority: Optional[int] = Field(
        ...,
        description="Priority of the event (0-9, where 0 is undefined and 1 is highest)",
    )
    status: Optional[str] = Field(
        ..., description="Status of the event (e.g., TENTATIVE, CONFIRMED, CANCELLED)"
    )
    transp: Optional[str] = Field(
        ..., description="Transparency of the event (OPAQUE or TRANSPARENT)"
    )
    url: Optional[str] = Field(
        ..., description="URL associated with the event for more information"
    )
    categories: Optional[List[str]] = Field(
        ..., description="List of categories or tags for the event"
    )
    attach: Optional[List[str]] = Field(
        ..., description="List of URIs pointing to attachments related to the event"
    )
    attendee: Optional[List[str]] = Field(
        ..., description="List of email addresses of attendees in mailto: format"
    )
    comment: Optional[List[str]] = Field(
        ..., description="List of comments about the event"
    )
    contact: Optional[List[str]] = Field(
        ..., description="List of contact information for the event"
    )
    rstatus: Optional[List[str]] = Field(
        ..., description="List of request status codes and messages"
    )
    related: Optional[List[str]] = Field(
        ..., description="List of related event identifiers"
    )
    resources: Optional[List[str]] = Field(
        ..., description="List of resources needed for the event"
    )
