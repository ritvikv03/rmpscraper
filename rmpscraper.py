pip install RateMyProfessorAPI
pip install RateMyProfessorAPI --upgrade
import ratemyprofessor

# Define the target school and professor names
target_school_name = "Texas A&M University at College Station"
professor_name = "Toryn Schafer"

# Attempt to find the school
school = ratemyprofessor.get_school_by_name(target_school_name)

# Ensure the school is found
if school is not None:
    # Attempt to find the professor at the found school
    professor = ratemyprofessor.get_professor_by_school_and_name(school, professor_name)
    
    # Ensure the professor is found and verify the school name matches exactly
    if professor is not None and professor.school.name == target_school_name:
        # Print professor details
        print("%s works in the %s Department at %s." % (professor.name, professor.department, professor.school.name))
        print("Rating: %s / 5.0" % professor.rating)
        print("Difficulty: %s / 5.0" % professor.difficulty)
        print("Total Ratings: %s" % professor.num_ratings)
        if professor.would_take_again is not None:
            print("Would Take Again: %s%%" % round(professor.would_take_again, 1))
        else:
            print("Would Take Again: N/A")
    else:
        print(f"Professor {professor_name} not found at {target_school_name}.")
else:
    print(f"School '{target_school_name}' not found.")


