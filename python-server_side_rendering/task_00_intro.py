#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") if attendee.get("name") is not None else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") is not None else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") is not None else "N/A"

        content = template.replace("{name}", name) \
                          .replace("{event_title}", event_title) \
                          .replace("{event_date}", event_date) \
                          .replace("{event_location}", event_location)

        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(content)
