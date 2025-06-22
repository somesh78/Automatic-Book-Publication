def manual_review(initial_text: str) -> str:
    print("=== AI Output Preview ===")
    print(initial_text[:500] + "\n…")
    print("\nProvide edits (empty line to finish):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    return "\n".join(lines) or initial_text
