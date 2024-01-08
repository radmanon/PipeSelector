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

    def ask_questions(self):
        answers = []
        for question in self.question:
            answer = input(question + " ")
            answers.append(answer.strip().lower())
        return answers
    
    def suggest_pipes(self, answers):
        purpose, material, diameter = answers
        if purpose in self.pipe_options:
            available_pipes = self.pipe_options[purpose]
            # this is the lcoation for add more filters to choose the suitable pipe
            suitable_pipes = [pipe for pipe in available_pipes if material.lower() in pipe.lower()]
            return suitable_pipes

def main():
    pipe_selector = PipeSelector()
    print("-- Welcome to the pipe selector application --")

    while True:
        answers = pipe_selector.ask_questions()
        suggest_pipes = pipe_selector.suggest_pipes(answers)

        if suggest_pipes:
            print(f"\n Suggested pipes for your requirements: {', '.join(suggest_pipes)}")
        else:
            print("\n sorry, no suitable pipes found for your requirements.")

        user_input = input("\n Do you want to find the pipe for another purpose? (yes/no) ").strip().lower()
        if user_input != 'yes':
            print(" Thank you for using the Pipe Selector application. GoodBye")
            break

if __name__ == "__main__":
    main()