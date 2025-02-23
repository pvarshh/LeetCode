import re

def update_README():
    difficulty = input("Difficulty: ").strip().capitalize()
    problem_number = input("Number: ").strip()
    problem_name = input("Name: ").strip()
    solution_link = input("Solution: ").strip()
    solved = input("Solved: ").strip().lower() == "y"

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
   
    with open("README.md", "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    update_README()