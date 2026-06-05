student={
    "name":"john",
    "subjects":{
        "maths":85,
        "english":90,
        "science":92
    }
}
print(student.keys()) #keys of the dictionary
print(list(student.keys())) #typecasting to list
print(len(student.keys())) #length of keys
print(student.values())#values of the dictionary
print(student.items()) #key value pairs of the dictionary
print(student.get("name")) #accessing value using get method
student.update({"city":"New York"})#updating the dictionary with new key value pair
print(student)