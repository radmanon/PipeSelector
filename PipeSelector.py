class PipeSelector:
    def __init__(self):
        self.question = [
            "What is the purpose of the pipe? (e.g., water supply, drainage, gas)",
            "What is the prefered material for the pipe? (e.g., PVC, copper, steel)",
            "What is the diameter needed for the pipe? (in inches)"
        ]
        self.pipe_options = {
            "water supply" : ["PVC", "Copper"],
            "drainage" : ["PVC", "Cast Iron"],
            "gas" : ["Steel", "Copper"]
        }
         