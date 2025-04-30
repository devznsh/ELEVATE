import json
from pathlib import Path

class RoadmapGenerator:
    def __init__(self):
        self.roadmaps = self._load_roadmaps()
    
    def _load_roadmaps(self):
        base_dir = Path(__file__).parent.parent.parent
        roadmaps_path = base_dir / "app" / "data" / "roadmaps.json"
        with open(roadmaps_path) as f:
            return json.load(f)
    
    def generate_roadmap(self, profession):
        if profession in self.roadmaps:
            return self.roadmaps[profession]
        
        lower_profession = profession.lower()
        for career in self.roadmaps.keys():
            if career.lower() == lower_profession:
                return self.roadmaps[career]
        
        return self.roadmaps["Generic"]

# Add this function to match the import
def generate_roadmap(profession):
    generator = RoadmapGenerator()
    return generator.generate_roadmap(profession)