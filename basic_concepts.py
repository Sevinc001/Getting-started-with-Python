"""
Python for Everybody - Core Mathematical & Conditional Exercises.
Author: Sevinc Zaur Qasimova
"""

def convert_elevator_floor(eu_floor: int) -> int:
    """Converts European elevator floors to US equivalent."""
    return eu_floor + 1


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Converts temperature from Celsius to Fahrenheit."""
    return (1.8 * celsius) + 32


def calculate_gross_pay(hours: float, rate: float) -> float:
    """
    Computes gross pay with overtime logic.
    Hours above 40 are paid at 1.5 times the hourly rate.
    """
    if hours <= 40:
        return hours * rate
    else:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)


def determine_grade(score: float) -> str:
    """Returns academic grade based on a score between 0.0 and 1.0."""
    if score < 0.0 or score > 1.0:
        raise ValueError("Score out of bounds (0.0 - 1.0)")
    
    if score >= 0.9: return "A"
    elif score >= 0.8: return "B"
    elif score >= 0.7: return "C"
    elif score >= 0.6: return "D"
    else: return "F"


# Self-test block to verify the logic
if __name__ == "__main__":
    print("[Test] 45 hours at 10.50/hr Pay:", calculate_gross_pay(45, 10.50)) # Expected: 498.75
    print("[Test] Score 0.85 Grade:", determine_grade(0.85)) # Expected: B
