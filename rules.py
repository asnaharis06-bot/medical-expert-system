# ============================================================
# rules.py
# This file defines WHAT a Rule looks like and lists ALL rules
# Think of each rule as: "IF [conditions] THEN [conclusion]"
# ============================================================


# A Rule is a simple object with:
#   - a name        → label so we know which rule fired
#   - conditions    → list of facts that must ALL be true
#   - conclusion    → new fact we can add if conditions match
class Rule:
    def __init__(self, name, conditions, conclusion):
        self.name = name
        self.conditions = conditions  # list of strings
        self.conclusion = conclusion  # single string

    def __repr__(self):
        cond_str = " AND ".join(self.conditions)
        return f"[{self.name}] IF {cond_str} THEN {self.conclusion}"


# ============================================================
# THE RULES BASE
# This is the expert knowledge — written by a domain expert.
# We use a medical diagnosis example (easy to understand).
# ============================================================

RULES = [
    # ---------- BASIC DISEASE DETECTION ----------

    Rule(
        name="Rule-1",
        conditions=["fever", "cough"],
        conclusion="possible_flu"
    ),

    Rule(
        name="Rule-2",
        conditions=["fever", "sore_throat"],
        conclusion="possible_cold"
    ),

    Rule(
        name="Rule-3",
        conditions=["rash", "fever"],
        conclusion="possible_measles"
    ),

    Rule(
        name="Rule-4",
        conditions=["cough", "shortness_of_breath"],
        conclusion="possible_asthma"
    ),

    Rule(
        name="Rule-5",
        conditions=["headache", "fever"],
        conclusion="possible_infection"
    ),

    # ---------- CHAINED RULES (multi-step inference) ----------
    # These rules use conclusions from earlier rules as conditions!
    # This is what makes it "chain" — step 1 result feeds into step 2.

    Rule(
        name="Rule-6",
        conditions=["possible_flu", "body_aches"],
        conclusion="severe_flu"
    ),

    Rule(
        name="Rule-7",
        conditions=["possible_flu", "vomiting"],
        conclusion="stomach_flu"
    ),

    Rule(
        name="Rule-8",
        conditions=["possible_cold", "runny_nose"],
        conclusion="common_cold_confirmed"
    ),

    Rule(
        name="Rule-9",
        conditions=["possible_measles", "red_eyes"],
        conclusion="measles_confirmed"
    ),

    Rule(
        name="Rule-10",
        conditions=["possible_infection", "stiff_neck"],
        conclusion="possible_meningitis"
    ),

    # ---------- RECOMMENDATIONS (final stage of chaining) ----------
    # These fire AFTER diseases are identified → give advice

    Rule(
        name="Rule-11",
        conditions=["severe_flu"],
        conclusion="recommend_antiviral_medication"
    ),

    Rule(
        name="Rule-12",
        conditions=["common_cold_confirmed"],
        conclusion="recommend_rest_and_fluids"
    ),

    Rule(
        name="Rule-13",
        conditions=["stomach_flu"],
        conclusion="recommend_hydration_and_rest"
    ),

    Rule(
        name="Rule-14",
        conditions=["measles_confirmed"],
        conclusion="recommend_see_doctor_immediately"
    ),

    Rule(
        name="Rule-15",
        conditions=["possible_meningitis"],
        conclusion="recommend_emergency_care"
    ),
]
