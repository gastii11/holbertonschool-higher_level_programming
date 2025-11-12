def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: template must be a string, not {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i in range(len(attendees)):
        person = attendees[i]
        content = template

        if "name" in person and person["name"] is not None:
            content = content.replace("{name}", person["name"])
        else:
            content = content.replace("{name}", "N/A")

        if "event_title" in person and person["event_title"] is not None:
            content = content.replace("{event_title}", person["event_title"])
        else:
            content = content.replace("{event_title}", "N/A")

        if "event_date" in person and person["event_date"] is not None:
            content = content.replace("{event_date}", person["event_date"])
        else:
            content = content.replace("{event_date}", "N/A")

        if "event_location" in person and person["event_location"] is not None:
            content = content.replace("{event_location}", person["event_location"])
        else:
            content = content.replace("{event_location}", "N/A")

        filename = "output_" + str(i + 1) + ".txt"
        file = open(filename, "w")
        file.write(content)
        file.close()
        print("Created:", filename)

    print("Done! Created", len(attendees), "files.")
