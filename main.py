# ============================================================
# main.py
# This is where the program STARTS.
# It handles all user interaction:
#   - Show available symptoms
#   - Accept user input
#   - Run the inference engine
#   - Display results and reasoning log
# ============================================================

from engine import InferenceEngine
from rules import RULES


# ============================================================
# HELPER: collect all valid symptom inputs from the rules
# We only show "base" symptoms — not inferred conclusions
# ============================================================
def get_all_symptoms():
    # Gather every conclusion that any rule can produce
    all_conclusions = {rule.conclusion for rule in RULES}

    # Gather every condition used across all rules
    all_conditions = set()
    for rule in RULES:
        for cond in rule.conditions:
            all_conditions.add(cond)

    # Base symptoms = conditions that are NOT conclusions of any rule
    # These are the "raw" facts only a user can provide
    base_symptoms = all_conditions - all_conclusions
    return sorted(base_symptoms)


# ============================================================
# HELPER: pretty-print conclusions in a human-readable way
# ============================================================
def format_conclusion(fact):
    # Replace underscores with spaces, capitalize each word
    return fact.replace("_", " ").title()


# ============================================================
# MAIN PROGRAM
# ============================================================
def main():
    print("\n" + "=" * 55)
    print("   🏥  MEDICAL EXPERT SYSTEM  🏥")
    print("   Rule-Based Diagnosis with Forward Chaining")
    print("=" * 55)
    print("\nNOTE: This is an educational demo, not real medical advice.\n")

    base_symptoms = get_all_symptoms()

    # Show all available symptoms to the user
    print("Available symptoms you can enter:")
    print("-" * 40)
    for i, symptom in enumerate(base_symptoms, start=1):
        print(f"  {i:2}. {symptom.replace('_', ' ')}")
    print("-" * 40)

    # Collect user symptoms
    print("\nEnter your symptoms one by one.")
    print("Type each symptom and press ENTER.")
    print("When done, just press ENTER on an empty line.\n")

    engine = InferenceEngine()
    entered_symptoms = set()

    while True:
        user_input = input("Enter symptom (or press ENTER to finish): ").strip()

        if user_input == "":
            if len(entered_symptoms) == 0:
                print("⚠  You haven't entered any symptoms yet. Please enter at least one.")
                continue
            else:
                break  # done entering symptoms

        # Normalize: lowercase and replace spaces with underscores
        normalized = user_input.lower().replace(" ", "_")

        # Check if it's a valid symptom
        if normalized in base_symptoms:
            if normalized in entered_symptoms:
                print(f"   ('{user_input}' already added)")
            else:
                engine.add_fact(normalized)
                entered_symptoms.add(normalized)
                print(f"   ✓ Added: {normalized.replace('_', ' ')}")
        else:
            print(f"   ✗ Unknown symptom: '{user_input}'")
            print(f"     Please choose from the list above.")

    # --------------------------------------------------------
    # Run the inference engine
    # --------------------------------------------------------
    print("\n⏳ Running inference engine...\n")
    engine.run()

    # --------------------------------------------------------
    # Show the inference log (the reasoning path)
    # --------------------------------------------------------
    engine.print_log()

    # --------------------------------------------------------
    # Show final conclusions
    # --------------------------------------------------------
    conclusions = engine.get_conclusions(entered_symptoms)

    print("\n" + "=" * 55)
    print("   DIAGNOSIS & RECOMMENDATIONS")
    print("=" * 55)

    if not conclusions:
        print("\n  No conclusions could be drawn from these symptoms.")
        print("  Try adding more symptoms.\n")
    else:
        # Separate diagnoses from recommendations
        diagnoses = [c for c in sorted(conclusions) if c.startswith("possible_")
                     or c.startswith("severe_") or c.endswith("_confirmed")
                     or c.endswith("_flu")]
        recommendations = [c for c in sorted(conclusions) if c.startswith("recommend_")]
        other = [c for c in sorted(conclusions) if c not in diagnoses and c not in recommendations]

        if diagnoses:
            print("\n  🔍 Possible Diagnoses:")
            for d in diagnoses:
                print(f"     • {format_conclusion(d)}")

        if other:
            print("\n  🔍 Other Findings:")
            for o in other:
                print(f"     • {format_conclusion(o)}")

        if recommendations:
            print("\n  💊 Recommendations:")
            for r in recommendations:
                print(f"     • {format_conclusion(r)}")

    print("\n" + "=" * 55)

    # --------------------------------------------------------
    # Ask if user wants to run again
    # --------------------------------------------------------
    again = input("\nWould you like to run again? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        engine.reset()
        main()
    else:
        print("\nThank you for using the Medical Expert System. Goodbye!\n")


# ============================================================
# Entry point — only runs if we execute this file directly
# ============================================================
if __name__ == "__main__":
    main()
