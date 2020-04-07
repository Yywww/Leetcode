def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    uf = [i for i in range(g_nodes+1)]
    res = 0
    g_weight_isort = sorted(range(len(g_weight)),key = lambda k:g_weight[k])

    for index in g_weight_isort:
        print(uf)
        n_from = g_from[index]
        n_to = g_to[index]
        if find(uf,n_from)!=find(uf,n_to):
            
            uf[find(uf,n_from)] = find(uf,n_to)
            res += g_weight[index]
    return res
def find(uf,child):
    while child!=uf[child]:
        child = uf[child]
    return child

ans = kruskals(4,[1,1,4,2,3,3],[2,3,1,4,2,4],[5,3,6,7,4,5])
print(ans)