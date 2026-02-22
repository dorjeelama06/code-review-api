def parse_diff(raw_diff: str) -> list[dict]:
    file_blocks = raw_diff.split("diff --git")[1:]
    results = []
    for files in file_blocks:
        file_data = {
            "filename": "",
            "+": [],
            "-": [],
            "context": ""
        }
        lines = files.split("\n")
        filename = lines[0].split(" ")[1][2:]
        file_data["filename"] = filename
        for line in lines:
            if line.startswith("+ "):
                file_data["+"].append(line[2:])
            elif line.startswith("- "):
                file_data["-"].append(line[2:])
            elif line.strip().startswith("def ") or line.strip().startswith("class "):
                file_data["context"] = line.strip()
        results.append(file_data)
    print(results)
    return results