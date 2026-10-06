def cohens_kappa(rater1: list, rater2: list) -> float:
    """
    Returns Cohen's kappa as a float.
    """
    categories=list(set(rater1+rater2))
    p0_count=0.0
    for r1,r2 in zip(rater1,rater2):
        if r1==r2:
            p0_count+=1
    p0=p0_count/len(rater1)
    pe = 0.0
    for cat in categories:
        count1 = rater1.count(cat)
        count2 = rater2.count(cat)
        pe += (count1 / len(rater1)) * (count2 / len(rater1))
    if pe == 1.0:
        return 1.0

    return (p0-pe)/(1-pe)
    