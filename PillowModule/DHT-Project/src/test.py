import sys

sys.path.insert(0, "json")
sys.path.insert(0, "hmi")
sys.path.insert(0, "func/json_client")
from atJsonData import atData

sys.path.insert(0, "hmi/simulation")

# print(atData.data)
sys.path.insert(0, "hmi/simulation/Font")
sys.path.insert(0, "hmi/simulation/Image")

import Simulation
Simulation.main()

#32->126