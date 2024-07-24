# Food Order Chatbot Project

This project aims to develop a user-friendly chatbot for food ordering. The chatbot allows users to place orders, view their current orders, and track their orders. The project is based on a natural language processing (NLP) model created using Dialogflow and a backend developed in Python. Additionally, a MySQL database is used to store order and menu information.

## Project Features

- **Dialogflow NLP Integration**: A chatbot that understands user input in natural language and provides appropriate responses.
  - **Intents**: Specific intents have been created to understand user intentions. For example, `add_to_order`, `remove_from_order`, `get_order_status`.
  - **Entities**: Custom entities are defined to understand order and food information. For example, `food-item`, `quantity`.
  - **Fulfillment**: Webhook fulfillment is used to process user requests and interact with the database.

- **MySQL Database**: A MySQL database used to store order and menu information.
  - **Tables**:
    - `food_item`: Stores information about the food items on the menu.
    - `order_tracking`: Tracks the status of orders.
    - `orders`: Stores user orders.

- **Python Backend**: A FastAPI application that forms the backend of the chatbot and handles database interactions.

## Setup

### Requirements

- Python 3.x
- MySQL
- Dialogflow Account

### Steps

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/username/project-name.git
    cd project-name
    ```

2. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Database Configuration**:
    - Create your MySQL database and use the following SQL commands to create the necessary tables:
        ```sql
        CREATE DATABASE pandeyji_eatery;

        USE pandeyji_eatery;

        CREATE TABLE food_item (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );

        CREATE TABLE orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            total_price DECIMAL(10, 2) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE order_tracking (
            tracking_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            status VARCHAR(255) NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ```

4. **Dialogflow Configuration**:
    - Log in to your Dialogflow account and create a new agent.
    - Create the necessary intents and entities.
    - Configure the webhook URL in the Fulfillment section.

5. **Run the Application**:
    ```sh
    uvicorn main:app --reload
    ```

## Usage

### Add New Order

The user can create a new order by specifying the food items and quantities. Example request:
```json
{
    "intent": "add_to_order",
    "parameters": {
        "food-item": ["pizza", "cola"],
        "quantity": [1, 2]
    },
    "session_id": "unique_session_id"
}
