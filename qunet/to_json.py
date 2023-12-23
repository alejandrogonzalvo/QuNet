import json
from qunet import Core

def to_json(core: Core):
    """Converts a Core object to a JSON string."""

    core_dict = {}

    core_dict["Core"] = {
        "id": core.id,
        "qubits": core.qubits,
        "gates": core.get_gate_ids(),
    }

    return json.dumps(core_dict, indent=4)