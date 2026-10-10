import math,json,random

def proportions(values,edges,epsilon=1e-6):
    if not values:raise ValueError('Empty sample')
    if any(not math.isfinite(v) for v in values):raise ValueError('Non-finite sample')
    counts=[epsilon]*(len(edges)+1)
    for v in values:
        index=next((i for i,e in enumerate(edges) if v<=e),len(edges));counts[index]+=1
    total=sum(counts);return [c/total for c in counts]

def fit_bins(reference,bins=10):
    if bins<2 or not reference or any(not math.isfinite(v) for v in reference):raise ValueError('Invalid reference')
    r=sorted(reference)
    return sorted(set(r[min(len(r)-1,int(len(r)*i/bins))] for i in range(1,bins)))

def monitor(reference,current):
    if not current:raise ValueError('Empty current window')
    edges=fit_bins(reference)
    valid=[v for v in current if v is not None and math.isfinite(v)]
    missing=1-len(valid)/len(current)
    if not valid:return {'status':'insufficient_data','missing_rate':missing,'psi':None}
    p=proportions(reference,edges);q=proportions(valid,edges)
    psi=sum((a-b)*math.log(a/b) for a,b in zip(p,q))
    return {'psi':psi,'status':'investigate' if psi>.2 or missing>.05 else 'stable','missing_rate':missing,'reference_n':len(reference),'current_valid_n':len(valid),'bin_edges':edges,'reference_proportions':p,'current_proportions':q}
if __name__=='__main__':
    r=random.Random(4);ref=[r.gauss(0,1) for _ in range(1000)];cur=[r.gauss(.8,1.2) for _ in range(1000)]
    print(json.dumps(monitor(ref,cur),indent=2))
