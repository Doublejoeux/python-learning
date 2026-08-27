#sorted
nums = [4,1,3]
print(sorted(nums)) #[1,3,4]
#sorted with a key
scores = [("Ade", 70), ("Bola", 95), ("Chi", 60)]
sorted_scores = sorted(scores, key= lambda x: x[1])
print(sorted_scores)
 