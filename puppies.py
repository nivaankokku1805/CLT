import numpy as np
np.random.seed(42)  

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p=puppies.mean()
print("Mean:", p)
print("Standard Deviation:", puppies.std())
print("Variance:", puppies.var())

np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

print("\nSampling distribution with size 5:\n")
sample_prop=[]
for i in range(10000):
    sample = np.random.choice(puppies, size=5, replace=True)
    sample_prop.append(sample.mean())
sample_prop = np.array(sample_prop)

sm = sample_prop.mean()
print("Mean of sampling distribution:",sample_prop.mean())
print("Standard Deviation of sampling distribution:",sample_prop.std())
print("Variance of sampling distribution:",sample_prop.var())

print("\nSampling distribution with size 20:\n")

twenty_sample_prop=[]
for i in range(10000):
    sample = np.random.choice(puppies, size=20, replace=True)
    twenty_sample_prop.append(sample.mean())
twenty_sample_prop = np.array(twenty_sample_prop)

print("New Mean:", twenty_sample_prop.mean())
print("New Standard Deviation:", twenty_sample_prop.std())
print("New Variance :", twenty_sample_prop.var())