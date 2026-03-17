# ============================================================
# engine.py
# This is the BRAIN of the expert system.
# It uses "Forward Chaining" to infer new facts from known facts.
#
# How Forward Chaining works:
#   1. Start with known facts (symptoms entered by user)
#   2. Check every rule: do we know ALL its conditions?
#   3. If YES → add the conclusion as a new fact
#   4. Repeat steps 2-3 until no new facts can be added
#   5. Whatever facts we have at the end = our conclusions
# ============================================================

from rules import RULES


class InferenceEngine:
    def __init__(self):
        # facts_base: a set of all currently known facts
        # A set means no duplicates — same fact won't be added twice
        self.facts_base = set()

        # inference_log: a list of strings recording every step
        # This lets the user SEE the reasoning path
        self.inference_log = []

    # ----------------------------------------------------------
    # add_fact: manually add a fact to the facts base
    # Used to input the user's symptoms at the start
    # ----------------------------------------------------------
    def add_fact(self, fact):
        fact = fact.strip().lower().replace(" ", "_")  # normalize input
        self.facts_base.add(fact)

    # ----------------------------------------------------------
    # run: the main forward chaining loop
    # Keeps going until no new facts can be inferred
    # ----------------------------------------------------------
    def run(self):
        self.inference_log.append("=" * 55)
        self.inference_log.append("   INFERENCE ENGINE STARTED")
        self.inference_log.append("=" * 55)
        self.inference_log.append(f"Initial facts: {sorted(self.facts_base)}\n")

        step = 1          # step counter for the log
        changed = True    # flag: did we add any new fact this round?

        # Keep looping as long as we added something new last round
        while changed:
            changed = False  # assume nothing new this round

            for rule in RULES:
                # Check if this rule's conclusion is already known
                # If we already know it, skip — no need to re-derive it
                if rule.conclusion in self.facts_base:
                    continue

                # Check if ALL conditions of this rule are in facts_base
                all_conditions_met = all(
                    cond in self.facts_base for cond in rule.conditions
                )

                if all_conditions_met:
                    # 🔥 RULE FIRES! Add the conclusion as a new fact
                    self.facts_base.add(rule.conclusion)
                    changed = True  # we added something new → loop again

                    # Log this inference step in a readable way
                    cond_str = " + ".join(rule.conditions)
                    log_entry = (
                        f"  Step {step}: {rule.name} fired\n"
                        f"           BECAUSE: {cond_str}\n"
                        f"           CONCLUDED: {rule.conclusion}"
                    )
                    self.inference_log.append(log_entry)
                    step += 1

        self.inference_log.append("\n" + "=" * 55)
        self.inference_log.append("   INFERENCE COMPLETE")
        self.inference_log.append("=" * 55)

    # ----------------------------------------------------------
    # get_conclusions: return only the inferred facts
    # (removes the original user-input symptoms)
    # ----------------------------------------------------------
    def get_conclusions(self, original_symptoms):
        # Conclusions = everything in facts_base EXCEPT original symptoms
        return self.facts_base - original_symptoms

    # ----------------------------------------------------------
    # print_log: display the full reasoning path
    # ----------------------------------------------------------
    def print_log(self):
        print("\n")
        for line in self.inference_log:
            print(line)

    # ----------------------------------------------------------
    # reset: clear everything so we can run again fresh
    # ----------------------------------------------------------
    def reset(self):
        self.facts_base = set()
        self.inference_log = []
