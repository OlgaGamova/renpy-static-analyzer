import json
from pathlib import Path


class GraphVisualizer:
    """
    Интерактивная визуализация графа сюжета через vis-network.
    Не требует дополнительных Python-зависимостей.
    """

    def render(self, graph: dict[str, set[str]], output_file: str = "graph.html"):
        nodes = []
        edges = []

        for label in graph.keys():
            color = "#97C2FC"

            # Стартовый узел
            if label == "start":
                color = "#7BE141"

            # Мёртвые концы (без исходящих рёбер)
            if not graph[label]:
                color = "#FB7E81"

            nodes.append({
                "id": label,
                "label": label,
                "color": color
            })

        for src, targets in graph.items():
            for tgt in targets:
                edges.append({"from": src, "to": tgt})

        nodes_json = json.dumps(nodes)
        edges_json = json.dumps(edges)

        html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Ren'Py Story Graph</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body {{ font-family: Arial; background: #f8f9fa; }}
  #network {{ width: 100%; height: 700px; border: 1px solid #ddd; }}
</style>
</head>
<body>

<h2>Ren'Py Story Graph</h2>
<div id="network"></div>

<script>
  var nodes = new vis.DataSet({nodes_json});
  var edges = new vis.DataSet({edges_json});

  var container = document.getElementById("network");
  var data = {{
    nodes: nodes,
    edges: edges
  }};

  var options = {{
    layout: {{
      hierarchical: {{
        direction: "UD",
        sortMethod: "directed"
      }}
    }},
    physics: false,
    nodes: {{
      shape: "box",
      font: {{ face: "monospace", size: 14 }},
      borderWidth: 2
    }},
    edges: {{
      arrows: "to",
      smooth: true
    }}
  }};

  new vis.Network(container, data, options);
</script>

</body>
</html>
"""

        Path(output_file).write_text(html, encoding="utf-8")
        print(f"Graph saved to {Path(output_file).resolve()}")
