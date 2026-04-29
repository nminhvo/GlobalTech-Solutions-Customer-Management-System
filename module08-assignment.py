# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 200,
    "Cloud Consulting": 220,
    "Technical Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "ABC Corporation",
    "contact_person": "John Smith",
    "email": "john.smith@abccorp.com",
    "phone": "813-555-1200"
}
customer2 = {
    "company_name": "TechNova Solutions",
    "contact_person": "Sarah Johnson",
    "email": "sarah.johnson@technova.com",
    "phone": "813-555-3400"
}
customer3 = {
    "company_name": "GreenField Industries",
    "contact_person": "Michael Lee",
    "email": "michael.lee@greenfield.com",
    "phone": "813-555-5600"
}
customer4 = {
    "company_name": "BlueWave Marketing",
    "contact_person": "Emily Davis",
    "email": "emily.davis@bluewave.com",
    "phone": "813-555-7800"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for customer_id, info in customers.items():
    print(f"Customer ID: {customer_id}")
    print(f"Company: {info['company_name']}")
    print(f"Contact Person: {info['contact_person']}")
    print(f"Email: {info['email']}")
    print(f"Phone: {info['phone']}")
    # Separator line to improve readability between customer records
    print("-" * 60)

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
c002_info = customers["C002"]
print(f"C002 Info: {c002_info}")
c003_contact = customers["C003"]["contact_person"]
print(f"C003 Contact Person: {c003_contact}")
c999_info = customers.get("C999", "Customer not found")
print(f"C999 Info: {c999_info}")

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
customers["C001"]["phone"] = "813-555-9999"
customers["C002"]["industry"] = "Technology"
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
project1 = {
    "name": "Corporate Website",
    "service": "Web Development",
    "hours": 120,
    "budget": 18000
}
project2 = {
    "name": "Sales Data Dashboard",
    "service": "Data Analysis",
    "hours": 80,
    "budget": 14000
}
project3 = {
    "name": "Cloud Migration",
    "service": "Cloud Consulting",
    "hours": 100,
    "budget": 22000
}
project4 = {
    "name": "Security Audit",
    "service": "Cybersecurity",
    "hours": 60,
    "budget": 15000
}
projects = {
    "C001": [project1],
    "C002": [project2],
    "C003": [project3],
    "C004": [project4]
}
for customer_id, project_list in projects.items():
    print(f"Customer ID: {customer_id}")
    for project in project_list:
        print(project)

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
for project_list in projects.values():
    for project in project_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(project["name"], "→", cost)

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
print("Customer IDs:", list(customers.keys()))
print("\nCustomer Companies:")
for c in customers.values():
    print(c["company_name"])
print("\nTotal customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
service_counts = {}
for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
total_hours = 0
total_budget = 0
all_budgets = []

for project_list in projects.values():
    for project in project_list:
        total_hours += project["hours"]
        total_budget += project["budget"]
        all_budgets.append(project["budget"])
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Most Expensive Project Budget:", max_budget)
print("Least Expensive Project Budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)

for customer_id, customer_info in customers.items():
    customer_projects = projects.get(customer_id, [])
    num_projects = len(customer_projects)

    customer_total_hours = 0
    customer_total_budget = 0

    for project in customer_projects:
        customer_total_hours += project["hours"]
        customer_total_budget += project["budget"]

    print(f"Customer ID: {customer_id}")
    print(f"Company: {customer_info['company_name']}")
    print(f"Contact Person: {customer_info['contact_person']}")
    print(f"Email: {customer_info['email']}")
    print(f"Phone: {customer_info['phone']}")
    print(f"Number of Projects: {num_projects}")
    print(f"Total Hours: {customer_total_hours}")
    print(f"Total Budget: {customer_total_budget}")
    # Separator line to improve readability between customer records
    print("-" * 60)

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
active_customers = {
    cid: cinfo
    for cid, cinfo in customers.items()
    if cid in projects
}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
customer_budgets = {
    cid: sum(project["budget"] for project in plist)
    for cid, plist in projects.items()
}
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
service_tiers = {
    service: "Premium" if rate >= 200
    else "Standard" if rate >= 100
    else "Basic"
    for service, rate in services.items()
}
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]   
    for field in required_fields:
        if field not in customer_dict:
            return False    
    return True
for cid, customer in customers.items():
    print(cid, "valid:", validate_customer(customer))

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
project1["status"] = "active"
project2["status"] = "completed"
project3["status"] = "pending"
project4["status"] = "active"

status_counts = {}
for project_list in projects.values():
    for project in project_list:
        status = project["status"]
        status_counts[status] = status_counts.get(status, 0) + 1

print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
def analyze_customer_budgets(projects_dict):
    results = {}
    for cid, project_list in projects_dict.items():
        total = 0
        count = len(project_list)
        for project in project_list:
            total += project["budget"]
        average = total / count if count > 0 else 0
        results[cid] = {
            "total": total,
            "average": average,
            "count": count
        }
    return results
budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
def recommend_services(customer_id, customers, projects, services):
    used_services = []
    customer_projects = projects.get(customer_id, [])
    for project in customer_projects:
        if project["service"] not in used_services:
            used_services.append(project["service"])
    recommendations = []
    for service in services:
        if service not in used_services:
            recommendations.append(service)
    return recommendations
for cid in customers:
    recommendations = recommend_services(cid, customers, projects, services)
    print(cid, recommendations)