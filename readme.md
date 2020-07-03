# Satisfactory Parser
Parses the Satisfactory gamepedia to collect component information such as recipe, crafting time, building, speeds, etc.

# Contributing
Python version `3.8.3`

This project requires `requests` and `beautifulsoup4`. Ideally install them into a `virtual environment`.

# Usage
Run the `main.py` script which prints relevant information to standard out.

# Example
Collecting: Biomass  
Biomass (Leaves): 10 × Leaves @ 120 / min in Constructor @ 5 sec per 5 × Biomass @ 60 / min  
Biomass (Wood): 4 × Wood @ 60 / min in Constructor @ 4 sec per 20 × Biomass @ 300 / min  
Biomass (Mycelia): 10 × Mycelia @ 150 / min in Constructor @ 4 sec per 10 × Biomass @ 150 / min  
Biomass (Alien Carapace): 1 × Alien Carapace @ 15 / min in Constructor @ 4 sec per 100 × Biomass @ 1500 / min  
Biomass (Alien Organs): 1 × Alien Organs @ 7.5 / min in Constructor @ 8 sec per 200 × Biomass @ 1500 / min  

Collecting: Cable  
Cable: 2 × Wire @ 60 / min in Constructor @ 2 sec per 1 × Cable @ 30 / min  
Coated Cable Alternate: 5 × Wire @ 37.5 / min and 2 × Heavy Oil Residue @ 15 / min in Refinery @ 8 sec per 9 × Cable @ 67.5 / min  
Insulated Cable Alternate: 9 × Wire @ 45 / min and 6 × Rubber @ 30 / min in Assembler @ 12 sec per 20 × Cable @ 100 / min  
Quickwire Cable Alternate: 3 × Quickwire @ 7.5 / min and 2 × Rubber @ 5 / min in Assembler @ 24 sec per 11 × Cable @ 27.5 / min  