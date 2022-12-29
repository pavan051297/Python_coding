d ={"bcpavan":22,"amohan":33,"hsekar":44}
f = {"Fan":3200,"Ac":5000,"TF":2000,"Cooler":3500}
print(dict(sorted(d.items())))
print(sorted(d))
dicd = {k :v for k ,v in sorted(f.items())}
print(dicd)
r = {k : v for k,v in sorted(f.items(),key= lambda v:v[1])}
print(r)
