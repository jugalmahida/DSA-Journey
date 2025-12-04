class Main:
    def __init__(self) -> None:
        # Strings & Tuples are Immutable, if assign new value in same ref of string then, it will creating new 
        # ref of it.(NOT CHANGE ORIGINAL ONES), check by id()
        # Encode & Decode String 
        print("DSA")
        str1 = "Hello 👋"
        encoded_str1 = str1.encode("utf-8")
        print(encoded_str1)
        print(encoded_str1.decode("utf-8"))
        
    def tuples_example(self) -> None:
        # Tuples
        animals = ("Dog","Cat","Rat","Lion","Tiger")
        print(animals)
        # Destructure(unpack) Tuples
        (a1,a2,a3,a4,a5) = animals # length of variables must be exact as length of tuple(animals   )
        print(f"Animals - ${a1,a2,a3,a4,a5}")
    
    def list_comprehension_example(self) -> None:
        # List Comprehension
        hobby = ["Cricket","Music","Coding","New Learning"]
        b = [x for x in hobby if "sic" in x]
        print(b)


a = Main()
# a.tuples_example()
a.list_comprehension_example()