# test ABC085C - Otoshidama

import atcoder.beginnersSelection.abc085c_otoshidama_make_testcase as otmk
import atcoder.beginnersSelection.abc085c_otoshidama_sub as ot


def make_cases(n:int):
    cases = []
    for i in range(n):
        cases.append(otmk.make_testcase())
    return cases

def test_case():
    cases = make_cases(10)

    # for cs in cases:
    #     otd = ot.otoshidama(n=cs["n"], kei=cs["kei"])
    #     print(f"{cs=},{otd=} ")
    #     (x,y,z) = otd
    #     otkei = (x*10000 + y*5000 + z*1000)
    #     print(f"test_case=({x=},{y=},{z=}:{otkei}, {cs["kei"]})")
    #     assert cs["kei"] == otkei
    otd = ot.otoshidama(n=cases[0]["n"], kei=cases[0]["kei"])
    (x,y,z) = otd
    otkei = (x*10000 + y*5000 + z*1000)
    print(f"cs[0]:{cases[0]=}")
    assert cases[0]["kei"] == otkei

