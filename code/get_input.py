from typing import List
from aocd import get_data
from dotenv import load_dotenv

def get_input(day: int, year: int =2024) -> List[str]:
    load_dotenv()
    return get_data(day=day, year=year).splitlines()