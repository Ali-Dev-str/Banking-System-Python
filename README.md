# Banking-System-Python
🏦 Object-Oriented ATM & Banking Simulation System
   A comprehensive, production-ready console application that simulates a real-world **ATM network** and **Banking Infrastructure**. Built purely with **Python**, this project showcases advanced architectural design patterns, strict **Object-Oriented Programming (OOP)**, and robust logical workflows.
   
🚀 Key Features Implemented
  *Multi-Entity Architecture: Separate decoupled layers representing `Bank`, `ATM`, `Customers`, `Account`, and `Card` components.
  * Card Authentication: Simulates secure login via card numbers and PIN verification linked directly to specific bank servers.
  * Core Banking Transactions:
  * Cash Withdrawal: Validates account balance dynamically to prevent overdrafts.
  * Cash Deposit: Real-time updates to financial ledger balances.
  * Balance Inquiry: Secure instantaneous retrieval of account funds.
  * Transaction History: Generates unique tracking IDs for every action using `UUID` along with timestamps.
  * Interactive UI Hardware Simulation:** Abstracted `Keypad` and `Screen` classes mimicking real physical ATM components.

🛠️ Advanced OOP Concepts Demonstrated
  1. Abstraction (ABC):** Utilized Python's `abc` module to abstract the base `transaction` class, guaranteeing a strict interface contraction for `execute()` across all financial action types.
2. Encapsulation:** Safe handling of sensitive fields like account balances, transactions history arrays, and cryptographic `uuid` generation.
3. Clean Code & Design Patterns:** Used `Enum` mapping for transactional states and utilized structural pattern matching (`match-case`) for clean code branching.

⚙️ How to Run & Test
  1. Clone this repository to your local machine.
  2. Run the main file:
    < bash.  python main.py >
  3. Use the predefined accounts setup at the bottom of the script to log in (e.g., Input Card Number and PIN).
