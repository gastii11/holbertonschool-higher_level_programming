def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid template type. Expected a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Invalid attendees type. Expected a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provied, no output files generated.")
        return

    for index, attendees in enumerate(attendees, start=1):
        from string import Formatter
        formatter = Formatter()
        keys_needed = [field_name for _, field_name, _, _ in formatter.parse(template) if field_name]

        complete_data = {}
        for key in keys_needed:
            value = attendees.get(key)
            complete_data[key] = str(value) if value is not None else "N/A"

        try:
            result = template.format(**complete_data)
            file_name = f"output_{index}.txt"
            with open (file_name, "w") as f:
                f.write(result)
            print(f"file '{file_name}' generated seccessfully.")
        except Exeption as e:
            print(f"Error generating file for attendee {index}: {e}")
