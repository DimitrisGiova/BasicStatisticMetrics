def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(1))


def euler_sieve(n):
    # δημιουργεί έναν πίνακα από περιττούς αριθμούς.
    num_tab = range(1, n, 2)
    # ο πίνακας είναι ο 1,3,5,7,... αλλάζουμε το 1ο στοιχείο
    # στον πρώτο αριθμό, 2
    num_tab[0] = 2
    i = 1
    # ο μεγαλύτερος αριθμός στον πίνακα
    highestval = num_tab[-1]
    while True:
        # βρες τον 1ο τελεστή στο κόσκινο
        cx = num_tab[i]
        # αν τιμή που δε δουλεύει, προχώρησε στην επόμενη
        if cx == False:
            i += 1
            continue
        # η 1η τιμή που περνάει από το κόσκινο είναι πάντα ο
        # τρέχων αριθμός * τον εαυτό του. όλοι οι άλλοι αριθμοί
        # στο κόσκινο θα είναι μεγαλύτεροι.
        if cx ** 2 > n:
            break
        # διαγράφει - κόσκινο
        tostrike = []
        for j in xrange(i, len(num_tab)):
            # βρίσκει τον 2ο τελεστή στο κόσκινο
            cy = num_tab[j]
            # αν τιμή που δε δουλεύει, αγνόησε τα υπόλοιπα
            if cy == False:
                continue
            cut = cx * cy
            # εκτός των ορίων του κόσκινου
            if cut > highestval:
                break
            # προσθέτει στο κόσκινο
            tostrike.append(cut)
        # περνάει από το κόσκινο τις τιμές από τον πίνακα των αριθμών μας
        for d in tostrike:
            ind = (d - 1) / 2
            num_tab[ind] = False
        # βρίσκει τη μεγαλύτερη τιμή στον πίνακα που δεν
        # έχει περάσει από το κόσκινο
        hiind = -1
        while num_tab[hiind] == False:
            hiind -= 1
        highestval = num_tab[hiind]

        i += 1
    return num_tab


...

print[x
for x in euler_sieve(100) if x != False]