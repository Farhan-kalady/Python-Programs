#check whether a given key already exists in a dictionary.merge two dictionaries. 
# Sort a dictionary in ascending and descending order by key.
# Create a new dictionary by inverting keys and values of an existing dictionary.
d1={1:100,2:200,3:300,4:400,5:500}
key=int(input("Enter the key to search: "))
if key in d1:
    print("Key found in d1 with value: ",d1[key])
else:
    print("Key not found in d1")


d2={6:600,7:700,8:800,9:900,10:1000}
d1.update(d2)
print("After merging: ",d1)

print("First dictionary in ascending order: ",sorted(d1))
print("First dictionary in descending order: ",sorted(d1,reverse=True))

inverted={v:k for k,v in d1.items()}
print("Inverted dictionary: ",inverted)