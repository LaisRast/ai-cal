import uuid

from icalendar import Event as IcalendarEvent, vDatetime, vText, vCalAddress

from app.models.ai_cal_event import AiCalEvent


def to_ai_cal_event(ical_event: AiCalEvent) -> IcalendarEvent:
    event = IcalendarEvent()

    if ical_event.summary:
        event.add("summary", vText(ical_event.summary))
    if ical_event.dtstart:
        event.add("dtstart", vDatetime(ical_event.dtstart.to_datetime()))
    if ical_event.dtend:
        event.add("dtend", vDatetime(ical_event.dtend.to_datetime()))
    event.add("dtstamp", vDatetime(ical_event.dtstamp.to_datetime()))
    event.add("uid", vText(uuid.uuid4()))
    if ical_event.recurrence_id:
        event.add("recurrence-id", vText(ical_event.recurrence_id))
    if ical_event.sequence is not None:
        event.add("sequence", ical_event.sequence)
    if ical_event.rrule:
        event.add("rrule", ical_event.rrule)
    if ical_event.rdate:
        for date in ical_event.rdate:
            event.add("rdate", vDatetime(date.to_datetime()))
    if ical_event.exdate:
        for date in ical_event.exdate:
            event.add("exdate", vDatetime(date.to_datetime()))
    if ical_event.vevent_class:
        event.add("class", vText(ical_event.vevent_class))
    if ical_event.created:
        event.add("created", vDatetime(ical_event.created.to_datetime()))
    if ical_event.description:
        event.add("description", vText(ical_event.description))
    if ical_event.geo_latitude and ical_event.geo_longitude:
        event.add("geo", f"{ical_event.geo_latitude};{ical_event.geo_longitude}")
    if ical_event.last_modified:
        event.add("last-modified", vDatetime(ical_event.last_modified.to_datetime()))
    if ical_event.location:
        event.add("location", vText(ical_event.location))
    if ical_event.organizer:
        event.add("organizer", vCalAddress(ical_event.organizer))
    if ical_event.priority is not None:
        event.add("priority", ical_event.priority)
    if ical_event.status:
        event.add("status", vText(ical_event.status))
    if ical_event.transp:
        event.add("transp", vText(ical_event.transp))
    if ical_event.url:
        event.add("url", vText(ical_event.url))
    if ical_event.categories:
        for category in ical_event.categories:
            event.add("categories", vText(category))
    if ical_event.attach:
        for attachment in ical_event.attach:
            event.add("attach", vText(attachment))
    if ical_event.attendee:
        for attendee in ical_event.attendee:
            event.add("attendee", vCalAddress(attendee))
    if ical_event.comment:
        for comment in ical_event.comment:
            event.add("comment", vText(comment))
    if ical_event.contact:
        for contact in ical_event.contact:
            event.add("contact", vText(contact))
    if ical_event.rstatus:
        for status in ical_event.rstatus:
            event.add("request-status", vText(status))
    if ical_event.related:
        for related in ical_event.related:
            event.add("related", vText(related))
    if ical_event.resources:
        for resource in ical_event.resources:
            event.add("resources", vText(resource))

    return event
