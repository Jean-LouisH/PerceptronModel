class ArtificialNeuron:
    
    def __init__(self):
        self.activationLevel = 0
        self.inputs = []
        self.output = 0

    def receiveInputs(self, previousLayerOutputs, inputWeights):
        self.inputs.clear()
        #
        pass
        
    def computeActivationLevel():
        pass
    
    def heavysideStepFunction(self, activationLevel):
        if self.activationLevel >= 0:
            self.output = 1
        else:
            self.output = 0
