import re

def update_total():
    """
    Updates the total.md file interactively based on user input.
    Tracks the number of solved problems in each section and updates the header.
    """
    # Ask for user input
    difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").strip().capitalize()
    problem_number = input("Enter the problem number (e.g., 1, 21): ").strip()
    problem_name = input("Enter the problem name (e.g., Two Sum): ").strip()
    solution_link = input("Enter the link to your solution (e.g., solutions/easy/two-sum.md): ").strip()
    solved = input("Is the problem solved? (y/n): ").strip().lower() == "y"

    # Define the checkbox status
    checkbox = "[X]" if solved else "[ ]"

    # Format the new problem entry
    new_entry = f"{checkbox} [{problem_number}. {problem_name}]({solution_link})"

    # Read the current total.md content
    with open("total.md", "r") as file:
        content = file.readlines()

    # Find the section for the given difficulty
    section_start = None
    section_end = None
    for i, line in enumerate(content):
        if line.startswith(f"### {difficulty}"):
            section_start = i
        elif section_start is not None and line.startswith("### "):
            section_end = i
            break

    if section_start is None or section_end is None:
        raise ValueError(f"Could not find the '{difficulty}' section in total.md.")

    # Check if the problem already exists in the section
    problem_exists = False
    for i in range(section_start + 1, section_end):
        if f"[{problem_number}. {problem_name}]" in content[i]:
            problem_exists = True
            # Update the checkbox if the problem is being marked as solved
            if solved:
                content[i] = re.sub(r"\[ \]", "[x]", content[i])
            break

    # If the problem doesn't exist, add it to the section
    if not problem_exists:
        content.insert(section_end - 1, f"- {new_entry}\n")

    # Sort the problems in the section by problem number
    section_content = content[section_start + 1:section_end]
    section_content_sorted = sorted(
        section_content,
        key=lambda x: int(re.search(r"\[(\d+)\.", x).group(1)) if re.search(r"\[(\d+)\.", x) else 0
    )
    content[section_start + 1:section_end] = section_content_sorted

    # Count the number of solved problems in the section
    solved_count = 0
    total_count = 0
    for line in content[section_start + 1:section_end]:
        if re.search(r"\[x\]", line):
            solved_count += 1
        if re.search(r"\[\d+\.", line):
            total_count += 1

    # Update the section header with the solved count
    header = content[section_start]
    header_updated = re.sub(r"\(\d+/\d+\)", f"({solved_count}/{total_count})", header)
    if header_updated == header:  # If no count was present, add it
        header_updated = header.strip() + f" ({solved_count}/{total_count})\n"
    content[section_start] = header_updated

    # Write the updated content back to total.md
    with open("total.md", "w") as file:
        file.writelines(content)

    print(f"total.md updated successfully for problem {problem_number}. {problem_name}!")
    print(f"Solved {solved_count}/{total_count} problems in the {difficulty} section.")


# Run the function interactively
if __name__ == "__main__":
    update_total()