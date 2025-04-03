import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake user names and phone numbers
fake = Faker()

# Define possible locations and products
locations = ["USA", "India", "UK", "Canada", "Australia", "Germany"]
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Smartwatch", "Mouse"]

# Generate 200 sample user interactions
data = []
for _ in range(200):
    user_name = fake.name()
    user_phone = fake.phone_number()
    interaction_time = fake.date_time_this_year()  # Random datetime this year
    user_location = random.choice(locations)
    product_purchased = random.choice(products)
    
    data.append([user_name, user_phone, interaction_time, user_location, product_purchased])

# Create DataFrame
df = pd.DataFrame(data, columns=["user_name", "user_phone", "interaction_time", "user_location", "product_purchased"])

# Save to Excel
df.to_excel("data/sample_data.xlsx", index=False)

print("✅ Sample data saved as data/sample_data.xlsx")
