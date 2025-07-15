# Personal Finance Tracker

A Python-based **Personal Finance Tracker** that helps users track their income, expenses, and savings. The tool supports categorizing transactions, setting budgets, generating monthly summaries, and visualizing financial data with graphs. This version now supports persistent storage using SQLite for storing transaction data.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Author](#author)

---

## Project Overview

This project allows users to manage their personal finances by:

-   **Adding transactions** with descriptions and categories (income and expenses)
-   **Viewing summaries** of income, expenses, and savings on a monthly basis
-   **Generating monthly summaries** and visualizing spending via charts
-   **Exporting transaction data** to CSV or Excel for external analysis
-   **Storing transaction data** persistently using SQLite

---

## Features

-   **Transaction Management**:

    -   Add income and expense transactions with detailed descriptions
    -   Categorize transactions for better tracking (e.g., Food, Rent, Entertainment)
    -   Data is stored persistently in an SQLite database for easy management

-   **Monthly Summary**:

    -   View a detailed summary of income, expenses, and savings on a monthly basis
    -   Visualize the breakdown of spending by category with charts

-   **Data Export**:

    -   Export your transaction data to **CSV** or **Excel** files for reporting or backup purposes

-   **Data Visualization**:
    -   Visualize your spending patterns using **Matplotlib** and **Seaborn** with pie charts and bar graphs

---

## Technologies Used

-   **Python**: The core language used to build this project
-   **Pandas**: For handling data structures and performing data analysis
-   **Matplotlib**: For data visualization, creating bar and pie charts
-   **Seaborn**: Enhances Matplotlib charts with better aesthetics
-   **SQLite**: For persistent storage of transactions
-   **CSV/Excel**: For exporting transaction data for further analysis

---

## Getting Started

Follow the steps below to set up the project locally:

### Prerequisites

Make sure you have Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/).

---

## Installation

To get started with the **Personal Finance Tracker** project, follow these steps:

1. **Clone this repository** to your local machine:

    ```bash
    git clone https://github.com/hiten-shah0106/personal-finance-tracker.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd personal-finance-tracker
    ```

3. **Create a virtual environment** (recommended):

    ```bash
    python -m venv finance_env
    ```

4. **Activate the virtual environment**:

    - On Windows:
        ```bash
        finance_env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source finance_env/bin/activate
        ```

5. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Run the main program**:

    ```bash
    python main.py
    ```

2. **Follow the interactive menu** to:

    - Add new transactions (income or expenses)
    - View your current balance and transaction history
    - Generate monthly reports
    - Export data to CSV or Excel files
    - Create visualizations of your spending patterns

3. **Example workflow**:
    - Start by adding some transactions
    - View monthly summaries to track your financial progress
    - Visualize your spendings
    - Export data for external analysis.

---

## Author

**Hiten Shah**

-   GitHub: [hiten-shah0106](https://github.com/hiten-shah0106)
-   LinkedIn: [Hiten Shah](https://www.linkedin.com/in/contact-hitenshah/)
-   Email: hiten010607shah@gmail.com

---

**Happy tracking your finances! 💰📊**

---
