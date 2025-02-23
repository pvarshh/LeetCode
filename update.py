import re

def update_README():
    difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").strip().capitalize()
    problem_number = input("Enter the problem number (e.g., 1, 21): ").strip()
    problem_name = input("Enter the problem name (e.g., Two Sum): ").strip()
    solution_link = input("Enter the link to your solution (e.g., solutions/easy/two-sum.md): ").strip()
    solved = input("Is the problem solved? (y/n): ").strip().lower() == "y"

    checkbox = "[X]" if solved else "[ ]"
   
    new_entry = f"- {checkbox} [{problem_number}. {problem_name}]({solution_link})"
   
    with open("README.md", "r") as file:
        content = file.readlines()

    section_start = None
    section_end = None
    for i, line in enumerate(content):
        if line.startswith(f"### {difficulty}"):
            section_start = i
        elif section_start is not None and line.startswith("### "):
            section_end = i
            break

    if section_start is None or section_end is None:
        raise ValueError(f"Could not find the '{difficulty}' section in README.md.")
   
    problem_exists = False
    for i in range(section_start + 1, section_end):
        if f"[{problem_number}. {problem_name}]" in content[i]:
            problem_exists = True           
            if solved:
                content[i] = re.sub(r"\[ \]", "[X]", content[i])
            break
   
    if not problem_exists:
        content.insert(section_end - 1, f"{new_entry}\n")

    section_content = content[section_start + 1:section_end]
    section_content_sorted = sorted(
        section_content,
        key=lambda x: int(re.search(r"\[(\d+)\.", x).group(1)) if re.search(r"\[(\d+)\.", x) else 0
    )
    content[section_start + 1:section_end] = section_content_sorted
   
    solved_count = 0
    total_count = 0
    for line in content[section_start + 1:section_end]:
        if re.search(r"\[X\]", line, re.IGNORECASE):
            solved_count += 1
        if re.search(r"\[\d+\.", line):
            total_count += 1
   
    header = content[section_start]
    header_updated = re.sub(r"\(\d+/\d+\)", f"({solved_count}/{total_count})", header)
    if header_updated == header: 
        header_updated = header.strip() + f" ({solved_count}/{total_count})\n"
    content[section_start] = header_updated
   
    total_solved = 0
    total_problems = 0
    for i, line in enumerate(content):
        if line.startswith("### "):
            match = re.search(r"\((\d+)/(\d+)\)", line)
            if match:
                total_solved += int(match.group(1))
                total_problems += int(match.group(2))

    total_solved_header = "## Total Solved\n"
    total_solved_content = f"**Total Solved:** {total_solved}/{total_problems}\n\n"
    total_solved_index = None
   
    main_header_index = None
    for i, line in enumerate(content):
        if line.startswith("# LeetCode Solutions"):
            main_header_index = i
            break

    if main_header_index is not None:       
        total_solved_index = main_header_index + 2
        if not content[total_solved_index].startswith("## Total Solved"):
            content.insert(total_solved_index, total_solved_content)
            content.insert(total_solved_index, total_solved_header)
        else:
            content[total_solved_index] = total_solved_header
            content[total_solved_index + 1] = total_solved_content
   
    with open("README.md", "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    update_README()