d1 = {
    'Raghu': 29,
    'Ravi': 33,
    'Kavya': 35
}

d2 = {
    'Ravi': 40,
    'Kavya': 28,
    'Nandan': 29
}

common = set(d1) & set(d2)
print(common)

union = set(d1.items()) | set(d2.items())
print(union)

check_emptiness = len({})==0
print(check_emptiness)


company = {
    "employees": {
        "E001": {
            "name": "Raghu",
            "age": 29,
            "department": "Engineering",
            "skills": ["Python", "FastAPI", "SQL"],
            "address": {
                "city": "Bangalore",
                "country": "India"
            },
            "projects": {
                "P101": {
                    "name": "Enterprise RAG",
                    "status": "active",
                    "technologies": ["Python", "PostgreSQL", "Redis"]
                },
                "P102": {
                    "name": "AI Assistant",
                    "status": "completed",
                    "technologies": ["Python", "FastAPI", "LLM"]
                }
            }
        },

        "E002": {
            "name": "Ravi",
            "age": 33,
            "department": "Data",
            "skills": ["Python", "SQL", "Machine Learning"],
            "address": {
                "city": "Chennai",
                "country": "India"
            },
            "projects": {
                "P103": {
                    "name": "Recommendation System",
                    "status": "active",
                    "technologies": ["Python", "ML", "PostgreSQL"]
                }
            }
        }
    },

    "company_info": {
        "name": "TechCorp",
        "location": "Bangalore",
        "departments": ["Engineering", "Data", "AI"]
    }
}

print(company['employees'])
print(company[0])