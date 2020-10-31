from dataclasses import dataclass

@dataclass
class TimeCosts :
	moveDiagTimeCost: float = 0.75
	moveForwardTimeCost: float = 1.0
	moveSideTimeCost: float = 1.25
	moveUpTimeCost: float = 1.5
	moveDownTimeCost: float = 1.75
	pickupTimeCost: float = 12.0


