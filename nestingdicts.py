# Nesting
capitals={
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 5},
}
print(travel_log)

# Nesting Dictionary in a list
travel_log:[
        {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits":12
        },
    
        {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"], 
        "total_visits": 5
        },
]
