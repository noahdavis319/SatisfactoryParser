# Satisfactory Parser
Parses the Satisfactory gamepedia to collect component information such as recipe, crafting time, building, speeds, etc.

# Contributing
Python version `3.8.3`

This project requires `requests` and `beautifulsoup4`. Ideally install them into a `virtual environment`.

# Usage
Run the `main.py` script which prints relevant information to standard out.

# Example
{  
    "A.I. Limiter": {  
        "building": {  
            "time": "12 sec",  
            "type": "Assembler"  
        },  
        "ingredients": {  
            "Copper Sheet": {  
                "amount": "5",  
                "rate": "25"  
            },  
            "Quickwire": {  
                "amount": "20",  
                "rate": "100"  
            }  
        },  
        "products": {  
            "A.I. Limiter": {  
                "amount": "1",  
                "rate": "5"  
            }  
        }  
    },  
    "Adaptive Control Unit": {  
        "building": {  
            "time": "120 sec",  
            "type": "Manufacturer"  
        },  
        "ingredients": {  
            "Automated Wiring": {  
                "amount": "15",  
                "rate": "7.5"  
            },  
            "Circuit Board": {  
                "amount": "10",  
                "rate": "5"  
            }  
        },  
        "products": {  
            "Adaptive Control Unit": {  
                "amount": "2",  
                "rate": "1"  
            }  
        }  
    },  