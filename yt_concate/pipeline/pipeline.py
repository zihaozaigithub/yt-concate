from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, data, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(inputs)
            except StepException as e:
                print('Error', e)
                break
