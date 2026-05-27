import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from core.parser.parser import RenPyParser
from core.parser.transformer import RenPyTransformer
from core.analysis.state import StateAnalyzer

parser = RenPyParser()
tree = parser.parse_file('tests/samples/flag_conflict.rpy')
script = RenPyTransformer().transform(tree)

analyzer = StateAnalyzer()
results = analyzer.analyze(script)

import json
print(json.dumps(results, indent=2, ensure_ascii=False))

