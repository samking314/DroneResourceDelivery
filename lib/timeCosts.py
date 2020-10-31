from dataclasses import dataclass

@dataclass
class TimeCosts :
	moveDiagTimeCost: float = 0.75
	moveForwardTimeCost: float = 1.0
	moveSideTimeCost: float = 1.25
	moveUpTimeCost: float = 1.5
	moveDownTimeCost: float = 1.75
	pickupTimeCost: float = 12.0

	# setter methods
	def setTimeCosts (
		self,
		moveDiagTimeCost,
		moveForwardTimeCost,
		moveSideTimeCost,
		moveUpTimeCost,
		moveDownTimeCost,
		pickupTimeCost
	) :
		self.moveDiagTimeCost = moveDiagTimeCost
		self.moveForwardTimeCost = moveForwardTimeCost
		self.moveSideTimeCost = moveSideTimeCost
		self.moveUpTimeCost = moveUpTimeCost
		self.moveDownTimeCost = moveDownTimeCost
		self.pickupTimeCost = pickupTimeCost

