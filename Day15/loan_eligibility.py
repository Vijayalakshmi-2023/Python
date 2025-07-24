class LowCreditScoreError(Exception):
    """Raised when credit score is too low for loan eligibility."""
    pass

def check_loan_eligibility():
    try:
        income = float(input("Enter your monthly income (₹): "))
        assert income > 0, "Income must be a positive number."

        credit_score = int(input("Enter your credit score (300–900): "))
        if credit_score < 650:
            raise LowCreditScoreError("Credit score too low for loan eligibility.")

    except ValueError:
        print("❌ Error: Please enter only numeric values for income and credit score.")
    except AssertionError as ae:
        print(f"❌ Error: {ae}")
    except LowCreditScoreError as lce:
        print(f"❌ Error: {lce}")
    else:
        print("✅ You are eligible for the loan!")

# Run the program
if __name__ == "__main__":
    check_loan_eligibility()
