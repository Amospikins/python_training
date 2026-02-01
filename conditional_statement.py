

# if age.isdigit():
#     age = int(age)
#     if age>=18:
#         print(f"Hello {name}, you can drive.")
#     else:
#         print(f"Hello {name}, you cannot drive yet.")
# else:
#     print("Invalid age input.")

# elif  else if

# score = int(input("Enter your math score: "))

# if score >= 70:
#     grade = "A"
# elif score >= 60:
#     grade = "B"
# elif score >= 50:
#     grade = "C"
# else: 
#     grade = "F"

# print(grade)



# age = 20
# has_id = False

# if age>= 18 and has_id:
#     print("You can enter") 


# PATTERN MATCHING FEATURE:
# SWITCH CASE

# match value:
#     case pattern1:
#         code to be executed
#     case pattern2:
#         code to be executed
#     case pattern3:
#         code to be executed
#     case pattern4:
#         code to be executed
#     case pattern5:
#         code to be executed
#     case _:
#         code to be executed





# STATUS CODE IS NUMBER THE SERVER RETURNS TO TELL THE CLIENT SOMETHING IS HAPPENING
# 1XX  => INFORMATIONAL => 100 => CONTINUE, 102 => PROCESSING
# 2XX  => SUCCESS => OK; 201=CREATED; 204=NO CONTENT 
# 3XX  => REDIRECT => 301=MOVED PERMANENTLY; 302: FOUND (temporary redirect); 303: CAN BE FOUND AT A DIFF URL; 304: NOT MODIFIED
# 4XX  => CLIENT ERROR (NA YOUR FAULT): 400: BAD REQUEST; 401: UNAUTHORISED; 403: FORBIDDEN; 404: NOT FOUND; 409: CONFLICT 
# 5XX  => SERVER ERROR (MEANING SERVER FAULT): 500 INTERNAL SERVER ERROR;



status_code = int(input("enter your status code: "))

match status_code:
    case 200:
        print("OK")
    case 404:
        print("NOT FOUND")
    case 500:
        print("SERVER ERROR")
    case _:
        print("UNKNOWN STATUS")
    
    
    
    # jkldghaljcfgjlgasfjdgasasfka