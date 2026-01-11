# Rule-Based Expert System

A Python implementation of a rule-based expert system with forward chaining inference.

## Features

- **Rule Engine**: If-then rules with conditions and conclusions
- **Facts Base**: Dynamic knowledge base for storing known facts
- **Forward Chaining**: Automatic inference from known facts to conclusions
- **Multi-step Inference**: Rules can chain together for complex reasoning
- **Inference Logging**: Complete reasoning path transparency
- **Interactive Interface**: User-friendly symptom input and diagnosis output

## Usage

Run the expert system:

```bash
python 01_task_rule_based_expert_system.py
```

Enter symptoms when prompted (one per line, empty line to finish):

```
fever
cough
fatigue
```

The system will perform inference and show:
- Initial symptoms
- Final conclusions/diagnosis
- Complete reasoning path

## Example Output

```
Initial symptoms: ['fever', 'cough', 'fatigue', 'chest_pain']

Final diagnosis/conclusions: {'pneumonia_risk', 'flu'}

=== REASONING PATH ===

Step 1: Rule 'Flu Diagnosis' fired
  Conditions met: {'fever', 'cough', 'fatigue'}
  New facts inferred: {'flu'}
  Total facts now: {'fever', 'flu', 'cough', 'chest_pain', 'fatigue'}

Step 2: Rule 'Pneumonia Risk' fired
  Conditions met: {'chest_pain', 'flu'}
  New facts inferred: {'pneumonia_risk'}
  Total facts now: {'fever', 'pneumonia_risk', 'flu', 'cough', 'chest_pain', 'fatigue'}
```

## Architecture

- `Rule` class: Represents individual if-then rules
- `ExpertSystem` class: Manages facts, rules, and inference process
- Forward chaining algorithm: Applies rules iteratively until no new conclusions

## Requirements

- Python 3.x

## License

MIT License