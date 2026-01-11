"""
Rule-Based Expert System

This is a simple rule-based expert system that implements:
- A rule engine with if-then rules
- A facts base to store known information
- Forward chaining inference algorithm
- Multi-step rule chaining
- Inference logging for transparency

The system uses forward chaining: starting from known facts (symptoms),
it applies rules to infer new conclusions, which can then trigger more rules.

Example Usage:
    python 01_task_rule_based_expert_system.py

Then enter symptoms like:
    fever
    cough
    fatigue

The system will infer conclusions and show the reasoning path.
"""

class Rule:
    """Represents an if-then rule with conditions and conclusions."""

    def __init__(self, name, conditions, conclusions):
        self.name = name
        self.conditions = set(conditions)  # Facts that must be true
        self.conclusions = set(conclusions)  # Facts that become true
        self.fired = False  # Track if rule has been fired

    def can_fire(self, facts):
        """Check if all conditions are satisfied by current facts."""
        return self.conditions.issubset(facts) and not self.fired

    def fire(self, facts):
        """Apply the rule: add conclusions to facts and mark as fired."""
        facts.update(self.conclusions)
        self.fired = True
        return self.conclusions

    def __str__(self):
        return f"Rule '{self.name}': IF {self.conditions} THEN {self.conclusions}"


class ExpertSystem:
    """Rule-based expert system with forward chaining inference."""

    def __init__(self):
        self.facts = set()  # Current known facts
        self.rules = []  # List of rules
        self.inference_log = []  # Log of inference steps

    def add_rule(self, rule):
        """Add a rule to the system."""
        self.rules.append(rule)

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def add_facts(self, facts_list):
        """Add multiple facts to the knowledge base."""
        self.facts.update(facts_list)

    def reset(self):
        """Reset the system for a new inference session."""
        for rule in self.rules:
            rule.fired = False
        self.inference_log = []

    def forward_chain(self):
        """Perform forward chaining inference."""
        self.reset()
        changed = True

        while changed:
            changed = False

            for rule in self.rules:
                if rule.can_fire(self.facts):
                    new_facts = rule.fire(self.facts)
                    self.inference_log.append({
                        'rule': rule.name,
                        'conditions': rule.conditions,
                        'conclusions': new_facts,
                        'facts_after': self.facts.copy()
                    })
                    changed = True

        return self.facts.copy()

    def get_reasoning_path(self):
        """Return the logged inference steps."""
        return self.inference_log

    def print_reasoning_path(self):
        """Print the reasoning path in a readable format."""
        if not self.inference_log:
            print("No inference steps recorded.")
            return

        print("\n=== REASONING PATH ===")
        for i, step in enumerate(self.inference_log, 1):
            print(f"\nStep {i}: Rule '{step['rule']}' fired")
            print(f"  Conditions met: {step['conditions']}")
            print(f"  New facts inferred: {step['conclusions']}")
            print(f"  Total facts now: {step['facts_after']}")


def create_medical_diagnosis_system():
    """Create a sample medical diagnosis expert system."""
    system = ExpertSystem()

    # Define rules for medical diagnosis
    system.add_rule(Rule(
        "Flu Diagnosis",
        ["fever", "cough", "fatigue"],
        ["flu"]
    ))

    system.add_rule(Rule(
        "Cold Diagnosis",
        ["runny_nose", "sore_throat", "cough"],
        ["cold"]
    ))

    system.add_rule(Rule(
        "Pneumonia Risk",
        ["flu", "chest_pain"],
        ["pneumonia_risk"]
    ))

    system.add_rule(Rule(
        "Severe Symptoms",
        ["high_fever", "difficulty_breathing"],
        ["severe_symptoms"]
    ))

    system.add_rule(Rule(
        "Emergency Case",
        ["severe_symptoms", "chest_pain"],
        ["emergency"]
    ))

    return system


def main():
    """Main function to run the expert system."""
    print("=== Rule-Based Expert System ===")
    print("Medical Diagnosis Example\n")

    # Create the expert system
    expert_system = create_medical_diagnosis_system()

    # Get user symptoms
    print("Please enter your symptoms (one per line, empty line to finish):")
    symptoms = []
    while True:
        symptom = input("> ").strip().lower()
        if not symptom:
            break
        symptoms.append(symptom)

    if not symptoms:
        print("No symptoms entered. Exiting.")
        return

    print(f"\nInitial symptoms: {symptoms}")

    # Add user symptoms as initial facts
    expert_system.add_facts(symptoms)

    # Perform inference
    print("\nPerforming inference...")
    final_facts = expert_system.forward_chain()

    # Display results
    print(f"\nFinal diagnosis/conclusions: {final_facts - set(symptoms)}")

    # Show reasoning path
    expert_system.print_reasoning_path()

    print("\n=== Inference Complete ===")


if __name__ == "__main__":
    main()