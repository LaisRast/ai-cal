import os
from datetime import datetime

from icalendar.cal import Calendar
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.models.ai_cal_event import AiCalEvent
from app.models.prase_request import ParseRequest
from app.models.prase_respones import ParseResponse
from app.mapping.mapping import to_ai_cal_event


def create_structured_extractor() -> callable:
    system_message: str = (
        "Extract event information in iCalendar format compliant with RFC 5545 specifications. "
        "Ensure that all email addresses, when detected, for ORGANIZER and ATTENDEE fields are formatted as mailto: URIs. "
        "Only fill fields that you get from the prompt"
        f"Today date and time is {datetime.now().isoformat()}."
    )
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
        [("system", system_message), ("human", "{input}")]
    )
    model = os.environ.get("MODEL")
    llm: ChatOpenAI = ChatOpenAI(model=model, temperature=0)
    structured_llm = llm.with_structured_output(AiCalEvent)
    return prompt | structured_llm


def parse_using_ai(parse_request: ParseRequest) -> ParseResponse:
    structured_extractor = create_structured_extractor()
    ai_cal_event: AiCalEvent = structured_extractor.invoke(
        {"input": parse_request.prompt.strip()}
    )

    cal = Calendar()
    cal.add("prodid", "-//AiCal//CalendarApp//EN")
    cal.add("version", "2.0")
    cal.add_component(to_ai_cal_event(ai_cal_event))
    ics = cal.to_ical().decode("utf-8").replace("\r\n", "\n").strip()

    return ParseResponse(ics=ics)
